# Stock Due Diligence — SEC EDGAR MCP server

This service exposes read-only Model Context Protocol tools backed by the U.S. SEC's public EDGAR datasets. It does not execute trades, place orders, or provide market prices.

## Tools

- `sec_search_company(query)`: find candidate companies and CIKs by ticker/name.
- `sec_get_company_profile(ticker_or_cik)`: retrieve SEC submissions profile metadata.
- `sec_get_recent_filings(ticker_or_cik, form_types)`: list recent filing metadata and primary document links.
- `sec_get_company_facts(ticker_or_cik, metric_names)`: retrieve selected annual US-GAAP XBRL facts with period, filing date, unit, and accession number.

## Deploy on Render (recommended simple hosted option)

1. Push this branch to GitHub and open a pull request into `main`; review and merge it when ready.
2. In Render, choose **New → Blueprint** and connect this repository. Select the `mcp_server/render.yaml` blueprint path if prompted.
3. Set `SEC_USER_AGENT` to a descriptive app name plus a monitored contact email, e.g. `StockDueDiligence support@example.com`. Use your real support email; do not put a secret or API key here.
4. Deploy the service. Render will assign a public HTTPS hostname. The MCP endpoint is normally `/mcp`; verify it in the Render logs and with an MCP client before configuring the plugin.
5. Add a health endpoint if the chosen host requires it; current server health is exposed by the MCP SDK's HTTP app only if the SDK maps `/health`. Confirm in deployment logs. Do not assume a green deploy means the MCP protocol has been tested.
6. After deployment, add the verified HTTPS endpoint to the plugin's MCP configuration and public-submission package. Never add a placeholder endpoint.

## Local run

Python 3.12+ recommended.

```bash
cd mcp_server
python -m venv .venv
# activate the virtual environment
pip install -r requirements.txt
export SEC_USER_AGENT='StockDueDiligence your-real-contact@example.com'
python server.py
```

The MCP server uses Streamable HTTP. Confirm the exact endpoint path with your MCP client/SDK version.

## SEC usage and safeguards

- The service uses public SEC endpoints and needs no API key.
- `SEC_USER_AGENT` is required so requests identify the application and a contact.
- SEC data are company-submitted disclosures; this service does not independently audit them.
- Company/ticker matching can be ambiguous. Use the exact CIK from `sec_search_company` when needed.
- XBRL concepts and units vary by issuer. Always inspect the linked filing and concept metadata before interpreting values.
- Annual facts are selected from 10-K submissions; amendments, special cases, and non-US GAAP reporting may require further review.
- This is an initial read-only implementation. It does not yet perform legal-case searches, cyber incident research, market-price retrieval, fair-value modeling, authentication, persistence, or personalized investment advice.
- Add observability, request throttling, automated tests, and production deployment checks before relying on this service for broad public use.
