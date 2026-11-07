# Roadmap and adoption

[Overview](../README.md) · [Product definition](product-definition.md) · [Concept paper](product-concept.pdf)

I proposed recruiting one messaging channel and a small group of brands for the same pilot. A brand has little reason to register a support agent until a channel will recognise it. The channel needs registered agents before it can find out whether the identity check helps it make a decision.

## Three proposed horizons

These time windows describe the plan I submitted. Each phase has a question the pilot partners would need to answer before expanding it.

| Planned window | What changes | What the partners would look for |
| --- | --- | --- |
| 0–3 months | Each brand registers one support agent and binds it to one messaging account. The channel checks its proof, binding, scope and current status at conversation start. | Can the channel recognise an active registered agent and block a new conversation once it reads a revoked status? |
| 3–6 months | Add repeatable onboarding, credential rotation, a second channel binding and abuse reporting. Introduce short-lived Authorisation Receipts for sensitive actions. | Can a second channel recognise the same Agent ID? Can the agent obtain approval for a single action such as a refund? |
| 6–12 months | Extend the model to personal and machine-owned agents, delegation chains and a limited pilot with another issuer. | Can participating channels reuse identity evidence and act on lifecycle or abuse reports while limiting what they disclose? |

## Why I left out a universal trust score

A support agent can prove which brand it represents and still give a customer a poor answer. A single score would hide which of those questions the channel actually checked. I kept identity, authority and observed behaviour separate, especially while the pilot would have little comparable evidence across channels.

## Questions for the pilot partners

- What evidence is enough to verify the principal, and what should the recipient understand when an agent appears as verified?
- Who can revoke an Agent ID, and how quickly does the channel need to see that change?
- Who reviews an appeal if a legitimate agent is blocked?
- Which records can the channel access, and how long can it wait for a verification result?

[Discovery assumption](discovery.md#main-assumption-to-validate) · [First-version boundary](product-definition.md#first-version-boundary)
