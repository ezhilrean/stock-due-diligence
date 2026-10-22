# Stock Due Diligence Plugin — Complete Chat Summary

Date: 2026-10-22

This document records the user's goals and requests across the conversation, including the original investment-research requirements that were missing from the first summary.

## 1. Original stock-investment question

The user asked: **“If I want to buy any new stocks, then what evaluation do I need to do?”**

They proposed a stock-analysis workflow that should examine:
- Company details and business quality.
- Court cases and legal exposure.
- Debt (the original message said “debut”), financial health, and liabilities.
- Fraud, violations, threats, and misconduct.
- Potential cybersecurity or IT issues, including account information not displaying correctly or records not appearing accurate.
- Whether material information is being hidden from the public or stock market.
- Other checks needed before making an investment decision.

The goal is a balanced, evidence-based due-diligence process, not an unsupported “safe/unsafe” label or guaranteed buy/sell recommendation.

## 2. Detailed checklist and quality documents requested

The user supplied detailed content and asked whether these documents were included, and to update them if missing.

### Stock Due-Diligence Checklist

The checklist must cover these nine areas:
A. **Identity and business** — legal entity, ticker, exchange, share class, jurisdiction, currency, fiscal year, business model, customers, suppliers, subsidiaries, competitors, dependencies, and sustainability.
B. **Financial health and accounting** — multi-year revenue and profit, margins, operating/free cash flow, cash, debt, interest coverage, liquidity, working capital, receivables, inventory, auditor opinions, restatements, accounting changes, dilution, unusual transactions, guarantees, and liabilities.
C. **Legal and regulatory** — civil and shareholder litigation, criminal investigations/charges/convictions, securities and accounting matters, bribery/corruption/insider trading, enforcement, sanctions, fines, licensing, taxes, labor, safety, consumer, environmental, competition/antitrust, IP disputes, and matters involving leaders or controlling shareholders. Record status, dates, outcome, exposure, and company response.
D. **Fraud, transparency, and disclosure** — verify material claims, related-party transactions, conflicts, undisclosed liabilities, disclosure gaps, filing delays, inconsistencies, insider sales in context, and credible whistleblower/journalism/short-seller claims. Separate evidence from allegation and speculation.
E. **Cybersecurity and IT integrity** — confirmed breaches, data leaks, ransomware, account and transaction integrity, regulatory findings, data protection, IT controls, outages, customer impact, remediation, and independent assurance. Do not claim malware or intentional manipulation without evidence.
F. **Management and governance** — leadership conduct, board and auditor independence, compensation, ownership/voting rights, minority protections, insider transactions, whistleblower systems, internal controls, and guidance versus outcomes.
G. **Valuation and outlook** — sector-appropriate metrics, history and peers, cash-flow assumptions, capital needs, optimistic/base/pessimistic scenarios, upside/downside, margin of safety, growth sustainability, capital allocation, dilution, competition, regulation, macroeconomics, and geopolitics.
H. **Trading and shareholder risks** — liquidity, transaction impact, volatility, halts, exchange compliance, unusual price/volume, short interest, issuance, buybacks, lock-ups, insider sales, delisting, restructuring, bankruptcy, dividends, and tax.
I. **Evidence quality** — prioritize primary sources, cite source links and dates, verify current legal/regulatory status, describe conflicting evidence and missing information, and never make unsupported claims that a company is “clean,” “fraudulent,” or “safe.”

Checklist statuses should be: `Reviewed`, `Flag`, `Not found in sources reviewed`, `Not applicable`, or `Not verified`. The checklist is an investigation aid, not proof that every risk has been eliminated.

### Definition of Done

A report is ready only when applicable checks are completed or explicitly marked incomplete:
- **Identity and scope:** verify company/security, ticker, exchange, share class, jurisdiction, analysis and price dates, currency, financial periods, and security ambiguity.
- **Evidence and sourcing:** trace material claims; prioritize official filings, exchange/regulator records, and court records; use current dates; never invent sources or citations; disclose conflicts and limitations; separate facts, allegations, interpretations, and unknowns.
- **Financial analysis:** use consistent periods/currencies, assess cash flow/debt/liquidity/accounting quality, check auditor opinions/restatements, use suitable valuation methods, and discuss downside sensitivity.
- **Risk investigation:** record legal status/outcomes, avoid treating allegations as proven, support cybersecurity claims, consider governance/disclosure/shareholder rights, and disclose material gaps.
- **Conclusion:** summarize positives and material risks, support and qualify the conclusion, avoid guarantees or unsupported personalized buy/sell instructions, identify conditions that could change the assessment, and include a source log and review triggers.

If a critical check cannot be completed, the report must state the limitation and use a `Further research` status rather than implying the company passed.

### End-to-End Stock Due-Diligence Playbook

The requested process has 11 steps:
1. Scope the request and identify the company/ticker, exchange, jurisdiction, intended purchase/holding/comparison, analysis date, and horizon. Ask a focused question if the security is ambiguous.
2. Build a source plan using annual and interim filings, exchange announcements, regulators, court records, investor relations, reputable journalism, and relevant cybersecurity research; record publication/access dates.
3. Understand the business model, customers, competition, dependencies, and concentration risks.
4. Analyze multi-year financial quality, cash flow, debt, liquidity, working capital, dilution, auditor comments, restatements, and unusual transactions.
5. Investigate legal, regulatory, fraud, sanction, tax, and disclosure matters; record conduct, dates, jurisdiction, status, outcome, impact, response, sources, and uncertainty.
6. Assess cybersecurity and IT risks using evidence and confirmed customer impact; do not infer malware or concealment from rumors or symptoms alone.
7. Review management and governance, including leadership, board/auditor independence, related parties, compensation, ownership, insider activity, shareholder rights, and management credibility.
8. Assess industry, macroeconomic, regulatory, trading, dilution, liquidity, and delisting risks.
9. Estimate valuation with sector-appropriate methods, explicit assumptions, and scenarios; avoid false precision.
10. Synthesize a qualified status: `Potential candidate`, `Watchlist`, `Further research`, or `Avoid / elevated risk`, with reasons, downside risks, and factors that could change the view.
11. Deliver the report using the template, source log, as-of date, and definition-of-done checks; define concrete follow-up triggers if monitoring is requested.

### Research and Reporting Standards

The requested standards include:
- **Source hierarchy:** official filings/financial statements/exchange disclosures/regulator orders/court records first; company statements; reputable journalism/specialist publications; independent research and short-seller reports; social media/forums only as leads.
- **Evidence labels:** confirmed fact; official allegation/proceeding; reported allegation; analysis/inference; unknown/not verified.
- **Legal matters:** record jurisdiction, case identifier, dates, parties, allegations, procedural status, findings, penalties/settlements, appeals, company response, and impact. A lawsuit does not prove allegations; a settlement is not automatically an admission.
- **Financial analysis:** identify periods and currencies, distinguish reported figures from calculations, explain unusual/non-GAAP items, compare profits with cash flow, assess debt/liquidity, use comparable periods, explain sector-specific limits, and never invent data.
- **Valuation:** state date, price source, method, and assumptions; use scenarios/sensitivity; explain limits; do not treat a low multiple as proof of cheapness.
- **Cybersecurity/IT integrity:** distinguish breaches, outages, data-quality problems, control weaknesses, allegations, and speculation; explain impact, evidence, investigation, and remediation.
- **Transparency/conflicts:** focus on required disclosures, material omissions, inconsistencies, related parties, and evidence of deception; do not treat legitimate trade-secret protection as wrongdoing.
- **Risk ratings:** define Low/Medium/High and consider likelihood, severity, financial materiality, evidence strength, time horizon, remediation, and price expectations; avoid unexplained numeric scores.
- **Responsible conclusions:** research aid, not return guarantee or personalized financial advice; trace conclusions to evidence and assumptions.

## 3. Requested plugin / skill packaging

The user first asked for this as a Markdown file, then requested a Codex-style skill structure:

```text
skills/<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── deliverable-template.md
└── references/
    ├── checklist.md
    ├── definition-of-done.md
    ├── end-to-end-playbook.md
    └── standards.md
```

The user then clarified that the intended deliverable should be a **ChatGPT plugin**, not a custom GPT, because they were concerned about a notice saying GPTs would be retired on December 11 and should be migrated. They asked to adapt the work to the ChatGPT plugin format.

They asked to update the revision number whenever changes warranted it, distinguishing minor fixes, new capabilities, and major releases. A sensible semantic-versioning interpretation is:
- Patch: backward-compatible fixes and documentation corrections.
- Minor: backward-compatible new capabilities or meaningful new workflow additions.
- Major: breaking changes to structure, interface, or expected behavior.

The user specifically asked that every version be committed to the GitHub repository `stock-due-diligence`.

## 4. Plugin and repository work recorded

- Plugin name: `stock-due-diligence`
- Plugin ID: `plugins_6ada26384798819191722437eddeb00b`
- Plugin URL: https://chatgpt.com/plugins/plugins_6ada26384798819191722437eddeb00b
- Scope: private/user
- Published plugin-platform version recorded in chat: `0.1.5`
- Latest plugin release ID recorded: `pluginrel_6ada27ba2dd88191a7683c23c6c15dc7`
- GitHub repository: https://github.com/ezhilrean/stock-due-diligence
- Current v0.1.5 source commit recorded: https://github.com/ezhilrean/stock-due-diligence/commit/814ff9401f5902ea5bf5bb0be423c51b79f9073a
- Source includes manifests, skill instructions, and supporting references: checklist, definition of done, deliverable template, playbook, and research standards.
- Branches `v0.1.1` through `v0.1.5` were created, but the recorded branches were all based on the same current source snapshot rather than verified historical snapshots of each archive.
- The user provided/mentioned version-specific ZIP archives and requested a corresponding branch and GitHub Release for each.
- A check of the GitHub Releases API returned an empty list at that time. Therefore, no GitHub Releases had been published at that point.

## 5. User's release-publishing questions

The user said they could not see the release and GitHub showed **“No releases published.”** The response explained that branches are not releases and described the GitHub website flow:
1. Open Releases and choose “Draft a new release.”
2. Select or create the matching tag, e.g. `v0.1.1`.
3. Choose the correct target branch/commit.
4. Add a title such as `Stock Due Diligence v0.1.1`.
5. Add version-accurate release notes.
6. Attach the matching ZIP, e.g. `stock-due-diligence-chatgpt-plugin-v0.1.1.zip`.
7. Publish and verify the release and asset on the Releases page.

Expected versions were `v0.1.1`, `v0.1.2`, `v0.1.3`, `v0.1.4`, and `v0.1.5`, each with its corresponding ZIP asset. This mapping must be checked against actual filenames and content before publishing. The correct historical source must be used for each tag.

## 6. Documentation requested and created

The user requested three Markdown files in a repository `documentation/` folder:
1. `documentation/CHAT-SUMMARY.md` — chat/project summary.
2. `documentation/GITHUB-RELEASE-GUIDE.md` — release creation and publishing steps.
3. `documentation/REUSABLE-PLUGIN-PROJECT-INSTRUCTIONS.md` — reusable instructions for future plugin projects.

The latter two were committed and verified at:
- https://github.com/ezhilrean/stock-due-diligence/blob/main/documentation/GITHUB-RELEASE-GUIDE.md
- https://github.com/ezhilrean/stock-due-diligence/blob/main/documentation/REUSABLE-PLUGIN-PROJECT-INSTRUCTIONS.md

This summary file was updated to include the previously omitted original investment-analysis questions and detailed requirements. Verify its latest commit after updating.

## 7. Important distinctions and remaining work

A plugin-platform version, Git branch, Git tag, GitHub Release, and ZIP asset are separate objects:
- A branch is a movable line of development.
- A tag identifies a specific commit.
- A GitHub Release is a published release record associated with a tag.
- A ZIP asset is an attached downloadable archive.
- Publishing a plugin in the plugin platform does not automatically publish a GitHub Release.

Remaining tasks, unless already completed after this summary was written:
- Verify that each historical branch/tag contains the exact matching version's source.
- Publish the five GitHub Releases and attach the correct ZIP archives.
- Verify each published release and downloadable asset.
- Ensure future plugin changes receive an appropriate version bump and a Git commit.
- Continue to keep the documentation aligned with the actual repository and release status.

Releases page: https://github.com/ezhilrean/stock-due-diligence/releases
