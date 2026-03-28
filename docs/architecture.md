# Architecture

## Monorepo Layout

```text
apps/
  api/   # Python FastAPI backend
  web/   # Next.js frontend
docs/    # shared architecture and onboarding docs
```

## Backend Ownership

The backend owns:

- job extraction
- TinyFish scraping orchestration
- question generation and ranking
- interview session state
- answer evaluation
- final feedback reports

## Frontend Ownership

The frontend owns:

- user flows
- authentication UX
- session rendering
- audio capture UI
- report presentation

## Integration Boundary

The frontend should treat the backend as the system of record for interview workflow state.

Core API flows:

1. Create or extract a job target
2. Trigger research
3. Fetch ranked question bank
4. Start interview session
5. Send interview events
6. Fetch feedback report
