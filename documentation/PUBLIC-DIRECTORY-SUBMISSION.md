# Public Plugins Directory Submission Preparation

**Target publisher:** ezhillarasan ramalingham (individual / personal developer)  
**Source branch:** `v1.0.1`  
**Package version prepared here:** `1.0.1`  
**Publication status:** GitHub source changes committed to `v1.0.1`; public website deployment and DNS are pending; not submitted to the public plugin directory.

Official instructions:
- [Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission)
- [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines)
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)

## Packaging-guide alignment and metadata corrections in this branch

The supplied copy of the official packaging guide (pages 5–7) describes a portable plugin rooted at `plugin.json`, with optional `skills/`, optional `mcp.json`, optional `.codex-plugin/plugin.json` compatibility metadata, and optional assets. It says OpenAI-specific presentation and marketplace metadata belongs under `extensions.com.openai` in the root `plugin.json`. This package is skill-based and does not declare an MCP server, so it should not invent an MCP endpoint or credentials.

- Replaced the inaccurate author value `OpenAI` with the publisher name supplied by the developer: `ezhillarasan ramalingham`.
- Aligned the listing's `developerName` with that supplied publisher name.
- Added the known repository and homepage URLs to both manifests; did not invent a license or personal profile URL.
- Bumped both manifests from `0.1.5` to `1.0.0` for this public-submission preparation update.
- Kept the existing skill instructions requiring verifiable sources, careful treatment of allegations, explicit unknowns and limitations, and no guaranteed investment outcomes.
- Added public submission release notes.

The directory displays the name associated with the verified Developer identity selected in the submission portal. The manifest's developer name should match that identity. Do not claim to be OpenAI or imply OpenAI endorsement.

## Proposed listing copy

**Display name:** Stock Due Diligence  
**Short description:** Investigate stocks and risks

**Long description:**

Research publicly traded companies before making investment decisions. Review business fundamentals, financial statements, debt and liquidity, legal and regulatory matters, fraud allegations, disclosure quality, cybersecurity disclosures, management and governance, valuation assumptions, and downside scenarios. The workflow prioritizes primary sources, cites evidence, distinguishes allegations from established findings, and identifies material gaps and unverified items. Results support independent research; they do not guarantee investment performance or constitute personalized financial advice. Verify important claims against original sources and consider qualified professional advice where appropriate.

## Before uploading

- [ ] Confirm your individual developer identity in OpenAI Platform settings and use that verified identity during upload.
- [ ] Review the current automated checks and the [public plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines).
- [ ] Confirm the listing copy accurately describes the package and its actual behavior.
- [ ] Inspect the ZIP contents; include the root `plugin.json`, `.codex-plugin/plugin.json`, skill files, and all referenced reference documents. Include only files required for the package; do not include internal working notes unless intended for users.
- [ ] Keep credentials, tokens, private information, and reviewer credentials out of the ZIP.
- [ ] Add an app logo/icon as required by the current portal. A 256 × 256 PNG icon is included at `assets/icon.png`; confirm the portal's current icon size requirements before submission.
- [x] Commerce is deferred for v1.0.1; see `documentation/COMMERCE-IMPLEMENTATION-PLAN.md` before planning a future paid release.
- [ ] Publish and verify the four URLs. Follow `documentation/PUBLIC-WEBSITE-DEPLOYMENT.md` for GitHub Pages and DNS setup.
- [ ] Skills-only plugins do not require MCP server review test cases or a demo recording, according to the current submission instructions. If you later add MCP functionality, follow the separate MCP review requirements.
- [ ] Upload the ZIP in the official Plugins dashboard. Resolve required validation errors and wait for required skill scans to complete.
- [ ] Review all findings. The portal's actual findings are authoritative; this checklist does not guarantee acceptance.
- [ ] Complete any required submission information and policy attestations, then select **Submit for review**.
- [ ] Track review status and respond to feedback.
- [ ] After approval, open the approved package version and select **Publish plugin**. Verify that the listing appears in the public directory.

## Safeguards to preserve

- Prefer primary sources such as company filings, audited financial statements, exchange notices, regulator records, and court records.
- Cite material claims and state the report's as-of date.
- Distinguish confirmed facts, official proceedings, reported allegations, analysis/inference, and unknown/not verified.
- A lawsuit, investigation, short-seller report, or allegation is not proof of wrongdoing.
- Never fabricate citations, source links, figures, case identifiers, or searches.
- Do not treat missing public evidence as proof that no issue exists.
- Do not infer malware or intentional manipulation from an account discrepancy or outage alone.
- State material gaps and recommend further research when critical checks remain incomplete.
- Do not present results as guaranteed performance or personalized financial advice.

## Important distinction

A GitHub branch or release is not a public Plugins Directory listing. The `v1.0.1` branch contains the website source and package preparation files, but GitHub Pages/DNS deployment has not been verified. Submission, automated checks, review, approval, and the final **Publish plugin** action must be completed in the official portal by the verified developer.
