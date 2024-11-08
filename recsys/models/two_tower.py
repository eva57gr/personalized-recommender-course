import tensorflow as tf
import tensorflow_recommenders as tfrs
from tensorflow.keras.layers import Normalization, StringLookup


class QueryTower(tf.keras.Model):
    def __init__(self, user_ids: list, emb_dim: int) -> None:
        super().__init__()

        self.user_embedding = tf.keras.Sequential(
            [
                StringLookup(vocabulary=user_ids, mask_token=None),
                tf.keras.layers.Embedding(
                    # Add an additional embedding to account for unknown tokens.
                    len(user_ids) + 1,
                    emb_dim,
                ),
            ]
        )

        self.normalized_age = Normalization(axis=None)

        self.fnn = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(emb_dim, activation="relu"),
                tf.keras.layers.Dense(emb_dim),
            ]
        )

    def call(self, inputs):
        concatenated_inputs = tf.concat(
            [
                self.user_embedding(inputs["customer_id"]),
                tf.reshape(self.normalized_age(inputs["age"]), (-1, 1)),
                tf.reshape(inputs["month_sin"], (-1, 1)),
                tf.reshape(inputs["month_cos"], (-1, 1)),
            ],
            axis=1,
        )

        outputs = self.fnn(concatenated_inputs)

        return outputs


class ItemTower(tf.keras.Model):
    def __init__(
        self,
        item_ids: list,
        garment_groups: list,
        index_groups: list,
        emb_dim: int,
    ):
        super().__init__()

        self.garment_groups = garment_groups
        self.index_groups = index_groups

        self.item_embedding = tf.keras.Sequential(
            [
                StringLookup(vocabulary=item_ids, mask_token=None),
                tf.keras.layers.Embedding(
                    # Add an additional embedding to account for unknown tokens.
                    len(item_ids) + 1,
                    emb_dim,
                ),
            ]
        )
        # Converts strings into integer indices (scikit-learn LabelEncoder analog)
        self.garment_group_tokenizer = StringLookup(
            vocabulary=garment_groups,
            mask_token=None,
        )
        self.index_group_tokenizer = StringLookup(
            vocabulary=index_groups,
            mask_token=None,
        )

        self.fnn = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(emb_dim, activation="relu"),
                tf.keras.layers.Dense(emb_dim),
            ]
        )

    def call(self, inputs):
        garment_group_embedding = tf.one_hot(
            self.garment_group_tokenizer(inputs["garment_group_name"]),
            len(self.garment_groups),
        )

        index_group_embedding = tf.one_hot(
            self.index_group_tokenizer(inputs["index_group_name"]),
            len(self.index_groups),
        )

        concatenated_inputs = tf.concat(
            [
                self.item_embedding(inputs["article_id"]),
                garment_group_embedding,
                index_group_embedding,
            ],
            axis=1,
        )

        outputs = self.fnn(concatenated_inputs)

        return outputs


class TwoTowerModel(tf.keras.Model):
    def __init__(
        self,
        query_model: QueryTower,
        item_model: ItemTower,
        item_ds: tf.data.Dataset,
        batch_size: int,
    ):
        super().__init__()
        self.query_model = query_model
        self.item_model = item_model
        self.task = tfrs.tasks.Retrieval(
            metrics=tfrs.metrics.FactorizedTopK(
                candidates=item_ds.batch(batch_size).map(self.item_model)
            )
        )

    def train_step(self, batch) -> tf.Tensor:
        # Set up a gradient tape to record gradients.
        with tf.GradientTape() as tape:
            # Loss computation.
            user_embeddings = self.query_model(batch)
            item_embeddings = self.item_model(batch)
            loss = self.task(
                user_embeddings,
                item_embeddings,
                compute_metrics=False,
            )

            # Handle regularization losses as well.
            regularization_loss = sum(self.losses)

            total_loss = loss + regularization_loss

        gradients = tape.gradient(total_loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))

        metrics = {
            "loss": loss,
            "regularization_loss": regularization_loss,
            "total_loss": total_loss,
        }

        return metrics

    def test_step(self, batch) -> tf.Tensor:
        # Loss computation.
        user_embeddings = self.query_model(batch)
        item_embeddings = self.item_model(batch)

        loss = self.task(
            user_embeddings,
            item_embeddings,
            compute_metrics=False,
        )

        # Handle regularization losses as well.
        regularization_loss = sum(self.losses)

        total_loss = loss + regularization_loss

        metrics = {metric.name: metric.result() for metric in self.metrics}
        metrics["loss"] = loss
        metrics["regularization_loss"] = regularization_loss
        metrics["total_loss"] = total_loss

        return metrics
