# KYC and Wallet Activation Explainer

A plain language guide to Redbelly KYC and wallet activation, written for the Redbelly DAO community. It answers the questions moderators get asked again and again, in one place, so people can link a single page.

Last verified: 23 October 2026.

## Quick answer

| Your situation | Redbelly KYC |
|---|---|
| I use Redbelly mainnet | Needed |
| I run a node and stake | Needed |
| I bridge RBNT onto mainnet | Verify first, you need an enabled wallet to use the coins |
| I hold RBNT on an exchange | Not needed |
| I hold wrapped RBNT on another chain | Not needed |
| I am a holder who wants to stake | Unconfirmed, no official page says |

Approval usually takes a few minutes, in rare cases a few days. One verified identity can link up to 10 wallets. The DAO is open to every region, and the network is not offered in 18 listed jurisdictions. These are two separate rules.

## What is inside

| File | What it is |
|---|---|
| `index.html` | The full guide, Parts A to D. This is the single source |
| `GUIDE.md`, `SOURCES.md`, `pin.txt` | Built from `index.html` by `scripts/build.py` |
| `img/decision-guide.png` and `.svg` | The Part A decision guide as an image |
| `evidence/` | Exact portal text from the portal code (E1, E2, E3), the saved bundle with its SHA-256, and screenshots |
| `KYC-and-Wallet-Activation-Explainer.pdf` | The guide as a PDF, built by `scripts/make_pdf.py` |
| `css/tokens.css` | Redbelly DAO brand tokens |
| `DEPLOY.md` | How to deploy on Vercel and what to run before each push |
| `scripts/check.py` | Checks dashes, emoji, source ids and that the pin matches the guide |

## Brand

Follows the Task Board brand kit at https://taskboard.redbellydao.network/brand: Be Vietnam Pro for text, JetBrains Mono only for machine values, the official colour tokens, the official logo, no em or en dashes, no emoji, and a dated last verified line.

## How the facts were checked

Official Redbelly and Averer pages, the Redbelly Access portal's own code (the wallet limit and the approval time message, saved in `evidence/`), the terms of service (clause 15 saved in `evidence/terms-clause-15.txt`), and the DAO vote on Snapshot.

## Known gaps

- Rejection reasons and an appeal route are not published.
- No official page covers staking for ordinary holders.
- Whether a bridge can deliver to a wallet that is not yet enabled is not published.

## Updating

```
python3 scripts/build.py
python3 scripts/check.py
```

If a step or a source no longer matches the live official page, open an issue or a pull request with the new official link.
