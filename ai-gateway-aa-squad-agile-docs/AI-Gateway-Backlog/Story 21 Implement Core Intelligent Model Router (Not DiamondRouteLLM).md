---
type: Page
title: 'Story 2.1: Implement Core Intelligent Model Router (Not Diamond/RouteLLM)'
description: null
icon: null
createdAt: '2025-06-17T21:41:03.121Z'
creationDate: 2025-06-17 16:41
modificationDate: 2025-07-06 15:05
tags: []
coverImage: null
---

# Story 2.1: Implement Core Intelligent Model Router (Not Diamond/RouteLLM)

## Status: Draft

## Story

- As a **developer**,

- I want to **integrate an intelligent model router (Not Diamond or RouteLLM) with the unified LLM API**,

- so that **I can dynamically select the most suitable LLM model for a given task based on predefined criteria**.

## Acceptance Criteria (ACs)

1. The chosen intelligent router (Not Diamond or RouteLLM) is integrated into the monorepo within the `services/intelligent-router/` directory, following the project structure outlined in the Architecture Document.

2. The router can receive a request (e.g., from the Unified LLM API Service) and select an appropriate LLM model from the configured providers.

3. Initial routing logic (e.g., based on simple cost or performance preference) is implemented and demonstrable.

4. The router successfully forwards the request to the selected LLM via the `unified-llm-api` service and returns a response.

5. The routing decision is logged, including input criteria and selected model, adhering to centralized logging standards.

6. The implementation adheres to the Python coding standards defined in the Architecture Document.

7. Local testability: A simple script or CLI command can invoke the router to demonstrate model selection and request forwarding from the local development environment.

## Tasks / Subtasks

- [ ] Research and decide between Not Diamond and RouteLLM for the core router, documenting rationale based on features (cost/performance optimization vs. custom control).

- [ ] Integrate the chosen library (Not Diamond or RouteLLM) into the `services/intelligent-router/` directory.

- [ ] Implement a service within `intelligent-router` that communicates with the `unified-llm-api` service.

- [ ] Define initial routing criteria (e.g., preference for a specific model for simple tasks).

- [ ] Implement basic routing logic to select a model based on the defined criteria.

- [ ] Ensure requests are forwarded from the router to the `unified-llm-api` service and responses are handled.

- [ ] Implement logging of routing decisions and outcomes, including model selected and rationale.

- [ ] Write unit tests for the routing logic and integration with the `unified-llm-api` service using `pytest`.

- [ ] Create a simple test script or CLI command to demonstrate router functionality.

- [ ] Document API client setup and routing configuration steps in a README within the `intelligent-router` service directory.

## Dev Technical Guidance

This story is fundamental for implementing the AI Gateway's core intelligence, enabling dynamic model selection and optimization.

- **Dependencies:** This story **depends on Epic 1: Core Gateway Infrastructure & Unified Access** (specifically Story 1.2: Implement Unified LLM API for the internal LLM service).

- **Technology Stack:** Choose between Not Diamond and RouteLLM. Python is the primary language for this backend service. FastAPI is the recommended backend framework.

- **API Design:** The router service should expose a clear API for model selection and request forwarding, adhering to the "API Design and Standards" in the Architecture Document.

- **Routing Logic:** The initial routing can be simple, but the design should allow for future expansion with more complex rules and optimization features.

- **Observability:** Implement robust logging, ensuring that routing decisions, selected models, and any relevant metrics (e.g., decision latency) are captured. Adhere to the "Centralized Logging" and "Monitoring & Metrics Collection" guidelines in the Architecture Document.

- **Error Handling:** Ensure the router gracefully handles failures from the `unified-llm-api` service and logs them appropriately, following the "Error Handling Strategy".

- **Security:** Adhere to "Security Best Practices" in the Architecture Document, especially concerning secure communication between internal services.

- **References:**

    - Not Diamond Documentation: [https://www.notdiamond.ai/](https://www.notdiamond.ai/)

    - RouteLLM Documentation: [https://github.com/lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM)

    - AI Gateway Architecture Document: `docs/architecture.md`

    - AI Gateway Product Requirements Document: `docs/prd.md`

    - Story 1.2: `docs/stories/1.2.story.md`

## Story Progress Notes

### Agent Model Used: Fiona "Flux" Rivera (SM Agent)

### Completion Notes List

{To be filled by Developer Agent upon completion}

### Change Log

- Initial Draft | 2025-06-17 | Fiona "Flux" Rivera (SM Agent)


