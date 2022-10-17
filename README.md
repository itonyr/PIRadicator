# PIRadicator

This is a slack application that will scrape all public channels for PII, notify the user who posted the PII, and flag the message for deletion. This utility will also be written in a way that will allow for connectors to be added for different ticketing systems or alerting systems.  

## Goals

- [x] Create Slack App  
- [x] Create Class for retrieving secrets from `Azure Key Vault`
- [x] Figure out how to retrieve messages from slack  
- [ ] Investigate NLP libraries  
- [ ] Imlement queueing for NLP scanning of message content  
- [ ] Retreive messages off of a queue  
- [ ] Spin up container apps  
- [ ] Lock down container apps to only communicate with one another  
- [ ] Implement an NSG so that the container apps can only reach out to slack  
- [ ] Allow for different batch sizes  
- [ ] Allow for different channels to have different retention policies
- [ ] Figure out how to send direct messages
- [ ] Determine a username for the account sending direct messages  
- [ ] Build a real-time workflow for flagging PII as it's sent using Real-Time Messaging API

## Stretch  

- [ ] Implement CI/CD  
- [ ] Use Terraform for resource deployment  
