import logging
from slack_sdk import WebClient

class Messages: 
    def __init__(self,Connection_String,Channel_Id=None,Message_Id=None,limit=1,inclusive=True):
        # Connection String for the Slack SDK. 
        self.Connection_String = Connection_String
        # Limit of messages to retrieve. Set to 1 by default 
        self.limit = limit
        # Inclusive 
        self.inclusive = inclusive
        # False by default. If True, will not return archived channels. 
        if Channel_Id !=None:
            self.Channel_Id = Channel_Id
        else: 
            raise ValueError('Channel ID required to retrieve messages.')
        # Set to None by default, used in the Get method 
        if Message_Id != None: 
            self.Message_Id = Message_Id
        
        
    def Get_All(self):
        # Initilize slack client 
        client = WebClient(self.Connection_String)
        try: 
            messages = client.conversations_history(
                channel=self.Channel_Id)['messages']
            logging.info('Retrieved {0} messages from conversation{1}'.format(len(messages),self.Channel_Id))  # type: ignore
            if len(messages) is 0: #type: ignore
                logging.error('Slack API returned no messages.')
                
            return messages
        except: 
            logging.error('Unable to get list of messages')

# If there is no channelID provided this function will fail.
    def Get(self):
        if self.Message_Id is None: 
            # raise and log an exception if there is no channel Id. 
            message = 'No Channel_Id provided to Messages.Get() method. Please proivde a valid Channel_Id'
            logging.error(message)
            raise ValueError(message)

        # Initilize slack client 
        client = WebClient(self.Connection_String)
        try: 
            # Pass the channel Id into the 'type' field to list a specific channel 
            messages = client.conversations_history(
                channel=self.Channel_Id,
                latest=self.Message_Id,
                limit=self.limit,
                inclusive=self.inclusive
                )['messages']
            logging.info('Retrieved {0} messages from conversation{1}'.format(len(messages),self.Channel_Id))  # type: ignore
            return messages
        except: 
            # If any unexpected exceptions occur, throw this error.
            message = ('An unexpected error occured. Unable to get messges from channel: {0}'.format(self.Channel_Id))
            logging.error(message)
            raise Exception(message)