# PIRadicator K8's RabbitMQ instance

## Overview

This RabbitMQ instance will have many subscriptions and many consumers. It needs to be built in a way that can withstand high levels of traffic when needed, but it's primary intent is to be horizontally scalable as this is going to be running in Kubernetes.

## Queues

### `SlackMessageOutbound`

#### Consumers

__Slack Message Sender__ -
Sends slack messages to a specificed channel.

Message Contents:

```json
{ 
    "ChannelId": "{ChannelId}",
    "MessageContents": "{MessageContents}",
    "MessageGuid": "{GUID}"
}

```

__MessageAnalyzerInbound__ -  
Messages that need to be analyzed by an analyzer  

Message Contents:  

```json  
{
    "AnalyzerType": "{NameOf3rdPartyService}",
    "MessageInfo": {
        "MessageContents": "{MessageContents}",
        "MessageGuid": "{MessageGuid}"
    },
    "AttemptAnon": true
}

```  

__MessageAnalyzerOutbound__ -  
Messages that have been reviewed by the analyzer and the results of the scan.  

Message Contents:  

```json  
{
    "MessageInfo": {
        "MessageGuid": "",
        "MessageContents": ""
    },
    "AnalysysResults": {
        "ContainsPII": true,
        "PIICHUNK": ""
    }
}
```
