---
type: Page
title: 'Story 1.2: Implement Unified LLM API (Portkey/LiteLLM)'
description: null
icon: null
createdAt: '2025-06-17T20:00:28.444Z'
creationDate: 2025-06-17 15:00
modificationDate: 2025-07-06 15:06
tags: []
coverImage: null
---

# Story 1.2: Implement Unified LLM API (Portkey/LiteLLM)

## Status: Draft

## Story

- As a **developer**,

- I want to **integrate either Portkey or LiteLLM as the primary unified LLM API interface**,

- so that **I can send requests to multiple LLM providers through a single, consistent API and manage their specific configurations**.

## Acceptance Criteria (ACs)

1. The chosen unified LLM API (Portkey or LiteLLM) is integrated into the monorepo, following the project structure outlined in the Architecture Document.

2. Configuration for at least two LLM providers (e.g., OpenAI, Anthropic, Groq, Ollama) is managed through this unified API.

3. A test endpoint demonstrates successfully sending a basic prompt to one LLM provider via the unified API and receiving a valid response.

4. Provider-specific API keys are securely managed by the unified API, adhering to the secrets management guidelines in the Architecture Document.

5. The implementation adheres to the Python and TypeScript coding standards defined in the Architecture Document.

6. Local testability: A simple script or CLI command can invoke a test LLM call through the unified API from the local development environment.

## Tasks / Subtasks

- [ ] Research and decide between Portkey and LiteLLM based on detailed requirements (e.g., broader model support, built-in observability features, specific API compatibility). Document rationale for the choice.

- [ ] Integrate the chosen library (Portkey or LiteLLM) into the `services/unified-llm-api/` directory within the monorepo.

- [ ] Configure the unified LLM API service to manage credentials and connections for at least two LLM providers.

- [ ] Implement a basic API endpoint within the `unified-llm-api` service that receives a prompt and forwards it to an LLM provider via the chosen unified API library.

- [ ] Ensure secure handling of LLM provider API keys as per "Secrets Management" guidelines.

- [ ] Write unit tests for the unified API integration and basic LLM invocation logic using `pytest`.

- [ ] Create a simple test script or CLI command to demonstrate invoking the endpoint and receiving responses.

- [ ] Document API client setup and configuration steps in a README within the `unified-llm-api` service directory.

## Dev Technical Guidance

This story is crucial for abstracting LLM provider complexities and establishing a single point of interaction.

- **Technology Stack:** Choose between Portkey and LiteLLM. Python is the primary language for backend services. FastAPI is the recommended backend framework.

- **API Design:** The unified API should standardize request/response formats compatible with the chosen library (Portkey/LiteLLM) while mapping to LLM provider specifics. Refer to "API Reference" in the Architecture Document.

- **Security:** Pay close attention to "Security Best Practices" for API Key Exposure and Secrets Management.

- **Error Handling:** Implement robust error handling for LLM API failures, rate limits, and ensure clear error responses, aligning with the "Error Handling Strategy".

- **Testing:** Focus on unit tests for the unified API integration and ensuring successful communication with LLM providers.

- **Environment Variables:** LLM API keys will be accessed via environment variables (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).

- **References:**

    - Portkey Documentation: [https://portkey.ai/](https://portkey.ai/)

    - LiteLLM Documentation: [https://www.litellm.ai/](https://www.litellm.ai/)

    - AI Gateway Architecture Document: `docs/architecture.md`

    - AI Gateway Product Requirements Document: `docs/prd.md`

## Story Progress Notes

### Agent Model Used: Fiona "Flux" Rivera (SM Agent)

### Completion Notes List

{To be filled by Developer Agent upon completion}

### Change Log

- Initial Draft | 2025-06-17 | Fiona "Flux" Rivera (SM Agent)


