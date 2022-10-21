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

### PII Generation TODO

- [ ] Create an inxex of a bunch of email domains  
- [ ] Create an index of a buch of street post-fixes  
- [ ] Create an index of commmon first and last names  
- [ ] Write logic for fake email generation  
- [ ] Write logic for fake address generation  
- [ ] Write logic for fake full name generation  
