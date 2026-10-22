# Stock Due Diligence Plugin — Complete Chat Summary

**Date:** 2026-10-22  
**Repository:** [ezhilrean/stock-due-diligence](https://github.com/ezhilrean/stock-due-diligence)

This document summarizes the user's original stock-investment questions, requested due-diligence framework, plugin packaging requirements, version-control work, and GitHub release questions.

## 1. Original stock-investment question

The user asked:

> If I want to buy any new stocks, then what evaluation do I need to do?

The proposed analysis should cover:

- **Company details:** business model, products, customers, competitors, and market position.
- **Legal exposure:** court cases, lawsuits, investigations, and regulatory proceedings.
- **Financial health:** debt (the original message used “debut”), liabilities, cash flow, profitability, and accounting quality.
- **Fraud and misconduct:** substantiated fraud, violations, threats, conflicts of interest, and other misconduct.
- **Cybersecurity and IT integrity:** confirmed breaches, system reliability, account-display discrepancies, transaction accuracy, and data integrity.
- **Transparency:** material omissions, inconsistent disclosures, and evidence of information being improperly withheld from investors or the market.
- **Investment decision factors:** valuation, downside scenarios, governance, market risks, and other relevant checks.

The goal is a balanced, evidence-based assessment—not an unsupported “safe/unsafe” label or a guaranteed buy/sell recommendation.

## 2. Stock Due-Diligence Checklist

The user supplied a checklist and asked that it be included and updated where necessary. It covers nine areas.

### A. Identity and business

- Verify the legal entity, ticker, exchange, share class, and listing jurisdiction.
- Record reporting currency, fiscal year, and analysis date.
- Understand products, services, revenue model, customers, and markets.
- Identify major customers, suppliers, competitors, dependencies, subsidiaries, joint ventures, and related parties.
- Assess competitive advantages and business sustainability.

### B. Financial health and accounting

- Review multi-year revenue, profit, margins, operating cash flow, and free cash flow.
- Assess cash, debt, interest coverage, liquidity, working capital, receivables, and inventory.
- Review auditor opinions, qualifications, auditor changes, restatements, accounting-policy changes, and unusual adjustments.
- Compare reported profit with cash flow.
- Examine share-based compensation, dilution, unusual expenses, transactions, guarantees, and liabilities.

### C. Legal and regulatory

- Search civil litigation, shareholder actions, criminal investigations, charges, and convictions.
- Review securities, accounting, bribery, corruption, and insider-trading matters.
- Check regulatory enforcement, fines, sanctions, license issues, and tax disputes.
- Consider labor, safety, consumer, environmental, competition, antitrust, and intellectual-property matters.
- Include matters involving executives, directors, founders, and controlling shareholders.
- For each material matter, record status, date, outcome, financial exposure, and company response.

### D. Fraud, transparency, and disclosure

- Verify material claims about contracts, customers, products, and growth.
- Check related-party transactions, conflicts of interest, undisclosed liabilities, guarantees, and material risks.
- Compare filings with company announcements and independent sources.
- Review filing delays, disclosure gaps, and unexplained inconsistencies.
- Assess insider sales in context; do not infer wrongdoing from sales alone.
- Consider credible whistleblower, investigative-journalism, and short-seller claims.
- Distinguish evidence from allegations and speculation.

### E. Cybersecurity and IT integrity

- Review confirmed breaches, data leaks, ransomware, and other security incidents.
- Assess customer-account integrity, transaction accuracy, and record reliability.
- Check regulatory findings, data-protection compliance, material IT-control weaknesses, audit findings, and repeated outages.
- Record customer impact, remediation, and independent assurance.
- Do not label an incident malware or deliberate manipulation without evidence.

### F. Management and governance

- Review leadership history and substantiated misconduct.
- Assess board effectiveness, board independence, and auditor independence.
- Compare executive compensation with performance.
- Examine ownership, voting rights, minority-shareholder protections, insider holdings, and transactions.
- Review whistleblower systems, internal controls, and management guidance versus actual outcomes.

### G. Valuation and business outlook

- Use valuation metrics appropriate to the sector.
- Compare with company history and relevant peers.
- Review cash-flow assumptions and capital requirements.
- Consider optimistic, base, and pessimistic scenarios.
- Estimate upside, downside, and margin of safety.
- Assess growth sustainability, capital allocation, dilution, competition, disruption, regulation, macroeconomics, and geopolitics.

### H. Trading and shareholder risks

- Review liquidity and likely transaction impact.
- Assess volatility, trading halts, and exchange compliance.
- Investigate unusual price or volume patterns without treating them as proof of misconduct.
- Review short interest and allegations with corroboration.
- Consider share issuance, buybacks, lock-up expirations, insider sales, delisting, restructuring, and bankruptcy risk.
- Assess dividend coverage and tax implications where relevant.

### I. Evidence quality

- Prioritize primary sources where available.
- Attach source links and dates to important claims.
- Verify current legal and regulatory status as of the report date.
- Describe conflicting evidence and material information gaps.
- Do not make unsupported claims that a company is “clean,” “fraudulent,” or “safe.”

**Checklist status labels:** `Reviewed`, `Flag`, `Not found in sources reviewed`, `Not applicable`, and `Not verified`.

The checklist is an investigation aid; it does not prove that every risk has been eliminated.

## 3. Definition of Done

A report is ready to deliver only when applicable checks are complete or clearly marked incomplete.

### Identity and scope

- Verify the legal company name, ticker, exchange, share class, and jurisdiction.
- State the analysis date, price date, reporting currency, and financial periods.
- Resolve ambiguity about the security or explicitly disclose it.

### Evidence and sourcing

- Make material factual claims traceable to sources.
- Prioritize official filings, exchange disclosures, regulator records, and court records where relevant.
- Use current dates for time-sensitive information.
- Never invent sources, searches, citations, or links.
- Disclose conflicting reports and source limitations.
- Distinguish facts, allegations, interpretations, and unknowns.

### Financial analysis

- Use consistent periods and currencies where possible.
- Assess cash flow, debt, liquidity, and accounting quality.
- Check auditor opinions and material restatements.
- Use appropriate valuation methods with visible assumptions.
- Discuss downside scenarios and sensitivity to key assumptions.

### Risk investigation

- Record legal and regulatory status and outcomes where available.
- Do not present allegations as proven facts without evidence.
- Support cybersecurity claims; do not equate an outage with malware.
- Consider governance, related-party transactions, disclosure quality, and shareholder rights.
- Identify material gaps and unresolved questions.

### Conclusion

- Summarize the strongest positives and material risks.
- Support and qualify the conclusion with evidence.
- Avoid guarantees and unsupported personalized buy/sell instructions.
- Record conditions that could change the assessment.
- Include a source log and concrete next-review triggers.

If a critical check cannot be completed, clearly state the limitation and use a **Further research** status rather than implying the company passed.

## 4. End-to-End Stock Due-Diligence Playbook

1. **Scope the request.** Record the company and ticker, exchange, jurisdiction, whether the user is considering a new purchase, an existing holding, or a comparison, plus the analysis date and time horizon. Ask a focused clarifying question if the security is ambiguous.
2. **Build a source plan.** Start with annual reports and audited statements, interim filings, exchange announcements, regulator records, official court records, company investor-relations materials, reputable journalism, and relevant cybersecurity research. Record publication and access dates.
3. **Understand the business.** Explain revenue generation, customers, competitive landscape, dependencies, business sustainability, and concentration risk.
4. **Analyze financial quality.** Review multi-year trends in revenue, profit, margins, cash flow, debt, liquidity, working capital, receivables, inventory, dilution, auditor comments, restatements, and unusual transactions.
5. **Investigate integrity risks.** Search official sources for litigation, enforcement, sanctions, tax issues, fraud findings, and disclosure concerns. Record the conduct, date, jurisdiction, status, outcome, potential impact, company response, source, and remaining uncertainty.
6. **Assess cybersecurity and IT risks.** Prioritize confirmed incidents, official notices, customer impact, material IT-control weaknesses, remediation, and repeated incidents. Do not infer malware or deliberate concealment from rumors or symptoms alone.
7. **Review management and governance.** Examine leadership, board and auditor independence, related-party transactions, compensation, insider holdings, shareholder rights, and management credibility.
8. **Assess industry and trading risks.** Consider competition, disruption, regulation, macroeconomic sensitivity, currencies, supply chains, geopolitical exposure, liquidity, dilution, unusual trading activity, and exchange compliance.
9. **Estimate valuation.** Choose methods suited to the sector and company maturity. Explain assumptions and limitations; use optimistic, base, and pessimistic cases where appropriate. Avoid false precision.
10. **Synthesize a qualified conclusion.** Choose a research status and explain why:
    - **Potential candidate:** evidence is broadly supportive, material risks appear manageable, and valuation may be attractive under stated assumptions.
    - **Watchlist:** the company is interesting, but price, timing, or unresolved questions require further review.
    - **Further research:** evidence gaps or unresolved risks prevent a sound conclusion.
    - **Avoid / elevated risk:** evidence indicates serious risks or an unattractive risk/reward profile under stated assumptions.
11. **Deliver and maintain the record.** Use the report template, include a source log and as-of date, complete the Definition of Done, and specify concrete review triggers if monitoring is requested.

## 5. Research and Reporting Standards

### Source hierarchy

Prefer sources in this general order, depending on the claim:

1. Official regulatory filings, audited financial statements, exchange disclosures, regulator orders, court judgments, and official records.
2. Direct company statements and investor-relations materials.
3. Reputable news organizations and established specialist publications.
4. Independent research, short-seller reports, and technical analysis.
5. Social media, forums, and unverified claims—as leads only, not proof.

Primary sources can still be incomplete or self-interested. Cross-check material claims when feasible.

### Evidence labels

Use clear labels:

- **Confirmed fact:** supported by authoritative records or strong corroborated evidence.
- **Official allegation / proceeding:** an authority or party has made a claim, but the outcome may remain unresolved.
- **Reported allegation:** a credible secondary source reports a claim that may not be independently established.
- **Analysis / inference:** a reasoned interpretation based on disclosed evidence.
- **Unknown / not verified:** evidence was not found or could not be confirmed in the sources reviewed.

Never convert an allegation into a finding or treat an absence of evidence as proof that no issue exists.

### Legal and regulatory matters

For each material case, seek the jurisdiction, case identifier, filing or announcement date, parties, allegations, procedural status, findings, penalties or settlement, appeals, company response, and potential financial impact. Check current status rather than relying on an old headline.

A settlement does not necessarily mean an admission of liability. A filed lawsuit does not prove the claims.

### Financial analysis

- State the reporting period and currency for financial metrics.
- Distinguish company-reported data from calculations and estimates.
- Explain unusual accounting items and non-GAAP measures.
- Compare profit with cash flow and assess debt and liquidity.
- Use comparable periods and peer groups where possible.
- Explain limitations for financial institutions, early-stage companies, and cyclical businesses.
- Never invent missing figures or silently fill gaps with assumptions.

### Valuation

- State valuation date, share-price source, method, and assumptions.
- Use methods appropriate to the sector, maturity, and business model.
- Include sensitivity analysis or scenarios when assumptions materially affect results.
- Explain limitations; do not present an estimate as certainty.
- Do not use a low multiple alone as proof that a stock is cheap.
- Explain the drivers behind any valuation range.

### Cybersecurity and IT integrity

Distinguish confirmed breaches, service outages, data-quality issues, control weaknesses, allegations, and speculative claims. A missing account display or inaccurate balance can have multiple causes and does not, by itself, establish malware or intent. Describe evidence, customer impact, investigation status, and remediation.

### Transparency and conflicts

Consider disclosure requirements and materiality in the relevant jurisdiction. Companies may legitimately protect trade secrets. Focus on required disclosures, material omissions, inconsistencies, related-party dealings, and evidence of deception—not all non-public information.

### Risk ratings

If using Low / Medium / High, define the labels and explain the basis. Consider likelihood, severity, financial materiality, evidence strength, time horizon, management response, remediation, and whether the risk is reflected in the price. Do not assign a precise numerical risk score without a consistent, explained method.

### Responsible conclusions

The report is a research aid, not a guarantee of returns or personalized financial advice. Avoid certainty about future price movements. Make the reasoning auditable by linking important conclusions to evidence and assumptions.

## 6. Requested plugin and skill packaging

The user first requested a Markdown file, then asked for a Codex-style skill layout:

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

The user clarified that the intended deliverable should be a **ChatGPT plugin**, not a custom GPT, citing a notice about migrating GPTs before December 11. They asked for the work to be adapted to the ChatGPT plugin format.

### Versioning expectations

The user requested a revision-number update when changes warrant it. A practical semantic-versioning interpretation is:

- **Patch:** backward-compatible fixes and documentation corrections.
- **Minor:** backward-compatible capabilities or meaningful workflow additions.
- **Major:** breaking changes to structure, interface, or expected behavior.

The user specifically requested that every version be committed to the GitHub repository `stock-due-diligence`.

## 7. Plugin and repository details recorded

- **Plugin name:** `stock-due-diligence`
- **Plugin ID:** `plugins_6ada26384798819191722437eddeb00b`
- **Plugin URL:** https://chatgpt.com/plugins/plugins_6ada26384798819191722437eddeb00b
- **Scope:** private/user
- **Plugin-platform version recorded in chat:** `0.1.5`
- **Latest plugin release ID recorded:** `pluginrel_6ada27ba2dd88191a7683c23c6c15dc7`
- **GitHub repository:** https://github.com/ezhilrean/stock-due-diligence
- **Current v0.1.5 source commit recorded:** https://github.com/ezhilrean/stock-due-diligence/commit/814ff9401f5902ea5bf5bb0be423c51b79f9073a

The source tree includes plugin manifests, skill instructions, and supporting references such as the checklist, Definition of Done, deliverable template, playbook, and research standards.

Branches `v0.1.1` through `v0.1.5` were created, but the recorded branches were all based on the same current source snapshot rather than verified historical snapshots of each archive. The user provided or referenced version-specific ZIP archives and requested a corresponding branch and GitHub Release for each.

A GitHub Releases API check returned an empty list at that time, meaning no GitHub Releases had been published then.

## 8. GitHub release-publishing questions

The user reported that GitHub showed **“No releases published.”** The following workflow was shared:

1. Open the repository's **Releases** page and choose **Draft a new release**.
2. Select or create the matching tag, such as `v0.1.1`.
3. Choose the correct target branch or commit.
4. Add a title, such as `Stock Due Diligence v0.1.1`.
5. Write release notes that describe the actual version contents.
6. Attach the matching ZIP, such as `stock-due-diligence-chatgpt-plugin-v0.1.1.zip`.
7. Publish the release.
8. Return to the Releases page and verify that the release and downloadable asset are visible.

The intended versions are `v0.1.1`, `v0.1.2`, `v0.1.3`, `v0.1.4`, and `v0.1.5`, each with its corresponding ZIP asset. Check actual filenames and contents before publishing. Each tag must point to the correct historical source.

## 9. Documentation files requested

The user requested three Markdown documents inside the repository's `documentation/` folder:

1. `documentation/CHAT-SUMMARY.md` — this chat and requirements summary.
2. `documentation/GITHUB-RELEASE-GUIDE.md` — steps to create and publish releases.
3. `documentation/REUSABLE-PLUGIN-PROJECT-INSTRUCTIONS.md` — reusable instructions for future plugin projects.

Links:

- [Chat summary](https://github.com/ezhilrean/stock-due-diligence/blob/main/documentation/CHAT-SUMMARY.md)
- [GitHub release guide](https://github.com/ezhilrean/stock-due-diligence/blob/main/documentation/GITHUB-RELEASE-GUIDE.md)
- [Reusable plugin project instructions](https://github.com/ezhilrean/stock-due-diligence/blob/main/documentation/REUSABLE-PLUGIN-PROJECT-INSTRUCTIONS.md)

## 10. Important distinctions and remaining work

A plugin-platform version, Git branch, Git tag, GitHub Release, and ZIP asset are separate objects:

- A **branch** is a movable line of development.
- A **tag** identifies a specific Git commit.
- A **GitHub Release** is a published release record associated with a tag.
- A **ZIP asset** is a downloadable archive attached to a release.
- Publishing a plugin on the plugin platform does not automatically publish a GitHub Release.

Remaining work, unless completed since this document was last checked:

- Verify each historical branch/tag contains the exact source for its version.
- Publish the five GitHub Releases and attach the correct ZIP archives.
- Verify each published release and downloadable asset.
- Apply appropriate version bumps and commit every future plugin change.
- Keep documentation aligned with the repository's actual source and release status.

**GitHub Releases page:** https://github.com/ezhilrean/stock-due-diligence/releases
