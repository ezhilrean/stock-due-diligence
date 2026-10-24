# Commerce Implementation Plan — Stock Due Diligence

**Document status:** Planning only; no commerce is implemented in v1.0.1  
**Version target:** A future release (version number to be assigned after scope approval)  
**Owner:** Plugin publisher / maintainer  
**Last updated:** 2026-10-23

## 1. Current decision

Commerce is deferred. Version 1.0.1 is intended to provide research workflows and educational/informational analysis only. It does not sell subscriptions, reports, credits, API access, premium research, or other paid products; it does not accept or process payments. Do not advertise paid features or represent any payment flow as available until implemented, tested, and documented.

This plan is an action plan, not a statement that legal, tax, payment, or platform requirements have been satisfied.

## 2. Decisions required before implementation

The publisher must decide and document:

- [ ] **What is sold:** subscription to features, one-time report, usage credits, access to a separate service, API access, or another product.
- [ ] **Customer:** individual, business, or both; minimum age and supported jurisdictions.
- [ ] **Pricing:** currency, price points, billing interval, free tier, trial, usage limits, taxes, and any refunds.
- [ ] **Payment location:** publisher website, payment provider hosted checkout, or a platform-approved in-product commerce flow. Do not assume ChatGPT supports a particular payment mechanism.
- [ ] **Payment provider:** evaluate providers and confirm account eligibility, supported countries, fees, dispute handling, payouts, tax tools, recurring billing, and data-processing terms.
- [ ] **Entitlements:** how paid access is granted, checked, renewed, suspended, cancelled, and revoked.
- [ ] **Deliverable:** what the buyer receives and when; report generation, delivery failures, retries, and service limits.
- [ ] **Support and refunds:** contact path, response target, cancellation and refund rules.
- [ ] **Legal/tax review:** consumer law, subscription disclosures, automatic-renewal rules, privacy obligations, tax/VAT/GST, sanctions, and financial-services restrictions in each target jurisdiction.
- [ ] **OpenAI policy review:** confirm the current plugin/ChatGPT directory rules and whether the intended payment model is allowed before building it.

Do not infer these choices from the publisher's other projects or from a payment provider's marketing.

## 3. Implementation stages

### Stage A — Product and policy definition

1. Write a concise product specification, user journey, feature matrix, and pricing proposal.
2. Separate free and paid features explicitly; avoid deceptive paywalls or ambiguous trial conversion.
3. Define cancellation, refund, failed-payment, chargeback, service outage, and account-deletion behavior.
4. Identify all personal and financial data fields touched by checkout, entitlement checks, support, analytics, and delivery.
5. Have the publisher approve the decisions above before implementation starts.

**Exit criteria:** approved product/pricing brief, country scope, data-flow diagram, and policy requirements checklist.

### Stage B — Architecture and payment integration

1. Choose a supported checkout method after checking current platform rules.
2. Keep secret API keys and webhook signing secrets in server-side secret storage; never put them in plugin manifests, skill files, website JavaScript, public repositories, prompts, or ZIP archives.
3. Prefer hosted checkout so the plugin/site does not directly handle raw card numbers.
4. Implement server-side checkout session creation and verified webhook handling.
5. Verify webhook signatures, event IDs, timestamps, and idempotency. Do not grant entitlements from a browser redirect alone.
6. Store the minimum entitlement record needed (customer reference, product/plan, status, start/end, provider event reference); avoid storing payment-card data.
7. Add retries, duplicate-event protection, reconciliation, logging without secrets, and a manual recovery process.
8. Design for cancellation, refunds, disputes, expired cards, failed renewals, and provider outages.

**Exit criteria:** reviewed data flow and threat model; sandbox checkout, webhook verification, idempotency, and recovery tests pass.

### Stage C — Plugin/site entitlement experience

1. Define how the user signs in and links a purchase to an account without exposing credentials.
2. Decide whether paid features are delivered on the website or through a backend API; a skill-only package cannot securely enforce paid entitlements by itself.
3. If a remote service is required, document its endpoint, authentication, availability, data retention, rate limits, and operational owner before adding any MCP/API integration.
4. Return clear states for active, expired, cancelled, refunded, disputed, and unknown entitlements.
5. Provide a non-payment path for users who only want the current research workflow.
6. Do not claim the plugin can verify a purchase unless the verification is actually implemented and tested.

**Exit criteria:** entitlement lifecycle tested end-to-end; authorization cannot be bypassed by editing client-side state or prompts.

### Stage D — Legal, privacy, and customer operations

1. Update the privacy notice to identify the actual controller/operator, collected fields, purposes, legal basis where applicable, recipients/processors, international transfers, retention, deletion, and contact channel.
2. Publish terms that accurately describe product scope, pricing, renewals, cancellation, refunds, availability, intellectual property, acceptable use, disclaimers, and governing-law terms chosen by the publisher after appropriate review.
3. Add clear checkout disclosures for total price, currency, billing cadence, renewal, trial conversion, taxes, cancellation, and refund rules where applicable.
4. Document support, incident response, refund/chargeback handling, and account-deletion procedures.
5. Have qualified legal/tax advisers review obligations for the intended countries; this plan is not legal advice.
6. Update the public listing, support page, privacy page, terms page, release notes, and submission declarations to match the implemented behavior.

**Exit criteria:** public pages match the product and have been reviewed by the publisher; support and incident procedures are assigned.

### Stage E — Security and quality assurance

- [ ] Test successful payment, decline, cancellation, refund, dispute, renewal, expiration, and duplicate webhook.
- [ ] Test webhook spoofing, replay, missing signatures, wrong amount/currency, and out-of-order events.
- [ ] Test entitlement access for users who have not paid, cancelled, refunded, or lost access.
- [ ] Test account linking, authorization boundaries, rate limits, and abuse prevention.
- [ ] Ensure secrets are absent from Git history, logs, browser code, prompts, and release ZIP.
- [ ] Verify data minimization, retention/deletion, backup handling, and access logging.
- [ ] Test checkout and policy disclosures on desktop and mobile, with accessibility checks.
- [ ] Run package and platform validation against the exact release candidate.
- [ ] Conduct a final privacy, security, legal, and operational review.

**Exit criteria:** test evidence recorded; critical/high findings resolved or formally accepted by the responsible owner.

### Stage F — Release and monitoring

1. Assign a new semantic version only after scope and tests are approved.
2. Update root `plugin.json`, compatibility manifest, release notes, skill docs, public website, support instructions, privacy policy, and terms together.
3. Build and inspect the exact ZIP; scan for secrets, stale URLs, placeholders, unexpected files, and inconsistent version numbers.
4. Upload a draft in the official portal and inspect all imported metadata and required declarations.
5. Complete required scans, review checks, and truthful attestations; submit only when ready.
6. After approval, publish the approved release and verify the listing and payment journey.
7. Monitor payment failures, refunds, disputes, webhook failures, security events, support volume, and policy changes.
8. Maintain a rollback and payment-provider outage plan.

## 4. Operational ownership and runbooks

Before launch, assign an owner and escalation path for:

| Area | Required runbook |
| --- | --- |
| Payments | Reconcile provider transactions against entitlements and investigate mismatches |
| Refunds/cancellations | Verify request, execute action in provider, update entitlement, confirm with customer |
| Webhooks | Inspect event IDs and signatures, replay safely, reconcile delayed or duplicate events |
| Security incident | Contain affected credentials, assess exposure, preserve evidence, notify appropriate parties |
| Data request | Verify requester, locate relevant records, respond within applicable deadlines |
| Outage | Communicate status, stop unsafe retries, reconcile missed events, restore service |
| Release rollback | Disable affected paid feature, preserve required records, restore last known good version |

## 5. Risk register

| Risk | Mitigation |
| --- | --- |
| Unsupported commerce model | Confirm current OpenAI/platform rules before implementation |
| Fraudulent payment events | Server-side signature verification, idempotency, reconciliation |
| Unauthorized paid access | Server-side entitlement checks and authorization tests |
| Sensitive data exposure | Hosted checkout, data minimization, secret management, logging controls |
| Subscription/cancellation disputes | Clear checkout disclosures, simple cancellation, accurate receipts and support |
| Legal or tax non-compliance | Jurisdiction-specific review before targeting a country |
| Listing/policy mismatch | Versioned review of manifest, website, privacy notice, terms, and actual product |
| Provider outage | Retries with bounds, queueing, reconciliation, manual recovery runbook |

## 6. Required deliverables before a future commerce release

- [ ] Approved product/pricing and country scope
- [ ] Architecture and data-flow diagram
- [ ] Provider decision and configured sandbox account
- [ ] Backend integration and secure secret configuration
- [ ] Entitlement model and lifecycle tests
- [ ] Payment, refund, cancellation, dispute, and outage runbooks
- [ ] Updated website, support, privacy policy, and terms
- [ ] Legal/tax/security review notes
- [ ] QA evidence and release checklist
- [ ] Updated manifest declarations and release notes
- [ ] Verified submission ZIP and portal review results

## 7. Do not do these things

- Do not collect card numbers or payment credentials in chat prompts.
- Do not embed API keys or webhook secrets in a public repository or ZIP.
- Do not mark a user as paid based only on a success-page redirect.
- Do not imply that commerce is available in v1.0.1.
- Do not invent refund rules, prices, legal entities, governing law, or privacy practices.
- Do not submit unsupported commerce declarations or claim platform approval without evidence.

## 8. Action log

| Action | Owner | Status |
| --- | --- | --- |
| Defer commerce for v1.0.1 | Publisher | Confirmed by publisher on 2026-10-23 |
| Decide what is sold and payment location | Publisher | Deferred to future planning |
| Verify current platform rules for intended payment flow | Publisher/maintainer | Not started |
| Select provider and country scope | Publisher | Not started |
| Complete architecture, legal, privacy, and security review | Publisher/maintainer/advisers | Not started |
| Implement, test, and prepare future release | Maintainer | Not started |

