---
type: Page
title: 'Story 5.3: Implement Virtual Key Management'
description: null
icon: null
createdAt: '2025-06-18T21:24:30.76Z'
creationDate: 2025-06-18 16:24
modificationDate: 2025-07-06 14:57
tags: []
coverImage: null
---

# Story 5.3: Implement Virtual Key Management

## Status: Draft

## Story

- As a **developer**,

- I want to **create and manage virtual keys within the AI Gateway**,

- so that **I can abstract away raw LLM provider API keys and apply specific configurations or rate limits per virtual key**.

## Acceptance Criteria (ACs)

1. A dedicated storage mechanism (e.g., PostgreSQL database table `virtual_keys`) is set up for virtual keys.

2. Users can create unique virtual keys that map to one or more underlying LLM provider API keys through a dedicated interface (e.g., via the API endpoint in `services/prompt-virtual-keys-service/` or the dashboard UI).

3. Each virtual key can have associated configurable parameters, such as a default LLM model, specific rate limits (e.g., RPM, TPM), or cost caps.

4. Requests made using a virtual key are correctly routed by the Intelligent Router Service according to its associated configuration.

5. Usage and cost can be tracked per virtual key, feeding into the observability system.

6. Demonstrate creating a virtual key, associating it with an LLM provider, and making a request through it that adheres to its configured parameters (e.g., rate limit, default model).

7. The implementation adheres to the Python and TypeScript coding standards defined in the Architecture Document.

8. Local testability: A simple script or CLI command can define a virtual key and demonstrate its usage for an LLM call, verifying the application of its associated configurations.

## Tasks / Subtasks

- [ ] Design the `virtual_keys` database schema (referencing `VirtualKey` data model in Architecture Document).

- [ ] Implement database interaction (CRUD operations) for virtual keys within the `services/prompt-virtual-keys-service/`.

- [ ] Develop API endpoint(s) for virtual key management (create, retrieve, update, delete).

- [ ] Modify the Intelligent Router Service (from Epic 2) to resolve virtual keys to actual LLM provider configurations and apply per-key parameters (rate limits, default model).

- [ ] Implement logic to track usage and cost specifically attributed to each virtual key.

- [ ] Ensure raw LLM provider API keys mapped to virtual keys are securely stored (encrypted) and accessed only when needed.

- [ ] Write unit tests for virtual key CRUD operations and their resolution logic within the router.

- [ ] Create a simple test script or CLI command to demonstrate virtual key management and application.

- [ ] Document virtual key API endpoints and usage in the `services/prompt-virtual-keys-service/` README.

## Dev Technical Guidance

This story is crucial for providing granular control, enhanced security, and fine-grained cost management over LLM interactions.

- **Dependencies:** This story relies on **Epic 2: Intelligent Routing & Optimization Engine** for the Intelligent Router Service. It also shares the `services/prompt-virtual-keys-service/` with Story 5.1 and 5.2.

- **Technology Stack:** Python, FastAPI for the backend service. PostgreSQL for data persistence.

- **Data Models:** Refer to the `VirtualKey` data model in the Architecture Document for the schema. Ensure secure storage for `mappedProviderKeys`.

- **Security:** This is a high-security story. Adhere strictly to "Security Best Practices" in the Architecture Document, especially "Secrets Management," "Authentication/Authorization Checks," and "Data Protection." Raw API keys MUST be encrypted at rest.

- **Integration with Router:** The `intelligent-router` service needs to be modified to accept virtual keys and apply their configurations. This modifies the critical path of LLM requests.

- **Observability Impact:** The ability to track usage and cost per virtual key is vital for billing and reporting. Ensure integration with metrics collection (Epic 4).

- **References:**

    - AI Gateway Architecture Document: `docs/architecture.md`

    - AI Gateway Product Requirements Document: `docs/prd.md`

    - Epic 2: `docs/prd.md#epic-2-intelligent-routing--optimization-engine`

    - Story 5.1: `docs/stories/5.1.story.md`

    - Story 5.2: `docs/stories/5.2.story.md`

## Story Progress Notes

### Agent Model Used: Fiona "Flux" Rivera (SM Agent)

### Completion Notes List

{To be filled by Developer Agent upon completion}

### Change Log

- Initial Draft | 2025-07-06 | Fiona "Flux" Rivera (SM Agent)


