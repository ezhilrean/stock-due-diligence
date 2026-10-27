#!/usr/bin/env python3
"""Build a complete OpenAI Developer Portal ZIP for Stock Due Diligence.

This creates a distributable plugin package, not a source-code repository archive.
The website and hosted MCP implementation remain in stock-due-diligence-web; the
plugin package references that HTTPS MCP endpoint instead of bundling a duplicate server.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT_FILES = (
    "plugin.json",
    "mcp.json",
    ".codex-plugin/plugin.json",
    "assets/icon.png",
    "assets/icon.svg",
    "README.md",
    "CHANGELOG.md",
    "documentation/SEC-EDGAR-TEST-CASES.md",
    "documentation/STOCK-DUE-DILIGENCE-PROMPTS-AND-USAGE.md",
)
REQUIRED_SKILL_FILES = (
    "skills/stock-due-diligence/SKILL.md",
    "skills/stock-due-diligence/references/checklist.md",
    "skills/stock-due-diligence/references/definition-of-done.md",
    "skills/stock-due-diligence/references/deliverable-template.md",
    "skills/stock-due-diligence/references/playbook.md",
    "skills/stock-due-diligence/references/research-standards.md",
)
EXPECTED_TOOLS = {
    "search_sec_company",
    "get_sec_company_facts",
    "due_diligence_checklist",
}


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("Cannot read valid JSON from {0}: {1}".format(path, exc)) from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def collect_package_files(root: Path) -> list[Path]:
    files = [root / name for name in PLUGIN_ROOT_FILES]
    skill_dir = root / "skills/stock-due-diligence"
    require(skill_dir.is_dir(), "Missing complete skills/stock-due-diligence directory.")
    # Include every skill support/reference file, not just an abbreviated allowlist.
    files.extend(path for path in skill_dir.rglob("*") if path.is_file())
    missing = [str(path.relative_to(root)) for path in files if not path.is_file()]
    require(not missing, "Required package files are missing: " + ", ".join(missing))
    unique = {path.relative_to(root).as_posix(): path for path in files}
    return [unique[name] for name in sorted(unique)]


def validate_source(root: Path) -> tuple[str, list[Path]]:
    plugin = read_json(root / "plugin.json")
    compatibility = read_json(root / ".codex-plugin/plugin.json")
    mcp = read_json(root / "mcp.json")

    version = plugin.get("version")
    require(isinstance(version, str) and bool(version), "plugin.json must set a version.")
    require(compatibility.get("version") == version,
            "plugin.json and .codex-plugin/plugin.json versions must match.")

    openai = plugin.get("extensions", {}).get("com.openai", {})
    interface = openai.get("interface", {})
    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        value = interface.get(field, "")
        require(isinstance(value, str) and value.startswith("https://"),
                "extensions.com.openai.interface.{0} must be an HTTPS URL.".format(field))
    for field in ("logo", "composerIcon"):
        value = interface.get(field)
        require(isinstance(value, str) and (root / value.removeprefix("./")).is_file(),
                "The plugin icon reference {0!r} does not resolve to a file.".format(value))

    demo_url = openai.get("review", {}).get("demo_recording_url")
    require(isinstance(demo_url, str) and demo_url.startswith("https://"),
            "Add a reviewer-accessible HTTPS demo_recording_url under extensions.com.openai.review.")

    servers = mcp.get("mcpServers", {})
    require(isinstance(servers, dict) and len(servers) == 1,
            "Expected exactly one remote MCP server in mcp.json.")
    _, server = next(iter(servers.items()))
    require(server.get("type") == "streamable-http",
            "MCP server must use streamable-http transport.")
    require(str(server.get("url", "")).startswith("https://"),
            "MCP server URL must be HTTPS.")

    test_cases = server.get("review", {}).get("test_cases", {})
    positive = test_cases.get("positive", [])
    negative = test_cases.get("negative", [])
    require(len(positive) == 5, "MCP review needs exactly five positive test cases.")
    require(len(negative) == 3, "MCP review needs exactly three negative test cases.")
    for index, case in enumerate(positive, start=1):
        for field in ("description", "prompt", "tools_triggered", "expected_behavior"):
            require(isinstance(case.get(field), str) and case[field].strip(),
                    "Positive test case {0} requires non-empty string field {1}.".format(index, field))
        triggered = {name.strip() for name in case["tools_triggered"].split(",")}
        require(triggered <= EXPECTED_TOOLS and bool(triggered),
                "Positive test case {0} names an unknown MCP tool.".format(index))
    for index, case in enumerate(negative, start=1):
        for field in ("description", "prompt", "expected_behavior"):
            require(isinstance(case.get(field), str) and case[field].strip(),
                    "Negative test case {0} requires non-empty string field {1}.".format(index, field))

    skill = root / "skills/stock-due-diligence/SKILL.md"
    require(skill.is_file(), "Missing main skill file.")
    skill_text = skill.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---", skill_text, re.S)
    require(frontmatter is not None, "SKILL.md must begin with YAML frontmatter.")
    require(re.search(r"(?m)^name:\s*stock-due-diligence\s*$", frontmatter.group(1)) is not None,
            "SKILL.md name must match stock-due-diligence.")
    require(re.search(r"(?m)^description:\s*\S", frontmatter.group(1)) is not None,
            "SKILL.md frontmatter must include a description.")

    for item in REQUIRED_SKILL_FILES:
        require((root / item).is_file(), "Missing core skill feature/reference: " + item)

    files = collect_package_files(root)
    return version, files


def build(output: Path) -> None:
    version, files = validate_source(ROOT)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            archive.write(path, arcname=path.relative_to(ROOT).as_posix())

    with zipfile.ZipFile(output, "r") as archive:
        bad_member = archive.testzip()
        require(bad_member is None, "ZIP integrity failure in member: " + str(bad_member))
        names = set(archive.namelist())
        missing = [path.relative_to(ROOT).as_posix() for path in files
                   if path.relative_to(ROOT).as_posix() not in names]
        require(not missing, "ZIP is missing files: " + ", ".join(missing))
        require("plugin.json" in names and "mcp.json" in names,
                "ZIP root must contain plugin.json and mcp.json.")
        require("skills/stock-due-diligence/references/playbook.md" in names,
                "ZIP omitted the playbook reference.")
        require("skills/stock-due-diligence/references/research-standards.md" in names,
                "ZIP omitted research standards.")

    print("Created and integrity-checked: {0}".format(output))
    print("Version: {0} | files: {1} | compressed bytes: {2}".format(
        version, len(files), output.stat().st_size))
    print("Included the complete skill directory and all of its reference files.")
    print("Website and hosted MCP source code remain in the separate website/MCP repository.")
    print("Before submission, confirm the configured demo recording is accessible and demonstrates the current release.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional output ZIP path.")
    args = parser.parse_args()
    try:
        plugin = read_json(ROOT / "plugin.json")
        version = plugin.get("version", "unknown")
        output = args.output or (ROOT / "dist" /
            "stock-due-diligence-feature-sec-edgar-improvements-v{0}.zip".format(version))
        build(output.resolve())
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        print("ERROR: {0}".format(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
