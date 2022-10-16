import logging
from slack_sdk import WebClient

class Channels: 
    def __init__(self,Connection_String,Channel_Id=None,Exclude_Acrhived=False):
        # Connection String for the Slack SDK. 
        self.Connection_String = Connection_String
        # Set to None by default, not used in Get_All method. 
        self.Channel_Id = Channel_Id
        # False by default. If True, will not return archived channels. 
        self.Exclude_Archived = Exclude_Acrhived

    def Get_All(self):
        # Initilize slack client 
        client = WebClient(self.Connection_String)
        try: 
            channels = client.conversations_list(exclude_archived=self.Exclude_Archived)['channels']
            logging.info('Retrieved {0} channels from slack'.format(len(channels)))  # type: ignore
            if len(channels) is 0: #type: ignore
                logging.error('Slack API returned no channels.')
                
            return channels
        except: 
            logging.error('Unable to get list of channels')

# If there is no channelID provided this function will fail.
    def Get(self):
        if self.Exclude_Archived != False:
            message = 'The Get method does not support the Exclude Archived parameter.'
            logging.error(message)
        if self.Channel_Id is None: 
            # raise and log an exception if there is no channel Id. 
            message = 'No Channel_Id provided to Channels.Get() method. Please proivde a valid Channel_Id'
            logging.error(message)
            raise ValueError(message)

        # Initilize slack client 
        client = WebClient(self.Connection_String)
        try: 
            # Pass the channel Id into the 'type' field to list a specific channel 
            channels = client.conversations_list(
                types=str(self.Channel_Id)
                )['channels']
            logging.info('Retrieved {0} channels from slack'.format(len(channels)))  # type: ignore
            return channels
        except: 
            # If any unexpected exceptions occur, throw this error.
            message = ('An unexpected error occured. Unable to get list of channels')
            logging.error(message)
            raise Exception(message)