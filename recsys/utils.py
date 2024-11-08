import os
import hopsworks

from loguru import logger


def get_hopsworks_feature_store():
    HOPSWORKS_API_KEY = os.environ.get("HOPSWORKS_API_KEY")
    if HOPSWORKS_API_KEY:
        logger.info("Loging to Hopsworks using HOPSWORKS_API_KEY env var.")
        project = hopsworks.login(api_key_value=HOPSWORKS_API_KEY)
    else:
        logger.info("Login to Hopsworks using cached API KEY.")
        project = hopsworks.login()

    return project.get_feature_store()
