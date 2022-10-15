import os
import sys
import logging
import requests
from slack_sdk import WebClient
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import PIRadVault as pv


def get_all_channels(client): 
    try: 
        store = {}
        channels = client.conversations_list()['channels']
        logging.info('Retrieved {0} channels from slack'.format(len(channels)))
        return channels
    except: 
        logging.error('Unable to get list of channels')

def main(): 
    print('PIRadicator starting up..')
    #client = WebClient(token=os.environ['SLACK_API_TOKEN'])
    connectionString = str(pv.SecretValue(Secret_Name="SlackConnectionString").get()) 
    client = WebClient(connectionString)
    response = get_all_channels(client=client)

main()

