# Public Website Deployment and DNS Setup

**Target domain:** `stock-due-diligence.chatgpt-plugin.developer.mesprk.com`  
**Repository:** [ezhilrean/stock-due-diligence](https://github.com/ezhilrean/stock-due-diligence)  
**Release branch:** `v1.0.1`  
**Submission branch:** `public-directory-submission_v1.0.1`  
**Hosting target:** GitHub Pages using the `site/` directory

## Current status

The developer confirmed on 2026-10-24 that all four public URLs below are accessible. The GitHub Pages workflow was also reported successful. This status is based on the developer's confirmation; recheck from a logged-out browser before each submission if anything changes.

The source and deployment workflow are in the repository. The workflow deploys the `site/` directory when site files change on branch `v1.0.1`, or when manually run. Changes to website source made only on `public-directory-submission_v1.0.1` will not automatically deploy under the current branch filter. If website source is changed on the submission branch, either merge/copy the approved change to `v1.0.1` or manually run the workflow from the intended branch after confirming Pages configuration.

## Pages and confirmed URLs

| Page | URL | Source file |
|---|---|---|
| Website | https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/ | `site/index.html` |
| Support | https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/support/ | `site/support/index.html` |
| Privacy policy | https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/privacy/ | `site/privacy/index.html` |
| Terms of service | https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/terms/ | `site/terms/index.html` |

The privacy and terms pages are draft language for publisher review, not legal advice. Confirm every statement against actual hosting, ChatGPT, GitHub, and service practices before relying on them. Commerce is deferred for v1.0.1; update all pages before introducing payments, subscriptions, accounts, analytics, or a backend.

## Deployment procedure

1. Open the repository on GitHub and select **Settings → Pages**.
2. Set the build/deployment source to **GitHub Actions**. The workflow at `.github/workflows/pages.yml` deploys the `site/` directory on the configured branch or when manually run.
3. Confirm that GitHub Actions is allowed to run and that the Pages deployment workflow completes successfully.
4. In **Settings → Pages**, confirm the custom domain is `stock-due-diligence.chatgpt-plugin.developer.mesprk.com`.
5. In the DNS control panel for `mesprk.com`, confirm the **CNAME** record:
   - **Name/host:** `stock-due-diligence.chatgpt-plugin.developer` (some DNS providers expect the full hostname)
   - **Target/value:** `ezhilrean.github.io`
   - **TTL:** provider default is fine
6. Do not create an A record for this subdomain unless GitHub's current Pages documentation specifically directs you to do so. Avoid conflicting CNAME/A/AAAA records at the same hostname.
7. In GitHub Pages settings, enable **Enforce HTTPS** when the option is available.
8. Test each URL in a private/logged-out browser. Verify no 404, access gate, certificate warning, placeholder, or repository-only page is shown.
9. Check navigation and stylesheet loading at the root and nested routes. Confirm the support link opens a public GitHub Issues page.
10. If any URL fails, fix it and re-test before using it in a listing.

## If deployment fails

- Review the Actions run log and confirm the workflow has `pages: write` and `id-token: write` permissions.
- Check the Pages settings source and the repository's Actions permissions.
- Confirm the DNS CNAME resolves to `ezhilrean.github.io` and that no conflicting records exist.
- Re-run the workflow after correcting the issue.
- If the custom domain is managed by another person/team, ask its DNS administrator to make the record change; do not share account passwords or tokens.

## Submission note

A successful GitHub commit or workflow run alone is not proof that the custom domain is reachable. In this project the developer has confirmed all four URLs accessible on 2026-10-24. Keep that claim time-bound and verify destinations again before submission.
