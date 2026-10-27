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
