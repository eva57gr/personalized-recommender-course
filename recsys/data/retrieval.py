def create_feature_view(fs):
    trans_fg = fs.get_feature_group(name="transactions", version=1)
    customers_fg = fs.get_feature_group(name="customers", version=1)
    articles_fg = fs.get_feature_group(name="articles", version=1)

    # You'll need to join these three data sources to make the data compatible
    # with out retrieval model. Recall that each row in the `transactions` feature group
    # relates information about which customer bought which item.
    # You'll join this feature group with the `customers` and `articles` feature groups
    # to inject customer and item features into each row.
    selected_features = (
        trans_fg.select(
            ["customer_id", "article_id", "t_dat", "price", "month_sin", "month_cos"]
        )
        .join(
            customers_fg.select(["age", "club_member_status", "age_group"]),
            on="customer_id",
        )
        .join(
            articles_fg.select(["garment_group_name", "index_group_name"]),
            on="article_id",
        )
    )

    feature_view = fs.get_or_create_feature_view(
        name="retrieval",
        query=selected_features,
        version=1,
    )

    return feature_view
