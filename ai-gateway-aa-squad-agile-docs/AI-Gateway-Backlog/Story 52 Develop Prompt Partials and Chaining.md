---
type: Page
title: 'Story 5.2: Develop Prompt Partials and Chaining'
description: null
icon: null
createdAt: '2025-06-18T21:02:52.634Z'
creationDate: 2025-06-18 16:02
modificationDate: 2025-07-06 14:58
tags: []
coverImage: null
---

# Story 5.2: Develop Prompt Partials and Chaining

## Status: Draft

## Story

- As a **developer**,

- I want to **define and combine smaller "prompt partials" to build complex prompts**,

- so that **I can reuse segments of prompts and create more modular and maintainable LLM interactions**.

## Acceptance Criteria (ACs)

1. A dedicated storage mechanism (e.g., PostgreSQL database table `prompt_partials`) is set up for prompt partials.

2. Users can define and save named prompt partials through a dedicated interface (e.g., via the API endpoint in `services/prompt-virtual-keys-service/` or the dashboard UI).

3. Prompt templates (from Story 5.1) can reference and correctly combine multiple prompt partials.

4. The gateway's services (e.g., Unified LLM API, Intelligent Router) correctly assemble a full prompt from a template and its referenced partials, resolving all partials in the correct order.

5. Prompt partials support versioning for backward compatibility, similar to templates.

6. Demonstrate a complex prompt successfully built and executed using a template and at least two prompt partials.

7. The implementation adheres to the Python and TypeScript coding standards defined in the Architecture Document.

8. Local testability: A simple script or CLI command can define partials, create a template referencing them, and demonstrate the correct assembly of a final prompt.

## Tasks / Subtasks

- [ ] Design the `prompt_partials` database schema (referencing `PromptPartial` data model in Architecture Document).

- [ ] Implement database interaction (CRUD operations) for prompt partials within the `services/prompt-virtual-keys-service/`.

- [ ] Develop API endpoint(s) for prompt partial management (create, retrieve, update, delete).

- [ ] Modify the prompt template application logic (from Story 5.1) in the `unified-llm-api` service to resolve and embed referenced prompt partials.

- [ ] Implement logic to handle chaining/embedding partials within templates, including conflict resolution or ordering.

- [ ] Ensure partial updates support versioning requirements.

- [ ] Write unit tests for prompt partial CRUD operations and the chaining/resolution logic.

- [ ] Create a simple test script or CLI command to demonstrate prompt partial management and chaining.

- [ ] Document prompt partial API endpoints and usage in the `services/prompt-virtual-keys-service/` README.

## Dev Technical Guidance

This story introduces a powerful modularity to prompt engineering, essential for complex and evolving LLM interactions.

- **Dependencies:** This story **depends on Story 5.1: Implement Prompt Template Management** as it builds on the concept of templates and shares the same service. It relies on the core gateway services for consuming the assembled prompts.

- **Technology Stack:** Python, FastAPI for the backend service. PostgreSQL for data persistence.

- **Data Models:** Refer to the `PromptPartial` data model in the Architecture Document for the schema.

- **Prompt Assembly Logic:** The logic for combining partials within templates needs to be robust, handling nesting and potential conflicts or implicit ordering.

- **Version Management:** The versioning for partials is critical, ensuring that changes to a partial don't inadvertently break older templates that reference it (unless intended).

- **Security:** Ensure secure handling of prompt content, adhering to "Data Protection" and "Input Sanitization/Validation" in the Architecture Document.

- **References:**

    - AI Gateway Architecture Document: `docs/architecture.md`

    - AI Gateway Product Requirements Document: `docs/prd.md`

    - Story 5.1: `docs/stories/5.1.story.md`

## Story Progress Notes

### Agent Model Used: Fiona "Flux" Rivera (SM Agent)

### Completion Notes List

{To be filled by Developer Agent upon completion}

### Change Log

- Initial Draft | 2025-07-06 | Fiona "Flux" Rivera (SM Agent)


