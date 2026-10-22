#!/usr/bin/env python3
"""Rebuild the roadmap data in index.html from README.md, the single source of the content.

Usage:
    python3 scripts/sync_site.py          # rewrite the generated block in index.html
    python3 scripts/sync_site.py --check  # exit 1 if index.html is out of date (used by CI)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SITE = ROOT / "index.html"
BEGIN = "    // BEGIN GENERATED FROM README.md (python3 scripts/sync_site.py); do not edit by hand\n"
END = "    // END GENERATED FROM README.md\n"

# Per-phase colours live only on the site
PHASE_STYLE = {
    1: {"color": "#00FF9C", "bg": "#0a1a0f"},
    2: {"color": "#FF6B35", "bg": "#1a0f0a"},
    3: {"color": "#A78BFA", "bg": "#0f0a1a"},
    4: {"color": "#FBBF24", "bg": "#1a150a"},
}


def plain(text):
    """Strip the inline Markdown used in the README (bold, italics, code)."""
    return re.sub(r"\*\*|\*|`", "", text).strip()


def sentence(text):
    text = text.strip()
    return text if text.endswith((".", "!", "?")) else text + "."


def parse_readme(md):
    phases = []
    for pm in re.finditer(r"^## Phase (\d+) — (.+)\n\*Months ([\d–]+) · (.+)\*$", md, re.M):
        pid = int(pm.group(1))
        end = md.find("\n## ", pm.end())
        body = md[pm.end(): end if end != -1 else len(md)]
        phase = {
            "id": pid,
            "title": pm.group(2).strip().upper(),
            "subtitle": f"Months {pm.group(3)}",
            **PHASE_STYLE[pid],
            "description": " ".join(sentence(p) for p in pm.group(4).split(" · ")),
            "months": [],
        }
        for block in body.split("<details>")[1:]:
            head = re.search(r"<strong>(Month \d+) — (.+?)</strong>.*?(~[\d–]+ hrs/week)", block)
            why = re.search(r"^\*\*Why this month:\*\* (.+)$", block, re.M)
            milestone = re.search(r"^> \*\*✦ Milestone:\*\* (.+)$", block, re.M)
            if not (head and why and milestone):
                name = head.group(1) if head else "a month"
                missing = [k for k, v in (("title", head), ("why", why), ("milestone", milestone)) if not v]
                raise ValueError(f"Phase {pid}, {name}: missing {', '.join(missing)} in README.md")
            tasks, current = [], None
            for line in block.split("</details>")[0].splitlines():
                cat = re.fullmatch(r"\*\*([^*]+)\*\*", line.strip())
                if cat:
                    current = {"cat": cat.group(1).upper(), "items": []}
                    tasks.append(current)
                elif line.startswith("- ") and current is not None:
                    current["items"].append(plain(line[2:]))
            phase["months"].append({
                "month": head.group(1),
                "focus": plain(head.group(2)),
                "hours": head.group(3),
                "why": plain(why.group(1)),
                "tasks": [t for t in tasks if t["items"]],
                "milestone": plain(milestone.group(1)),
            })
        phases.append(phase)

    tools_section = md.split("## Tools Reference", 1)[1].split("\n## ", 1)[0]
    tools = [{"name": plain(m.group(1)), "when": m.group(2), "why": plain(m.group(3))}
             for m in re.finditer(r"^\| (.+?) \| (Month \d+) \| (.+?) \|$", tools_section, re.M)]
    if len(phases) != 4 or not tools:
        raise ValueError(f"Expected 4 phases and a tools table, found {len(phases)} phases, {len(tools)} tools")
    return phases, tools


def render(phases, tools):
    dump = lambda v: json.dumps(v, ensure_ascii=False, indent=2)
    indent = lambda s: "\n".join("    " + line for line in s.splitlines())
    return (BEGIN + indent(f"const phases = {dump(phases)};") + "\n\n"
            + indent(f"const toolsAlways = {dump(tools)};") + "\n" + END)


def main():
    phases, tools = parse_readme(README.read_text(encoding="utf-8"))
    site = SITE.read_text(encoding="utf-8")
    if BEGIN not in site or END not in site:
        sys.exit("index.html is missing the generated-data markers")
    start, stop = site.index(BEGIN), site.index(END) + len(END)
    updated = site[:start] + render(phases, tools) + site[stop:]
    if "--check" in sys.argv:
        if updated != site:
            sys.exit("index.html is out of date with README.md; run: python3 scripts/sync_site.py")
        print("index.html matches README.md")
        return
    SITE.write_text(updated, encoding="utf-8")
    months = sum(len(p["months"]) for p in phases)
    print(f"index.html updated: {len(phases)} phases, {months} months, {len(tools)} tools")


if __name__ == "__main__":
    main()
