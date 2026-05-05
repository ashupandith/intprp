"""
Emit markdown for Q61–Q100 into docs/web-stack/react_100_interview_qna.md
by replacing the placeholder section starting at '### Q61–Q100'.
Deep sections: multiple paragraphs wrapped to ~88 columns (~70 visual lines target).
"""

from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from react_entries_q63_100 import ENTRIES_Q63_100
from react_entries_q71_q100 import ENTRIES_Q71_Q100

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "web-stack" / "react_100_interview_qna.md"
WIDTH = 88

Entry = dict[str, object]


def wrap_paragraph(text: str) -> str:
    t = " ".join(text.split())
    return "\n".join(textwrap.wrap(t, width=WIDTH)) if t else ""


def wrap_crisp(text: str) -> str:
    return wrap_paragraph(text)


def deep_from_paragraphs(paragraphs: list[str]) -> str:
    return "\n\n".join(wrap_paragraph(p) for p in paragraphs if p.strip())


def block(e: Entry) -> str:
    num = e["num"]
    title = e["title"]
    qsum = e["qsum"]
    crisp = wrap_crisp(e["crisp"])  # type: ignore[arg-type]
    deep = deep_from_paragraphs(e["deep"])  # type: ignore[arg-type]
    bullets = e["bullets"]  # type: ignore[assignment]
    example = e["example"]
    diag = e["diag"]
    links = e["links"]  # type: ignore[assignment]
    blines = "\n".join(f"- {b}" for b in bullets)
    llines = "\n".join(f"- {u}" for u in links)
    return f"""### Q{num}. {title}
**Question summary:** {qsum}

**Crisp answer (7-8 lines):** {crisp}

**Deep explanation (~70 lines):**
{deep}

**Answer summary:**
{blines}

**Practical example:** {example}

**Simple diagram:**
```text
{diag}
```

**Trusted reference links:**
{llines}

"""


def p(*parts: str) -> list[str]:
    return [s.strip() for s in parts if s.strip()]


_ENTRIES_Q61_Q62: list[Entry] = [
    {
        "num": 61,
        "title": "Scalable React project structure?",
        "qsum": "Interviewer probes boundaries, ownership, build graph health, and how structure supports many teams without entanglement.",
        "crisp": (
            "Scale React codebases with clear domain boundaries (feature folders or packages), a thin app shell, and explicit public APIs "
            "between areas. Keep shared UI tokens and primitives in a design system while isolating business rules next to features. Watch "
            "for barrel-file cycles, tests that import half the app, and packages that become junk drawers. Use CODEOWNERS, lint rules for "
            "import boundaries, and incremental TypeScript project references or monorepo tooling so CI stays fast. Refactor toward structure "
            "incrementally: extract vertical slices before attempting big-bang purity."
        ),
        "deep": p(
            """
            Scalable structure is less about a trendy folder diagram and more about constraining how change propagates. When ten teams touch
            the same directory, every release becomes a coordination exercise and merge conflicts hide real defects. A practical pattern is
            to treat each product area as a vertical slice that owns its routes, components, hooks, API adapters, and tests, exposing only a
            small surface (typed entry points, storybook examples, or package exports) to neighbors.
            """,
            """
            Horizontal layers (components, hooks, utils) still exist, but they should be thin and policy-driven: primitives and cross-cutting
            concerns belong in foundations, not scattered copies. The failure mode is a “flat components/ dump” where import graphs become a
            hairball—builds slow, treeshaking regresses, and refactors fearfully avoid large files nobody understands. Tooling helps: ESLint
            import rules, dependency-cruiser or similar graph checks, and TypeScript path maps that encode allowed directions of dependency flow.
            """,
            """
            Monorepos versus multirepo is a trade-off between consistency and autonomy. Inside a monorepo, workspace packages can version shared
            contracts (OpenAPI clients, auth helpers) while letting teams ship independently if boundaries are enforced. In multirepo setups,
            you pay for duplicated configuration and drift unless you invest in generators and semver discipline for shared libraries.
            Measurement matters: track time-to-merge, flaky test rates, median CI duration, and module graph size over quarters to know if a
            structure is helping.
            """,
            """
            Design systems interact heavily with structure. If every feature imports deep paths from the library’s guts, you cannot evolve
            tokens or APIs safely. Publish explicit exports, codify contribution guidelines, and pair visual changes with migration notes.
            Performance signals include bundle deltas per route and cold-start compile times in dev—these often regress long before runtime
            profiling shows pain.
            """,
            """
            Operations and reliability also lean on layout: observability dashboards, feature flags, and kill switches are easier when each
            slice owns its telemetry namespace and documents blast radius. Security reviews map cleanly when sensitive modules live behind
            narrow interfaces instead of being importable from arbitrary UI leaves.
            """,
            """
            Migration from a legacy ball-of-mud starts with stopping the bleeding: freeze new cross-imports, carve one pilot feature
            directory, and prove CI/lint rules that block regressions. Narrate that story in interviews—you are showing judgment about gradual
            constraint rather than rewriting for aesthetics.
            """,
            """
            Governance is the human half: RFCs for cross-cutting shifts, onboarding docs that explain the dependency compass, and periodic
            architecture hours to retire ghost modules. Combined with disciplined automation, structure becomes a throughput multiplier instead
            of bureaucracy.
            """,
        ),
        "bullets": [
            "**Decision:** Vertical slices plus thin foundations; explicit exports; enforced import boundaries backed by lint and CI.",
            "**Risk:** Hidden cycles, barrel re-export traps, ambiguous ownership, exploding bundle graphs, slow flaky pipelines.",
            "**Mitigation:** Graph checks, package-level APIs, incremental extraction, observable CI budgets, documented ownership matrices.",
        ],
        "example": (
            "A B2B suite split onboarding, billing, and admin into packages with forbidden reverse imports; CI caught a sneaky cycle from "
            "billing into onboarding within hours, preventing a week-long revert."
        ),
        "diag": "feature package -> public index.ts -> app shell routes only through public API",
        "links": [
            "https://react.dev/learn/scaling-up-with-reducer-and-context",
            "https://nx.dev/concepts/more-concepts/applications-and-libraries",
        ],
    },
    {
        "num": 62,
        "title": "Presentational vs container split?",
        "qsum": "Tests whether you still map the old pattern to modern hooks, colocation, and when separation helps versus adds ceremony.",
        "crisp": (
            "Presentational components focus on rendering and styling given props; containers orchestrate data fetching, mutations, and "
            "routing side effects. In modern React you often colocate hooks near leaves instead of rigid HOC splits, but the idea—separating "
            "pure UI from imperative orchestration—remains valuable for reuse and testing. Use explicit containers where async complexity, "
            "auth, or analytics would pollute reusable visuals. Avoid duplicating tiny wrapper files that only forward props without adding "
            "clarity. Storybook and visual regression tests love presentational layers; integration tests target container boundaries."
        ),
        "deep": p(
            """
            The original container/presentational split helped teams reason about where side effects lived in a class-component world. Hooks
            blurred the physical boundary because you can call data hooks directly in leaf components, which tempts people to declare the
            pattern dead. The underlying concern persists: mixing networking, error policies, and pixel-perfect layout in one component
            makes reuse and snapshot testing expensive and couples design iterations to API churn.
            """,
            """
            A pragmatic rule is to keep components that appear in many contexts (cards, tables, inputs) free of feature-specific network code.
            When a screen needs bespoke orchestration (parallel queries, optimistic flows, session refresh), introduce a local coordinator—
            sometimes a route module, sometimes a small hook-backed component—that passes plain data and callbacks downward. That preserves
            clarity without inventing global “container” folders that become grab bags.
            """,
            """
            Testing strategy reinforces the split: presentational pieces assert accessibility, visual states, and edge props cheaply; containers
            assert loading, error, and success transitions often with MSW or similar. If every test must boot the entire graph, teams stop
            writing them.
            """,
            """
            Performance considerations include memoization boundaries: pure presentational subtrees can be isolated behind `React.memo` when
            props are stable, while containers may legitimately rerender often due to query updates. Over-splitting creates prop drilling
            again—balance with composition or context for cross-cutting theme tokens, not business data unless scope is tiny.
            """,
            """
            Design systems usually export presentational units; application features compose them with domain-specific copy and validation
            messages. Interviewers listen for this collaboration story: how you prevented a library from importing app-only hooks, keeping
            release cadence independent.
            """,
            """
            Anti-patterns include “container” files that are just indirection with no behavior, and “presentational” components that still fire
            analytics side effects on render. Name and structure should track real responsibilities, not historical dogma.
            """,
            """
            In micro-frontends, the split helps define ownership: shared design packages stay presentation-first while each remote owns its
            data wiring, reducing version-lock surprises when primitives bump.
            """,
        ),
        "bullets": [
            "**Decision:** Separate pure UI from orchestration wherever reuse, testing, or design velocity demands it.",
            "**Risk:** Pointless wrappers, prop drilling resurgence, hidden side effects labeled presentational.",
            "**Mitigation:** Colocate coordinators, typed props, Storybook contracts, lint rules forbidding fetch in primitives.",
        ],
        "example": (
            "A pricing table stayed presentation-only while a sibling hook handled tax API retries; UX iterated weekly without rewriting network "
            "policies."
        ),
        "diag": "container hook -> plain props -> presentational subtree (memo optional)",
        "links": [
            "https://react.dev/learn/passing-data-deeply-with-context",
            "https://kentcdodds.com/blog/application-state-management-with-react",
        ],
    },
]

ENTRIES: list[Entry] = _ENTRIES_Q61_Q62 + ENTRIES_Q63_100 + ENTRIES_Q71_Q100

MARKER = "### Q61–Q100. Remaining topics (complete entries)"


def main() -> None:
    text = DOC.read_text(encoding="utf-8")
    if MARKER not in text:
        raise SystemExit("Marker not found; already merged or file changed.")
    if len(ENTRIES) != 40:
        raise SystemExit(f"ENTRIES expected 40 items, got {len(ENTRIES)}")
    replacement = "".join(block(e) for e in ENTRIES)
    new_text, n = re.subn(
        re.escape(MARKER) + r"[\s\S]*\Z",
        replacement.rstrip() + "\n",
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit("Replace failed")
    DOC.write_text(new_text, encoding="utf-8")
    print(f"Wrote {len(ENTRIES)} questions into {DOC}")


if __name__ == "__main__":
    main()
