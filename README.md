# PIRadicator

This is a slack application that will scrape all public channels for PII, notify the user who posted the PII, and flag the message for deletion. This utility will also be written in a way that will allow for connectors to be added for different ticketing systems or alerting systems.  

## Goals

- [x] Create Slack App  
- [x] Create Class for retrieving secrets from `Azure Key Vault`
- [X] Complete message retrieval logic
- [ ] Spin Up Mongo DB using Terraform 
- [ ] Write and document `DbUpsertWorker` logic
- [ ] Write and document `SlackMessageSenderWorker` logic
- [ ] Spin up Service Bus Queue using Terraform
- [ ] 
- [ ] Decide which NLP library to leverage  
- [ ] Write `SlackMessageAnalyzerWorker` logic
- [ ] Allow for different batch sizes  
- [ ] Allow for different channels to have different retention policies
- [ ] Complete direct message sending logic
- [ ] Determine a username for the account sending direct messages  
- [ ] Build a real-time workflow for flagging PII as it's sent using Real-Time Messaging API

## Real-Time workflow  

### Overview  

The Real-Time scanning portion of the application would scan each message immediately after it's sent, then immediately flag a message as PII. The current implementaiton I am writing will scan slack at regular intervals, looking for messages older than a certain date. I'm planning on writing these as two separate applications; the core application, and the real time scanner.  

## Stretch  

- [ ] Implement CI/CD  
- [ ] Create sample Terraform for resource deployment
