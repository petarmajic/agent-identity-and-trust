# Agent Identity & Trust

**Agent Trust Gateway** is my product concept for verifying an AI agent, the organisation or person it represents and its authority to use a channel. The case study covers **Discovery and Definition**, from researching the problem to specifying the first product version.

**Product Management · Product Discovery · Problem Framing · Product Definition · MVP Scoping · Roadmapping**

[Full concept paper](docs/product-concept.pdf)

## Task and problem

The assignment was to define an identity and trust platform for AI agents. It required research, stakeholder insight and a specific problem statement, followed by a value proposition, product definition, annotated architecture and roadmap.

I focused on a **communication channel operator** receiving traffic from a brand's customer-support agent. A familiar name or business account does not establish which agent is making a request, whether it represents the claimed brand or whether its authority is still valid. The channel needs that evidence when the interaction happens.

## How I approached the task

| Phase | Work and outcome |
| --- | --- |
| **Discovery** | Compared NIST, OpenID and ANS material and analysed a published stakeholder statement. Selected the channel operator as the first customer and identified verification of the active caller as the problem to solve. [Research and assumptions](docs/discovery.md). |
| **Definition** | Defined Agent Trust Gateway's value proposition, linked identity records and runtime checks. Scoped a pilot around one messaging channel, then planned additional bindings, sensitive-action approval and federation. [Product definition](docs/product-definition.md). |

## The idea: authenticate at interaction time

Registration gives the agent a stable identity. At conversation start, the channel checks the caller's signed proof against the **current** identity record, principal relationship, approved account, capability scope and lifecycle status.

![One agent retains Agent ID A-01 across registration, an allowed interaction and revocation. The same registered identity is blocked when the next verification reads its revoked status.](assets/agent-lifecycle.svg)

**Figure 1.** An illustrative interaction using the proposed product flow. The Agent ID stays the same after revocation; the updated status changes the verification result. Account and agent identifiers are examples.

I prioritised this check so a change in status can change the channel's next decision, while the agent keeps its identity and history.

## Identity, visibility and revocation

The registry connects the agent to its principal, approved channels and permitted scope. Verification events and lifecycle changes remain associated with that Agent ID in the audit history.

| Product decision | What the channel can establish |
| --- | --- |
| **Separate agent and principal identities** | Which agent is acting and for whom, using the registered relationship and checked credentials. |
| **Approved channel bindings** | Where the agent is authorised: approved accounts or endpoints, permitted purpose and binding validity. |
| **Current-status verification** | Whether the identity is still valid. A check that reads a revoked status rejects the verified result. |
| **Audit history by Agent ID** | Which verification decisions, identity updates and lifecycle changes have been recorded for that agent. |

Visibility comes from **registered channel bindings and recorded checks**. The identity signal establishes the agent, its principal and its approved channel context. Sensitive actions such as refunds or account changes require the separate authorisation flow planned for the next phase.

[Architecture, identity fields and verification checks](docs/product-definition.md#identity-model)

## First version and rollout

The pilot connects a small group of brands with **one anchor channel**. Each brand registers one agent against an approved messaging account. This gives both sides a reason to participate: the brands supply identities and the channel uses them in its verification decisions.

| Proposed horizon | Product scope | Outcome to establish |
| --- | --- | --- |
| **Now · 0–3 months** | Principal verification, registration, channel binding, runtime checks, status and revocation. | Recognise registered pilot agents and reject revoked identities. |
| **Next · 3–6 months** | Repeatable onboarding, credential rotation, additional bindings, abuse reporting and approval for sensitive actions. | Verify the same Agent ID on a second surface and approve sensitive actions without broad standing access. |
| **Later · 6–12 months** | Personal and machine-owned agents, delegation chains, behavioural signals and a controlled federation pilot. | Reuse identity evidence across more channels and issuers. |

A universal trust score is outside the first-year scope. The product keeps verified identity, valid authority and observed behaviour distinct. [Roadmap, adoption and governance](docs/roadmap.md).

## Repository guide

| Material | Contents |
| --- | --- |
| [Concept paper](docs/product-concept.pdf) | Full individual submission: discovery, product definition, architecture and roadmap. |
| [Discovery](docs/discovery.md) | Sources, stakeholder insight, problem statement and adoption assumptions. |
| [Product definition](docs/product-definition.md) | Value proposition, customer scenario, identity model, architecture and MVP decisions. |
| [Roadmap](docs/roadmap.md) | Supply and demand, planned capabilities, exit conditions and launch decisions. |
| [Assignment](docs/assignment.html) | Original course brief in HTML. |

*Individual assignment for Fundamentals of Product Management at [FER Zagreb](https://www.fer.unizg.hr/en/course/fopm_a), with Infobip, 2026.*
