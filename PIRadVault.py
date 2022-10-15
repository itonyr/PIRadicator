from mimetypes import init
import os
import logging
from typing_extensions import Self
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Python 3.10 function that will retrive secrets from AKV. 

class SecretValue: 
    
    def __init__(self,Secret_Name): 
        self.vault_name = os.getenv("VAULT_NAME")
        self.secret_name = Secret_Name
    
    def get(self):
        
        # Build the AKV URI string 
        Uri = f"https://{self.vault_name}.vault.azure.net"
        logging.info('Retreiving secret: {0} from: {1}'.format(self.secret_name,self.vault_name))
        resp = SecretClient(Uri,DefaultAzureCredential()).get_secret(self.secret_name)
        
        # If the secret value is Null, throw an error
        if resp != None: 
            return str(resp)
        else: 
            message = 'Unable to retrieve secret{0}}'.format(self.secret_name)
            logging.error(message)
            raise ValueError(message)
