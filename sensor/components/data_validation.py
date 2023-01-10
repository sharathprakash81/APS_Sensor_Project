from sensor.entity import artifact_entity, config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os, sys
import pandas as pd
from  typing import Optional

class DataValidation:
    
    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.validation_error = dict()
        except Exception as e:
            raise SensorException(e, sys)
        
      
    def drop_missing_values_columns(self,df:pd.DataFrame, threshold)-> Optional[pd.DataFrame]:
        """
        This function drops column values containing missing values more than specified threshold
        
        df: accepts pandas DataFrame
        threshold: percentage of missing values
        ================================================================
        returns: pandas DataFrame if atleast one column is available after missing columns are dropped else None
        """
            
        try:
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum()/df.shape[0]
            #* Selecting column names which contain null values
            drop_column_names = null_report[null_report>threshold].index
            self.validation_error["dropped_columns"]=drop_column_names
            df.drop(list(drop_column_names),axis=1,inplace=True)
            
            #return None
            if len(df.columns)==0:
                return None
            return df
                
        except Exception as e:
            raise SensorException(e, sys)
        
    def is_required_columns_exists(self,base_df:pd.DataFrame, current_df:pd.DataFrame)->bool:
        try:
            base_columns = base_df.columns
            current_columns = current_df.columns
            
            missing_columns =[]
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_column)
            
            if len(missing_columns)>0:
                self.validation_error["Missing Columns"] = missing_columns
                return False
            return True
        
        except Exception as e:
            raise e
    
    def data_drift(self, base_df:pd.DataFrame, current_df:pd.DataFrame):
        try:
            pass
        
        except Exception as e:
            raise SensorException(e,sys)        
           
    
    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        pass
    
    
    