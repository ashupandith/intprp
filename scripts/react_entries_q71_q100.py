"""Entries Q71–Q100 for build_react_q61_100.py (chunked for maintainability)."""

from __future__ import annotations


def px(*paragraphs: str) -> list[str]:
    return [p.strip().replace("\n", " ") for p in paragraphs if p.strip()]


ENTRIES_Q71_Q100: list[dict] = [
    {
        "num": 71,
        "title": "Best place for API calls?",
        "qsum": "Data routers, hooks, server components, avoiding duplicate loaders and cache fights.",
        "crisp": (
            "Prefer fetching at the boundary that owns navigation and suspense—router loaders/server components/route modules—when you need SSR and early bytes. Else colocate TanStack Query (or "
            "similar) in feature hooks keyed by stable query keys tied to URLs. Avoid mirroring identical calls in loaders and mount effects unless you hydrate shared cache deliberately. Mutations "
            "belong beside UI emitting them, reused across screens via hooks. Instrument waterfalls; cancel with AbortSignal on navigation."
        ),
        "deep": px(
            """
            Boundary choice encodes UX: loaders start work at navigation minimizing spinners chained after paint, while CSR-only bolts may suffice for ancillary widgets. SSR frameworks shift the optimal
            insertion point upward—verify cache semantics versus client stores.
            """,
            """
            Ownership clarity prevents contradictory caches—document whether React Query hydration wraps loader output or loaders stay thin gateways populating caches with `initialData` plus sensible
            `staleTime`.
            """,
            """
            Network policies—auth refreshing, tenancy headers—should live inside a single typed client reused by loaders and mutations to avoid divergence that breaks only in production gateways.
            """,
            """
            Governance includes tracing names on fetch spans, alerting on duplicated identical requests per navigation, ADRs spelling where server actions replace legacy POST glue.
            """,
        ),
        "bullets": [
            "**Decision:** Fetch where navigation/SSR coherence demands; unify cache stories; typed shared clients.",
            "**Risk:** Double fetch waterfalls, contradictory caches, untraced hotspots, leaky credentials in duplicated clients.",
            "**Mitigation:** Loader + query hydration pattern, AbortSignal discipline, centralized fetch policies.",
        ],
        "example": (
            "A dashboard loader prefetched KPI JSON into TanStack Query initial cache; mounts skipped redundant GETs yet still polled per tab policy afterward."
        ),
        "diag": "navigation -> loader/server fetch -> hydrate query cache OR mount hook subscribe",
        "links": ["https://tanstack.com/query/latest", "https://reactrouter.com/en/main/route/loader"],
    },
    {
        "num": 72,
        "title": "Cancel in-flight requests?",
        "qsum": "AbortController, TanStack cancellation, respecting navigation and strict mode quirks.",
        "crisp": (
            "`fetch` wrappers should wire `AbortSignal` from callers; combine with TanStack Query’s automatic cancellation on unmount/query invalidation. Clean up timers and subscriptions similarly. When "
            "using Redux-saga-like patterns propagate abort through typed clients. SSR streaming must tolerate aborted promises without logging false errors. Duplicate concurrent requests collapse via "
            "dedupe keys in libraries or shared in-flight promises. Document double-invocation expectations under Strict Mode tests."
        ),
        "deep": px(
            """
            Cancellation prevents race updates: slower responses overwriting fresher edits after reordering navigations destroys trust—you must ignore or gate responses with correlation ids.
            """,
            """
            Libraries differ: native `AbortController` interoperates broadly; Axios supports signals; Apollo uses different ergonomics—standardize wrappers for teams.
            """,
            """
            Operational logging should classify intentional abort separately from failures to avoid polluting SLI burn rates masking real outage signals.
            """,
            """
            Accessibility ties to cancelling spinners cleanly—halt aria-busy when work stops—even if aborted—so AT users aren’t stranded waiting forever.
            """,
        ),
        "bullets": [
            "**Decision:** Abort on navigation/component teardown; correlate responses; classify abort noise in telemetry.",
            "**Risk:** Stale commits, leaky listeners, flaky Strict Mode doubles, drowned SLO dashboards.",
            "**Mitigation:** Shared fetch façade, regression tests swapping routes mid-flight, humane error mapping.",
        ],
        "example": (
            "A search palette aborted prior typeahead GETs via AbortSignal—only latest term painted results eliminating odd flicker regressions QA flagged."
        ),
        "diag": "navigation/unmount -> controller.abort -> fetch rejects AbortError -> ignore stale handlers",
        "links": ["https://developer.mozilla.org/en-US/docs/Web/API/AbortController", "https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation"],
    },
    {
        "num": 73,
        "title": "Handle async race conditions?",
        "qsum": "Request versioning, reducer patterns, guarding state updates.",
        "crisp": (
            "Track monotonically increasing request ids or AbortController per async unit; discard late responses mismatching ids. Prefer reducers that fold events over ad hoc sequential `setState`. "
            "When impossible to abort upstream, freeze UI snapshots until authoritative merge or show conflict dialogs. SSR should serialize consistent seeds so CSR doesn’t regress. Observability compares "
            "timestamps correlating anomalies. Property-style tests fuzz ordering of completions against shared fixtures."
        ),
        "deep": px(
            """
            Race bugs surface when parallel fetches reorder around user edits—they are classic yet still ship when teams skip discipline during crunch.
            """,
            """
            Redux-saga/channel patterns or reactive streams formalize concurrency; lighter apps use reducer hooks or finite machines inside features.
            """,
            """
            Operational triage distinguishes races from infra latency using span ids—pair support tickets with chronological logs instead of guesses.
            """,
            """
            Governance mandates code review checklist items for effects touching remote data—cheap insurance relative to escalation hours.
            """,
        ),
        "bullets": [
            "**Decision:** Correlate requests, centralize merges, finite states for multi-step workflows.",
            "**Risk:** Stale renders, contradictory forms, flaky tests masking production races.",
            "**Mitigation:** Abort + ids, exhaustive tests ordering completions, SSR parity checks.",
        ],
        "example": (
            "A pricing panel ignored quote responses lacking matching request tokens after users edited quantities rapidly—finance stopped seeing impossible crossed prices."
        ),
        "diag": "effect issues request N -> only apply results where N matches latest",
        "links": ["https://react.dev/reference/react/useEffect", "https://kentcdodds.com/blog/fix-the-not-an-error-console-warning"],
    },
    {
        "num": 74,
        "title": "API failure and retries?",
        "qsum": "Backoff, jitter, idempotency, Surfacing degraded UX responsibly.",
        "crisp": (
            "Retry idempotent reads with exponential backoff and jitter via libraries or gateways; POST mutations require tokens or uniquely keyed server semantics to replay safely—never blind automatic "
            "POST storms. Surfacing deterministic error taxonomy helps localization and alerting. Offline-first flows queue with durable rules. Tie circuit-breaker thresholds to dashboards so partial "
            "degrades page-by-page—not global blackouts—for blast radius containment."
        ),
        "deep": px(
            """
            Client retries interact with infra rate limits—uncoordinated thundering herds can worsen incidents; coordinate with gateways and backoff budgets documented in SLAs.
            """,
            """
            UX distinguishes retryable flaky networks from permanent authorization failures minimizing helpless loops frustrating users unnecessarily.
            """,
            """
            Security forbids blindly echoing upstream stack traces yet still requires actionable correlation ids for SOC triage aligning browser to server logs responsibly.
            """,
            """
            Operational playbooks annotate which routes degrade gracefully caching last-known-good snapshots read-only acknowledging staleness ethically.
            """,
        ),
        "bullets": [
            "**Decision:** Retry safe reads thoughtfully; POST only with idempotency; categorize errors powering UX telemetry.",
            "**Risk:** Double-spend mutations, amplification outages, leaky sensitive errors.",
            "**Mitigation:** Mutation keys, server dedupe tables, backoff policies, degraded read-only shells.",
        ],
        "example": (
            "A checkout POST retried safely using idempotency keys—gateway deduped duplicates while flaky Wi-Fi ceased double charges support escalations noticed previously."
        ),
        "diag": "error taxonomy -> transient (retry backoff) vs permanent (block + guide) vs conflict (manual)",
        "links": ["https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/", "https://stripe.com/docs/api/idempotent_requests"],
    },
    {
        "num": 75,
        "title": "SWR vs React Query?",
        "qsum": "Feature depth, suspense integration, normalization, ecosystems.",
        "crisp": (
            "TanStack Query leads many teams needing mutations, retries, persistence plugins, DevTools richness, suspense experiments, predictable cache hierarchies keyed explicitly. SWR excels at ergonomic "
            "fetch hooks with lighter footprint historically—evaluate current feature matrices before choosing. Both dwarf ad hoc contexts; standardize conventions (keys, serializers, SSR hydration). "
            "Migration cost matters if legacy code ingrained SWR patterns prematurely before mutation complexity arrived."
        ),
        "deep": px(
            """
            Decision drivers include mutation choreography, optimistic update tooling, prefetch APIs, SSR patterns, governance around shared defaults per product line consuming one platform SDK.
            """,
            """
            Architectural alignment with routers and suspense boundaries informs selection when streaming HTML must align with hydrating queries deterministically avoiding double penalties.
            """,
            """
            Operational tooling—time-travel devtools adoption—helps incident reproduction when stale caches blamed incorrectly without inspectable timelines.
            """,
            """
            Teams standardize wrappers adding auth, tracing headers, exponential policies—regardless which core library—to avoid seventeen bespoke fetch dialects drifting subtly.
            """,
        ),
        "bullets": [
            "**Decision:** Pick TanStack Query when mutation-heavy; SWR acceptable for read-mostly ergonomics until complexity grows—audit yearly.",
            "**Risk:** Split conventions across squads causing cache chaos; training debt when choices drift silently.",
            "**Mitigation:** Org-wide query client factory document, scaffolding templates, SSR guidelines.",
        ],
        "example": (
            "A commerce org standardized React Query wrappers—gift cards reused mutation helpers onboarding features instead of rewriting retry logic inconsistently fragmenting reliability."
        ),
        "diag": "QueryClient defaults -> feature hooks -> suspense/error boundaries overlay",
        "links": ["https://tanstack.com/query/latest/docs/framework/react/overview", "https://swr.vercel.app/docs/getting-started"],
    },
    {
        "num": 76,
        "title": "React Testing Library philosophy?",
        "qsum": "User-centric queries and resilience to refactors—not coupling to internals.",
        "crisp": (
            "React Testing Library steers queries toward roles, labels, and accessible text because those mirror how humans and assistive tech encounter the UI. Tests should survive refactors that keep "
            "behavior intact—the suite protects users, not a specific hook layout. Prefer MSW over module mocks that silently delete integration signal. Narrow unit tests still fit pure parsers and tiny "
            "utilities. When markup is inaccessible, fix the markup or escalate with axe reports instead of leaning on brittle test hacks long term."
        ),
        "deep": px(
            """
            Confidence grows when refactor diffs unrelated to UX stop failing CI arbitrarily—teams ship faster knowing protection targets contracts customers feel.
            """,
            """
            Anti-patterns include selecting by classnames or undocumented DOM structure that designers change freely; coupling tests to Redux store internals when behavior could be asserted via rendered outcomes invites churn.
            """,
            """
            Organizational adoption pairs RTL with guidelines on faker usage, deterministic clocks, and accessibility lint in CI so quality is a default, not an individual heroics pattern that drifts by squad.
            """,
            """
            Leadership metrics might track mean time to add a behavior test, flake rate, and coverage on top five revenue paths—keeping discussion grounded in delivery data instead of dogma.
            """,
        ),
        "bullets": [
            "**Decision:** Accessible queries plus integration breadth; HTTP-level mocks; prioritize tests on core journeys.",
            "**Risk:** Flaky timeouts, shallow snapshots, module mocks hiding integration bugs, inaccessible DOM that tests paper over.",
            "**Mitigation:** Deterministic providers, MSW, axe in CI, review checklists for query choice and async handling.",
        ],
        "example": (
            "A design refresh renamed CSS modules wholesale—RTL suites stayed green while visual regression flagged intentional pixel deltas separately without conflating behavior drift."
        ),
        "diag": "render(AppProviders) -> user interacts -> assert visible accessible outcomes",
        "links": ["https://testing-library.com/docs/react-testing-library/intro/", "https://mswjs.io/"],
    },
    {
        "num": 77,
        "title": "Testing components effectively?",
        "qsum": "Granularity versus realism—providers, branches, suspense, and stable factories.",
        "crisp": (
            "Provide a thin `renderWithProviders` layering router, TanStack Query, theme, feature flags, and i18n as production does. Enumerate scenarios: loading, empty, success, forbidden, degraded read-only "
            "mode, and hard failure—not only the sunny path. Use `@testing-library/user-event` for realistic input. Exercise suspense boundaries from routers and `React.lazy` with deliberate fallbacks. "
            "Stabilize time and network mocks so animations and polls do not flake. Keep factories readable; avoid giant props blobs that obscure intent."
        ),
        "deep": px(
            """
            Scenario matrices outperform single asserts: multilingual copy, RTL layout quirks, keyboard-only workflows, and screen reader-visible error summaries should appear in suites that stakeholders trust for release gates.
            """,
            """
            Boilerplate creep is solved by scaffolding and small builders for common entities—not by skipping sad paths that customers hit during incidents.
            """,
            """
            Suspense and error boundaries need explicit assertions: stalled promises should reveal fallback UI without infinite spinners locking focus traps incorrectly.
            """,
            """
            Governance includes flake budgets: when tests become noisy, teams delete or silence them—which is worse than missing coverage unless you discipline reruns versus root fixes transparently during retrospectives.
            """,
        ),
        "bullets": [
            "**Decision:** Default to realistic provider stacks; scripted scenario matrices; tame async with MSW plus fake timers.",
            "**Risk:** Unrepresentative tests, flaky CI, duplication of gigantic setup blocks, asserting implementation trivia.",
            "**Mitigation:** Shared render helpers, data builders, prioritized journey list, alerting on flake spikes.",
        ],
        "example": (
            "A checkout flow asserted card decline and retry branches; regressions tied to PSP timeouts were caught pre-release instead of inflaming support queues."
        ),
        "diag": "renderWithProviders -> user flows -> RTL queries -> assert UX states + suspense/error",
        "links": [
            "https://testing-library.com/docs/react-testing-library/setup/",
            "https://kentcdodds.com/blog/integration-testing",
        ],
    },
    {
        "num": 78,
        "title": "Unit vs integration test split?",
        "qsum": "Pyramid realism, seams, ROI on React codebases.",
        "crisp": (
            "Unit-test pure utilities, reducers, validators, serializers, formatters—they are cheap, deterministic, pinpoint regressions precisely. Integration-test feature slices with RTL plus MSW to "
            "exercise hooks, routers, caches, i18n, and loaders together—that is where most React regressions hide. Reserve E2E for few critical scripts users cannot tolerate breaking. Prefer coverage on "
            "money paths over vanity percentages. Adapt the pyramid when micro-frontends or complex auth demand more contract tests near boundaries."
        ),
        "deep": px(
            """
            Misplaced unit tests mocking every module evaporate confidence because they celebrate strings matching instead of coherent behavior customers feel end-to-end.
            """,
            """
            Conversely, gigantic integration setups that boot entire apps per test lengthen CI feedback loops until developers skip suites locally—trade width for parallelization and ruthless prioritization journeys.
            """,
            """
            Architecture seams like OpenAPI-generated clients deserve contract tests aligning consumer expectations with backends independent of JSX specifics.
            """,
            """
            Governance tracks defect escape rate by layer: spikes in integration-layer misses justify investment; pervasive E2E flakes justify surgical replacement with lower layers first.
            """,
        ),
        "bullets": [
            "**Decision:** Thick integration for React features; skinny pure units; sparing E2E on irreplaceable paths.",
            "**Risk:** Mock-heavy false greens, oversized slow suites, meaningless coverage quotas.",
            "**Mitigation:** MSW realism, flaky budgets, prioritized journey backlog, parallelism.",
        ],
        "example": (
            "A payments team redirected effort from mocking internals to RTL+MSW integration tests; Sev2 regressions dropped while CI stayed under ten minutes partitioned."
        ),
        "diag": "pure helpers (unit fast) <- feature slice RTL+MSW (integration) -> few Playwright smokes",
        "links": ["https://kentcdodds.com/blog/write-tests", "https://martinfowler.com/articles/practical-test-pyramid.html"],
    },
    {
        "num": 79,
        "title": "Mocking API calls in tests?",
        "qsum": "MSW versus module mocks and maintenance cost.",
        "crisp": (
            "Prefer MSW (or parallel HTTP stubs) intercepting realistic URLs, headers, and bodies so components exercise serializers and error parsers you ship. Avoid mocking your own modules unless crossing "
            "system boundaries unavoidable. Encode delay, failure injectors, pagination edges as reusable handlers. Snapshot handler contracts when APIs version. Teach teams not to drift handlers from "
            "OpenAPI—generate fixtures when feasible."
        ),
        "deep": px(
            """
            Layered mocking mirrors production networking—latency, chunked bodies, redirects—rather than abruptly resolving promises that omit parsing branches never executed until incidents.
            """,
            """
            Operations benefit when tests assert telemetry headers correlate with mocks simulating infra slowdowns distinguishing client bugs from gateway brownouts realistically.
            """,
            """
            Maintenance debt hits when swagger updates skip MSW parity—automate drift checks tying schema versions to handlers in CI.
            """,
            """
            Accessibility still matters inside mocked stacks: asserting error dialogs appear when mocked 403 matches production semantics not silent blank screens.
            """,
        ),
        "bullets": [
            "**Decision:** Mock at HTTP boundaries; share fixtures; version handlers with schemas.",
            "**Risk:** Handlers lying about reality; double maintenance; mocking away critical parsing paths.",
            "**Mitigation:** Contract tests, OpenAPI codegen, reviewer checklist for unhappy paths.",
        ],
        "example": (
            "Handlers simulated 429+Retry-After; UI surfaced polite backoff copy—production matched because parser code paths were warmed in tests beforehand."
        ),
        "diag": "RTL render -> fetch hits MSW -> handlers return realistic payloads/errors",
        "links": ["https://mswjs.io/docs/", "https://testing-library.com/docs/react-testing-library/example-intro/"],
    },
    {
        "num": 80,
        "title": "Testing hooks?",
        "qsum": "`renderHook`, providers, timers, SSR-safe patterns.",
        "crisp": (
            "`@testing-library/react` `renderHook` (or wrappers) validates custom hooks isolated with realistic provider trees—especially when hooks touch QueryClient, routers, locales. Fake timers systematically "
            "for intervals and debouncing. Assert cleanup on unmount discards subscriptions. Prefer integration through components when feasible because hooks seldom exist devoid of rendering context realistically; "
            "reach for isolated hook tests mainly for reusable libraries or gnarly async state machines needing exhaustive tables."
        ),
        "deep": px(
            """
            Library authors shipping hooks externally discipline surface area with exhaustive cases—consumers embedding those hooks benefit from narrower tests assuming library coverage exists but still asserting integration seams.
            """,
            """
            Operational reliability demands verifying Strict Mode double-invocation expectations do not explode duplicate intervals when developers forget guards during refactors hurriedly patching incidents overnight.
            """,
            """
            SSR parity sometimes requires running hooks under dual environments or extracting environment-agnostic cores tested purely while thin adapters stay trivial.
            """,
            """
            Governance encourages naming hook test utilities mirroring production providers so onboarding contributors stop inventing twenty bespoke wrapper variants diverging silently.
            """,
        ),
        "bullets": [
            "**Decision:** `renderHook` with real providers; fake timers; verify cleanup; prefer component integration when possible.",
            "**Risk:** Over-mocking React internals, missing provider context, flaky timers.",
            "**Mitigation:** Shared wrapper utilities, docs on hook contracts, property tests for reducers.",
        ],
        "example": (
            "A `useSessionRefresh` hook test advanced fake timers ensuring duplicate refresh storms did not schedule after unmount—mobile webviews stopped draining batteries reported earlier."
        ),
        "diag": "renderHook(() => useFoo(), { wrapper }) -> act/advanceTimers -> assert state + cleanup",
        "links": ["https://testing-library.com/docs/react-testing-library/api/#renderhook", "https://react.dev/reference/reactStrictMode"],
    },
    {
        "num": 81,
        "title": "E2E options for React?",
        "qsum": "Playwright versus Cypress versus ROI and environments.",
        "crisp": (
            "Playwright often wins parallelization, tracing, multi-browser matrix, codegen—Cypress excels DX for many teams historically with rich time-travel debugging. Align E2E against ephemeral preview envs seeded "
            "deterministically. Tag smoke versus deep regressions nightly. Stable selectors prioritize roles/`data-testid` policy over CSS chaos. Correlate traces with backend logs using shared ids. Fight flake with "
            "retry policies but measure root causes—retries mask product bugs if abused."
        ),
        "deep": px(
            """
            React hydration races surface uniquely in E2E—assert only after network idle or explicit readiness markers instead of arbitrary sleeps destabilizing pipelines randomly.
            """,
            """
            Operations integrate deployment hooks running smokes before promoting canary traffic—fail fast when micro-frontends version skew breaks shell assumptions customers would hit minutes later otherwise.
            """,
            """
            Cost management caps parallel workers versus license spend—executive stakeholders prefer fewer deeper flows over hundreds of shallow duplicates that cheaper layers already stress adequately.
            """,
        ),
        "bullets": [
            "**Decision:** Small high-signal E2E set on Playwright or Cypress with tracing and tagged suites.",
            "**Risk:** Flake, slow feedback, environment drift, over-reliance on CSS selectors.",
            "**Mitigation:** Seed data, readiness contracts, role/testid policy, nightly triage ritual.",
        ],
        "example": (
            "Five Playwright smokes guarded login, pay, and refund—rolled back a canary when shell authentication cookie changes broke before full traffic shift."
        ),
        "diag": "preview env -> seed -> E2E navigates -> trace + logs correlated",
        "links": ["https://playwright.dev/", "https://www.cypress.io/"],
    },
    {
        "num": 82,
        "title": "Stable selectors in UI tests?",
        "qsum": "Roles, labels, `data-testid` policy, resisting brittle CSS.",
        "crisp": (
            "Default to accessible roles and visible labels per RTL guidance. When markup cannot expose stable accessible names, adopt a disciplined `data-testid` namespace (`screen`, `checkout.submit`) agreed with "
            "design systems—never raw CSS classes designers rename weekly. Document policies in CONTRIBUTING. E2E should share philosophy with component tests to reduce dual mental models. Review changes removing "
            "testids with same rigor as API breaks."
        ),
        "deep": px(
            """
            Brittle selectors couple tests to implementation noise—refactors improving semantics should not break CI if behavior preserved; conversely tests must catch broken accessibility when labels disappear silently harming customers truly.
            """,
            """
            Governance publishes allowlists and lint rules preventing duplicate conflicting testid conventions bloating DOM unnecessarily confusing designers aesthetically yet pragmatically accepting minimal attributes improving automation reliability measurably.
            """,
            """
            Internationalization complicates text-based queries—prefer roles with name options referencing translated strings via keys or aria-label attributes stable across locales intentionally chosen during design reviews collaboratively.
            """,
            """
            Observability tags sometimes align testids with analytics funnels—avoid leaking PII into attributes scraped by third-party RUM tooling.
            """,
        ),
        "bullets": [
            "**Decision:** Accessible queries first; namespaced testids when necessary; written policy.",
            "**Risk:** CSS-chained selectors, duplicate ids, locale-flaky text matching.",
            "**Mitigation:** Lint, design pairing, shared testing cookbook, periodic audits.",
        ],
        "example": (
            "Switching design tokens renamed CSS modules but `data-testid='invoice-total'` kept E2E stable while a11y roles improved simultaneously."
        ),
        "diag": "prefer getByRole -> else label text -> else stable data-testid (documented)",
        "links": ["https://testing-library.com/docs/queries/about#priority", "https://playwright.dev/docs/locators"],
    },
    {
        "num": 83,
        "title": "Common React security risks?",
        "qsum": "XSS, unsafe HTML, bad auth assumptions, dependency supply chain.",
        "crisp": (
            "Top risks: injecting unsanitized HTML or URLs, trusting client-only route guards, leaking secrets into bundles, unsafe `postMessage` bridges in micro-frontends, bad Content-Security-Policy hygiene, "
            "vulnerable dependencies, and logging PII to client analytics. React escapes text by default but not when you bypass with `dangerouslySetInnerHTML`, custom URL schemes, or JSON-LD embedded raw. Treat npm "
            "audits and lockfile review as release gates; pin CI provenance."
        ),
        "deep": px(
            """
            Architecture reviews ask where user-generated content flows—comments, bios, CMS blocks—and ensure sanitization libraries versioned centrally with tests reproducing historical bypasses researchers publish periodically responsibly.
            """,
            """
            Supply chain attacks remind teams verify package integrity with provenance signatures increasingly supported by registries—automation blocks merges when checksums drift inexplicably indicating potential compromise requiring incident response immediately.
            """,
            """
            Operational dashboards should correlate CSP violations with recent feature-flag toggles—experiments adding tags without security review are a routine source of avoidable regressions caught late otherwise.
            """,
            """
            Governance ties threat models to React surfaces: only vetted modules expose `dangerouslySetInnerHTML` wrappers with PR templates capturing risk acceptance for regulated features.
            """,
        ),
        "bullets": [
            "**Decision:** Treat UGC as hostile; server authority; CSP; supply chain checks; minimal dangerous APIs.",
            "**Risk:** XSS, token theft, open redirects, vulnerable packages, micro-frontend trust holes.",
            "**Mitigation:** Sanitize, httpOnly cookies, strict `postMessage` origins, audits, ADRs for exceptions.",
        ],
        "example": (
            "A CMS rich-text field attempted raw HTML; a sanitizer wrapper plus CSP report-only mode caught third-party script injections before enforcement blocked customers."
        ),
        "diag": "trusted templates only -> sanitize UGC -> CSP reports -> audited deps",
        "links": ["https://react.dev/learn/dom-components#dangerously-setting-the-inner-html", "https://owasp.org/www-project-top-ten/"],
    },
    {
        "num": 84,
        "title": "How React prevents XSS?",
        "qsum": "Default escaping and where it stops.",
        "crisp": (
            "React escapes string children inserted into DOM text nodes, limiting classic HTML injection unless you circumvent via `dangerouslySetInnerHTML`, custom attribute handlers injecting raw HTML into DOM APIs directly, "
            "or buggy server rendering pipelines emitting unsanitized HTML ahead of hydration. URLs in `href`/`src` still need validation blocking `javascript:` schemes. Serialization of JSON into script tags demands "
            "safe embed patterns. CSP provides defense-in-depth layering beyond framework defaults indispensable for mature programs."
        ),
        "deep": px(
            """
            Hydration mismatches are rarely XSS by themselves but they reveal when SSR templates stray from client escaping conventions—attackers probe weird Unicode and parser edges when those layers disagree.
            """,
            """
            Third-party widgets that write imperative DOM may bypass React’s child escaping—vendor review must confirm they treat content as hostile, not “trusted CMS output.”
            """,
            """
            Operational cadences pair automated scanners with staged DAST before big releases—especially when marketing adds third-party tags that collide with tightened CSP rollout plans.
            """,
            """
            Training should separate framework defaults from product policy: legal rich text and embeds still need sanitization pipelines even when plain JSX text is safe.
            """,
        ),
        "bullets": [
            "**Decision:** Trust default escaping; treat explicit escape hatches as privileged; validate URLs; add CSP.",
            "**Risk:** Sanitizer bypass, unsafe URLs, imperative DOM libraries, bad SSR templates.",
            "**Mitigation:** Allowlisted components, security review, automated scans, safe JSON embedding helpers.",
        ],
        "example": (
            "Pen testers failed to inject script via JSX text but flagged `javascript:` bookmarklets in unsanitized deep links—URL policy closed the gap."
        ),
        "diag": "JSX text -> escaped -> DOM; bypass only via explicit dangerous APIs + review",
        "links": ["https://react.dev/learn/dom-components#dangerously-setting-the-inner-html", "https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html"],
    },
    {
        "num": 85,
        "title": "dangerouslySetInnerHTML usage?",
        "qsum": "When justified, sanitization, CSP, auditing.",
        "crisp": (
            "Use only behind an audited sanitizer (`DOMPurify` configs reviewed) with strict allowlists, never raw CMS HTML unchecked. Narrow surface: wrap in dedicated component forbidding arbitrary props escalation. Pair "
            "with CSP disallowing unsafe-inline except nonces pinned carefully. Log usage in codeowners file requiring security stamp. Prefer markdown-to-safe-HTML pipelines over pasting CMS blobs when possible alternatives exist."
        ),
        "deep": px(
            """
            Sanitizer allowlists decay the moment new embed types ship without joint design/security review—treat changes like API changes with versioning and penetration retests where warranted.
            """,
            """
            Performance and resilience matter: sanitizing gigantic HTML blobs on every render burns CPU—cache sanitized output immutably by content hash when possible yet invalidate on policy bumps.
            """,
            """
            CSP nonces rotated per request interplay with CDN caching—architecture must avoid caching personalized HTML carrying stale nonces that break hydration or inadvertently loosen policy.
            """,
            """
            Audit trails listing every callsite importing the sanctioned wrapper help SOC teams scope incident response instead of blindly searching mega-repos manually during adrenaline-heavy nights.
            """,
        ),
        "bullets": [
            "**Decision:** Centralize sanitized component; forbid scattered calls; CSP + audits.",
            "**Risk:** Sanitizer bypass, oversized HTML denial-of-service, nonce misconfiguration.",
            "**Mitigation:** Threat modeling, incremental allowlist changes, fuzzing payloads, caching sanitized output server-side.",
        ],
        "example": (
            "A help center migrated to a single `SanitizedHtml` module; penetration retests narrowed focus and logging proved no stray call sites remained."
        ),
        "diag": "CMS HTML -> server sanitize -> store -> client renders via SanitizedHtml only",
        "links": ["https://github.com/cure53/DOMPurify", "https://react.dev/reference/react-dom/components/common#dangerously-set-inner-html"],
    },
    {
        "num": 86,
        "title": "Secure token handling?",
        "qsum": "httpOnly cookies, storage trade-offs, XSS blast radius.",
        "crisp": (
            "Prefer short-lived sessions in httpOnly, Secure, SameSite cookies with rotation and server-side binding where possible—avoid long-lived refresh tokens in `localStorage` readable by any XSS. When SPAs talk to "
            "third-party APIs, use BFF or token exchange patterns that keep secrets off the client. Document CORS rules and CSRF protections explicitly. Treat successful XSS as credential compromise unless tokens are "
            "inaccessible to JavaScript by design."
        ),
        "deep": px(
            """
            Bearer tokens reachable from React enlarge XSS blast radius compared with httpOnly session cookies—even excellent component hygiene cannot promise zero XSS forever, so placement of secrets is architectural insurance.
            """,
            """
            Micro-frontends complicate scopes: agreeing on registrable domains, cookie attributes, SharedWorker usage, and which remotes may call which session endpoints prevents silent divergence that pen tests exploit later between squads onboarded asynchronously.
            """,
            """
            Operations teams correlate refresh spikes versus botnets versus flaky mobile radios so WAF thresholds do not punish legitimate users—observability on auth churn is humanitarian as much as statistical.
            """,
            """
            Incident runbooks should rotate sessions decisively while keeping user messaging factual—over-announcing breach details harms trust when root cause was benign config drift instead of adversary action.
            """,
        ),
        "bullets": [
            "**Decision:** Prefer opaque cookies via same-site APIs or vetted auth SDKs; keep refresh off client when feasible.",
            "**Risk:** XSS token theft, permissive CORS, CSRF gaps on cookie sessions, secrets in env bundles.",
            "**Mitigation:** PKCE where OAuth applies, CSP, churning sessions on privilege change, secure logging discipline.",
        ],
        "example": (
            "A SaaS dashboard moved OAuth refresh entirely server-side; red-team XSS payloads could perturb UI yet could not harvest refresh material stored in JS memory previously."
        ),
        "diag": "browser cookie (httpOnly) -> BFF/session API -> downstream services (no bearer in SPA)",
        "links": ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies", "https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html"],
    },
    {
        "num": 87,
        "title": "Accessibility best practices?",
        "qsum": "WCAG-aligned patterns in React-heavy SPAs.",
        "crisp": (
            "Design keyboard-first flows, visible focus, logical heading hierarchy, landmarks, captions or transcripts for media, and color contrast backed by tokens—not hover-only affordances. Prefer real labels over "
            "`placeholder` text. Use live regions sparingly for async status that isn’t already exposed via text. Wire `eslint-plugin-jsx-a11y` and axe in CI. Virtualized lists must keep focus and announcements "
            "coherent when rows recycle."
        ),
        "deep": px(
            """
            Accessibility is product quality—not a checkbox sprint: inclusive flows widen the addressable market and cut support churn when users can finish tasks without workarounds.
            """,
            """
            Components using portals (`createPortal`) need deliberate focus traps, escape handling, scroll locking, and returning focus to the element that opened the overlay.
            """,
            """
            Token-driven themes still need contrast budgets; automate checks on light, dark, and high-contrast modes because designers iterate faster than audits can run manually each sprint.
            """,
            """
            Instrument customer journeys with qualitative feedback loops—sessions with disabled users catch what automated rules miss (live region verbosity, confusing landmark structure, timing of validation messages).
            """,
        ),
        "bullets": [
            "**Decision:** Automate lint + axe; pair with manual passes on top journeys; document modal/focus patterns.",
            "**Risk:** Keyboard dead-ends, unreadable errors, motion sickness from undamped animations, token contrast regressions.",
            "**Mitigation:** Design review gates, reduced-motion CSS, usability studies with assistive tech users.",
        ],
        "example": (
            "A retail checkout restored focus to the triggering control after address validation modals; cart abandonment on mobile screen readers dropped in post-release surveys."
        ),
        "diag": "semantics + focus order -> keyboard path -> CI a11y -> spot manual audit",
        "links": ["https://www.w3.org/WAI/WCAG22/quickref/", "https://www.npmjs.com/package/eslint-plugin-jsx-a11y"],
    },
    {
        "num": 88,
        "title": "Keyboard and focus management?",
        "qsum": "Traps, restoration, roving tabindex, route changes.",
        "crisp": (
            "Manage focus explicitly for modals/menus: trap inside while open, restore to the trigger on close, and expose `Escape` behavior consistent with platform expectations. For composite widgets (toolbars, grids) "
            "use roving tabindex or library helpers that follow ARIA Authoring Practices. On SPA route changes move focus to headings or main content via `skip links` patterns. Avoid disabling outline—replace with visible "
            "themed focus rings. Test with keyboard-only workflows in every release train."
        ),
        "deep": px(
            """
            Route transitions without focus moves strand assistive tech users: the view changes but the reading cursor does not—move focus to an `h1` or `main` region after navigations complete meaningfully.
            """,
            """
            Portals detach nodes from their React parents in the DOM tree; `aria-modal`, inert backdrops, and z-index must align so focus cannot reach “ghost” interactive elements behind sheets.
            """,
            """
            Data grids and composite widgets need roving tabindex patterns or vetted headless libraries that implement keyboard specs—reinventing grids without reading APG recipes ships subtle violations fast.
            """,
            """
            Operations includes logging when focus-trap libraries throw in production because third-party scripts injected modals without coordination—coordinate marketing tags with accessibility owners before campaigns land.
            """,
        ),
        "bullets": [
            "**Decision:** Explicit focus contracts for overlays; document patterns; test SPA navigations.",
            "**Risk:** Silent focus loss, cyclic tab traps, inaccessible nested scroll areas.",
            "**Mitigation:** Headless primitives audited, e2e keyboard scripts, design/dev paired reviews.",
        ],
        "example": (
            "An admin SPA moved focus to the page title on each route change—support tickets citing “lost voiceover context” fell sharply within a quarter."
        ),
        "diag": "open overlay -> trap focus -> close -> restore trigger; route -> focus main heading",
        "links": ["https://www.w3.org/WAI/ARIA/apg/patterns/", "https://react.dev/reference/react-dom/createPortal"],
    },
    {
        "num": 89,
        "title": "Semantic HTML in components?",
        "qsum": "Choosing correct elements versus `div` soup; heading levels; landmarks.",
        "crisp": (
            "Prefer `<button>` for actions, anchors with real `href` for navigation (even in SPAs via router links), `<nav>`/`main>`/`aside>` landmarks sparingly but consistently, `<table>` for tabular "
            "data—not CSS grid fakery harming screen reader semantics. Preserve heading ladders (`h1`…`h6`) so outline navigation works; avoid skipping levels arbitrarily. Styled components still carry "
            "semantic tags internally. Lint for landmark uniqueness per page shells."
        ),
        "deep": px(
            """
            Native elements expose platform behaviors—`<button>` handles Space/Enter, participates in implicit form submission, and lands in tab order—without reimplementing keyboards in scattered `div` handlers.
            """,
            """
            Heading ladders build an outline for assistive tech and SEO; skipping levels purely for typography breaks predictable navigation analogous to brittle JSON hierarchies slowing incident response when humans parse logs under pressure.
            """,
            """
            Router links should still render `<a href>` so open-in-new-tab, copying URLs, prefetch, and browser history ergonomics behave honestly—`history.push` on `div` removes affordances power users depend on.
            """,
            """
            Landmarks (`main`, `nav`, `aside`) help when shells define them once; duplicate `main` regions per nested layout confuse “skip to content” shortcuts—encode rules in your layout components.
            """,
        ),
        "bullets": [
            "**Decision:** Map UI affordances to native elements before adding ARIA; landmarks once per logical page.",
            "**Risk:** Inert controls, bogus links breaking middle-click/open-in-new-tab, tables mislabeled as grids.",
            "**Mitigation:** Component guidelines, JSX lint rules, design/dev pairing on patterns.",
        ],
        "example": (
            "A reporting team replaced clickable `div`s with `<button>`; keyboard activation parity improved and CSP-friendly click handlers simplified."
        ),
        "diag": "meaningful tag -> implicit role -> minimal aria -> CSS decorates safely",
        "links": ["https://developer.mozilla.org/en-US/docs/Glossary/Semantics", "https://html.spec.whatwg.org/"],
    },
    {
        "num": 90,
        "title": "SSR vs CSR vs SSG?",
        "qsum": "Latency, SEO, freshness, infra cost, interactivity island trade-offs.",
        "crisp": (
            "CSR ships JS-heavy shells—great for highly interactive authenticated apps tolerating spinner-first loads if cached bundles fast. SSR renders markup per request boosting SEO and perceived speed yet costs "
            "compute and couples release cadence with Node edge budgets. SSG pre-renders at build suitable for stable marketing/help content with revalidation bridging freshness gaps. Mixed architectures hydrate "
            "islands sparingly balancing TTFB and TTI narratives—instrument both RUM synthetic lab Web Vitals deliberately."
        ),
        "deep": px(
            """
            CSR fits authenticated, highly interactive shells where SEO is secondary: you pay TTI and bundle-size taxes but gain simpler deploy surfaces if CDN edge rendering is not in your skill set yet.
            """,
            """
            SSR improves first meaningful paint and crawlability for public pages, but it ties availability to server pools—protect hot paths with caching, deadlines, and circuit breakers so slow databases do not brown out HTML globally.
            """,
            """
            SSG (and incremental regeneration) fits content that changes on known cadences—pair with webhooks or time-based revalidation instead of rebuilding the world for each typo in a blog post.
            """,
            """
            Mixed models are normal: land marketing on SSG/ISR, hydrate interactive islands, and keep deeply personal dashboards CSR-first—validate with field Web Vitals segmented by page template, not sitewide averages that hide losers.
            """,
        ),
        "bullets": [
            "**Decision:** Match rendering mode to content volatility + SEO + interactivity; measure field data not opinions.",
            "**Risk:** Hydration mismatch, expensive SSR hot paths, stale SSG under sudden content shifts.",
            "**Mitigation:** ISR/revalidate, edge caching, selective client islands, consistent data loaders.",
        ],
        "example": (
            "A marketplace kept catalog SSG with hourly revalidation while checkout stayed CSR behind auth—Core Web Vitals improved on landing without overloading origin SSR pools during flash sales."
        ),
        "diag": "static content SSG/ISR -> mixed shells -> interactive CSR enclaves",
        "links": ["https://web.dev/articles/rendering-on-the-web", "https://nextjs.org/docs/app/building-your-application/rendering"],
    },
    {
        "num": 91,
        "title": "ISR and edge rendering?",
        "qsum": "Freshness windows, cache invalidation, regional latency, consistency.",
        "crisp": (
            "Incremental Static Regeneration serves cached HTML while background rebuilds refresh defined paths—great for catalog-like data with tolerable staleness windows. Edge functions move auth checks, "
            "geo personalization, and security headers closer to users yet complicate debugging and cold starts. Pair tags or webhooks for invalidation when upstream CMS changes. Document eventual consistency: "
            "editors may see lagging pages briefly—set expectations and monitoring on stale-serve rates."
        ),
        "deep": px(
            """
            ISR is an explicit staleness contract: decide how old data may be before a path rebuilds or revalidates, and communicate that honestly to editorial teams who blame “CDN ghosts” otherwise.
            """,
            """
            Edge handlers reduce latency but shift debugging toward distributed traces—cold starts and regional configuration skew become first-class observability dashboards, not anecdotes during war rooms.
            """,
            """
            Invalidation can be temporal (TTL), tag-based (group related URLs), or event-driven via CMS hooks—missing automation means manual purges become runbooks typed under stress prone to typo outages.
            """,
            """
            Security teams review edge logs for secrets echoed by misconfigured redirects; partition env vars per region and tighten retention because edges multiply surface area compared with a single origin.
            """,
        ),
        "bullets": [
            "**Decision:** Use ISR/edge when traffic geography and cache hit rates justify ops complexity; define SLOs for staleness.",
            "**Risk:** Thundering herds on rebuild, poisoned caches, regional divergence, secret leakage in edge logs.",
            "**Mitigation:** Keyed revalidation, canary regions, observability on cache age headers, least-privilege edge env vars.",
        ],
        "example": (
            "A news site revalidated article paths on CMS webhooks—readers saw updates within seconds while origin databases avoided per-request rendering crushing sports traffic spikes."
        ),
        "diag": "request -> edge cache HIT (fresh) | MISS -> origin build -> populate edge",
        "links": ["https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration", "https://www.cloudflare.com/learning/cdn/what-is-edge-computing/"],
    },
    {
        "num": 92,
        "title": "Client vs server components?",
        "qsum": "RSC-era split: secrecy, bundle cost, waterfalls, serialization constraints.",
        "crisp": (
            "Frameworks such as Next App Router differentiate server components fetching close to data without bloating bundles versus client components owning state, effects, and browser APIs—keep serialization "
            "constraints in mind: props crossing the wire must be JSON-like. Decide boundaries per route: dashboards may stay client-heavy while marketing reads server-first. Explicitly hoist shared layout server "
            "components to shrink JS. Mis-boundaries inflate waterfalls or duplicate fetches across layers accidentally—trace with tooling."
        ),
        "deep": px(
            """
            Server components run where data and credentials already live, shrinking the browser bundle—but any value passed into a client component is part of the public payload, so never treat those props as places to hide secrets.
            """,
            """
            Serialization rules reject functions, class instances, and symbols naively—plan DTO layers or shared Zod schemas so the server→client contract stays explicit and versioned like an API.
            """,
            """
            Boundaries affect data waterfalls: lifting fetches into the server tree can remove client round trips, while over-nesting client wrappers can reintroduce spinner chains you were trying to delete.
            """,
            """
            Tooling (`next build` analyzer, `@next/bundle-analyzer`) validates that whole subtrees remain server-only; pairing this with code review stops accidental `"use client"` at the top of huge layout files.
            """,
        ),
        "bullets": [
            "**Decision:** Server by default for read-mostly shells; promote to client for interactivity; audit boundaries with bundle analyzer.",
            "**Risk:** Accidental mega-client subgraphs, non-serializable props, duplicated fetch + query stacks.",
            "**Mitigation:** Lint rules, ADRs per route, shared fetch clients, suspense boundaries with explicit fallbacks.",
        ],
        "example": (
            "A docs site rendered MDX server-side for zero-JS readers while interactive playgrounds imported client islands—global JS budget fell while editors kept rich components."
        ),
        "diag": "server tree (data+layout) -> client leaves (state/effects) -> streamed HTML + selective hydration",
        "links": ["https://nextjs.org/docs/app/building-your-application/rendering/client-components", "https://nextjs.org/docs/app/building-your-application/rendering/server-components"],
    },
    {
        "num": 93,
        "title": "Streaming SSR trade-offs?",
        "qsum": "TTFB vs progressive HTML, suspense coordination, error handling mid-stream.",
        "crisp": (
            "Streaming sends HTML in chunks so browsers can parse early skeletons while slow data resolves—improving LCP when paired with meaningful placeholder design. It complicates error handling: failures mid-stream "
            "need fallbacks or partial replacement strategies. Ensure compatible CDNs/proxies buffer policies align. Client hydration must match streamed order to avoid mismatch bugs. Load-test combined SSR+DB paths because "
            "parallelism shifts bottlenecks."
        ),
        "deep": px(
            """
            Streaming helps when some queries are predictably slow—users see meaningful structure early instead of a single white screen, which improves perceived performance even if total time is unchanged.
            """,
            """
            Trade-offs include partial failure modes: if a chunk throws late, you need error UI that does not trash the already-streamed shell without confusing assistive tech reading half a page.
            """,
            """
            Infrastructure must not buffer entire responses—misconfigured reverse proxies or WAFs can negate streaming benefits silently until RUM shows no stepwise paint improvements despite engineering effort.
            """,
            """
            Hydration ordering matters: mismatched suspense boundaries between server and client trees recreate classic mismatch bugs—disciplined keys and data loaders reduce that class of defect during refactors.
            """,
        ),
        "bullets": [
            "**Decision:** Stream when variance in backend latency dominates; combine with suspense per route slice.",
            "**Risk:** Hydration mismatch, chunked error visibility, intermediary buffering defeating streaming gains.",
            "**Mitigation:** Boundaries per feature, deterministic fallbacks, edge config review, CLS budgets.",
        ],
        "example": (
            "A commerce PLP streamed category shell immediately while recommendations hydrated later—field LCP improved without blocking the hero grid on personalization latency."
        ),
        "diag": "shell streams -> suspense holes resolve -> hydrate in order matching stream",
        "links": ["https://react.dev/reference/react-dom/server/renderToPipeableStream", "https://web.dev/learn/core-web-vitals/"],
    },
    {
        "num": 94,
        "title": "Next.js vs Remix vs SPA?",
        "qsum": "Framework coupling, data APIs, hosting, migration cost.",
        "crisp": (
            "Next dominates hiring mindshare and integrates Vercel-era patterns (App Router, RSC, ISR) with large ecosystem examples. Remix emphasizes nested routing loaders/actions and web standards—great when you want progressive enhancement and explicit transitions. Plain SPA+Vite excels for "
            "B2B consoles behind CDN with CSR tolerable SEO-wise and simpler deployment footprints. Choices hinge on SSR needs, backend colocation willingness, organizational expertise, licensing, observability tooling "
            "compatibility—not benchmark religion alone."
        ),
        "deep": px(
            """
            Adoption risk is mostly staffing—framework ergonomics matter less than whether your org can mentor patterns consistently through hiring waves and acquisitions without fragmenting conventions silently.
            """,
            """
            Next’s ecosystem depth helps when you want batteries-included hosting stories, ISR, image optimization knobs, and copy-paste examples at scale; Remix shines when transitions, forms, and nested data routes model your product faithfully with fewer moving parts mentally.
            """,
            """
            Pure SPAs remain valid for authenticated dense UIs where SEO is negligible and operational simplicity outweighs SSR tax—provided you still instrument Web Vitals and manage bundle growth ruthlessly anyway.
            """,
            """
            Migration should be incremental: pilot one subdomain, watch CI timings and incidents, retire duplicate routers instead of indefinitely operating two incompatible stacks side by side.
            """,
        ),
        "bullets": [
            "**Decision:** Match framework to SSR/SEO requirements, DX hiring pool, infra vendor strategy, incremental migration realism.",
            "**Risk:** Over-frameworking tiny sites, mismatched talents, duplicated patterns during hybrid migrations.",
            "**Mitigation:** ADRs with measurable criteria, training budget, scaffolding templates standardized org-wide.",
        ],
        "example": (
            "A SaaS reboot chose Remix for multipart form-heavy flows while marketing stayed on ISR Next—teams shared React primitives but routed data differently per subdomain constraints."
        ),
        "diag": "requirements matrix -> SSR depth -> team skills -> pilot route -> broaden",
        "links": ["https://nextjs.org/docs", "https://remix.run/docs/en/main", "https://vitejs.dev/"],
    },
    {
        "num": 95,
        "title": "i18n strategy?",
        "qsum": "Message catalogs, ICU formatting, routing, SSR parity, RTL.",
        "crisp": (
            "Centralize strings in namespace files or TMS exports; load translations at build or runtime with lazy chunks per locale to protect bundle size. Use ICU-aware formatters for dates, numbers, plural rules—never "
            "string-concatenate. Route strategies include locale prefixes, subdomains, or cookies with explicit SEO decisions. SSR must emit the same language the user expects (cookie + Accept-Language policy). Test RTL "
            "layouts and mirrored icons. Pair with pseudo-localization in CI to catch truncation early."
        ),
        "deep": px(
            """
            Glossaries reconcile product, legal, and engineering: stable keys prevent “fix copy in JSX” hacks that auditors cannot diff across locales when regulations change quarterly.
            """,
            """
            ICU matters because plural and gender rules are not cosmetic—finance and healthcare wording mistakes create liability; format numbers and dates with locale-aware APIs shared between server and client to avoid hydration mismatches.
            """,
            """
            Routing choices affect SEO: prefixing `/en/` makes alternates explicit; cookie-only locale detection can confuse crawlers unless you document canonical behavior and hreflang carefully.
            """,
            """
            Operations cares about translator SLAs, TMS downtime, and phased rollouts—feature flags that hide partially localized surfaces beat shipping mixed languages that confuse customers and support desks.
            """,
        ),
        "bullets": [
            "**Decision:** Namespace keys, ICU formatting, locale routing policy, lazy locale bundles, RTL regression tests.",
            "**Risk:** Divergent SSR/CSR languages, huge combined bundles, legal copy drift, layout truncation.",
            "**Mitigation:** TMS integration, CI pseudo-locale, design constraints for expansion, content freeze windows.",
        ],
        "example": (
            "A fintech froze trading copy behind a CMS with keys consumed by both Next server and mobile web—regulators received identical phrasing across surfaces after prior inconsistent manual edits."
        ),
        "diag": "locale detect -> load messages -> format with ICU -> render mirrored layout if RTL",
        "links": ["https://formatjs.io/docs/react-intl/", "https://unicode-org.github.io/icu/userguide/"],
    },
    {
        "num": 96,
        "title": "Theme system design?",
        "qsum": "Tokens, density, dark mode, SSR/hydration parity, performance.",
        "crisp": (
            "Model design tokens as semantic roles (color.background.default) resolved to values per theme; ship via CSS variables injected at root for runtime switching without rebundling entire style sheets. Separate brand "
            "from density modes (compact vs comfortable). Ensure SSR outputs the correct theme class or variables matching cookies to avoid flashy mismatches during hydration. Test contrast automatically in CI. Prefer "
            "co-located token JSON consumed by tooling (Figma, Storybook)."
        ),
        "deep": px(
            """
            Semantic tokens decouple product vocabulary from raw hex values so rebrands update variable maps instead of sweeping PRs across unrelated features owned by different teams.
            """,
            """
            CSS variables at the document root let themes switch without rebuilding large CSS-in-JS caches on every toggle—pair with a small FOUC-avoidance snippet when you must read cookies or `prefers-color-scheme` before paint.
            """,
            """
            Density modes interact with data grids and forms: tokens should encode spacing scales so compact enterprise UIs do not break touch targets on tablets when users roam between offices and factories.
            """,
            """
            Governance ships token schema in versioned packages; designers and engineers review diffs together because token breaks are API breaks for every consuming screen and charting library embedded downstream.
            """,
        ),
        "bullets": [
            "**Decision:** Semantic tokens mapped to vars; SSR-safe initial theme; contrast automation; documented density ladders.",
            "**Risk:** Flash of wrong theme, inconsistent token usage drifting hex values, sluggish theme toggles rebuilding CSS-in-JS caches.",
            "**Mitigation:** Blocking inline script snippets for theme hints when acceptable, lint disallowed raw colors, visual regression thresholds.",
        ],
        "example": (
            "A healthcare portal resolved tokens to CSS vars at build and hydrated `prefers-color-scheme` with a deterministic cookie override—clinical staff stopped reporting painful white flashes overnight shifts."
        ),
        "diag": "tokens.json -> ThemeProvider sets CSS vars -> components consume semantic vars only",
        "links": ["https://design-tokens.github.io/community-group/format/", "https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties"],
    },
    {
        "num": 97,
        "title": "Error boundaries design?",
        "qsum": "Granularity, resets, logging, integration with routers and observability.",
        "crisp": (
            "Place boundaries around route segments, data-heavy widgets, and third-party shells so failures localize—avoid one global boundary hiding all context. Pair with `componentDidCatch`/reporting hooks sending "
            "fingerprints, component stack, route, build version, and correlation ids. Offer reset actions that remount subtrees or navigate home. Remember boundaries do not catch event handler errors or async "
            "errors unless wrapped—use disciplined error policies in data layers too. Test boundary UI for accessibility."
        ),
        "deep": px(
            """
            Fat boundaries turn every failure into the same generic outage page—route-level and feature-level cages keep revenue-critical panels alive when an optional widget crashes, improving both UX and mean time to diagnose.
            """,
            """
            Async and event-handler errors bypass boundaries by design; pairing React error reporting with global `unhandledrejection` listeners and data-layer try/catch avoids false confidence that boundaries alone secure reliability.
            """,
            """
            Telemetry should dedupe identical build/version fingerprints so a misconfiguration does not emit a million events blowing observability budgets masking genuinely novel incidents requiring human attention immediately.
            """,
            """
            Recovery UX needs keyboard-accessible exit paths—offer clear navigation back to safe routes and avoid modal traps that strand assistive tech users inside broken subtrees without focus management discipline.
            """,
        ),
        "bullets": [
            "**Decision:** Boundaries per route + risky leaf widgets; reporting with rich context; humane recovery UX.",
            "**Risk:** Silent async failures, flooding logs without dedupe, trapping users without exit affordances.",
            "**Mitigation:** Error policies in data libs, deduped client reporting, retries with limits, E2E drills.",
        ],
        "example": (
            "A maps widget wrapped in its own boundary prevented a third-party SDK crash from blanking entire dashboards—users saw an isolated retry card while core KPIs kept rendering."
        ),
        "diag": "error -> boundary catches -> report + localized fallback -> optional reset navigation",
        "links": ["https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary", "https://github.com/getsentry/sentry-javascript"],
    },
    {
        "num": 98,
        "title": "React observability strategy?",
        "qsum": "RUM, Core Web Vitals, tracing, logging hygiene, tying client signals to backends.",
        "crisp": (
            "Collect field Web Vitals (LCP, INP, CLS) sliced by route template, device class, locale, and release version—averages disguise bad mobile outliers. Inject trace IDs from APIs into fetch clients so RUM slowdowns align "
            "with spans in backend dashboards. Restrict client logs to schemas without PII. Tag crashes with bundle version and active feature flags. Review incidents jointly between frontend and platform teams rather than blaming "
            "React whenever latency spikes ambiguously across layers."
        ),
        "deep": px(
            """
            Monetizing routes deserve tighter budgets than internal admin pages—tiered SLIs force honest trade-offs between feature backlog and responsiveness where money actually converts.
            """,
            """
            Trace context propagation differentiates sluggish APIs from sluggish React reconciliation—joined dashboards shorten incidents compared with guessing in chat threads under pressure.
            """,
            """
            Structured client events need schemas and redaction—free-form logging of objects leaks PII into observability vendors and makes retention policies unenforceable during audits.
            """,
            """
            Correlate rollouts with flags and bundle IDs so you can answer whether a regression is a deployment, an experiment, or organic traffic mix shifts without burning a weekend bisecting blindly.
            """,
        ),
        "bullets": [
            "**Decision:** RUM + traces + structured client errors; segmented budgets; correlate flags/releases.",
            "**Risk:** PII leakage, noisy logs, masking backend faults, alert fatigue from duplicated signals.",
            "**Mitigation:** Schema validation on events, sampling, linked dashboards, privacy review checkpoints.",
        ],
        "example": (
            "A retailer correlated INP regressions with a specific remote bundle and flag combo—rollback took minutes once traces tied slow interactions to hydration stalls, not databases wrongly suspected initially."
        ),
        "diag": "instrumented fetch -> propagate traceparent -> spans -> FE RUM overlays + backend APM joins",
        "links": ["https://web.dev/vitals/", "https://opentelemetry.io/docs/concepts/signals/traces/"],
    },
    {
        "num": 99,
        "title": "Enterprise-scale React preparation?",
        "qsum": "RFC culture, scaffolding, staffed platform teams, continuous modernization.",
        "crisp": (
            "Treat the React stack as internal infrastructure: staffed platform crews, RFCs for majors (React bumps, routers, SSR hosts), shared scaffolds with lint/tests/budgets enforced in CI, and ADRs anchored to KPIs—not "
            "heroics that vanish after one principal engineer exits. Rotate dependency upgrades on a schedule with codemods and release notes. Quarterly portfolio reviews on bundle drift, axe regressions, CVEs, flaky tests, "
            "and onboarding time so executives can see engineering health numerically—not just story throughput."
        ),
        "deep": px(
            """
            Boring consistency beats heroics: repeatable scaffolds, shared CI recipes, and onboarding paths let new hires ship safely in week one instead of reverse-engineering seventeen variants of the same repo layout.
            """,
            """
            Codemods amortize React and framework upgrades across squads—without them, majors pile up until CVEs or broken toolchains force risky big-bang migrations during the worst possible business quarter.
            """,
            """
            ADRs anchored to KPIs survive leadership churn better than slides arguing library popularity without conversion, incident, or onboarding numbers on the same page.
            """,
            """
            Executive reviews belong on security advisory backlogs and flake rates—not only feature velocity—so maintenance competes for capacity before outages force it during the worst quarter.
            """,
        ),
        "bullets": [
            "**Decision:** Platform ownership + RFC/ADR rituals + templated repos + quantitative health reviews.",
            "**Risk:** Drift across teams, stalled majors increasing CVE exposure, burnout bus factors.",
            "**Mitigation:** Office hours, upgrade trains, shared codemods, executive-sponsored quality capacity.",
        ],
        "example": (
            "A conglomerate chartered a UI platform guild to ship Next majors quarterly with codemods; pods stopped maintaining seventeen bespoke compiler stacks and reused one upgrade train."
        ),
        "diag": "RFC -> scaffold update -> codemods -> CI gates green -> fleets adopt",
        "links": ["https://martinfowler.com/articles/scaling-architecture-conversationally.html", "https://nx.dev/getting-started/tutorials/react-monorepo-tutorial"],
    },
    {
        "num": 100,
        "title": "How to explain React architecture trade-offs?",
        "qsum": "Executive narratives linking UX, resilience, staffing, velocity, capital spend.",
        "crisp": (
            "Tell architecture as bounded bets with KPIs: CSR stays operationally simple while SSR trades origin capacity for SEO and LCP; shared design systems speed delivery at the cost of governance; strict CSP tightens "
            "XSS blast radius while slowing some marketing experiments needing tag exceptions. Tie each bullet to dashboards leadership already trusts—conversion, SLA minutes, infra spend—instead of debating taste."
        ),
        "deep": px(
            """
            Executives approve budgets when narratives connect engineering choices to shopper latency, outage minutes, hiring friction, or compliance exposure—framework brands are footnotes unless recruiting markets demand them explicitly.
            """,
            """
            Present risk envelopes for each architectural bet—best case, expected case, and rollback—so leaders see guarded optionality rather than ideological all-or-nothing arguments.
            """,
            """
            Anchor stories to KPIs executives already defend in quarterly reviews—otherwise engineering narratives feel like discretionary spend disconnected from conversions, SLA minutes, or payroll efficiency.
            """,
            """
            Close with disciplined pilots: bounded surfaces, pre-agreed metrics, and explicit dates to expand or revert so decisions end with evidence rather than infinite opinion churn.
            """,
        ),
        "bullets": [
            "**Decision:** Tie stack choices to metrics + bounded risks stakeholders already track.",
            "**Risk:** Techno-religious debates devoid of KPI anchoring confuse executives blocking budgets.",
            "**Mitigation:** ADRs summarized in one-slide trade matrices; periodic outcome reviews tying releases to deltas.",
        ],
        "example": (
            "A CTO funded incremental SSR rollout after dashboards tied LCP changes to signup lift forecasts with scenario bands—numeric narrative beat a technology popularity pitch without customer evidence."
        ),
        "diag": "customer metric <- engineering lever -> measured delta -> iterative funding loop",
        "links": ["https://react.dev/", "https://web.dev/learn/performance/why-performance-matters/"],
    },
]
