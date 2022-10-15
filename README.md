# PIRadicator
This is a slack application that will scrape all public channels for PII, notify the user who posted the PII, and flag the message for deletion. This utility will also be written in a way that will allow for connectors to be added for different ticketing systems or alerting systems. 

## Goals

- [ ] Create Slack App 

- [ ] Figure out how to retrieve messages from slack 
- [ ] Investigate AI libraries for scraping the messages within slack 
- [ ] Implement CI/CD 
- [ ] Use Terraform for resource deployment
- [ ] Place messages onto a queue 
- [ ] Retreive messages off of a queue 
- [ ] Spin up container apps 
- [ ] Lock down container apps to only communicate with one another 
- [ ] Implement an NSG to that the container apps can only reach out to slack 
