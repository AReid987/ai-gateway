---
type: Page
title: AI Gateway Frontend Architecture Document
description: null
icon: null
createdAt: '2025-06-16T01:34:46.783Z'
creationDate: 2025-06-15 20:34
modificationDate: 2025-07-06 15:08
tags: []
coverImage: null
---

# AI Gateway Frontend Architecture Document

## Introduction

This document details the technical architecture specifically for the frontend of the AI Gateway, which is the Observability & Analytics Dashboard. It complements the main AI Gateway Architecture Document and builds upon its foundational decisions (e.g., overall tech stack, CI/CD, primary testing tools). Frontend-specific elaborations or deviations from general patterns must be explicitly noted here. The goal is to provide a clear blueprint for frontend development, ensuring consistency, maintainability, and alignment with the overall system design and user experience goals.

- **Link to Main Architecture Document (REQUIRED):** `docs/architecture.md`

- **Link to UI/UX Specification (REQUIRED if exists):** (Not yet created - will be `docs/front-end-spec.md` if defined)

- **Link to Primary Design Files (Figma, Sketch, etc.) (REQUIRED if exists):** (Not yet provided - will be updated when available)

- **Link to Deployed Storybook / Component Showcase (if applicable):** (To be added if a Storybook is implemented)

## Overall Frontend Philosophy & Patterns

The frontend will be built as a Single-Page Application (SPA) utilizing Next.js, focusing on developer experience, performance, and scalability.

- **Framework & Core Libraries:** React 18.x with Next.js 14.x+. These are derived from the 'Definitive Tech Stack Selections' in the main Architecture Document. We will leverage Next.js's features for routing, server-side rendering (SSR) or static site generation (SSG) where appropriate, and API routes for simplified backend interactions if needed for dashboard-specific functionalities.

- **Component Architecture:** We will adopt a modular, component-based architecture. Components will be organized based on their reusability and domain (e.g., global UI components, layout components, feature-specific components). A presentational/container pattern will be generally followed where UI components (`components/ui`) are purely responsible for rendering, and "container" components or pages handle data fetching and state logic.

- **State Management Strategy:** Given the dashboard's role in displaying complex, real-time data and managing configurations, a global state management solution like **Zustand** or **Redux Toolkit** will be evaluated and selected by the Design Architect for the detailed implementation. This will be complemented by React's built-in `useState` and `useReducer` for local component state, and `React Query` or `SWR` for server-side data fetching and caching.

- **Data Flow:** Unidirectional data flow will be maintained, primarily from services/state management down to components via props. Server-side data fetching (SSR/SSG/API routes) will feed initial data, and client-side interactions will trigger API calls that update global state where necessary.

- **Styling Approach:** **Tailwind CSS** will be the primary styling solution, enabling a utility-first approach for rapid UI development and consistent design. This may be complemented by CSS Modules for specific, complex component styles if necessary. `tailwind.config.js` will define the design tokens and theme extensions.

- **Key Design Patterns Used:** Provider pattern (for context, state management), Hooks (for reusable logic), and Service patterns (for API interactions) will be consistently applied.

## Detailed Frontend Directory Structure

This ASCII diagram represents the frontend application's specific folder structure within the `dashboard/` root directory (as part of the monorepo).

Plaintext

```text
dashboard/
├── public/                     # Static assets (images, fonts, etc.)
├── src/
│   ├── app/                    # Next.js App Router: Pages, Layouts, Routes
│   │   ├── (auth)/             # Route group for authentication pages (e.g., login, signup)
│   │   ├── (dashboard)/        # Route group for main dashboard features
│   │   │   ├── page.tsx        # Main dashboard view
│   │   │   ├── layout.tsx      # Dashboard-specific layout
│   │   │   ├── llm-usage/      # LLM usage analytics page
│   │   │   │   └── page.tsx
│   │   │   ├── config/         # Configuration pages
│   │   │   │   ├── providers/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── virtual-keys/
│   │   │   │       └── page.tsx
│   │   │   └── settings/
│   │   │       └── page.tsx
│   │   ├── api/                # Next.js API Routes (if dashboard needs its own backend)
│   │   │   └── auth/
│   │   │       └── route.ts
│   │   ├── globals.css         # Global styles for Tailwind CSS setup
│   │   └── layout.tsx          # Root layout for the entire dashboard application
│   ├── components/             # Shared/Reusable UI Components
│   │   ├── ui/                 # Generic, reusable, presentational UI elements (Button, Input, Card)
│   │   │   ├── Button.tsx
│   │   │   └── ...
│   │   ├── layout/             # Layout components (Header, Sidebar, Footer)
│   │   │   ├── Header.tsx
│   │   │   └── Sidebar.tsx
│   │   ├── charts/             # Reusable charting components (e.g., for metrics)
│   │   │   └── LineChart.tsx
│   │   └── common/             # Other common components not tied to a specific feature or UI element
│   ├── features/               # Feature-specific logic, hooks, non-global state, services, and components solely used by that feature.
│   │   ├── auth/
│   │   │   ├── components/
│   │   │   ├── hooks/
│   │   │   ├── services/
│   │   │   └── store.ts        # Feature-specific state slice
│   │   └── metrics/
│   │       ├── components/
│   │       └── hooks/
│   │       └── services/
│   ├── hooks/                  # Global/sharable custom React Hooks (e.g., useAuth)
│   │   └── useDebounce.ts
│   ├── lib/                    # Utility functions, helpers, constants (pure functions)
│   │   └── utils.ts
│   ├── services/               # Global API service clients or SDK configurations (e.g., apiClient.ts)
│   │   └── gatewayApi.ts       # Service to interact with AI Gateway internal API
│   ├── store/                  # Global state management setup (if used, e.g., Redux Toolkit store)
│   │   ├── index.ts
│   │   └── slices/
│   │       └── userSlice.ts
│   ├── styles/                 # Additional global styles or Tailwind-specific CSS
│   └── types/                  # Global TypeScript type definitions/interfaces
│       └── index.ts
├── package.json                # Project dependencies
├── tsconfig.json               # TypeScript configuration
├── next.config.js              # Next.js configuration
├── tailwind.config.js          # Tailwind CSS configuration
└── README.md                   # Dashboard-specific README
```

### Notes on Frontend Structure:

- The `app/` directory aligns with Next.js App Router conventions for defining routes and layouts.

- Components are primarily organized by their reusability (`components/ui`, `components/layout`) or co-located within their feature directory (`features/`). Components used exclusively by a single feature should reside within `features/[featureName]/components/`.

- Global state slices will reside in `store/slices/` or be co-located within feature directories if they are feature-specific.

## Component Breakdown & Implementation Details

The frontend will primarily consist of components for data visualization (charts, graphs), configuration forms, tables for logs/metrics, and navigation elements. Most feature-specific components will be detailed as user stories are implemented. The AI agent MUST follow the "Template for Component Specification" below whenever a new component is identified for development.

### Component Naming & Organization

- **Component Naming Convention:** PascalCase for files and component names (e.g., `LLMUsageChart.tsx`, `ProviderConfigForm.tsx`). All component files MUST follow this convention.

- **Organization:** Globally reusable components in `src/components/ui/` or `src/components/layout/`. Feature-specific components co-located within their feature directory (e.g., `src/features/metrics/components/LLMUsageSummary.tsx`).

### Template for Component Specification

For each significant UI component, the following details MUST be provided.

#### Component: `{ComponentName}`

- **Purpose:** {Briefly describe what this component does and its role in the UI. MUST be clear and concise.}

- **Source File(s):** {e.g., `src/components/llm-usage/LLMUsageChart.tsx`. MUST be the exact path.}

- **Visual Reference:** {Link to specific Figma frame/component, or Storybook page. REQUIRED.}

- **Props (Properties):** | Prop Name | Type | Required? | Default Value | Description | | :--- | :--- | :--- | :--- | :--- | | `{propName}` | `{Specific primitive, imported type, or inline interface/type definition}` | {Yes/No} | {If any} | {MUST clearly state the prop's purpose and any constraints.} |

- **Internal State (if any):** | State Variable | Type | Initial Value | Description | | :--- | :--- | :--- | :--- | | `{stateVariable}` | `{type}` | `{value}` | {Description of state variable and its purpose.} |

- **Key UI Elements / Structure:**

- **Events Handled / Emitted:**

    - **Handles:** {e.g., `onClick` on a button.}

    - **Emits:** {If the component emits custom events/callbacks not covered by props, describe them with their exact signature.}

- **Actions Triggered (Side Effects):**

    - **State Management:** {e.g., "Dispatches `metricsSlice.actions.fetchUsageData()`."}

    - **API Calls:** {Specify which service/function from the "API Interaction Layer" is called. e.g., "Calls `gatewayApi.getLLMUsage()` on mount."}

- **Styling Notes:**

    - {MUST specify Tailwind CSS classes or reference custom CSS module class names. Any dynamic styling logic based on props or state MUST be described.}

- **Accessibility Notes:**

    - {MUST list specific ARIA attributes, required keyboard navigation behavior, and any focus management requirements.}

## State Management In-Depth

The chosen solution for global state management will be either **Zustand** or **Redux Toolkit**, selected based on a more detailed evaluation by the Design Architect during implementation.

- **Chosen Solution:** (To be finalized: Zustand or Redux Toolkit)

- **Decision Guide for State Location:**

    - **Global State (e.g., Redux/Zustand):** Data shared across many unrelated components (e.g., authentication status, global loading indicators, application-wide configuration data like current virtual key selected); data persisting across routes (e.g., user preferences); complex state logic managed via reducers/thunks. MUST be used for session data, user preferences, application-wide notifications.

    - **React Context API:** State primarily passed down a specific component subtree where prop drilling is undesirable but global state is overkill (e.g., theming, form context, specific feature flags affecting a local subtree). MUST be used for localized state not suitable for prop drilling but not needed globally.

    - **Local Component State (**`useState`**,** `useReducer`**):** UI-specific state, not needed outside the component or its direct children (e.g., form input values, dropdown open/close status, temporary loading states). MUST be the default choice unless criteria for Context or Global State are met.

    - **Server State (React Query/SWR):** Data fetched from the backend that benefits from caching, deduplication, and automatic re-fetching. SHOULD be used for most data fetching from the AI Gateway's internal APIs (e.g., LLM usage metrics, virtual key lists, logs).

### Store Structure / Slices

Conventions for organizing global state will follow either Zustand's implicit store pattern or Redux Toolkit's "slice" pattern (e.g., "Each major feature requiring global state will have its own slice").

- **Core Slice Example (e.g.,** `sessionStore` **for Zustand, or** `sessionSlice` **for Redux Toolkit):**

    - **Purpose:** Manages user session, authentication status, and basic user profile info accessible globally for dashboard access.

    - **State Shape (Interface/Type):**

        TypeScript

        ```text
        interface SessionState {
          currentUser: { id: string; email: string; roles: string[]; } | null;
          isAuthenticated: boolean;
          token: string | null;
          status: "idle" | "loading" | "succeeded" | "failed";
          error: string | null;
        }
        ```

    - **Key Actions (for Zustand) / Reducers/Actions (for Redux Toolkit):** `login`, `logout`, `setAuthStatus`.

    - **Async Thunks (if any, for Redux Toolkit):** `authenticateUser`.

    - **Selectors (if using Redux Toolkit with Reselect):** `selectCurrentUser`, `selectIsAuthenticated`.

### Key Selectors

All selectors deriving data or combining multiple state pieces MUST use `createSelector` from Reselect (or equivalent for other state libraries) for memoization to prevent unnecessary re-renders.

- `selectCurrentUser` (from session slice/store): Returns the `currentUser` object.

- `selectIsAuthenticated` (from session slice/store): Returns `isAuthenticated` boolean.

### Key Actions / Reducers / Thunks

Complex asynchronous operations will be managed by async thunks (Redux Toolkit) or similar patterns (Zustand).

- **Example:** `authenticateUser(credentials: AuthCredentials)`**:**

    - **Purpose:** Handles user login by calling the internal API and updating session state.

    - **Parameters:** `credentials: { email: string; password: string }`

    - **Flow (conceptual):** Dispatches loading state, calls `gatewayApi.login(credentials)`, on success dispatches success state and user data, on failure dispatches error state.

## API Interaction Layer

The frontend dashboard will primarily communicate with the AI Gateway's internal APIs.

- **HTTP Client Setup:** A single Axios instance (e.g., in `src/services/gatewayApi.ts`) will be configured with:

    - Base URL (from environment variable `NEXT_PUBLIC_GATEWAY_API_URL`).

    - Default headers (e.g., `Content-Type: 'application/json'`).

    - Interceptors for automatic auth token injection (from global state, e.g., `sessionStore.token`) and standardized error handling/normalization.

- **Service Definitions:**

    - `gatewayApi.ts` **(in** `src/services/gatewayApi.ts`**):** This central service will encapsulate all interactions with the AI Gateway's internal API.

    - **Functions:** Each service function MUST have explicit parameter types, a return type (`Promise<T>`), JSDoc/TSDoc explaining purpose, params, return value, and any specific error handling.

        - `getLLMUsageMetrics(filters: MetricsFilters): Promise<LLMUsageData>`

        - `getVirtualKeys(): Promise<VirtualKey[]>`

        - `createVirtualKey(data: CreateVirtualKeyDto): Promise<VirtualKey>`

- **Error Handling & Retries (Frontend):**

    - **Global Error Handling:** API errors will be caught globally via Axios response interceptors. They will be presented via a global notification system (e.g., toast notifications) and logged to the console/monitoring service. A global error state (e.g., `uiStore.error`) will manage application-wide error display.

    - **Specific Error Handling:** Components MAY handle specific API errors locally for more contextual feedback (e.g., displaying inline validation messages on forms).

    - **Retry Logic:** Client-side retry logic will be implemented for idempotent API calls (GET, PUT, DELETE) where appropriate (e.g., using `axios-retry`), with configurable max retries and exponential backoff.

## Routing Strategy

Next.js App Router will be used for defining the dashboard's navigation structure.

- **Routing Library:** Next.js App Router.

### Route Definitions

| **Path Pattern**                  | **Component/Page (src/app/...)**              | **Protection**            | **Notes**                                   |
| :-------------------------------- | :-------------------------------------------- | :------------------------ | :------------------------------------------ |
| `/`                               | `app/page.tsx`                                | Authenticated             | Redirects to `/login` if not authenticated. |
| `/login`                          | `app/login/page.tsx`                          | Public (redirect if auth) | Redirects to `/` if already authenticated.  |
| `/dashboard`                      | `app/dashboard/page.tsx`                      | Authenticated             | Main overview.                              |
| `/dashboard/metrics`              | `app/dashboard/metrics/page.tsx`              | Authenticated             | LLM usage, cost, performance metrics.       |
| `/dashboard/config/providers`     | `app/dashboard/config/providers/page.tsx`     | Authenticated             | Management of LLM inference providers.      |
| `/dashboard/config/virtual-keys`  | `app/dashboard/config/virtual-keys/page.tsx`  | Authenticated             | Management of virtual keys.                 |
| `/dashboard/config/routing-rules` | `app/dashboard/config/routing-rules/page.tsx` | Authenticated             | Management of intelligent routing rules.    |
| `/dashboard/logs`                 | `app/dashboard/logs/page.tsx`                 | Authenticated             | View raw logs.                              |
| `/dashboard/traces`               | `app/dashboard/traces/page.tsx`               | Authenticated             | View distributed traces.                    |
| `/dashboard/prompts`              | `app/dashboard/prompts/page.tsx`              | Authenticated             | Prompt template and partial management.     |

### Route Guards / Protection

- **Authentication Guard:** Routes will be protected using Next.js middleware (`middleware.ts`) or higher-order components/wrappers. Unauthenticated users attempting to access protected routes MUST be redirected to `/login`. Logic will check the authentication status from the global session state.

- **Authorization Guard (if applicable):** If role-based access control is implemented (e.g., admin vs. viewer roles for dashboard features), authorization checks will occur at the middleware/layout level, redirecting unauthorized users to a "Forbidden" page or a safe default.

## Build, Bundling, and Deployment

Frontend build and deployment will integrate with the overall monorepo CI/CD pipeline.

- **Build Process & Scripts:** Standard Next.js build scripts (`npm run build`). Environment variables (e.g., `NEXT_PUBLIC_GATEWAY_API_URL`) will be managed via `.env` files or CI/CD environment variables.

- **Key Bundling Optimizations:**

    - **Code Splitting:** Next.js handles route-based code splitting automatically. Dynamic imports (`React.lazy(() => import('./MyComponent'))`) will be used for component-level code splitting for non-critical, large components.

    - **Tree Shaking:** Ensured by modern build tools.

    - **Lazy Loading:** Next.js's Image component handles lazy loading by default. Other assets will be lazily loaded where beneficial.

    - **Minification & Compression:** Handled by Next.js's build process.

- **Deployment to CDN/Hosting:** The dashboard will be deployed to a static site hosting service (e.g., Vercel, Netlify, Cloudflare Pages, S3/CloudFront) as part of the overall monorepo deployment pipeline. Asset caching strategies will ensure optimal delivery and revalidation.

## Frontend Testing Strategy

The frontend testing strategy complements the main Architecture Document.

- **Link to Main Overall Testing Strategy:** `docs/architecture.md#overall-testing-strategy`

### Component Testing

- **Scope:** Testing individual UI components in isolation.

- **Tools:** React Testing Library with Jest/Vitest.

- **Focus:** Rendering with various props, user interactions (clicks, input changes), event emission, basic internal state changes. Snapshot testing used sparingly for stable, presentational components.

- **Location:** `*.test.tsx` or `*.spec.tsx` files co-located alongside components, or in `__tests__` subdirectories.

### Feature/Flow Testing (UI Integration)

- **Scope:** Testing interactions between multiple components to fulfill a small user flow or feature within a page (e.g., a configuration form submission, data filtering in a table). API calls and global state management will be mocked.

- **Tools:** React Testing Library with Jest/Vitest.

- **Focus:** Data flow between components, conditional rendering, navigation within a feature, integration with mocked services/state.

### End-to-End UI Testing Tools & Scope

- **Tools:** Playwright.

- **Scope (Frontend Focus):** Key user journeys such as:

    1. User login and successful navigation to the dashboard.

    2. Viewing LLM usage metrics and applying filters.

    3. Creating and updating a virtual key.

    4. Viewing recent logs and traces.

- **Test Data Management for UI:** API mocking layers (e.g., MSW - Mock Service Worker) or dedicated test backend endpoints will be used to provide consistent test data.

## Accessibility (AX) Implementation Details

Accessibility will be a core consideration from design to implementation, aiming for **WCAG 2.1 AA** compliance.

- **Semantic HTML:** Strict emphasis on using correct HTML5 elements. AI agents MUST prioritize semantic elements over generic `div`/`span` with ARIA roles where a native element exists.

- **ARIA Implementation:** ARIA attributes will be used for custom interactive components (e.g., custom dropdowns, sliders, tabs) following ARIA Authoring Practices Guide (APG) patterns.

- **Keyboard Navigation:** All interactive elements MUST be focusable and operable via keyboard. Logical tab order will be maintained.

- **Focus Management:** Focus will be managed for dynamic content (e.g., modals, dialogs) ensuring focus is trapped within the overlay and returned to the triggering element upon closure.

- **Testing Tools for AX:** Axe DevTools browser extension for manual checks. Automated Axe scans (e.g., `jest-axe` for component tests, Playwright Axe integration for E2E tests) MUST be integrated into the CI pipeline and fail the build on new violations.

## Performance Considerations

Frontend performance will be optimized for fast loading times and responsiveness.

- **Image Optimization:** All images will use Next.js's `Image` component (or equivalent framework-specific optimizer) for automatic optimization, responsive sizing, and lazy loading. SVGs will be preferred for icons.

- **Code Splitting & Lazy Loading:** Next.js's automatic code splitting for routes will be leveraged. Dynamic imports (`import()`) will be used for component-level lazy loading for non-critical, large components.

- **Minimizing Re-renders:** `React.memo` will be used for components that render frequently with the same props. Memoized selectors for global state (if Redux Toolkit is chosen) will be implemented. Avoid passing new object/array literals or inline functions as props directly in render methods where it causes unnecessary re-renders.

- **Debouncing/Throttling:** Utility functions will be used for event handlers (e.g., search input, window resize) to reduce unnecessary executions.

- **Virtualization:** Yes, virtualization will be considered for any long lists or large data sets displayed in the dashboard if performance degradation is observed (e.g., for extensive log or metrics tables).

- **Caching Strategies (Client-Side):** Leverage HTTP caching headers for static assets. React Query/SWR will handle client-side caching of server-fetched data.

- **Performance Monitoring Tools:** Yes, Lighthouse and browser DevTools performance tab will be used for performance monitoring and analysis during development and post-deployment.

## Internationalization (i18n) and Localization (l10n) Strategy

Internationalization is not a primary requirement for this MVP. However, the architecture will consider future support for multiple languages.

- **Requirement Level:** Not required for MVP.

- **Future Library Consideration:** `react-i18next` (or similar) will be considered for future implementation due to its widespread adoption and React integration.

- **Default Language:** `en-US`.

## Feature Flag Management

Feature flags are not a primary architectural concern for this project at this time. However, the system should be designed to allow for easy integration of a feature flag system in the future if required.

## Frontend Security Considerations

Frontend security practices will complement the main Architecture Document.

- **Cross-Site Scripting (XSS) Prevention:** React's JSX auto-escaping MUST be relied upon for rendering dynamic content. If direct DOM manipulation is unavoidable, use a trusted sanitization library (e.g., DOMPurify). Content Security Policy (CSP) will be enforced via HTTP headers set by the backend/CDN.

- **Cross-Site Request Forgery (CSRF) Protection:** If the Next.js API routes handle state-changing operations and use cookie-based sessions, CSRF tokens will be implemented.

- **Secure Token Storage & Handling:** Authentication tokens (e.g., JWTs) will be stored securely (e.g., in `HttpOnly` cookies set by the backend for session management, or in-memory within state management for single-session use). `localStorage` is STRONGLY DISCOURAGED for token storage.

- **Third-Party Script Security:** All third-party scripts will be vetted, loaded asynchronously, and use Subresource Integrity (SRI) hashes where possible.

- **Client-Side Data Validation:** Client-side validation is for UX improvement (immediate feedback) ONLY. All critical data validation MUST occur server-side (as defined in the main Architecture Document).

- **Preventing Clickjacking:** Not explicitly mentioned, but typically covered by HTTP headers (e.g., `X-Frame-Options` via Kong/CDN).

- **API Key Exposure:** API keys for client-side consumed services (if any) MUST be restricted (e.g., HTTP referrer, IP address). For sensitive keys, a backend proxy endpoint will be created.

- **Secure Communication (HTTPS):** All communication with backend APIs MUST use HTTPS.

- **Dependency Vulnerabilities:** Automated vulnerability scans (`npm audit`) will be run in CI. High/critical vulnerabilities MUST be addressed.

## Browser Support and Progressive Enhancement

- **Target Browsers:** Latest 2 stable versions of Chrome, Firefox, Safari, Edge. Internet Explorer is NOT supported.

- **Polyfill Strategy:** `core-js` (via Babel `preset-env`) will be used.

- **JavaScript Requirement & Progressive Enhancement:** Core application functionality REQUIRES JavaScript enabled.

- **CSS Compatibility & Fallbacks:** Autoprefixer will be used.

## Change Log

| **Change**    | **Date**   | **Version** | **Description**                                                                  | **Author**          |
| :------------ | :--------- | :---------- | :------------------------------------------------------------------------------- | :------------------ |
| Initial Draft | 2025-06-14 | 1.0.0       | Comprehensive Frontend Architecture Document based on Main Architecture and PRD. | Phoenix "Prism" Kim |
