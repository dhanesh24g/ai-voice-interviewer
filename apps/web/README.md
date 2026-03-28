# Web App Contract

Recommended frontend stack for this repo:

- Next.js 14+ with App Router
- TypeScript
- Tailwind CSS
- Vercel deployment

Recommended structure:

```text
apps/web/
  app/
  components/
  features/
  lib/
  public/
  styles/
  tests/
  package.json
  next.config.ts
  tsconfig.json
```

Recommended integration rules:

- Use `NEXT_PUBLIC_API_BASE_URL` for the backend base URL.
- Align local frontend origin with `BACKEND_CORS_ORIGINS` in the backend env.
- Keep API calls isolated in `lib/api/`.
- Keep domain-specific screens in `features/`.
- Add shared types for request and response contracts in `lib/types/`.
- Do not call Supabase directly from the UI for core interview orchestration if the backend already owns that workflow.
- Route all interview, extraction, research, and evaluation actions through the backend API.

Recommended feature folders:

- `features/job-targets/`
- `features/question-bank/`
- `features/interview-session/`
- `features/feedback/`

Recommended API client modules:

- `lib/api/job-targets.ts`
- `lib/api/research.ts`
- `lib/api/interview.ts`
- `lib/api/evaluation.ts`
