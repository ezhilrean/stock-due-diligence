# Stock Due Diligence

Version-controlled source for the Stock Due Diligence ChatGPT plugin package.

- Plugin package version: `1.0.3` (release candidate; publication status must be confirmed in the Developer Portal)
- Current plugin listing: https://chatgpt.com/plugins/plugins_6adbfa1c18e88191bbc6fa153a003af0
- Repository: https://github.com/ezhilrean/stock-due-diligence
- Active development branch: `feature/sec-edgar-improvements`

## Repository layout

- `plugin.json` — plugin metadata, version, listing prompts and release notes
- `mcp.json` — remote Streamable HTTP MCP server configuration
- `.codex-plugin/plugin.json` — Codex plugin manifest
- `skills/stock-due-diligence/SKILL.md` — main workflow and safety/evidence rules
- `skills/stock-due-diligence/references/` — checklist, playbook, report template, research standards, and definition of done
- `documentation/SEC-EDGAR-TEST-CASES.md` — positive, negative and acceptance test plans
- `CHANGELOG.md` — release-by-release change history
- `releases/` — version history notes

## v1.0.3 release-candidate focus

- Read-only SEC EDGAR company identification and company-facts research.
- Exact ticker/name matching preference and clarification for ambiguous companies.
- Reported financial concept, units, fiscal periods and filing metadata retained where available.
- Primary-source verification and explicit missing-data/industry-taxonomy caveats.
- Checklist questions are not presented as completed diligence findings.
- No brokerage access, order placement, live-market-price feed or guaranteed-return functionality.

Before submitting, verify the hosted endpoint, domain-challenge verification, MCP tool discovery, all three explicit Boolean safety annotations on each tool, positive/negative scenarios, and published support/privacy/terms pages. This README records release intent, not proof that live tests passed or that the release is published.


## Build the Developer Portal upload ZIP

Run `python scripts/build_plugin_zip.py` from a checkout of `feature/sec-edgar-improvements`. The script verifies manifest versions, HTTPS URLs, the configured review recording URL, the MCP review-case schema (exactly five positive and three negative cases), and all required skill references. It writes a root-level ZIP to `dist/stock-due-diligence-feature-sec-edgar-improvements-v1.0.3.zip` for the current 1.0.3 manifest.

The package includes the full `skills/stock-due-diligence/` tree—including `checklist.md`, `definition-of-done.md`, `deliverable-template.md`, `playbook.md`, and `research-standards.md`—plus both manifests, MCP configuration, icons, README/changelog, and SEC usage/test documentation. The GitHub Actions workflow also uploads the validated ZIP as a build artifact on changes to this branch.

This ZIP is a plugin upload package, not a full repository archive. Website source and the live MCP implementation remain in `ezhilrean/stock-due-diligence-web` on `feature/mcp-server`; nothing is deleted from either GitHub repository when these runtime files are not duplicated inside the upload ZIP. Confirm that the configured demo recording is accessible and demonstrates this release before portal submission.
