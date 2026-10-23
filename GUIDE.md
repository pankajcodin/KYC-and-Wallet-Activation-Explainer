# KYC and Wallet Activation Explainer

Generated from index.html by scripts/build.py. Edit index.html, not this file.


## Two things people mix up

Native mainnet activity

Using an account on Redbelly Network itself. This needs identity verification and an enabled account [S12].

Wrapped or bridged RBNT on another chain

A token on a different network. It is not an account on Redbelly Network.

The DAO and the network have different regional rules. The DAO is open to every region [S9]. The network is not offered in the 18 jurisdictions in clause 15.1 of its terms [S3].


## Part A: Do I need KYC?

How to read the answers: Needed means an official source says so. Not needed means no page says it in those words, but it follows from an official rule that is named. Unconfirmed means no official page settles it.

| Your situation | Redbelly KYC | Reason |
|---|---|---|
| I use Redbelly mainnet (send, swap, use apps) | Needed | Every user must claim an access credential before the account gets write access [S12]. |
| I run a node and stake | Needed | Node operators must have network access for 2 accounts [S6]. Every node stakes 100,000 RBNT [S7]. |
| I bridge RBNT onto Redbelly mainnet | Needed | Once the coins arrive, moving or using them needs an enabled account [S12] [S13]. Whether a bridge can deliver to a wallet that is not yet enabled is unconfirmed, so verify first. |
| I hold RBNT on an exchange | Not needed | The rule is about write access to accounts on Redbelly Network [S12]. Gate and MEXC are listed as places to get RBNT [S13]. The exchange has its own KYC. |
| I hold wrapped or bridged RBNT on another chain | Not needed | The token lives on that chain, not on Redbelly Network [S12] [S13]. |
| I am an ordinary holder who wants to stake | Unconfirmed | The official staking pages describe node operators [S7]. Delegated staking is on the roadmap [S8]. No page states a rule for ordinary holders. |

The same table is in [decision-guide.png](img/decision-guide.png).


## Part B: The five common questions


### 1. When is KYC required, and when is it not?

KYC is required to use Redbelly mainnet. It is not required to hold RBNT on an exchange or on another chain.

Before an account can write to the network, its owner claims an access credential from an accredited issuer and then enables the account [S12]. The issuer for the official portal is Averer, and it covers the fees for network access [S2]. Holding RBNT outside Redbelly Network does not involve this process (Part A).


### 2. How many wallets can one verified identity cover?

Up to 10 wallets per verified identity. At 10 the portal shows "Account allocation exhausted."

After your first account is enabled, the portal lets you connect more accounts to the same identity, with a "Link another wallet" option [E1]. The portal compares your linked accounts with 10. When you reach 10, the Add another account button is no longer shown and the portal shows the message "Account allocation exhausted." [E1]

The limit is set by the Redbelly Access portal itself. No official page describes a way past it, so use one of the wallets you already have.


### 3. How long does approval take?

Usually a few minutes. In rare cases, a few days.

That is the portal's own wording while your verification is pending: "This could take a few minutes but in some (rare) cases it could take a few days. Please check again soon." [E2] If it is still pending after a few days, open a ticket with Averer (Part D).

For context, not as a promise: in January 2025 Redbelly said Averer had over 1.1 million sign-up requests in two weeks, and over 20 thousand tickets for incomplete documents [S5]. That was a peak. Send complete, readable documents the first time.


### 4. Can I join from my country?

You can join the DAO from any region. The network is not offered in 18 listed jurisdictions. These are two separate rules.

The DAO: open to every region

The DAO vote "Increase Governance Accessibility and Protect Contributor Privacy" closed on 5 July 2026. It asked to remove geographic restrictions for General DAO Members, and to keep the existing geographic limits for High Council Members and General DAO Leadership. Result: For 8,514,893, Against 5,983,785, Abstain 1,340,338 [S9].

The network: not offered in 18 places

Clause 15.1 of Redbelly's terms lists the jurisdictions. Clause 15.2 says tax residents of, or people located in, those places may not use the website, platform, software or tools [S3].

- Afghanistan
- Central African Republic
- Democratic People's Republic of Korea
- Democratic Republic of the Congo
- Guinea-Bissau
- Iran
- Iraq
- Lebanon
- Libya
- Myanmar
- Russia
- Somalia
- South Sudan
- Sudan
- Syria
- Ukraine
- Yemen
- Zimbabwe
The DAO vote changed the DAO's own membership rule. It did not change the network's terms, so joining the DAO does not give you network access from a listed jurisdiction. The terms define the Website to include access.redbelly.network, so Redbelly Access is covered by clause 15.2 [S3]. The exact clause text is saved in [evidence/terms-clause-15.txt](evidence/terms-clause-15.txt).


### 5. Is KYC needed to stake?

Needed for node operators. Unconfirmed for ordinary holders.

A node operator must have network access for 2 accounts [S6] and stake 100,000 RBNT, which can be slashed if the node acts maliciously [S7]. Staking is a transaction on Redbelly mainnet [S7], and only enabled accounts can write to the network [S12]. No official page states a rule for ordinary holders [S8].


## Part C: Get verified and activate your wallet

You do this once, at [access.redbelly.network](https://access.redbelly.network/) [S1]. The process covers wallet authentication, the KYC check and setting up the account's permission on the network [S4]. Button names are written as they appear in the portal [E3].

Before you start

- A wallet. The portal lists MetaMask and Coinbase Wallet [S2].
- A valid passport. The issuer checks a photo identity document with biometric checks [S12].
- Check that you are not a tax resident of, or located in, one of the 18 jurisdictions in question 4 [S3].
- No fee for access. The issuer covers it [S2].
1. Open the portal. Go to https://access.redbelly.network/ and check the address before you connect anything [S1].
2. Connect wallet. Press Connect wallet and approve the connection in your wallet [E3].
3. Begin identity verification. On the "Get access credential" screen, press Begin identity verification. The portal explains that Averer manages the check and that your documents are not shared with, nor stored on, Redbelly Network. Tick I understand, then press Continue with Averer [E3].
4. Submit your passport. A window titled "Interacting with averer.co" opens. Submit your passport and complete the biometric check [S12].
5. Wait for approval. The portal shows "Identity verification pending". Usually a few minutes, rarely a few days [E2]. Press Check verification status to refresh [E3].
6. Enable account. When you are approved, press Enable account and sign the transaction in your wallet. Before this the account shows "Account status: Not enabled", and after it shows "Account status: Enabled" [E3]. If the portal says "It seems you haven't received the RBNT yet", wait a few minutes and try again [E3].
7. Done. The account can now send transactions on Redbelly mainnet [S12].
If your wallet does not show the network, add it by hand [S14]:

| Field | Value |
|---|---|
| Network name | Redbelly Network Mainnet |
| RPC URL | https://governors.mainnet.redbelly.network |
| Chain ID | 151 |
| Currency symbol | RBNT |
| Block explorer | https://redbelly.routescan.io/ |

The portal also offers a Testnet account once your first account is enabled [S2]. Testnet is chain ID 153 and is separate from mainnet [S14].


### Add another wallet to your verified identity

1. Open the portal with a wallet that is already enabled. You do not verify again [S2].
2. In the Accounts section, press Add another account to add an account of the same wallet, or press Link another wallet for a different wallet [E1] [E3].
3. For Link another wallet, use the wallet widget in the top right corner of the portal to connect the additional wallet. By linking it, you become accountable for all the actions taken by that wallet on the network [E3].
4. Press Enable account for the new wallet. Each new wallet must be enabled before it can send transactions [S12].
5. You can link up to 10 wallets in total (question 2).
Safety

Never type your seed phrase or private key anywhere. Redbelly states that it will never intentionally gain access to or store private wallet keys [S3]. Averer's documentation says its design uses zero-knowledge proofs, so proof is shown without revealing the credential itself [S10].


## Part D: When something goes wrong

The portal sends identity problems to Averer [S2].


### Approval is taking too long

1. Press Check verification status. Most checks take a few minutes and rare ones a few days [E2].
2. Check that every document was complete and readable. Incomplete documents are checked by hand [S5].
3. If it is still pending after a few days, open an Averer ticket (below).

### Verification was not completed

| The portal says | What it means | What to do |
|---|---|---|
| "Identity verification incomplete": "The issuer, Averer, is not yet able to verify your identity. You may need to resubmit some information." [E2] | Retry state | Press Retry identity verification and resubmit the missing information. If it continues, open an Averer ticket. |
| "Identity verification failed": "The issuer, Averer, was not able to verify your identity. You may need to reach out to Averer directly." [E2] | Failed state | Press CONTACT AVERER, or open an Averer ticket and ask for the reason. |

Rejection reasons and an appeal route are not published. Do not resubmit the same documents again and again.


### The wallet limit is reached

At 10 linked accounts the Add another account button is no longer shown and the portal shows "Account allocation exhausted." [E1] No official page describes a way past it. Use one of your 10 wallets. If you think the count is wrong, open an Averer ticket and give your wallet address.


### The wallet will not connect or will not enable

Add the network by hand (Part C) and check that you are on mainnet and not testnet [S14]. If you see "It seems you haven't received the RBNT yet", wait a few minutes and try again [E3]. For help building on the network, Redbelly's support page points to its official Discord [S15].


### How to open a support ticket with Averer

1. Open Averer's support portal at [averer-help.freshdesk.com/support/home](https://averer-help.freshdesk.com/support/home) [S16].
2. Open the ticket form at [averer-help.freshdesk.com/support/tickets/new](https://averer-help.freshdesk.com/support/tickets/new) [S16]. Do not use the login page.
3. Fill in the five required fields: Full Name, Email Address, Subject, "What is your issue?" and Redbelly Wallet Address [S16]. In "What is your issue?", say what the portal screen shows, and in the wallet field give the address you used in Redbelly Access.
4. Use Attach files to add a screenshot of the portal screen if it helps, then submit the form [S16].
Never put a seed phrase or private key in a ticket. The form only asks for your wallet address [S16].

