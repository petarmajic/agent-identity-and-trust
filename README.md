# Agent Identity & Trust

Product discovery and definition for **Agent Trust Gateway**, a proposed platform for verifying AI agents and the organisations or people they represent. I researched the identity problem, selected the first customer and use case, and defined the identity model, verification flow and product roadmap.

**Product Management · Product Discovery · Problem Framing · Product Definition · MVP Scoping · Roadmapping**

[Full concept paper](docs/product-concept.pdf)

## Problem and first customer

The case study focuses on a **communication channel operator** receiving traffic from a brand's customer-support agent. The channel needs to establish who is making the request, which brand the agent represents and whether that relationship is still valid.

I chose **authentication at interaction time** as the first problem to solve. The proposed pilot connects one channel with a small group of brands, each registering an agent against an approved business messaging account.

## Proposed first version

![Agent Trust Gateway: verified brand registration creates linked identity records; the Verification API checks a signed runtime proof against current identity, binding, scope and lifecycle evidence before the channel allows or blocks an interaction](assets/platform-overview.svg)

**Figure 1.** Proposed identity model and verification flow. Registration establishes the records used during an interaction. The channel receives a current verification result and applies its access policy. [Identity model and product scope](docs/product-definition.md).

The verification signal confirms the agent's identity, its principal and its approved channel binding. Sensitive actions such as refunds or account changes require the separate authorisation flow planned for the next phase.

## Product work and decisions

| Area | What I worked on | Detail |
| --- | --- | --- |
| **Discovery and problem framing** | Compared NIST, OpenID and ANS material, analysed a published stakeholder statement and chose verification of the active caller as the first problem to address. | [Research and problem statement](docs/discovery.md) |
| **Customer and value proposition** | Chose the channel operator as the first customer and a brand-owned support agent as the initial scenario. | [First customer](docs/product-definition.md#customer-and-first-use-case) |
| **Identity and trust model** | Defined separate principal, agent, channel-binding and authorisation records. Distinguished registration, authentication and policy checks. | [Records and verification](docs/product-definition.md#identity-model) |
| **MVP scope** | Included registration, runtime verification, lifecycle status and revocation. Deferred action-specific receipts, behavioural scoring and federation. | [First-version boundary](docs/product-definition.md#first-version-boundary) |
| **Roadmap and adoption** | Planned registered agents and channel integrations together, with an exit condition for each stage. | [Three-horizon roadmap](docs/roadmap.md) |

## Scope and adoption

The pilot needs both brands that register agents and a channel that checks their identities. The roadmap develops these two sides together.

| Proposed horizon | Registered agents | Channels and verification |
| --- | --- | --- |
| **Now · 0–3 months** | A small group of brands; one agent and one approved account per brand. | One anchor channel checks identity, binding, scope and status. |
| **Next · 3–6 months** | Repeatable onboarding, credential rotation and multiple channel bindings. | A second surface; abuse reporting and approval for sensitive actions. |
| **Later · 6–12 months** | Personal and machine-owned agents, delegation chains and a federation pilot. | Reuse of identity evidence across messaging, web, voice and API channels. |

The first pilot's exit condition is reliable recognition of registered agents and rejection of revoked identities. A universal trust score is excluded from the first year because it would combine identity, authority and behaviour into one signal. [Roadmap, exit conditions and governance](docs/roadmap.md).

## Repository guide

| Material | Contents |
| --- | --- |
| [Concept paper](docs/product-concept.pdf) | Full individual submission: discovery, product definition, architecture and roadmap. |
| [Discovery](docs/discovery.md) | Research, stakeholder insight, problem statement and the main adoption assumption. |
| [Product definition](docs/product-definition.md) | Customer scenario, identity records, runtime checks and MVP decisions. |
| [Roadmap](docs/roadmap.md) | Supply and demand, staged capabilities, exit conditions and launch decisions. |
| [Assignment](docs/assignment.html) | Original course brief in HTML. |

*Individual assignment for Fundamentals of Product Management at [FER Zagreb](https://www.fer.unizg.hr/en/course/fopm_a), with Infobip, 2026.*
