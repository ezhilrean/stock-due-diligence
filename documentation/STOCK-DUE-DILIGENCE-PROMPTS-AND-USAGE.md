# How to Use Stock Due Diligence — Prompt Library

This guide explains how to use the Stock Due Diligence plugin and provides copy-ready prompts for common workflows. It is intended for the repository's users and future maintainers.

## 1. What this tool is for

Use the stock due-diligence workflow to research a publicly traded company before investing, review a current holding, compare companies, or revisit an earlier assessment. The workflow examines business quality, financial health, accounting, legal and regulatory matters, transparency, cybersecurity and IT integrity, governance, valuation, trading risks, and evidence quality.

It is a research aid—not a guarantee of safety or returns and not personalized financial advice.

## 2. How to start

1. Open the Stock Due Diligence plugin/skill in the ChatGPT environment where it is available.
2. Start a new message with a company name and ticker, plus the exchange or country if known.
3. Say whether you are considering a new purchase, reviewing a current holding, or comparing stocks.
4. Provide a time horizon and any areas of concern you want investigated.
5. Ask for an evidence-based report with source links, publication/access dates, and an explicit analysis date.
6. Answer a clarification question if the ticker or security is ambiguous.
7. Review the report's findings, limitations, risk status, valuation assumptions, and unresolved questions before making your own decision.

### Recommended input details

Provide as many of these as you know:
- Company name and ticker.
- Exchange and listing jurisdiction.
- Whether this is a new purchase, an existing holding, or a comparison.
- Time horizon (for example, 1–3 years or 5+ years).
- Your main concerns (financial quality, lawsuits, accounting, cybersecurity, governance, valuation, or all areas).
- Relevant share price/date, if you want valuation tied to a specific price.
- Reporting currency or investor jurisdiction if relevant.

Do not share passwords, brokerage login credentials, account numbers, or other secrets.

## 3. Master prompt — full due-diligence report

Copy and fill in the brackets:

```text
Act as an evidence-focused stock due-diligence research assistant.

Company: [LEGAL COMPANY NAME]
Ticker: [TICKER]
Exchange / jurisdiction: [EXCHANGE AND COUNTRY]
Purpose: [NEW PURCHASE / EXISTING HOLDING / COMPARISON]
Investment time horizon: [HORIZON]
Analysis date: [TODAY OR REQUESTED DATE]
Share price and date (optional): [PRICE, CURRENCY, DATE]
Focus areas: [ALL AREAS OR SPECIFIC CONCERNS]

Prepare a structured pre-investment due-diligence report.

Investigate:
1. Company identity, business model, products, customers, competitors, and dependencies.
2. Multi-year financial performance, cash flow, debt, liquidity, working capital, accounting quality, auditor opinions, restatements, and dilution.
3. Civil and criminal cases, regulatory proceedings, sanctions, tax disputes, and other material legal exposure.
4. Fraud allegations, disclosure gaps, related-party transactions, conflicts of interest, and transparency concerns.
5. Confirmed cybersecurity incidents, IT-control weaknesses, account/transaction integrity issues, outages, customer impact, and remediation.
6. Management, board, auditor independence, executive compensation, insider activity, ownership, and minority-shareholder rights.
7. Industry, competition, macroeconomic, geopolitical, trading, liquidity, and delisting risks.
8. Valuation using methods appropriate to the business, with assumptions and optimistic/base/pessimistic scenarios where supportable.
9. Main positive factors, downside risks, unresolved questions, and events that could change the assessment.

Research and evidence rules:
- Prioritize official filings, audited financial statements, exchange announcements, regulator records, court records, and direct company disclosures; use credible independent sources for context.
- Cite sources near the claims they support and include source dates and an as-of date.
- Do not claim to have searched a source that was not actually accessed. Do not invent figures, citations, cases, or links.
- Clearly distinguish confirmed facts, official proceedings/allegations, reported allegations, analysis/inference, and unknown/not verified.
- A lawsuit or allegation is not proof of wrongdoing. An outage or account discrepancy alone is not proof of malware or intent.
- Do not treat missing evidence as proof that no issue exists. Describe source coverage and information gaps.
- Explain valuation assumptions and limitations; do not imply false precision.
- Do not guarantee returns or provide unsupported personalized buy/sell instructions.

Use these research statuses as appropriate:
- Potential candidate
- Watchlist
- Further research
- Avoid / elevated risk

Explain why the status fits the evidence, what could change it, and what needs further verification. Include a source log and a checklist of completed, flagged, not found, not applicable, and not verified items.
```

## 4. Copy-ready prompts for specific tasks

### A. Quick initial screening

```text
Run an initial stock due-diligence screen for [COMPANY, TICKER, EXCHANGE]. Summarize the business, financial strength, valuation context, major legal/regulatory issues, governance concerns, confirmed cybersecurity issues, and the most important risks. Use current, traceable sources and dates. Separate facts from allegations and unknowns. End with a qualified research status and a list of questions that require deeper investigation. Do not present the screen as a final investment recommendation.
```

### B. Financial statements and accounting quality

```text
Analyze the financial health and accounting quality of [COMPANY, TICKER]. Review multi-year revenue, margins, earnings, operating cash flow, free cash flow, debt, liquidity, working capital, receivables, inventory, dilution, auditor opinions, restatements, unusual transactions, and off-balance-sheet commitments where disclosed. Compare profits with cash generation. Cite filings and periods, distinguish reported values from calculations, and identify gaps or warning signs without assuming fraud.
```

### C. Lawsuits and regulatory history

```text
Investigate material legal and regulatory matters involving [COMPANY, TICKER] and, where relevant, its executives and controlling shareholders. Prioritize official court registers, judgments, regulator notices, enforcement announcements, and company filings. For each matter, record jurisdiction, case ID if available, dates, parties, allegations, current procedural status, findings/outcome, penalties or settlement, appeals, company response, potential financial/operational impact, and source. Distinguish allegations from established findings and state what could not be verified.
```

### D. Fraud, disclosure, and transparency review

```text
Assess potential fraud indicators and disclosure-quality concerns for [COMPANY, TICKER]. Compare audited statements, exchange filings, company announcements, regulator records, and credible independent reporting. Review related-party transactions, conflicts, unusual accounting, delayed filings, restatements, material omissions, undisclosed liabilities, and substantiated whistleblower or short-seller claims. Treat claims as allegations unless supported by findings or corroborated evidence. State both supporting and conflicting evidence.
```

### E. Cybersecurity and account-integrity review

```text
Review publicly documented cybersecurity and IT-integrity risks for [COMPANY, TICKER]. Look for confirmed breaches, data leaks, ransomware, regulatory findings, material IT-control weaknesses, outages, inaccurate or missing customer records, transaction/account discrepancies, customer impact, remediation, and independent assurance. Prioritize official disclosures, regulator notices, court records, and credible technical research. Do not infer malware, concealment, or intentional manipulation from symptoms alone. Label each claim by evidence status.
```

### F. Management and corporate governance

```text
Assess the governance and management risks of [COMPANY, TICKER]. Review leadership track records, substantiated misconduct, board and auditor independence, compensation, related-party transactions, insider holdings/trading, voting rights, minority-shareholder protections, whistleblower controls, and management guidance versus outcomes. Use traceable sources, distinguish allegations from findings, and explain the possible impact on shareholders.
```

### G. Valuation and scenarios

```text
Estimate a reasonable valuation range for [COMPANY, TICKER] as of [DATE], using share price [PRICE/CURRENCY/DATE if supplied]. Choose methods suitable for the sector and business maturity. Show key inputs, assumptions, source dates, and limitations. Where supportable, build optimistic, base, and pessimistic scenarios; discuss sensitivity, downside, upside, and margin of safety. Compare with company history and relevant peers. Do not present estimates as certainty or use one multiple alone to declare the stock cheap.
```

### H. Compare multiple stocks

```text
Compare [COMPANY A / TICKER A] and [COMPANY B / TICKER B] for a potential investment over [TIME HORIZON]. Use comparable periods and currencies where possible. Compare business quality, financial strength, accounting quality, legal/regulatory exposure, transparency, cybersecurity disclosures, governance, valuation, liquidity, and key downside risks. Cite sources and dates, flag incomparable metrics, and identify which company has stronger evidence on each dimension. Give a qualified comparison, not a guaranteed winner.
```

### I. Review an existing holding

```text
Reassess my existing holding in [COMPANY, TICKER] as of [DATE]. Identify material changes in financial performance, guidance, valuation, legal/regulatory matters, governance, cybersecurity, capital allocation, and industry conditions since [LAST REVIEW DATE if known]. Explain what has improved, worsened, or remains uncertain. List the next events or disclosures that could change the thesis. Do not assume my purchase price or personal circumstances unless I provide them.
```

### J. Investigate a specific red flag

```text
Investigate this concern about [COMPANY, TICKER]: [DESCRIBE THE CLAIM OR INCIDENT]. Find primary sources first, then credible independent reporting. Determine what is confirmed, alleged, disputed, or unknown; identify dates, relevant entities, official case/regulator records where applicable, company response, impact, and follow-up developments. Do not repeat the claim as fact without evidence. Explain what additional evidence would be needed to reach a stronger conclusion.
```

### K. Run the checklist and Definition of Done

```text
Apply the Stock Due-Diligence Checklist and Definition of Done to the current report for [COMPANY, TICKER]. For each applicable item, mark Reviewed, Flag, Not found in sources reviewed, Not applicable, or Not verified. Link evidence and dates for material findings. Identify incomplete critical checks, conflicting evidence, missing sources, and unresolved questions. If any critical check remains incomplete, clearly mark the report Further research rather than implying the company passed.
```

### L. Update a prior report

```text
Update the prior stock due-diligence report for [COMPANY, TICKER]. Keep the previous analysis date and current analysis date clear. Check for new filings, earnings, guidance changes, court decisions, regulatory announcements, auditor changes, cybersecurity incidents, capital raises, insider disclosures, and material valuation changes since the last report. Summarize only meaningful changes, cite new sources and dates, and state whether the prior research status should change and why.
```

### M. Prepare an executive summary

```text
Turn the due-diligence findings for [COMPANY, TICKER] into a concise executive summary. Include business overview, strongest positives, top material risks, financial/accounting quality, legal/regulatory status, governance, confirmed cybersecurity issues if any, valuation context, key unknowns, research status, and next review triggers. Cite the most important sources. Do not hide material caveats to make the summary shorter.
```

## 5. How to interpret the output

Use the research status as a summary of evidence and unresolved work, not as a guarantee.

- **Potential candidate:** evidence is broadly supportive, material risks appear manageable, and valuation may be attractive under stated assumptions.
- **Watchlist:** the company is interesting, but price, timing, or open questions warrant follow-up.
- **Further research:** important evidence gaps or unresolved risks prevent a sound conclusion.
- **Avoid / elevated risk:** evidence suggests serious risks or an unattractive risk/reward profile under the stated assumptions.

Read the source links, note the analysis date, check important claims against primary records where possible, and consider whether the assumptions fit your circumstances. Do not interpret “not found in sources reviewed” as “does not exist.”

## 6. Useful follow-up prompts

After the first report, you can ask:

- “Show me the five most material risks and the evidence behind each.”
- “Which claims are allegations rather than established findings?”
- “What important sources could not be accessed?”
- “Which financial metrics are deteriorating, and over what periods?”
- “What assumptions drive the valuation most strongly?”
- “What evidence would invalidate the investment thesis?”
- “Which checklist items remain Not verified?”
- “Update this report with developments since [DATE].”
- “Create a source log with links, publication dates, access dates, and the claims each source supports.”

## 7. Source and safety rules

- Use the company's actual listing jurisdiction to select official sources.
- Prefer primary sources but cross-check material claims where feasible.
- Never invent a court case, regulator action, financial number, source link, or search result.
- Make uncertainty visible. If information cannot be verified, say so.
- Distinguish public allegations from legal findings and technical symptoms from confirmed security incidents.
- Avoid guarantees and unsupported personalized buy/sell instructions.
- Never include passwords, private brokerage credentials, or sensitive account information in prompts.

## 8. Related repository documents

- [Stock due-diligence checklist](../skills/stock-due-diligence/references/checklist.md)
- [Definition of Done](../skills/stock-due-diligence/references/definition-of-done.md)
- [End-to-end playbook](../skills/stock-due-diligence/references/playbook.md)
- [Research standards](../skills/stock-due-diligence/references/research-standards.md)
- [GitHub release guide](GITHUB-RELEASE-GUIDE.md)

If a linked path changes in the repository, update this section to match the actual file names.
