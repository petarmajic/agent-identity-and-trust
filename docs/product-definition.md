# Product definition

[Overview](../README.md) · [Discovery](discovery.md) · [Concept paper](product-concept.pdf)

I designed Agent Trust Gateway for a messaging channel that needs to decide whether to accept a conversation from a brand’s support agent. In the proposed flow, the gateway supplies the identity evidence and the channel applies its own access policy.

## Identity model

A brand can operate several agents. I gave each agent its own **Agent ID** so the channel can distinguish them even when they represent the same brand. The principal record identifies the person, organisation or system responsible for the agent.

| Record | What it tells the channel |
| --- | --- |
| Principal | Who is responsible for the agent, how their identity was verified and whether their registration is active. |
| Agent identity | Which Agent ID the caller claims, which principal it represents and which public key the gateway should use to check its proof. The record also holds the agent’s declared purpose, capabilities, version and status. |
| Channel binding | Which account or endpoint the agent may use, for what purpose and until when. |
| Authorisation grant | Which capabilities the principal grants the agent, on which resources and under what limits. |

The Agent ID stays the same when an agent changes its display name, account or software version. A change of principal or control that creates an independent actor calls for a new Agent ID.

![Proposed architecture. Registration links the agent to a principal, a channel binding and an authorisation grant. At conversation start, the Verification API checks those records before the channel applies its policy.](../assets/platform-overview.svg)

## Runtime verification

1. **Authenticate the caller.** The agent presents a short-lived signed proof. The Verification API checks it against the registered public key and credential for that Agent ID.
2. **Check current authority.** The gateway checks the principal relationship, lifecycle status, channel binding and capability scope for this interaction.
3. **Apply channel policy.** The channel uses the result to allow or block the conversation. A verified signal tells the recipient which agent is speaking, for whom and on which channel.

Consider a support conversation that turns into a refund request. Verification covers the agent’s identity and its authority to use the support account. I deferred approval of the refund itself to a later phase, where a short-lived Authorisation Receipt would cover that specific action.

## Identity continuity and revocation

The registry keeps the Agent ID after revocation so a reviewer can trace the earlier decision and the later block to the same agent. The audit history covers checks and lifecycle changes recorded by participating channels and the gateway. A block depends on a fresh check that reads the revoked status. Revocation delivery time and the handling of conversations already underway are open design questions. [Illustrated example](../README.md#one-agent-two-conversations).

## First-version boundary

| Included in the pilot | Why it is needed |
| --- | --- |
| Principal verification, agent registration and a channel binding | A brand can register one support agent for one approved messaging account. |
| Credential issuance, Verification API and a channel adapter | The channel can check a caller at the start of a conversation. |
| Lifecycle status, revocation and audit history | The channel can act on an updated record and review an earlier decision. |
| Developer API and console | Owners can submit and update declared metadata. The platform controls credentials and lifecycle state. |

Before launch, the pilot partners would need to agree on acceptable identity evidence, who may suspend or revoke an agent and how an owner can challenge an incorrect block. Channels would have read-only access to verification evidence and could submit abuse reports. Protocol formats and service implementation remain engineering work beyond this product definition.

[Roadmap](roadmap.md) · [Figure source](../scripts/draw_figures.py)
