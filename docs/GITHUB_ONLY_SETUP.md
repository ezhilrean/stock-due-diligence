# GitHub-only static site and SEC refresh

This adds a separate static research site under `site/`; it does not replace the existing plugin site, manifests, skill, or MCP server. The MCP server remains in `mcp_server/` as a future integration path.

## What is included

- `site/index.html`: static research UI for company profile metadata, selected annual reported metrics, and recent SEC filings.
- `config/watchlist.json`: tickers included in the static dataset.
- `scripts/refresh_sec_data.py`: pulls public SEC company submissions and XBRL Company Facts.
- `.github/workflows/refresh-sec-data.yml`: weekday scheduled refresh and manual workflow dispatch; commits updated `site/data/research.json`.

The initial watchlist is AAPL, MSFT, NVDA, AMZN, GOOGL, META, and TSLA. Edit `config/watchlist.json` to change it.

## One-time GitHub setup

1. Open repository **Settings → Secrets and variables → Actions → Variables**.
2. Add a repository variable named `SEC_USER_AGENT`. Set its value to a descriptive application name and a real, monitored contact email, for example `StockDueDiligence contact@your-domain.example`. Replace the example with your real email. This is a contact identifier, not a secret.
3. Open **Actions → Refresh SEC EDGAR research data → Run workflow** to test the refresh.
4. Confirm that `site/data/research.json` was created or updated by the workflow.
5. Enable Pages at **Settings → Pages** and choose **Deploy from a branch**, then branch `main` and folder `/site`. If your repository uses a custom domain or a different Pages source, review its current setting first and do not overwrite the existing website's DNS/custom domain.
6. The website will be available at the repository's GitHub Pages URL, unless the Pages setting or custom domain points elsewhere.

## Scheduled refresh

The workflow runs at 12:20 UTC on weekdays (20:20 Singapore time). GitHub scheduled workflows can be delayed and are not guaranteed to run at an exact minute. You can also start it manually from the Actions tab.

## Important limitations

- This is a static website. It does not host or execute the Python MCP server.
- The dataset only covers the configured watchlist; it is not a full live company search or live market-price feed.
- The refresh depends on SEC public services and an accurate contact identifier. SEC rate limits and upstream outages can cause a run to fail.
- Financial concepts can differ by issuer. Values are displayed with the XBRL concept name and filing date; inspect the original filing before interpreting them.
- No login, saved notes, private reports, live prices, or trading features are included.
- To prepare a future MCP deployment, keep the Python service and Docker files in `mcp_server/`; later connect a verified HTTPS MCP endpoint without moving or replacing this static site.
