# Discovery and problem framing

[Overview](../README.md) · [Concept paper](product-concept.pdf)

I chose the messaging channel operator as the first customer because the operator has to make a decision at a specific moment. A support agent has started a conversation through a familiar business account. What evidence would let the operator accept it as the brand’s agent?

## What I took from the research

| Source | Decision it informed |
| --- | --- |
| [NIST/NCCoE concept paper](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf) | I separated identity, credentials and authority. A channel should be able to recognise an agent and still deny a request outside its scope. |
| [OpenID Foundation white paper](https://openid.net/wp-content/uploads/2025/10/Identity-Management-for-Agentic-AI.pdf) | I gave the agent its own identity and linked it to the party it represents. Both remain visible when the agent acts on someone’s behalf. |
| [GoDaddy Agent Name Service architecture](https://www.godaddy.com/resources/news/building-the-agent-name-service-using-a-one-system-approach) | I used a registry to keep an agent’s identity and lifecycle history together. The caller would still have to present proof linked to that record. |

## Stakeholder insight

In a public announcement about agent-led commerce, Akamai’s Patrick Sullivan described the need to recognise both the agent and the party it represents. I carried that distinction into the messaging scenario. A channel might recognise the brand’s account and still have too little information to identify the agent using it. [Akamai and Visa announcement](https://www.akamai.com/newsroom/press-release/2025/akamai-and-visa-join-forces-to-secure-the-next-era-of-agentic-commerce).

## Problem statement

A channel operator can receive a request from an agent claiming to handle support for a brand. When the agent’s registration, credentials and approved account are checked in different places, the operator can block a legitimate agent or let an impersonator reach a customer.

I prioritised authentication at conversation start. The signed proof would let the channel check the caller against the registered agent. The current record would then tell the channel whether that agent still has permission to use the account.

## Main assumption to validate

The public statement came from commerce. I would validate the messaging use case directly with channel operators. Which claims do they need before accepting a support conversation? How quickly must a revocation reach their next decision? Their answers would shape both the Verification API and the pilot’s success criteria.

[Product definition](product-definition.md) · [Roadmap](roadmap.md)
