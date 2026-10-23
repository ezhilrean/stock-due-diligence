# Public Website Deployment and DNS Setup

**Target domain:** `stock-due-diligence.chatgpt-plugin.developer.mesprk.com`  
**Repository:** [ezhilrean/stock-due-diligence](https://github.com/ezhilrean/stock-due-diligence)  
**Branch:** `v1.0.1`  
**Hosting target:** GitHub Pages using the `site/` directory

## Current status

The static website, support page, privacy notice, terms draft, CSS, custom-domain file, and GitHub Actions deployment workflow are committed to branch `v1.0.1`. They are **not confirmed live** yet. DNS and GitHub Pages settings require access to the repository settings and the DNS zone for `mesprk.com`. Do not claim the public URLs are accessible until you test them from a logged-out browser.

## Pages included

| Page | Intended URL | Source file |
|---|---|---|
| Website | `https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/` | `site/index.html` |
| Support | `https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/support/` | `site/support/index.html` |
| Privacy policy | `https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/privacy/` | `site/privacy/index.html` |
| Terms of service | `https://stock-due-diligence.chatgpt-plugin.developer.mesprk.com/terms/` | `site/terms/index.html` |

The privacy and terms pages are draft language for publisher review, not legal advice. Confirm the statements against actual hosting, ChatGPT, GitHub, and future service practices before relying on them. Commerce is deferred for v1.0.1; update all pages before introducing payments, subscriptions, accounts, analytics, or a backend.

## Deployment procedure

1. Open the repository on GitHub and select **Settings → Pages**.
2. Set the build/deployment source to **GitHub Actions**. The workflow at `.github/workflows/pages.yml` deploys the `site/` directory when files under `site/` change on branch `v1.0.1`, or when manually run.
3. Confirm that GitHub Actions is allowed to run and that the Pages deployment workflow completes successfully.
4. In **Settings → Pages**, set the custom domain to `stock-due-diligence.chatgpt-plugin.developer.mesprk.com` if GitHub has not picked it up from `site/CNAME`.
5. In the DNS control panel for `mesprk.com`, create a **CNAME** record:
   - **Name/host:** `stock-due-diligence.chatgpt-plugin.developer` (some DNS providers expect the full hostname)
   - **Target/value:** `ezhilrean.github.io`
   - **TTL:** provider default is fine
6. Do not create an A record for this subdomain unless GitHub's current Pages documentation specifically directs you to do so. Avoid conflicting CNAME/A/AAAA records at the same hostname.
7. Wait for DNS propagation. In GitHub Pages settings, enable **Enforce HTTPS** when the option becomes available.
8. Test each of the four URLs in a private/logged-out browser. Verify that no 404, access gate, certificate warning, placeholder, or repository-only page is shown.
9. Check navigation and stylesheet loading at the root and nested routes. Confirm the support link opens a public GitHub Issues page.
10. Only after all URLs are live and verified should they be treated as complete listing URLs for submission.

## If deployment fails

- Review the Actions run log and confirm that the workflow has `pages: write` and `id-token: write` permissions.
- Check the Pages settings source and the repository's Actions permissions.
- Confirm that the DNS CNAME resolves to `ezhilrean.github.io` and that no conflicting records exist.
- Re-run the workflow after correcting the issue.
- If the custom domain is managed by another person/team, ask its DNS administrator to make the record change; do not share account passwords or tokens.

## Submission note

A successful GitHub commit or workflow run is not proof that the custom domain is reachable. The public plugin directory requires the actual URLs to be accessible and to serve their stated purpose. Verify all destinations before uploading the final plugin ZIP.
