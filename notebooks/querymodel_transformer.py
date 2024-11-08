
import os
import numpy as np
import pandas as pd
from datetime import datetime

import hopsworks

import logging


class Transformer(object):
    
    def __init__(self):            
        # Connect to the Hopsworks
        project = hopsworks.connection().get_project()
        ms = project.get_model_serving()
    
        # Retrieve the 'customers' feature view
        fs = project.get_feature_store()
        self.customer_fv = fs.get_feature_view(
            name="customers", 
            version=1,
        )
        # Retrieve the ranking deployment 
        self.ranking_server = ms.get_deployment("rankingdeployment")
        
        
    def preprocess(self, inputs):
        # Check if the input data contains a key named "instances"
        # and extract the actual data if present
        inputs = inputs["instances"] if "instances" in inputs else inputs
        
        # Extract customer_id and transaction_date from the inputs
        customer_id = inputs["customer_id"]
        transaction_date = inputs["transaction_date"]
        
        # Extract month from the transaction_date
        month_of_purchase = datetime.fromisoformat(inputs.pop("transaction_date"))
        
        # Get customer features
        customer_features = self.customer_fv.get_feature_vector(
            {"customer_id": customer_id}, 
            return_type="pandas",
        )
        
        # Enrich inputs with customer age
        inputs["age"] = customer_features.age.values[0]   
        
        # Calculate the sine and cosine of the month_of_purchase
        month_of_purchase = datetime.strptime(transaction_date, "%Y-%m-%dT%H:%M:%S.%f").month
        
        # Calculate a coefficient for adjusting the periodicity of the month
        coef = np.random.uniform(0, 2 * np.pi) / 12
        
        # Calculate the sine and cosine components for the month_of_purchase
        inputs["month_sin"] = float(np.sin(month_of_purchase * coef)) 
        inputs["month_cos"] = float(np.cos(month_of_purchase * coef))
                
        return {
            "instances" : [inputs]
        }
    
    def postprocess(self, outputs):
        # Return ordered ranking predictions        
        return {
            "predictions": self.ranking_server.predict({ "instances": outputs["predictions"]}),
        }
