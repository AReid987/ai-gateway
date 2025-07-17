---
type: Page
title: AI Gateway Architecture Final
description: null
icon: null
createdAt: '2025-06-14T21:22:26.854Z'
creationDate: 2025-06-14 16:22
modificationDate: 2025-06-14 16:33
tags: []
coverImage: null
---

# AI Gateway Architecture Document

## Introduction / Preamble

This document outlines the overall project architecture for the AI Gateway, including backend systems, shared services, and non-UI specific concerns. Its primary goal is to serve as the guiding architectural blueprint for AI-driven development, ensuring consistency and adherence to chosen patterns and technologies.

The AI Gateway's core purpose is to increase reliability, accuracy, and cost-efficiency for interactions with Large Language Models (LLMs) by providing a unified API, intelligent routing, enhanced resilience, and comprehensive observability.

**Relationship to Frontend Architecture:** As the project includes a significant user interface (the Observability & Analytics Dashboard), a separate Frontend Architecture Document will detail the frontend-specific design and must be used in conjunction with this document. Core technology stack choices documented herein (see "Definitive Tech Stack Selections") are definitive for the entire project, including any frontend components.

## Table of Contents

- [Introduction / Preamble](https://www.google.com/search?q=%23introduction--preamble)

- [Technical Summary](https://www.google.com/search?q=%23technical-summary)

- [High-Level Overview](https://www.google.com/search?q=%23high-level-overview)

- [Architectural / Design Patterns Adopted](https://www.google.com/search?q=%23architectural--design-patterns-adopted)

- [Component View](https://www.google.com/search?q=%23component-view)

- [Project Structure](https://www.google.com/search?q=%23project-structure)

    - [Key Directory Descriptions](https://www.google.com/search?q=%23key-directory-descriptions)

    - [Notes](https://www.google.com/search?q=%23notes)

- [API Reference](https://www.google.com/search?q=%23api-reference)

    - [External APIs Consumed](https://www.google.com/search?q=%23external-apis-consumed)

    - [Internal APIs Provided (If Applicable)](https://www.google.com/search?q=%23internal-apis-provided-if-applicable)

- [Data Models](https://www.google.com/search?q=%23data-models)

    - [Core Application Entities / Domain Objects](https://www.google.com/search?q=%23core-application-entities--domain-objects)

    - [API Payload Schemas (If distinct)](https://www.google.com/search?q=%23api-payload-schemas-if-distinct)

    - [Database Schemas (If applicable)](https://www.google.com/search?q=%23database-schemas-if-applicable)

- [Core Workflow / Sequence Diagrams](https://www.google.com/search?q=%23core-workflow--sequence-diagrams)

- [Definitive Tech Stack Selections](https://www.google.com/search?q=%23definitive-tech-stack-selections)

- [Infrastructure and Deployment Overview](https://www.google.com/search?q=%23infrastructure-and-deployment-overview)

- [Error Handling Strategy](https://www.google.com/search?q=%23error-handling-strategy)

- [Coding Standards](https://www.google.com/search?q=%23coding-standards)

    - [Detailed Language & Framework Conventions](https://www.google.com/search?q=%23detailed-language--framework-conventions)

        - [Python Specifics:](https://www.google.com/search?q=%23python-specifics)

        - [TypeScript/Node.js Specifics:](https://www.google.com/search?q=%23typescriptnode.js-specifics)

- [Overall Testing Strategy](https://www.google.com/search?q=%23overall-testing-strategy)

- [Security Best Practices](https://www.google.com/search?q=%23security-best-practices)

- [Key Reference Documents](https://www.google.com/search?q=%23key-reference-documents)

- [Change Log](https://www.google.com/search?q=%23change-log)

## Technical Summary

The AI Gateway will be a layered, intelligent proxy for Large Language Models, designed to enhance reliability, accuracy, and cost-efficiency. It will utilize a monorepo structure, deploying via containerization and orchestration across various cloud platforms. Key components include Kong for external API management, Portkey/LiteLLM for unified LLM access, Not Diamond/RouteLLM for intelligent routing, and OptiLLM for advanced optimization. An external Next.js dashboard will provide comprehensive observability and configuration management. The system prioritizes high availability, performance, and robust security, with a strong emphasis on automated testing and continuous delivery.

## High-Level Overview

The architecture follows a layered gateway pattern with distinct responsibilities for traffic management, LLM abstraction, intelligent routing, and optimization. The entire system will reside within a monorepo, facilitating coordinated development and deployment. Requests will flow from external applications through Kong, then internally to the LLM management and routing layers, eventually reaching various LLM providers. Observability components will continuously collect data across all layers, feeding into an external dashboard.

[ai-gateway-mmd](https://app.capacities.io/6002bb54-716f-4804-8c6a-17e1e219e363/b02fd260-3ec4-45a7-a2cc-e931dae2e8dd)

```markdown
graph TD
    subgraph Client-Facing Layer
        U[User/Application] --> A[Kong API Gateway]
    end

    subgraph Core Gateway Services
        A --> B[Unified LLM API Service<br>(Portkey/LiteLLM)]
        B --> C[Intelligent Router Service<br>(Not Diamond/RouteLLM)]
        C --> D[Optimization Service<br>(OptiLLM)]
    end

    subgraph LLM Providers
        D --> E[External LLM Providers<br>(OpenAI, Anthropic, Groq, etc.)]
        E --> D
    end

    subgraph Management & Observability
        B --- F[Observability Services<br>(Logging, Metrics, Tracing)]
        C --- F
        D --- F
        F --> G[Analytics & Config Dashboard<br>(Next.js UI)]
    end

    subgraph Supporting Functions
        H[Prompt Management]
        I[Virtual Key Management]
    end

    G -- Configures --> H
    G -- Configures --> I
    H -- Applies to --> B
    I -- Applies to --> C

    style A fill:#D9E8F5,stroke:#3470AD,stroke-width:2px
    style B fill:#D9E8F5,stroke:#3470AD,stroke-width:2px
    style C fill:#D9E8F5,stroke:#3470AD,stroke-width:2px
    style D fill:#D9E8F5,stroke:#3470AD,stroke-width:2px
    style U fill:#F5E8D9,stroke:#AD7034,stroke-width:2px
    style E fill:#F5E8D9,stroke:#AD7034,stroke-width:2px
    style F fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style G fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style H fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style I fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style J fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style K fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
```

*Description: This C4 Model Layer 1 (System Context) and Layer 2 (Container Diagram) hybrid illustrates the main components of the AI Gateway. User/Applications interact with the Kong API Gateway, which routes requests to internal services for unified LLM API access, intelligent routing, and optimization before reaching external LLM Providers. All core services contribute data to Observability Services, which feed into the Analytics & Config Dashboard. Prompt and Virtual Key Management functions support the core gateway services.*

## Architectural / Design Patterns Adopted

- **API Gateway Pattern:** Kong serves as the central entry point, handling routing, security, and rate limiting.

- **Service Layer Pattern:** The Unified LLM API, Intelligent Router, and Optimization services represent distinct layers with well-defined responsibilities.

- **Strategy Pattern (Implicit):** Intelligent routing will likely employ variations of the strategy pattern to dynamically select LLMs based on cost, performance, or task.

- **Circuit Breaker/Retry Pattern:** For reliability, automatic retries and fallbacks will implement variations of these patterns.

- **Load Balancing Pattern:** Distributing requests across multiple LLM providers.

- **Observability Pattern:** Implementing centralized logging, monitoring, and distributed tracing across services.

- **Microservices/Modular Monolith (Hybrid):** While a monorepo is chosen for development ease, the components are logically separated as distinct services, allowing for potential future independent deployment.

## Component View

The system is composed of several major logical components, each with specific responsibilities:

- **Kong API Gateway:**

    - **Responsibility:** External API traffic management, security (authentication, authorization), rate limiting, request routing to internal services.

- **Unified LLM API Service (Portkey/LiteLLM):**

    - **Responsibility:** Provides a single, consistent API interface for all LLM calls, abstracts away provider-specific complexities, manages LLM provider API keys and configurations, handles prompt serialization/deserialization.

- **Intelligent Model Router Service (Not Diamond/RouteLLM):**

    - **Responsibility:** Dynamically selects the most suitable LLM model for a given request/task based on defined criteria (cost, performance, accuracy, specific capabilities), handles fallback logic, manages load balancing across providers.

- **Optimization Service (OptiLLM):**

    - **Responsibility:** Fine-tunes model selection and parameters, potentially pre-processes prompts or post-processes responses for further optimization (cost, token usage, relevance).

- **Observability Services:**

    - **Responsibility:** Centralized collection, processing, and storage of logs, metrics, and trace data from all gateway components.

- **Analytics & Configuration Dashboard (Next.js):**

    - **Responsibility:** Provides an intuitive UI for visualizing operational insights (logs, metrics, traces), managing gateway configurations (LLM providers, virtual keys, routing rules), and prompt template management.

- **Prompt Management Module:**

    - **Responsibility:** Stores, retrieves, and applies prompt templates and partials, handles prompt chaining and assembly.

- **Virtual Key Management Module:**

    - **Responsibility:** Creates and manages virtual keys, maps them to underlying LLM provider API keys, applies per-key configurations (rate limits, cost caps).

- **Data Persistence Layer:**

    - **Responsibility:** Stores configuration data, historical metrics, logs, cached prompts/responses, and potentially prompt templates/partials and virtual key definitions. (PostgreSQL and/or MongoDB).

## Project Structure

The project will adhere to a monorepo structure. A high-level view of the projected folder structure:

```markdown
{project-root}/
├── .github/                    # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       └── main.yml
├── docs/                       # Project documentation (PRD, Arch, etc.)
│   ├── prd.md                  # Product Requirements Document
│   ├── architecture.md         # This Architecture Document
│   └── ... (other .md files)
├── infra/                      # Infrastructure as Code (e.g., CDK, Terraform, Kuma configs)
│   ├── kuma/                   # Kuma specific configurations for service mesh
│   ├── kubernetes/             # Kubernetes manifests
│   └── cloud-provider-specific/ # e.g., aws-cdk, gcp-terraform
├── services/                   # Application source code for distinct services
│   ├── kong-gateway/           # Kong configuration and custom plugins (if any)
│   ├── unified-llm-api/        # Python backend service (Portkey/LiteLLM integration)
│   ├── intelligent-router/     # Python backend service (Not Diamond/RouteLLM integration)
│   ├── optimization-service/   # Python backend service (OptiLLM integration)
│   ├── observability-service/  # Python/Go/etc. service for metrics/logs/traces ingestion
│   └── prompt-virtual-keys-service/ # Python backend service for management APIs
├── dashboard/                  # Next.js frontend application for Analytics & Configuration
│   ├── public/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── ...
├── shared/                     # Shared code, types, utilities across services
│   └── python-utils/
│   └── ts-types/
├── tests/                      # Automated tests
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore rules
├── package.json                # For Next.js/Frontend
├── pyproject.toml / requirements.txt # For Python services
├── Dockerfile                  # Base Dockerfile or per-service Dockerfiles
└── README.md                   # Project overview and setup instructions
```

### Key Directory Descriptions

- `docs/`: Contains all project planning and reference documentation, including the PRD and this Architecture Document.

- `infra/`: Holds Infrastructure as Code definitions for deploying the gateway components.

- `services/`: Contains the source code for each distinct backend service (e.g., Unified LLM API, Intelligent Router), primarily in Python.

- `dashboard/`: Contains the Next.js frontend application for the Analytics & Configuration Dashboard.

- `shared/`: Contains code (e.g., types, utilities) that can be shared across multiple services within the monorepo.

- `tests/`: Contains all automated tests (unit, integration, E2E), mirroring the `services/` and `dashboard/` structures.

### Notes

The `services/` directory will contain logically separated Python services, allowing for clearer separation of concerns even within the monorepo. While `Dockerfile` is shown at the root, individual services may have specific Dockerfiles or a build system will handle multi-service containerization.

## API Reference

### External APIs Consumed

The AI Gateway will consume APIs from various LLM Providers. The specific endpoints and authentication methods will vary per provider but will be abstracted by the Unified LLM API Service.

#### **OpenAI API**

- **Purpose:** Access to OpenAI's various LLM models (e.g., GPT-3.5, GPT-4).

- **Authentication:** API Key (Bearer Token in Header).

- **Key Endpoints Used:** `/v1/chat/completions`, `/v1/completions`, potentially others for embeddings or fine-tuning.

- **Rate Limits:** Managed by OpenAI per API key/organization.

- **Link to Official Docs:** `https://platform.openai.com/docs/api-reference`

#### **Anthropic API**

- **Purpose:** Access to Anthropic's Claude models.

- **Authentication:** API Key (Header `x-api-key`).

- **Key Endpoints Used:** `/v1/messages`

- **Rate Limits:** Managed by Anthropic.

- **Link to Official Docs:** `https://docs.anthropic.com/claude/reference/getting-started-with-the-api`

#### **Groq API**

- **Purpose:** Access to Groq's fast inference models.

- **Authentication:** API Key (Bearer Token in Header).

- **Key Endpoints Used:** `/openai/v1/chat/completions` (OpenAI-compatible API).

- **Rate Limits:** Managed by Groq.

- **Link to Official Docs:** `https://groq.com/docs/api`

#### **Other LLM Providers (e.g., Ollama, Hugging Face via LiteLLM)**

- **Purpose:** Broaden model support and leverage niche or local models.

- **Authentication:** Varies (API Keys, local endpoint access, etc.).

- **Key Endpoints Used:** Varies depending on integration.

- **Rate Limits:** Varies.

### Internal APIs Provided (If Applicable)

The AI Gateway itself will expose an internal API for the Dashboard and potentially other internal services. The primary external API for LLM interaction will be managed by Kong.

#### **AI Gateway Internal API**

- **Purpose:** Provides a unified interface for the Dashboard to configure and monitor the gateway, and for internal services to interact with core LLM management.

- **Base URL(s):** e.g., `/api/v1/gateway`, `/api/v1/config`, `/api/v1/metrics`

- **Authentication/Authorization:** Internal API key or token-based authentication for dashboard access; service-to-service authentication for internal components.

- **Endpoints:**

    - `POST /llm/invoke`: Primary endpoint for LLM calls (handled internally by routing).

    - `GET /config/providers`: Retrieve configured LLM providers.

    - `POST /config/virtual-keys`: Create/manage virtual keys.

    - `GET /metrics/usage`: Retrieve usage metrics.

    - `GET /logs`: Retrieve filtered logs.

    - `GET /traces/{traceId}`: Retrieve specific trace data.

    - `POST /prompts/templates`: Manage prompt templates.

## Data Models

### Core Application Entities / Domain Objects

#### **LLMRequest**

- **Description:** Represents a request made to an LLM, including its context and parameters.

- **Schema / Interface Definition:**

```typescript
export interface LLMRequest {
  id: string; // Unique identifier for the request (traceId)
  virtualKeyId?: string; // Virtual key used for the request
  prompt: string; // The full prompt sent to the LLM
  templateId?: string; // ID of the template used
  partialIds?: string[]; // IDs of partials used
  modelRequested: string; // Model originally requested by the client
  modelUsed: string; // Actual model used after routing/optimization
  providerUsed: string; // LLM provider used
  parameters: { [key: string]: any }; // LLM parameters (temperature, max_tokens, etc.)
  timestamp: Date; // Time of request
  status: 'success' | 'failure' | 'fallback'; // Request status
  latencyMs: number; // Latency of response from LLM provider
  costUsd?: number; // Estimated cost of the request
  tokensUsed?: { // Token usage details
    promptTokens: number;
    completionTokens: number;
    totalTokens: number;
  };
  errorMessage?: string; // Error message if failure
}
```

#### **VirtualKey**

- **Description:** Represents an abstraction over raw LLM provider API keys, allowing for granular control and tracking.

- **Schema / Interface Definition:**

```typescript
export interface VirtualKey {
  id: string; // Unique identifier
  name: string; // Human-readable name
  mappedProviderKeys: { providerId: string; apiKey: string; }[]; // Mapped actual provider API keys (encrypted)
  rateLimit?: { rpm?: number; tpm?: number; }; // Requests per minute, tokens per minute
  costCap?: number; // Maximum monthly cost for this key
  defaultModel?: string; // Default model to use if not specified in request
  isActive: boolean;
  createdAt: Date;
  updatedAt: Date;
}
```

#### **PromptTemplate**

- **Description:** A reusable template for constructing LLM prompts.

- **Schema / Interface Definition:**

```typescript
export interface PromptTemplate {
  id: string; // Unique identifier
  name: string; // Name of the template
  templateString: string; // The template string with placeholders (e.g., "Analyze the following: {text}")
  partialsUsed?: string[]; // IDs of prompt partials used within this template
  version: string; // Version of the template
  createdAt: Date;
  updatedAt: Date;
}
```

#### **PromptPartial**

- **Description:** A reusable segment of a prompt.

- **Schema / Interface Definition:**

### API Payload Schemas (If distinct)

Payload schemas will largely mirror the core entities for configuration and management. For LLM invocation, the unified API will aim to standardize request/response formats compatible with underlying libraries (Portkey/LiteLLM) while mapping to LLM provider specifics.

### Database Schemas (If applicable)

#### **llm_requests (PostgreSQL)**

- **Purpose:** Stores historical LLM request data for observability and cost tracking.

- **Schema Definition:**

```sql
CREATE TABLE llm_requests (
  id VARCHAR(36) PRIMARY KEY,
  virtual_key_id VARCHAR(36),
  prompt TEXT NOT NULL,
  template_id VARCHAR(36),
  model_requested VARCHAR(100),
  model_used VARCHAR(100),
  provider_used VARCHAR(50),
  parameters JSONB,
  timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  status VARCHAR(20),
  latency_ms INTEGER,
  cost_usd DECIMAL(10, 6),
  prompt_tokens INTEGER,
  completion_tokens INTEGER,
  total_tokens INTEGER,
  error_message TEXT
);
CREATE INDEX idx_llm_requests_timestamp ON llm_requests (timestamp);
CREATE INDEX idx_llm_requests_virtual_key ON llm_requests (virtual_key_id);
```

#### **virtual_keys (PostgreSQL)**

- **Purpose:** Stores configuration for virtual API keys.

- **Schema Definition:**

[ai-gateway-mmd](https://app.capacities.io/6002bb54-716f-4804-8c6a-17e1e219e363/ead24f5d-9157-4da0-bc1e-e8809aa2f3b7)
