# Stock Due Diligence

Version-controlled source for the Stock Due Diligence ChatGPT plugin package.

- Plugin package branch: `mcp-sec-edgar-v1.0.2` (release candidate; not yet confirmed published)
- Current listing: https://chatgpt.com/plugins/plugins_6ada26384798819191722437eddeb00b
- Plugin: https://chatgpt.com/plugins/plugins_6ada26384798819191722437eddeb00b
- Repository history: https://github.com/ezhilrean/stock-due-diligence

## Repository layout

- `plugin.json` — plugin manifest (version 1.0.2)
- `mcp.json` — remote Streamable HTTP MCP server configuration
- `.codex-plugin/plugin.json` — Codex plugin manifest
- `skills/stock-due-diligence/SKILL.md` — main workflow and safety/evidence rules
- `skills/stock-due-diligence/references/` — checklist, playbook, report template, research standards, and definition of done
- `CHANGELOG.md` — release-by-release change history
- `releases/` — version history notes

The v1.0.2 candidate adds a remote, read-only SEC EDGAR MCP server. Before submitting it, verify the hosted endpoint, OpenAI domain-challenge verification, MCP tool discovery, and positive/negative test cases. Do not claim the release is published until the developer portal confirms it.
