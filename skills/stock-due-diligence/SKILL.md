---
name: stock-due-diligence
description: Investigate publicly traded companies before investment by assessing business quality, financial statements, legal and regulatory exposure, fraud indicators, cybersecurity, governance, valuation, and investment risks. Use when researching a stock, screening a company, or preparing a documented pre-investment review.
---

# Stock Due-Diligence Skill

## Purpose

Produce a balanced, evidence-based stock due-diligence report. Evaluate the company, its financial health, legal and regulatory history, transparency, cybersecurity and IT risks, management, market conditions, valuation, and downside scenarios.

This skill supports research and decision-making; it does not guarantee an investment will be safe or profitable and must not present itself as personalized financial advice.

## When to use

Use this skill when asked to:
- Evaluate a company or ticker before buying shares.
- Investigate a company's financial health, lawsuits, fraud allegations, regulatory violations, or governance.
- Assess cybersecurity, customer-account integrity, data-protection, or IT-control concerns.
- Compare a stock's price with an estimated fair value.
- Create or update a documented investment due-diligence report.

## Workflow

1. **Identify the security.** Confirm legal company name, ticker, exchange, share class, listing jurisdiction, reporting currency, and the date of analysis. Resolve ticker ambiguity before proceeding. Record whether the user is considering a new purchase, reviewing an existing holding, or comparing securities, and capture the time horizon if supplied.
2. **Gather primary evidence first.** Review official filings, audited statements, exchange disclosures, regulator notices, court records, and company announcements. Use reputable independent reporting to add context. Record publication/filing and access dates where available.
3. **Assess business quality.** Explain how the company earns money, its customers, competitors, suppliers, market position, and key dependencies.
4. **Assess financial and accounting quality.** Examine multi-year revenue, profitability, cash flow, debt, liquidity, working capital, receivables, inventory, dilution, auditor opinions, restatements, and unusual transactions.
5. **Investigate legal, regulatory, and integrity risks.** Search for cases, enforcement actions, sanctions, fraud allegations, misconduct, undisclosed liabilities, related-party transactions, and material disclosure concerns. For each material matter, capture status, dates, outcome, company response, impact, and remaining uncertainty where available.
6. **Assess cybersecurity and IT integrity where relevant.** Review confirmed incidents, regulatory findings, customer impact, system reliability, controls, and remediation. Never infer malware or deliberate manipulation from a mere outage or account discrepancy.
7. **Assess governance and leadership.** Review directors, executives, auditor independence, compensation, ownership, insider transactions, minority-shareholder protections, and management credibility.
8. **Assess industry and market risks.** Consider competition, disruption, macroeconomic sensitivity, regulation, liquidity, unusual trading activity, dilution, and delisting risk.
9. **Estimate valuation.** Select methods suitable for the sector; state assumptions and compare a base case with optimistic and pessimistic cases where reasonable. Do not rely on one ratio alone or present estimates as certainty.
10. **Reach a qualified conclusion.** State strengths, risks, unresolved questions, valuation range if supportable, and a status such as `Further research`, `Watchlist`, `Potential candidate`, or `Avoid / elevated risk`. Explain what could change the conclusion.
11. **Document the evidence.** Attach sources and dates to material claims. Distinguish facts, allegations, analysis, and unknowns. Never invent sources, searches, citations, figures, case numbers, or assumptions.
12. **Run the definition of done.** Check `references/definition-of-done.md` before delivering. Follow `references/playbook.md`, use `references/checklist.md`, `references/deliverable-template.md`, and `references/research-standards.md` as supporting controls.

## Evidence and research standards

- Prefer primary sources and cite sources close to the claims they support.
- For time-sensitive claims, use current sources and provide publication or filing dates and the report's as-of date.
- Verify the relevant jurisdiction and current status of legal or regulatory matters.
- An allegation, lawsuit, short-seller report, or investigation is not proof of wrongdoing. Report status, response, outcome, and materiality where available.
- Do not treat a lack of public evidence as proof that no issue exists. Say when coverage is incomplete and what was actually checked.
- Do not claim to have searched databases or records that were not actually accessed.
- If evidence conflicts, describe the conflict and prioritize the most authoritative available source.
- Do not invent financial figures, case numbers, citations, valuation assumptions, or source links.
- Distinguish confirmed facts, official allegations/proceedings, reported allegations, analysis/inference, and unknown/not verified.
- Avoid definitive buy/sell instructions. Present evidence, assumptions, risks, and decision factors.
- For Low / Medium / High risk ratings, explain likelihood, severity, financial materiality, evidence strength, time horizon, management response, and whether the risk may be reflected in price. Do not assign numerical scores without a consistent, explained method.

## Required report sections

Use `references/deliverable-template.md` as the report template and consult:
- `references/checklist.md` for investigation areas.
- `references/playbook.md` for the step-by-step process.
- `references/research-standards.md` for source and interpretation standards.
- `references/definition-of-done.md` for final quality checks.

Put the executive conclusion and most material risks near the beginning. Include company identity, business model, financial and accounting quality, legal/regulatory matters, fraud and transparency, cybersecurity where relevant, governance, industry and trading risks, valuation and scenarios, open questions, conclusion, source log, as-of date, and review triggers.

## Handling missing information

If a material item cannot be verified:
- Label it `Not found in sources reviewed` or `Not verified`, as appropriate.
- Describe which sources or date range were checked, when known.
- Explain why the gap matters and what research would resolve it.
- If a critical check remains incomplete, add a clear limitation note and use `Further research` rather than implying the company passed.
- Do not convert missing information into a clean bill of health.

## Output style

Use concise, professional language. Put the executive conclusion and most material risks near the beginning. Use tables for financial metrics, legal matters, risk ratings, and source logs when they improve clarity. State the as-of date and distinguish company-reported information from independent assessment. Keep citations close to supported claims. Never describe a company as definitively safe, clean, or fraudulent without strong evidence and appropriate qualifications.

## Status definitions

- **Potential candidate:** Evidence is broadly supportive, key risks appear manageable, and valuation may be attractive under stated assumptions.
- **Watchlist:** Interesting company, but price, timing, or unresolved questions require further review.
- **Further research:** Material evidence gaps or unresolved risks prevent a sound conclusion.
- **Avoid / elevated risk:** Evidence indicates serious risks or an unattractive risk/reward profile under stated assumptions.

These are research labels, not guaranteed buy/sell instructions.

## Review metadata

Include workflow version `0.1.5` in the report metadata or notes when useful. Include the analysis as-of date and dates of key sources.
