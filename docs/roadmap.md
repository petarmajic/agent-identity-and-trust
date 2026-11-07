# Roadmap and adoption

[Overview](../README.md) · [Product definition](product-definition.md) · [Concept paper](product-concept.pdf)

The proposed rollout starts with a **closed two-sided pilot**: one anchor channel and a small group of high-volume brands. Brands supply registered agents; the channel creates value by using their identity evidence in live access decisions. Both sides need to participate for the first version to be useful.

## Three proposed horizons

| Horizon | Supply: registered agents | Demand: channel adoption | Exit condition |
| --- | --- | --- | --- |
| **Now · 0–3 months** | Brands verify the organisation principal, register one agent, declare purpose and capabilities, bind an approved messaging account and manage runtime credentials. | One anchor channel integrates the Verification API and checks signed proof, binding, scope and lifecycle status before returning an allow/block decision. | Registered pilot agents are recognised reliably. Revoked identities no longer receive a verified result. |
| **Next · 3–6 months** | More brands use repeatable onboarding, rotate credentials and add multiple bindings under the same Agent ID. | A second surface or partner checks the same identity. Abuse reporting, step-up approval and short-lived Authorisation Receipts support sensitive actions. | The same Agent ID works on more than one surface. Sensitive actions can be approved without broad standing access. |
| **Later · 6–12 months** | Personal and machine-owned agents, delegation chains and a controlled federation pilot extend participation. | Messaging, web, voice and API channels reuse evidence. Review and suspension draw on lifecycle and abuse signals with limited disclosure of private data. | Multiple channels reuse identity evidence, and lifecycle events inform their decisions. |

These are proposed release horizons and qualitative exit conditions. They define what each stage needs to establish before the scope expands.

## Why seed both sides together

An unused registry gives brands little reason to register an agent. A verification integration gives a channel little value if it has no registered agents to recognise. The anchor channel and initial brands therefore form the same pilot rather than separate launches.

The initial support-agent scenario keeps the first release focused: one type of principal, one messaging surface and a concrete verification decision. Additional bindings and sensitive-action approval follow once that path is established.

## Deliberate exclusion: a universal trust score

The first year excludes a single number that claims whether an agent is trustworthy. The concept expects too little comparable evidence across channels to support that claim. Combining verified identity, valid authority and safe behaviour into one score would also make the verification result harder to interpret.

The product instead returns evidence tied to a particular agent, principal, channel and interaction. Behavioural signals can inform later decisions while those distinctions remain visible.

## Decisions required before a pilot

- Agree which evidence establishes a principal and which assurance levels the first channel accepts.
- Define who can suspend or revoke an identity and how those changes reach channel decisions.
- Set the meaning of the recipient-facing signal and the responsibility attached to it.
- Establish appeals and correction procedures for incorrect verification or blocking.
- Validate channel adoption, required claims, privacy constraints and acceptable integration latency.

[Discovery assumptions](discovery.md#main-assumption-to-validate) · [First-version boundary](product-definition.md#first-version-boundary)
