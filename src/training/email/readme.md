---
ParentService:
  - PIRadicator
  - PIRadicatorSlack
Dependencies:
  - SlackMessageSenderWorker
  - DbUpsertWorker
---

# Email PII generator and formatter  

## Overview  

This training module will reach out to a fake PII generator, then add the PII onto two service bus subscriptions. The `DbUpsert` subscription will have the `DbUpsertWorker` as a consumer and the `SlackMessageOutbound` will have the `SlackMessageSenderWorker` as a consumer.
