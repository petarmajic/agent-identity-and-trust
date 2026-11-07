# Discovery and problem framing

[Overview](../README.md) · [Concept paper](product-concept.pdf)

The assignment asks for product discovery followed by product definition: research the identity gap, identify a stakeholder's need, choose a specific failure and translate it into a product concept. I focused on the channel operator that must decide whether to accept an incoming agent interaction.

## Research and product implications

| Research | Finding used in the case study | Product decision |
| --- | --- | --- |
| [NIST/NCCoE concept paper, February 2026](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf) | Agent identity involves identification, authentication, authority, delegation and audit. These require separate checks. | Keep persistent identity, credentials, authority and lifecycle status distinct in the product model. |
| [OpenID Foundation white paper, October 2025](https://openid.net/wp-content/uploads/2025/10/Identity-Management-for-Agentic-AI.pdf) | An agent acting through a user's account can lose its own identity. Explicit delegation preserves the distinction between the agent and the party it represents. | Link agent and principal records while retaining both identities during verification. |
| [GoDaddy ANS architecture](https://www.godaddy.com/resources/news/building-the-agent-name-service-using-a-one-system-approach) | DNS-based identity, certificates and a transparency log provide a basis for registration and lifecycle evidence. | Use registration as the source of identity evidence, then check that evidence against the active caller. |

The common product question is how a channel can connect a presented Agent ID to a verified principal, a valid runtime credential and current lifecycle status. The resulting direction is a registry-backed verification service.

## Stakeholder insight

I used a published statement from **Patrick Sullivan, Akamai's CTO for Security Strategy**, in the [December 2025 Akamai–Visa announcement](https://www.akamai.com/newsroom/press-release/2025/akamai-and-visa-join-forces-to-secure-the-next-era-of-agentic-commerce). His statement identifies a dual-identity requirement: recognising the agent and the party it acts for.

My product implication was to carry the agent–principal relationship into the interaction itself. A name or previously issued registration record gives the channel less information than a current check of that relationship and its credentials.

This is a public stakeholder statement from the commerce context. It supports the selected direction; channel-specific requirements still need direct validation.

## Problem statement

**Channel operators trying to accept legitimate AI-agent traffic struggle to verify that an incoming caller is the registered agent of its claimed principal. Identity records, principal bindings and runtime authentication are fragmented across systems. This can block legitimate agents while allowing impersonators or unauthorised automation to reach users and protected services.**

| Part | Selected focus |
| --- | --- |
| User | Communication channel operator. |
| Goal | Accept legitimate agents while protecting users and downstream services. |
| Failure | The channel cannot reliably verify the active agent and its relationship to the claimed principal at interaction time. |
| Root cause | Fragmented identity, binding and authentication mechanisms. |
| Consequence | Incorrect blocking, impersonation risk and unauthorised access. |

**Authentication** is the first component to prioritise. Registration supplies the record; runtime authentication establishes whether the caller controls the corresponding credentials. Validation then checks status, channel binding and permitted scope.

## Main assumption to validate

Channel operators must be willing and technically able to consume interoperable identity evidence in their access decisions. This assumption determines whether channel-integrated verification is a viable first product.

Further discovery needs to establish the claims each channel requires, the evidence needed for higher-risk interactions, issuer responsibilities and acceptable privacy, latency and integration constraints.

[Product definition](product-definition.md) · [Roadmap](roadmap.md)
