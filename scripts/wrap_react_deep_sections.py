"""Wrap single-line **Deep explanation** blocks to ~88 columns (physical line count ~70+)."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "web-stack" / "react_100_interview_qna.md"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    # Single-line form: header and entire body share one physical line; followed by blank line then Answer summary.
    pattern = re.compile(
        r"(?m)^(?P<hdr>\*\*Deep explanation \(~70 lines\):\*\*)\s*(?P<body>\S.*)\n\n(?=\*\*Answer summary:\*\*)",
    )

    def repl(m: re.Match[str]) -> str:
        hdr = m.group("hdr")
        body = m.group("body").strip()
        wrapped = textwrap.fill(
            body,
            width=88,
            break_long_words=False,
            break_on_hyphens=False,
        )
        return f"{hdr}\n{wrapped}\n\n"

    new_text, count = pattern.subn(repl, text)
    TARGET.write_text(new_text, encoding="utf-8")
    print(f"Wrapped {count} single-line deep explanations into multiple lines.")


if __name__ == "__main__":
    main()
