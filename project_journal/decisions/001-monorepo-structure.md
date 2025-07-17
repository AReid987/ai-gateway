# ADR 001: Monorepo Structure

## Status
✅ Accepted

## Context
Initial project setup required choosing between:
- Separate repos per service
- Monorepo approach

## Decision
Adopted Turborepo monorepo structure because:
1. Shared code reuse (configs, utils)
2. Simplified dependency management
3. Atomic commits across services
4. Unified CI/CD pipeline

## Consequences
- Requires disciplined directory structure
- Build caching essential (handled by Turborepo)
- All services versioned together
