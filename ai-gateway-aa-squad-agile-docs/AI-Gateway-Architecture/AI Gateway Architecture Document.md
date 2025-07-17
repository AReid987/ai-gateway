---
type: Page
title: AI Gateway Architecture Document
description: null
icon: null
createdAt: '2025-07-06T20:10:52.119Z'
creationDate: 2025-07-06 15:10
modificationDate: 2025-07-06 15:12
tags: []
coverImage: null
---

### 2. AI Gateway Architecture Document

# AI Gateway Architecture Document

## Introduction / Preamble

This document outlines the overall project architecture for the AI Gateway, including backend systems, shared services, and non-UI specific concerns. Its primary goal is to serve as the guiding architectural blueprint for AI-driven development, ensuring consistency and adherence to chosen patterns and technologies.

The AI Gateway's core purpose is to increase reliability, accuracy, and cost-efficiency for interactions with Large Language Models (LLMs) by providing a unified API, intelligent routing, enhanced resilience, and comprehensive observability.

**Relationship to Frontend Architecture:** If the project includes a significant user interface, a separate Frontend Architecture Document (typically named `front-end-architecture-tmpl.txt` or similar, and linked in the "Key Reference Documents" section) details the frontend-specific design and MUST be used in conjunction with this document. Core technology stack choices documented herein (see "Definitive Tech Stack Selections") are definitive for the entire project, including any frontend components.

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

- [Definitive Tech Stack Selections](https://www.google.com/search?q=%23definitivetech-stack-selections)

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

Code snippet

```text
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

Plaintext

```text
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

    TypeScript

    ```text
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

    TypeScript

    ```text
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

    TypeScript

    ```text
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

    TypeScript

    ```text
    export interface PromptPartial {
      id: string; // Unique identifier
      name: string; // Name of the partial
      partialString: string; // The partial string (e.g., "Always respond in JSON format.")
      version: string; // Version of the partial
      createdAt: Date;
      updatedAt: Date;
    }
    ```

### API Payload Schemas (If distinct)

Payload schemas will largely mirror the core entities for configuration and management. For LLM invocation, the unified API will aim to standardize request/response formats compatible with underlying libraries (Portkey/LiteLLM) while mapping to LLM provider specifics.

### Database Schemas (If applicable)

#### **llm_requests (PostgreSQL)**

- **Purpose:** Stores historical LLM request data for observability and cost tracking.

- **Schema Definition:**

    SQL

    ```text
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

    SQL

    ```text
    CREATE TABLE virtual_keys (
      id VARCHAR(36) PRIMARY KEY,
      name VARCHAR(255) NOT NULL UNIQUE,
      mapped_provider_keys JSONB NOT NULL, -- Stored securely, e.g., encrypted
      rate_limit_rpm INTEGER,
      rate_limit_tpm INTEGER,
      cost_cap DECIMAL(10, 2),
      default_model VARCHAR(100),
      is_active BOOLEAN DEFAULT TRUE,
      created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    ```

#### **prompt_templates (PostgreSQL)**

- **Purpose:** Stores reusable prompt templates.

- **Schema Definition:**

    SQL

    ```text
    CREATE TABLE prompt_templates (
      id VARCHAR(36) PRIMARY KEY,
      name VARCHAR(255) NOT NULL UNIQUE,
      template_string TEXT NOT NULL,
      partials_used VARCHAR(36)[], -- Array of partial ID strings
      version VARCHAR(50) NOT NULL,
      created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    ```

#### **prompt_partials (PostgreSQL)**

- **Purpose:** Stores reusable prompt segments.

- **Schema Definition:**

    SQL

    ```text
    CREATE TABLE prompt_partials (
      id VARCHAR(36) PRIMARY KEY,
      name VARCHAR(255) NOT NULL UNIQUE,
      partial_string TEXT NOT NULL,
      version VARCHAR(50) NOT NULL,
      created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    ```

*(MongoDB may be considered for unstructured logging or highly dynamic configuration if benefits outweigh relational complexity for specific data types later.)*

## Core Workflow / Sequence Diagrams

This diagram illustrates the core request flow through the AI Gateway.

Code snippet

```text
sequenceDiagram
    actor A as User/Application
    participant K as Kong API Gateway
    participant U as Unified LLM API (Portkey/LiteLLM)
    participant R as Intelligent Router (Not Diamond/RouteLLM)
    participant O as Optimization (OptiLLM)
    participant P as LLM Provider
    A->>K: LLM Request (API Key/Virtual Key)
    K->>K: Authenticate, Rate Limit, Route
    K->>U: Forward Request
    U->>U: Validate Request, Apply Virtual Key Config
    alt Prompt Template/Partial Applied
        U->>U: Fetch & Assemble Prompt (from Prompt Management)
    end
    U->>R: Request for Model Selection
    R->>R: Evaluate Routing Rules (Cost, Performance, Task, Load)
    R->>R: Select Best Model & Provider
    R->>O: Forward Request with Selected Model
    O->>O: Fine-tune Parameters / Prompt (OptiLLM)
    O->>P: Send Optimized LLM Request
    P-->>O: LLM Response
    O-->>R: Optimized Response
    R-->>U: Routed Response
    U-->>K: Unified Response
    K-->>A: Final Response
    alt Failure or Fallback
        O--xP: Primary LLM Provider Fails
        O->>R: Failure Notification
        R->>R: Initiate Fallback / Retry Logic
        R->>O: Request (to Fallback Provider)
    end
```

*Description: This sequence diagram details the journey of an LLM request from the User/Application through Kong, the Unified LLM API, Intelligent Router, and Optimization layers, finally reaching an LLM Provider. It highlights key decision points like model selection and potential fallback/retry mechanisms. Prompt assembly and virtual key application are integrated into the flow.*

## Definitive Tech Stack Selections

This table outlines the definitive technology choices for the project. These selections are based on the project's requirements, the proposed architecture, and the technologies provided in the initial brief and supporting files.

| Category             | Technology                                            | Version / Details                                        | Description / Purpose                                     | Justification (Optional)                                                                        |
| :------------------- | :---------------------------------------------------- | :------------------------------------------------------- | :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **Languages**        | Python                                                | 3.11+ (latest stable preferred)                          | Primary language for all backend gateway services.        | Expressly mentioned in user's context files and for LLM interaction libraries.                  |
|                      | TypeScript                                            | 5.x (latest stable preferred)                            | Primary language for frontend dashboard.                  | User specified Next.js.                                                                         |
| **Runtime**          | Node.js                                               | 20.x+ (for Next.js)                                      | Frontend runtime.                                         | Required for Next.js.                                                                           |
| **Frameworks**       | Kong                                                  | Latest stable                                            | Outer API Gateway.                                        | User specified.                                                                                 |
|                      | Portkey                                               | Latest stable                                            | Primary Unified LLM API/Observability (or LiteLLM).       | User specified, strong observability features.                                                  |
|                      | LiteLLM                                               | Latest stable                                            | Alternative Unified LLM API (broader model support).      | User specified, for broad model flexibility.                                                    |
|                      | Not Diamond                                           | Latest stable                                            | Primary Intelligent LLM Router (or RouteLLM).             | User specified, focused on cost/performance optimization.                                       |
|                      | RouteLLM                                              | Latest stable                                            | Alternative Intelligent LLM Router (open-source control). | User specified, for custom routing logic.                                                       |
|                      | OptiLLM                                               | Latest stable                                            | LLM Optimization Layer.                                   | User specified, for fine-tuning model selection.                                                |
|                      | Next.js                                               | Latest stable (e.g., 14.x+)                              | Frontend UI framework.                                    | User specified.                                                                                 |
|                      | FastAPI (Python)                                      | Latest stable                                            | Recommended Backend API framework for Python services.    | High performance, ease of use for API development, type hinting.                                |
| **Databases**        | PostgreSQL                                            | 15+ (latest stable preferred)                            | Primary relational data store (for configs, analytics).   | User specified, robust for structured data.                                                     |
|                      | MongoDB                                               | Latest stable (if needed for specific unstructured data) | Potential secondary non-relational data store.            | User specified, for flexible schema if required.                                                |
| **Cloud Platform**   | AWS / GCP / Cloudflare / Fly.io / Railway             | N/A                                                      | Primary cloud providers (flexibility).                    | User specified, supports diverse deployment strategies.                                         |
| **Cloud Services**   | (To be determined by Architect)                       | N/A                                                      | Serverless compute, object storage, managed databases.    | Architect will select specific services based on chosen cloud provider and detailed design.     |
| **Infrastructure**   | Docker                                                | Latest stable                                            | Containerization.                                         | User specified, for consistent deployment.                                                      |
|                      | Kubernetes                                            | Latest stable                                            | Container Orchestration (if chosen for scale).            | User provided `kuma.yaml`, implies container orchestration.                                     |
|                      | Kuma                                                  | Latest stable                                            | Service Mesh (for microservices/Kubernetes).              | User provided `kuma.yaml`, for robust service management.                                       |
|                      | Infrastructure as Code (IaC)                          | (Tool to be selected, e.g., Terraform, AWS CDK)          | Automated infrastructure provisioning.                    | Required for consistent and repeatable deployments.                                             |
| **UI Libraries**     | (To be selected by Design Architect based on Next.js) | N/A                                                      | UI component library for Next.js dashboard.               | Will align with Next.js best practices and design system needs.                                 |
| **State Management** | (To be selected by Design Architect for Next.js)      | N/A                                                      | Frontend state management for Next.js dashboard.          | Will align with Next.js best practices.                                                         |
| **Testing**          | pytest (Python)                                       | Latest stable                                            | Unit/Integration testing framework for Python.            | Standard for Python, user provided `test_integration.py` implies its use.                       |
|                      | Playwright (TypeScript)                               | Latest stable                                            | End-to-end testing framework for dashboard.               | Robust for UI E2E testing.                                                                      |
|                      | Jest/Vitest (TypeScript)                              | Latest stable                                            | Unit testing for Next.js dashboard components.            | Standard for React/Next.js.                                                                     |
| **CI/CD**            | GitHub Actions                                        | N/A                                                      | Continuous Integration/Deployment.                        | User specified GitHub for VCS, logical CI/CD choice.                                            |
| **Other Tools**      | Crawl4AI                                              | Latest stable                                            | Web scraping (from user's other project context).         | Included in user's provided `scout_agent.py` versions. Could be a component for data ingestion. |
|                      | OpenRouter Client (Python)                            | Latest stable                                            | LLM integration (from user's other project context).      | Demonstrated in user's `ai_gateway.py` and `scout_agent.py` versions.                           |

Export to Sheets

## Infrastructure and Deployment Overview

- **Cloud Provider(s):** The architecture is designed for multi-cloud compatibility, with initial deployment targets including AWS, GCP, Cloudflare, Fly.io, or Railway. Specific services will be chosen based on the selected provider during detailed design.

- **Core Services Used:** Will include compute (e.g., EC2, Cloud Run, serverless functions), managed database services (e.g., RDS PostgreSQL, MongoDB Atlas), object storage (e.g., S3, GCS), and networking services.

- **Infrastructure as Code (IaC):** A robust IaC tool (e.g., Terraform, AWS CDK) will be used to define and manage all infrastructure components, ensuring consistency and repeatability across environments.

- **Deployment Strategy:** A fully automated CI/CD pipeline (e.g., via GitHub Actions) will be implemented to support frequent, incremental deployments. The strategy will involve containerization (Docker) and orchestration (e.g., Kubernetes, potentially managed via Kuma service mesh for advanced traffic management and observability). Blue/Green or Canary deployments will be considered for critical updates to minimize downtime.

- **Environments:** Standard environments will include:

    - **Development:** Local developer machines, potentially shared dev environments.

    - **Staging:** Pre-production environment for integration testing, performance testing, and stakeholder review.

    - **Production:** Live environment for end-users.

- **Environment Promotion:** Automated promotion from Development to Staging upon successful CI/CD checks, with manual approval and/or automated E2E tests required for promotion to Production.

- **Rollback Strategy:** Automated rollback procedures will be in place for deployments, triggered by failed health checks or critical alerts post-deployment, or via manual intervention through the CI/CD pipeline.

## Error Handling Strategy

- **General Approach:** A consistent, centralized error handling strategy will be implemented across all services. Errors will be classified (e.g., client errors, server errors, external API errors) and handled appropriately, with clear error codes and messages provided to calling applications (where applicable) without exposing sensitive internal details.

- **Logging:**

    - **Library/Method:** Structured logging will be implemented (e.g., using Python's `logging` module with JSON formatters, or a dedicated logging library like Pino for Node.js if relevant).

    - **Format:** JSON format for all logs to facilitate centralized ingestion and analysis.

    - **Levels:** Standard log levels (DEBUG, INFO, WARN, ERROR, CRITICAL) will be used consistently.

    - **Context:** All logs will include relevant contextual information such as trace IDs, request IDs, component names, LLM provider, model used, and timestamps. Sensitive PII or API keys will be strictly excluded from logs.

- **Specific Handling Patterns:**

    - **External API Calls:** Retry mechanisms (e.g., exponential backoff with jitter, configurable max retries) will be applied for transient failures (e.g., 429, 5xx errors) when interacting with LLM providers. Circuit breaker patterns (e.g., for failing LLM providers) will be implemented at the Intelligent Router layer to prevent cascading failures. Timeouts (connect and read) will be strictly enforced for all external calls.

    - **Internal Errors / Business Logic Exceptions:** Custom error types will be defined for domain-specific errors. Internal errors will result in generic, user-friendly messages for external callers, while detailed error information (including stack traces) will be logged internally.

    - **Transaction Management:** Data consistency will be ensured through appropriate transaction management (e.g., database transactions for PostgreSQL, or idempotent operations for services).

## Coding Standards

These standards are mandatory for all code generation by AI agents and human developers. Deviations are not permitted unless explicitly approved and documented as an exception.

- **Style Guide & Linter:**

    - **Python:** Black for code formatting, Flake8 for linting, MyPy for static type checking. Configuration files (`pyproject.toml`) will be committed.

    - **TypeScript/JavaScript:** ESLint with a recommended configuration (e.g., Airbnb or Google style) and Prettier for formatting. Configuration files (`.eslintrc.js`, `.prettierrc`) will be committed.

- **Naming Conventions:**

    - **Python:** `snake_case` for variables, functions, methods; `PascalCase` for classes; `UPPER_SNAKE_CASE` for constants.

    - **TypeScript/JavaScript:** `camelCase` for variables, functions, methods; `PascalCase` for classes, types, interfaces; `UPPER_SNAKE_CASE` for constants.

    - **Files:** `kebab-case.ts` for TypeScript/JavaScript files; `snake_case.py` for Python files.

- **File Structure:** Adhere strictly to the monorepo layout defined in the "Project Structure" section.

- **Unit Test File Organization:**

    - **Python:** `test_*.py` files in a `tests/unit` or `tests/integration` directory parallel to the source code, or within `tests/` subdirectories of each service.

    - **TypeScript/JavaScript:** `*.test.ts` or `*.spec.ts` files co-located with the source files they test, or within a `__tests__` subdirectory.

- **Asynchronous Operations:**

    - **Python:** Use `async`/`await` with `asyncio` for asynchronous I/O operations (e.g., FastAPI handlers).

    - **TypeScript/JavaScript:** Always use `async`/`await` for promise-based operations; avoid raw Promise `.then().catch()` chains unless specifically justified.

- **Type Safety:**

    - **Python:** Full type hints (`mypy` enforced in CI).

    - **TypeScript:** Strict mode (`strict: true` in `tsconfig.json`) must be enabled. Avoid `any` type; prefer explicit checks or type assertions when necessary.

- **Comments & Documentation:**

    - Code Comments: Explain *why* complex logic is implemented, not *what* it does. Use standard formats (Python docstrings, JSDoc/TSDoc).

    - READMEs: Each major service/module and the root of the monorepo will have a comprehensive README detailing purpose, setup, and usage.

- **Dependency Management:**

    - **Python:** `poetry` (preferred) or `pip-tools` for dependency management and locking.

    - **TypeScript/JavaScript:** `npm` or `yarn` with `package-lock.json`/`yarn.lock`.

    - Policy on adding new dependencies: Vetting for security vulnerabilities, licensing, and active maintenance. Prefer pinning exact versions.

### Detailed Language & Framework Conventions

#### Python Specifics:

- **Immutability:** Use tuples for immutable sequences. Consider `@dataclass(frozen=True)` for immutable data structures.

- **Functional vs. OOP:** Employ classes for representing entities, services, and API controllers (e.g., FastAPI `APIRouter`). Use pure functions for stateless operations.

- **Error Handling Specifics:** Raise specific, custom exceptions inheriting from a base `GatewayError` for domain-specific errors. Use `try-except` blocks appropriately; avoid broad `except Exception:` clauses.

- **Resource Management:** Always use `with` statements for resources (e.g., database connections, file handles).

- **Type Hinting:** All new functions and methods must have full type hints. MyPy will be run in CI.

- **Logging Specifics:** Use Python's standard `logging` module, configured for structured (JSON) output. Include correlation IDs and sanitize sensitive data.

- **Framework Idioms (FastAPI):** Adhere to FastAPI's Pydantic models for request/response validation and serialization. Leverage FastAPI's dependency injection system for service dependencies.

#### TypeScript/Node.js Specifics:

- **Immutability:** Prefer immutable data structures. Use `Readonly<T>`, `ReadonlyArray<T>`, `as const` for object/array literals. Consider libraries like Immer for complex state updates in the frontend.

- **Functional vs. OOP:** Favor functional programming constructs (map, filter, reduce, pure functions) for data transformation. Use classes for services or framework-specific constructs (e.g., Next.js API routes).

- **Error Handling Specifics:** Always use `Error` objects or extensions thereof for `throw`. Ensure `Promise` rejections are always `Error` objects. Use custom error classes inheriting from a base `AppError` for domain-specific errors in the frontend.

- **Null/Undefined Handling:** Strict null checks (`strictNullChecks: true`) must be enabled. Avoid `!` non-null assertion operator; prefer explicit checks, optional chaining (`?.`), or nullish coalescing (`??`).

- **Module System:** Use ESModules (`import`/`export`) exclusively.

- **Logging Specifics:** Use a structured logging library in the Next.js backend (if applicable) and ensure consistent logging practices for frontend events (e.g., error boundaries).

- **Framework Idioms (Next.js):** Follow Next.js App Router conventions for pages, layouts, and API routes. Use built-in Image and Link components for optimization.

## Overall Testing Strategy

This section outlines the project's comprehensive testing strategy, which all AI-generated and human-written code must adhere to.

- **Tools:** Primary testing frameworks include `pytest` for Python backend, `Jest`/`Vitest` for Next.js unit tests, and `Playwright` for E2E tests.

- **Unit Tests:**

    - **Scope:** Test individual functions, methods, classes, or small modules in isolation (e.g., specific routing logic, prompt assembly, API client functions).

    - **Location:** Python `test_*.py` files in parallel `tests/unit` directories. TypeScript `*.test.ts` or `*.spec.ts` co-located or in `__tests__` subdirectories.

    - **Mocking/Stubbing:** Mock all external dependencies (network calls to LLMs, database interactions, external services) using appropriate mocking libraries (`unittest.mock` in Python, Jest mocks in TypeScript).

    - **AI Agent Responsibility:** AI agents must generate unit tests covering all public methods, significant logic paths, edge cases, and error conditions for any new or modified code.

- **Integration Tests:**

    - **Scope:** Test the interaction between several components or services within the application boundary (e.g., Kong routing to Unified API, Router selecting model and calling Unified API, Prompt Management module integrating with Unified API).

    - **Location:** Python `test_*.py` files in parallel `tests/integration` directories.

    - **Environment:** Use lightweight test doubles or actual services with dedicated test configurations (e.g., test containers for databases, mocked LLM endpoints).

    - **AI Agent Responsibility:** AI agents may be tasked with generating integration tests for key service interactions or API endpoints based on specifications.

- **End-to-End (E2E) Tests:**

    - **Scope:** Validate complete user flows or critical paths through the system from the user's perspective, focusing on the external dashboard and its interaction with the gateway's configuration APIs (e.g., configuring a virtual key, viewing LLM usage metrics).

    - **Tools:** Playwright.

    - **AI Agent Responsibility:** AI agents may be tasked with generating E2E test stubs or scripts based on user stories or dashboard functionalities.

- **Test Coverage:**

    - **Target:** Strive for high test coverage (e.g., aiming for 80% line/branch coverage for unit tests on critical business logic), recognizing that quality of tests is paramount over raw numbers.

    - **Measurement:** Integrated into CI/CD pipeline with tools like `coverage.py` for Python and `Istanbul/nyc` for JavaScript/TypeScript.

- **Test Data Management:** Strategies for creating, managing, and isolating test data (e.g., factories, fixtures, database seeding scripts).

## Security Best Practices

Key security considerations relevant to the codebase are mandatory and must be actively addressed.

- **Input Sanitization/Validation:** All external inputs (API requests, user-provided data via dashboard, prompt content) must be rigorously validated and sanitized at the entry points of each service to prevent injection attacks (e.g., prompt injection, SQL injection, XSS). Use schema validation libraries (e.g., Pydantic for Python/FastAPI, Zod/Joi for TypeScript).

- **Output Encoding:** All dynamic data rendered in the Next.js dashboard UI must be contextually auto-escaped by the framework to prevent XSS. If generating content manually, use approved encoding libraries.

- **Secrets Management:** API keys (LLM provider keys, internal service keys), database credentials, and other sensitive information must be stored securely using environment variables, cloud secret management services (e.g., AWS Secrets Manager, GCP Secret Manager), or a dedicated secret management solution (e.g., HashiCorp Vault). Never hardcode secrets or commit them to version control.

- **Dependency Security:** Automated vulnerability scanning tools (`pip-audit` for Python, `npm audit` for Node.js, Dependabot/Snyk alerts) will be integrated into the CI/CD pipeline to identify and mitigate vulnerabilities in third-party libraries promptly.

- **Authentication/Authorization Checks:**

    - **Gateway Access:** Kong will enforce robust authentication (e.g., API keys, OAuth 2.0) for external applications interacting with the AI Gateway.

    - **Internal API/Dashboard:** The internal API and Dashboard will use strong authentication (e.g., OAuth 2.0, JWT) and role-based access control (RBAC) to ensure only authorized users/services can configure and monitor the gateway.

    - **LLM Provider Keys:** Virtual keys will provide an abstraction layer for fine-grained authorization to LLM providers.

- **Principle of Least Privilege:** Database users, service accounts, and IAM roles for cloud services will be granted only the minimum necessary permissions to perform their functions.

- **API Security (General):** All external and internal APIs will enforce HTTPS/TLS. Rate limiting and throttling (managed by Kong and potentially internal services) will be implemented. Standard HTTP security headers (e.g., CSP, HSTS) will be configured.

- **Error Handling & Information Disclosure:** Error messages will not leak sensitive information (stack traces, internal paths, detailed SQL errors) to external callers. Detailed errors will be logged internally for debugging.

- **Security Testing:** Regular security testing, including static application security testing (SAST) and dynamic application security testing (DAST) in CI/CD, and potentially penetration testing, will be considered.

## Key Reference Documents

- [AI Gateway Product Requirements Document (PRD)](https://www.google.com/search?q=prd.md)

- [Frontend Architecture Document (if created)](https://www.google.com/search?q=front-end-architecture.md)

- [UI/UX Specification (if created)](https://www.google.com/search?q=front-end-spec.md)

- [Data Models Document (derived from this Arch document's data models section)](https://www.google.com/search?q=data-models.md)

- [API Reference Document (derived from this Arch document's API Reference section)](https://www.google.com/search?q=api-reference.md)

- [Project Structure Guide (derived from this Arch document's Project Structure section)](https://www.google.com/search?q=project-structure.md)

- [Operational Guidelines Document (derived from this Arch document's Coding Standards, Testing Strategy, Error Handling, and Security Best Practices sections)](https://www.google.com/search?q=operational-guidelines.md)

- [Technology Stack Document (derived from this Arch document's Definitive Tech Stack Selections section)](https://www.google.com/search?q=tech-stack.md)

## Change Log

| Change                        | Date       | Version | Description                                                            | Author            |
| :---------------------------- | :--------- | :------ | :--------------------------------------------------------------------- | :---------------- |
| Initial Draft                 | 2025-06-14 | 1.0.0   | Comprehensive Architecture Document based on PRD and provided context. | Ava "Atlas" Patel |
| Added Design Architect Prompt | 2025-06-14 | 1.0.1   | Appended prompt for Design Architect to guide frontend architecture.   | Ava "Atlas" Patel |

Export to Sheets

---

### 3. AI Gateway Frontend Architecture Document

