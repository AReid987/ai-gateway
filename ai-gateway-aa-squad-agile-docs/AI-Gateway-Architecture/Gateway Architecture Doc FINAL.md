---
type: Page
title: Gateway Architecture Doc FINAL
description: null
icon: null
createdAt: '2025-06-16T00:12:29.645Z'
creationDate: 2025-06-15 19:12
modificationDate: 2025-06-15 20:21
tags: []
coverImage: null
---

### 1. AI Gateway Product Requirements Document (PRD)

# AI Gateway Product Requirements Document (PRD)

## Goal, Objective and Context

This project aims to create an AI Gateway that leverages various technologies such as Kong, Portkey, Not Diamond, LiteLLM, RouteLLM, and OptiLLM. The overarching goal is to significantly **increase reliability and accuracy while simultaneously keeping costs down** for interactions with Large Language Models (LLMs).

The problems this AI Gateway addresses include:

- **Rate Limits and Cost Management:** Current LLM interactions often hit rate limits when relying on a single provider, leading to operational bottlenecks or drastically increased costs.

- **Resilience and Network Errors:** A single LLM provider creates a single point of failure; network errors can completely disrupt LLM interactions. The gateway will provide resilience through fallbacks and automatic retries to alternative providers.

- **Optimized LLM Selection:** No single LLM is superior for all tasks. The gateway will intelligently route requests to the most suitable model for a given task, even at a granular "per step of each task" level, by utilizing an intelligent model router. This allows for dynamic switching to smaller, potentially local (and free) models for sub-tasks, optimizing both cost and inference speed.

The AI Gateway will achieve these goals through the implementation of key features:

- **Fallbacks:** Seamless transition to alternative LLM providers in case of failures.

- **Automatic Retries:** Automated attempts to re-send failed requests.

- **Load Balancing across LLM Providers:** Distributing requests across multiple LLM providers to prevent rate limits and optimize usage.

- **Caching prompts / responses:** Storing frequently used prompts and their responses to reduce redundant LLM calls and costs.

- **Prompt Templates and Partials:** Enabling standardized and reusable prompt structures for consistent interactions.

- **Observability, tracing, monitoring, logging:** Comprehensive insights into LLM usage, performance, and costs for fine-tuning.

- **Intelligent model router:** A system that selects the best LLM model for each specific task or even per step of a task.

- **Enhanced reasoning:** Support for more sophisticated AI processing.

- **Unified API endpoint:** A single entry point to enable access to all LLM Providers.

The primary users of this AI Gateway will be **developers in their IDEs**, who will benefit from building with more accuracy, reliability, and at a lower cost. There is also potential for expansion to your Aigency app users post-launch.

## Functional Requirements (MVP)

The AI Gateway will provide the following essential functional capabilities in its Minimum Viable Product:

1. **Unified API Endpoint:**

    - Provide a single, consistent API entry point for interacting with various LLM providers.

    - Manage provider-specific API keys and configurations transparently.

    - Support a wide range of LLMs (e.g., OpenAI, Anthropic, Hugging Face, and custom models).

2. **Intelligent Model Routing:**

    - Dynamically route requests to the most cost-effective or performant LLM model.

    - Enable custom routing logic, including fallback models and retries.

    - Select the best model based on task-specific criteria, even at a granular "per step of each task" level.

3. **Reliability Features:**

    - Implement fallbacks to alternative LLM providers in case of failures.

    - Incorporate automatic retries for failed requests to ensure continuous operation.

4. **Cost Optimization:**

    - Perform load balancing across various LLM providers.

    - Implement caching for prompts and responses to reduce redundant LLM calls and associated costs.

5. **Prompt Management:**

    - Provide capabilities for creating and managing prompt templates and partials for consistent and efficient LLM interactions.

6. **Observability & Monitoring:**

    - Offer built-in observability, tracing, monitoring, and logging functionalities to provide insights into LLM usage, performance, and costs.

7. **Enhanced Reasoning:**

    - Support for more sophisticated AI processing (to be further defined, but architecture should support future integration).

8. **API Traffic Management (Outer Layer):**

    - Manage overall API traffic, including security and rate limiting, acting as the outer layer of the gateway.

## Non Functional Requirements (MVP)

- **Performance:** The system should be capable of optimizing cost/performance trade-offs dynamically and fine-tuning model selection and parameters.

    - **Response Time:** Aim for typical LLM API call response times (e.g., sub-200ms for direct passthrough, with variations for complex routing/optimization).

    - **Throughput/Capacity:** The gateway should be able to handle a high volume of concurrent LLM requests (e.g., supporting 1000+ requests per second for core routing, scaled as needed).

    - **Load Handling:** The system should gracefully degrade under extreme load and recover automatically.

    - **Resource Utilization:** The gateway components should be designed to optimize resource usage (CPU, memory, network) to control operational costs, especially considering the fluctuating demands of LLM inference.

- **Scalability:** The gateway should be designed for large-scale deployments, with components capable of horizontal scaling to handle increased demand efficiently.

- **Security:** It needs to include advanced security features at the API gateway layer.

    - **Data Protection:** Ensure sensitive data (e.g., API keys, user prompts, responses) is encrypted at rest and in transit.

    - **Authentication/Authorization:** Implement robust authentication and authorization mechanisms for gateway access and virtual key usage.

    - **Compliance Requirements:** Adhere to relevant data privacy regulations (e.g., GDPR, CCPA, if applicable) and implement industry-standard secure coding practices.

    - **Vulnerability Management:** Implement regular security scanning for vulnerabilities in dependencies and code, adhering to common security best practices like input validation and protection against common web vulnerabilities (e.g., XSS, SQL Injection).

    - **Privacy Considerations:** Design should minimize collection and storage of Personally Identifiable Information (PII) and ensure adherence to data privacy principles.

- **Reliability & Resilience:**

    - **Availability:** Aim for high availability (e.g., 99.9% uptime for core gateway functionality).

    - **Backup & Recovery:** The system should support automated backup mechanisms for critical configurations and data, enabling quick recovery and restoration in case of system failures.

    - **Fault Tolerance:** The system should tolerate failures of individual LLM providers and internal components via fallbacks and retries.

    - **Maintenance and Support:** The system should be easy to deploy, monitor, update, and troubleshoot, with clear documentation and operational guides.

- **Configurability:** The gateway should allow for selection of LLM inference providers and management of virtual keys and configurations through an intuitive interface.

- **Usability:** The overall system, including any external interfaces, should be intuitive for developers.

- **Technical Constraints:**

    - **Platform/Technology Constraints:** Kong, Portkey, Not Diamond, LiteLLM, RouteLLM, OptiLLM, Next.js, PostgreSQL, and potentially MongoDB are mandated technologies.

    - **Integration Requirements:** Clear APIs and protocols for integration between the selected tools (e.g., Kong routing to Portkey/LiteLLM, Not Diamond/RouteLLM integrating with Portkey/LiteLLM, OptiLLM integrating with routing layer).

    - **Third-party Service Dependencies:** Primary dependencies include various LLM providers (e.g., OpenAI, Anthropic, Groq, Ollama) and potentially other external services based on specific LLM integrations.

    - **Infrastructure Requirements:** Automated infrastructure provisioning (Infrastructure as Code - IaC) is required. Components should be containerized (e.g., Docker) and orchestrated (e.g., Kubernetes, Kuma) for consistent deployment across chosen cloud providers (AWS, GCP, Cloudflare, Fly.io, Railway).

    - **Development Environment Needs:** The local development environment setup should be consistent, easy to replicate, and support rapid iteration. It should allow developers to run and test components independently.

## User Interaction and Design Goals

If the product includes a User Interface (UI), this section captures the Product Manager's high-level vision and goals for the User Experience (UX). This information will serve as a crucial starting point and brief for the Design Architect.

- **Overall Vision & Experience:** The experience should be intuitive for developers.

- **Key Interaction Paradigms:**

    - **External Dashboard:** Provide a dedicated external dashboard for managing the gateway.

    - **Unified Interface:** All components and configurations should be aggregated into one cohesive view, potentially via embedded iframes or a more integrated approach.

    - **Configuration & Management:** Users should be able to easily select LLM inference providers, manage virtual keys, and configure logging, monitoring, and tracing settings through this interface.

- **Target Devices/Platforms:** Primarily web desktop for the dashboard.

## Technical Assumptions

This section outlines the foundational technical decisions and preferences for the AI Gateway project, which will guide the Architect and development teams.

- **Primary Frontend Framework (if applicable):** Next.js will be used for any frontend user interface components.

- **Database Choices:** PostgreSQL is the primary choice for relational data, with a possibility of using MongoDB if specific non-relational data storage needs arise.

- **Cloud Platform & Hosting:** AWS, Google Cloud Platform (GCP), Cloudflare, Fly.io, and Railway are all acceptable choices for cloud providers and hosting.

- **Version Control System:** GitHub will be used for version control.

- **Repository & Service Architecture:** The project will utilize a monorepo structure, containing all components (Kong, Portkey/LiteLLM, Not Diamond/RouteLLM, OptiLLM) within a single repository.

- **Core Technologies (Confirmed from prior discussion/document):** Kong, Portkey, Not Diamond, LiteLLM, RouteLLM, and OptiLLM. These will integrate to form the AI Gateway.

    - **Proposed Architecture Structure:** Kong will serve as the outer API gateway layer, managing traffic, security, and rate limiting. Portkey or LiteLLM will act as the primary unified gateway for LLM calls, handling provider-specific configurations. Not Diamond or RouteLLM will form the routing layer for dynamic model selection based on cost/performance. OptiLLM will be integrated for fine-tuning model selection and parameters.

## Epic Overview

## **Epic 1: Core Gateway Infrastructure & Unified Access**

- Goal: Establish the foundational API gateway, unified LLM access, and initial traffic management capabilities.

- Story 1.1: Set Up Core API Gateway (Kong)

    - As a developer,

    - I want to deploy and configure Kong as the outermost API gateway layer,

    - so that it can manage all incoming API traffic, including LLM calls, provide basic security, and handle rate limiting.

    - Acceptance Criteria (ACs):

        1. Kong Gateway is deployed and accessible.

        2. A basic route is configured in Kong to forward requests to an internal service (placeholder for LLM gateway).

        3. Basic rate limiting is enabled and demonstrable on a test route.

        4. Initial security configurations (e.g., basic API key authentication) are in place.

- Story 1.2: Implement Unified LLM API (Portkey/LiteLLM)

    - As a developer,

    - I want to integrate either Portkey or LiteLLM as the primary unified LLM API interface,

    - so that I can send requests to multiple LLM providers through a single, consistent API and manage their specific configurations.

    - Acceptance Criteria (ACs):

        1. The chosen unified LLM API (Portkey or LiteLLM) is integrated into the monorepo.

        2. Configuration for at least two LLM providers (e.g., OpenAI, Anthropic) is managed through this unified API.

        3. A test endpoint demonstrates sending a basic prompt to one LLM provider via the unified API and receiving a response.

        4. Provider-specific API keys are securely managed by the unified API.

- Story 1.3: Integrate Kong with Unified LLM API

    - As a developer,

    - I want to configure Kong to route LLM requests to the unified LLM API (Portkey/LiteLLM),

    - so that all external LLM traffic passes through Kong's management layer to the unified LLM interface.

    - Acceptance Criteria (ACs):

        1. Kong is configured to proxy LLM-related requests to the unified LLM API service.

        2. An external request through Kong successfully reaches an LLM provider via the unified API and returns a response.

        3. Kong's rate limiting and basic security measures apply correctly to the proxied LLM requests.

## **Epic 2: Intelligent Routing & Optimization Engine**

- Goal: Implement dynamic model selection, routing logic, and initial performance/cost optimization features.

- Story 2.1: Implement Core Intelligent Model Router (Not Diamond/RouteLLM)

    - As a developer,

    - I want to integrate an intelligent model router (Not Diamond or RouteLLM) with the unified LLM API,

    - so that I can dynamically select the most suitable LLM model for a given task based on predefined criteria.

    - Acceptance Criteria (ACs):

        1. The chosen intelligent router (Not Diamond or RouteLLM) is integrated with Portkey/LiteLLM.

        2. The router can receive a request and select an appropriate LLM model from the configured providers.

        3. Initial routing logic (e.g., based on simple cost or performance preference) is implemented and demonstrable.

        4. The routing decision is logged (for future observability).

- Story 2.2: Develop Cost & Performance Optimization Rules

    - As a developer,

    - I want to define and apply rules for optimizing LLM selection based on cost and performance,

    - so that the gateway prioritizes cheaper or faster models for specific tasks when appropriate.

    - Acceptance Criteria (ACs):

        1. Configuration allows defining cost and performance metrics for each LLM model.

        2. The intelligent router utilizes these metrics to make routing decisions.

        3. Demonstrate routing a low-complexity task to a cheaper/faster model and a high-complexity task to a potentially more capable model.

        4. The routing decision is logged (for future observability).

- Story 2.3: Integrate OptiLLM for Fine-Tuning

    - As a developer,

    - I want to integrate OptiLLM into the routing layer,

    - so that the gateway can fine-tune model selection and parameters for specific tasks, further optimizing performance and cost.

    - Acceptance Criteria (ACs):

        1. OptiLLM is integrated with the intelligent router (Not Diamond/RouteLLM).

        2. OptiLLM can receive a request and suggest optimized model parameters or selection.

        3. The gateway uses OptiLLM's recommendations to adjust the LLM call.

        4. Demonstrate a scenario where OptiLLM's intervention improves a specific outcome (e.g., reduces tokens, improves relevance).

## **Epic 3: Enhanced Reliability & Resilience**

- Goal: Build in automatic fallbacks, retries, and load balancing across LLM providers to ensure high availability.

- Story 3.1: Implement Automatic Retries for LLM Calls

    - As a developer,

    - I want to configure the AI Gateway to automatically retry failed LLM calls,

    - so that transient network errors or temporary provider issues do not immediately result in a failed request.

    - Acceptance Criteria (ACs):

        1. The unified LLM API (Portkey/LiteLLM) or routing layer (Not Diamond/RouteLLM) can detect a failed LLM call.

        2. The system automatically retries the failed call a configurable number of times.

        3. A configurable delay (e.g., exponential backoff) is applied between retries.

        4. Requests that exhaust all retries are properly logged as failures.

        5. Demonstrate a scenario where a transient failure is successfully recovered by a retry.

- Story 3.2: Develop Fallback Mechanism for LLM Providers

    - As a developer,

    - I want to configure the AI Gateway to seamlessly fallback to an alternative LLM provider when a primary provider fails or is unavailable,

    - so that LLM interactions remain uninterrupted.

    - Acceptance Criteria (ACs):

        1. The routing layer can identify an unresponsive or failing primary LLM provider.

        2. The system automatically switches to a predefined fallback LLM provider for the same request.

        3. The fallback mechanism handles requests transparently to the calling application.

        4. Successful fallback is logged, and primary provider failures are alerted.

        5. Demonstrate a scenario where a primary provider is unavailable, and a request is successfully handled by a fallback provider.

- Story 3.3: Implement Load Balancing Across LLM Providers

    - As a developer,

    - I want to configure the AI Gateway to distribute LLM requests across multiple healthy providers,

    - so that usage is optimized, rate limits are managed, and overall throughput is increased.

    - Acceptance Criteria (ACs):

        1. The routing layer supports distributing incoming LLM requests across a pool of configured LLM providers.

        2. Configurable load balancing strategies (e.g., round-robin, least-connections, weighted) are available.

        3. The system intelligently considers provider health and current load when distributing requests.

        4. Demonstrate requests being distributed across multiple LLM providers.

        5. The system prevents individual providers from hitting their rate limits due to aggregated traffic (e.g., by intelligent distribution or active rate limit awareness).

## **Epic 4: Observability & Analytics Dashboard**

- Goal: Develop comprehensive logging, monitoring, tracing, and an intuitive external dashboard for operational insights and management.

- Story 4.1: Implement Centralized Logging for Gateway Operations

    - As a developer,

    - I want to ensure all AI Gateway operations (requests, responses, errors, routing decisions) are centrally logged,

    - so that I can effectively troubleshoot issues and gain insights into system behavior.

    - Acceptance Criteria (ACs):

        1. All components of the AI Gateway (Kong, unified API, router, optimizers) emit structured logs.

        2. Logs include relevant contextual information (e.g., request ID, timestamp, LLM provider used, model name, response status).

        3. Logs are directed to a centralized logging system (e.g., a file, or a log management service).

        4. Error logs clearly indicate the source and nature of the failure (e.g., LLM provider error, gateway internal error).

- Story 4.2: Develop Core Monitoring & Metrics Collection

    - As a developer,

    - I want to collect key performance metrics and operational data from the AI Gateway,

    - so that I can monitor system health, performance, and usage trends in real-time.

    - Acceptance Criteria (ACs):

        1. Metrics are collected for LLM request latency, success rates, and error rates per provider/model.

        2. Metrics are collected for caching effectiveness (hit/miss ratio).

        3. Metrics are collected for intelligent router decision counts (e.g., how often each model is selected).

        4. These metrics are exposed via a standard interface (e.g., Prometheus endpoint, or push to a monitoring service).

        5. Basic alerts can be configured based on predefined thresholds for critical metrics (e.g., high error rate for a provider).

- Story 4.3: Implement Distributed Tracing for LLM Requests

    - As a developer,

    - I want to implement end-to-end distributed tracing across all gateway components for LLM requests,

    - so that I can visualize the full path of a request and pinpoint bottlenecks or failures within the system.

    - Acceptance Criteria (ACs):

        1. Each LLM request generates a unique trace ID that propagates across Kong, the unified API, the routing layer, and any optimization components.

        2. Spans are created for significant operations within each component (e.g., Kong routing, Portkey/LiteLLM call, Not Diamond/RouteLLM decision, OptiLLM processing).

        3. Trace data includes relevant attributes for filtering and analysis (e.g., model chosen, latency, status).

        4. The tracing data can be exported to a compatible tracing system (e.g., Jaeger, OpenTelemetry collector).

- Story 4.4: Build External Analytics & Configuration Dashboard

    - As a developer,

    - I want to build an intuitive external dashboard (using Next.js as frontend UI),

    - so that I can visualize the collected logs, metrics, and traces, and manage gateway configurations (providers, virtual keys, routing rules).

    - Acceptance Criteria (ACs):

        1. A Next.js application serves as the external dashboard.

        2. The dashboard provides visualizations for LLM usage, cost, and performance metrics (from Story 4.2).

        3. Users can view logs and trace data, with filtering capabilities (from Story 4.1 & 4.3).

        4. The dashboard includes an interface for configuring LLM inference providers and managing virtual keys.

        5. The dashboard allows configuration of routing rules and optimization parameters.

        6. All components of the dashboard are aggregated into one cohesive view, possibly leveraging embedded iframes or a unified component model.

- **Epic 5: Prompt Management & Virtualization**

    - Goal: Provide features for creating, managing, and applying prompt templates, partials, and virtual keys.

    - Story 5.1: Implement Prompt Template Management

        - As a developer,

        - I want to create, store, and manage reusable prompt templates within the AI Gateway,

        - so that I can standardize common LLM interactions and ensure consistency across different applications.

        - Acceptance Criteria (ACs):

            1. Users can define and save named prompt templates through a dedicated interface (e.g., via the dashboard or API).

            2. Templates support placeholders for dynamic content insertion.

            3. The gateway can retrieve and apply a specified template to a raw prompt.

            4. Templates can be updated and versioned.

    - Story 5.2: Develop Prompt Partials and Chaining

        - As a developer,

        - I want to define and combine smaller "prompt partials" to build complex prompts,

        - so that I can reuse segments of prompts and create more modular and maintainable LLM interactions.

        - Acceptance Criteria (ACs):

            1. Users can define and save named prompt partials.

            2. Prompt templates can reference and combine multiple prompt partials.

            3. The gateway correctly assembles a full prompt from a template and its referenced partials.

            4. Demonstrate a complex prompt built from several partials and a template.

    - Story 5.3: Implement Virtual Key Management

        - As a developer,

        - I want to create and manage virtual keys within the AI Gateway,

        - so that I can abstract away raw LLM provider API keys and apply specific configurations or rate limits per virtual key.

        - Acceptance Criteria (ACs):

            1. Users can create unique virtual keys that map to one or more underlying LLM provider API keys.

            2. Each virtual key can have associated configurations (e.g., default model, specific rate limits, cost caps).

            3. Requests made using a virtual key are routed according to its associated configuration.

            4. Usage and cost can be tracked per virtual key.

## Key Reference Documents

{ This section will be created later, from the sections prior to this being carved up into smaller documents }

## Out of Scope Ideas Post MVP

Anything you and the user agreed it out of scope or can be removed from scope to keep MVP lean. Consider the goals of the PRD and what might be extra gold plating or additional features that could wait until the MVP is completed and delivered to assess functionality and market fit or usage.

