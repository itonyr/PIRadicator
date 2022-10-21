import logging
import random
import requests as r 

class Generator(): 
    def __init__(self): 
        logging.info("Email Generator Initalized")
   ## In the future, we should have the list of possible domains in AppConfig.
   ## def Get_Domains_From_AppConfig(): 
   
   ## Just for POC: 'Domains' thing should probably not exist in the future. 
   # We shouldn't train this thing to only look for specific domains 
   # but instead to look for patterns that make up an email. I'll get that done eventually.
    def create(self): 
        ## List of all the domains I could think of quickly 
        Domains = ["gmail.com","aol.com","ymail.com","yahoo.com","outlook.com","protonmail.com"]
        url = "https://random-word-api.herokuapp.com/word"  
        resp = r.get(url).json()
        
        # Throw an error if we don't get 
        if resp['status_code'] != 200:
            message = 'Unable to retrieve email base name'
            logging.error(message)
            raise ValueError(message) 

        # Pick a random domain from our domain list 
        Domain = Domains[random.randrange(len(Domains))]
        logging.info("Creating email with domain {0}".format(resp))
    
        # Use our results from the API call to the random word generator to create 
        # a fake email
        email = "{0}@{1}".format(resp[0],Domain)
        logging.info("created email {0}".format(email))
        return email