import pandas as pd
import tensorflow as tf


def preprocess(train_df: pd.DataFrame, model_schema) -> pd.DataFrame:
    # Get the list of input features for the candidate model from the model schema
    input_model_schema = model_schema["input_schema"]["columnar_schema"]
    candidate_features = [feat["name"] for feat in input_model_schema]

    # Select the candidate features from the training DataFrame
    item_df = train_df[candidate_features]

    # Drop duplicate rows based on the 'article_id' column to get unique candidate items
    item_df.drop_duplicates(subset="article_id", inplace=True)

    return item_df


def postprocess(candidate_embeddings) -> pd.DataFrame:
    # Concatenate all article IDs and embeddings from the candidate_embeddings dataset
    all_article_ids = tf.concat([batch[0] for batch in candidate_embeddings], axis=0)
    all_embeddings = tf.concat([batch[1] for batch in candidate_embeddings], axis=0)

    # Convert tensors to numpy arrays
    all_article_ids_np = all_article_ids.numpy().astype(int)
    all_embeddings_np = all_embeddings.numpy()

    # Convert numpy arrays to lists
    items_ids_list = all_article_ids_np.tolist()
    embeddings_list = all_embeddings_np.tolist()

    # Create a DataFrame
    data_emb = pd.DataFrame(
        {
            "article_id": items_ids_list,
            "embeddings": embeddings_list,
        }
    )

    return data_emb
