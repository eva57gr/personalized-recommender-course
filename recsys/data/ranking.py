def create_feature_views(fs):
    customers_fg = fs.get_feature_group(
        name="customers",
        version=1,
    )

    articles_fg = fs.get_feature_group(
        name="articles",
        version=1,
    )

    rank_fg = fs.get_feature_group(
        name="ranking",
        version=1,
    )

    selected_features_customers = customers_fg.select_all()
    fs.get_or_create_feature_view(
        name="customers",
        query=selected_features_customers,
        version=1,
    )

    selected_features_articles = articles_fg.select_except(["embeddings"])
    fs.get_or_create_feature_view(
        name="articles",
        query=selected_features_articles,
        version=1,
    )

    # Select features
    selected_features_ranking = rank_fg.select_except(["customer_id", "article_id"])
    feature_view_ranking = fs.get_or_create_feature_view(
        name="ranking",
        query=selected_features_ranking,
        labels=["label"],
        version=1,
    )

    return feature_view_ranking
