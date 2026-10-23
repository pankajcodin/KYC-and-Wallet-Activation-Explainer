# Redbelly Access portal: on-screen text (evidence)

Source: the Redbelly Access portal's own JavaScript, https://access.redbelly.network/
Read by: pankajcodin, from the portal's public JS, on 23 October 2026.

| Entry | Where the text was read |
|---|---|
| E1 wallet limit | `index-25986869981a8ae9.js` (saved in this folder) and screenshot `e1-wallet-limit.png` |
| E2 verification messages | Screenshot `e2-approval-time.png` of the portal's code. This text is in a different JS file from the saved bundle. The file name is not recorded in the screenshot. |
| E3 button and screen labels | `index-25986869981a8ae9.js` (saved in this folder) |

Saved bundle: `index-25986869981a8ae9.js`
SHA-256: `4a128d38b556eeae044f703b1aba895f9ec7fa3d7872020c2d6038718d7db357`

Check it yourself: search the saved bundle for "Account allocation exhausted" (E1) and for the E3 labels. Search the portal's other JS files for "few minutes but in some (rare) cases" to find the E2 text.

## E1. Wallet limit

Code, as shown in the screenshot:

```js
onClick: () => F(),
children: "Link another wallet"
}), L.length >= Number("10") ? (0,
i.jsx)(d.A, {
  severity: "info",
  children: "Account allocation exhausted."
}) : null
```

What it shows:

- The portal compares the number of linked accounts (`L.length`) with 10.
- When the count is 10 or more, it shows an info message: "Account allocation exhausted."
- So the limit is 10 linked accounts per verified identity, set by the portal itself.

The Add another account button has its own condition in the same file: `I||L.length>=Number("10")||T?null:(...add-another-account-button...)`. So when 10 or more accounts are linked, the Add another account button is not rendered. The Link another wallet button is rendered separately.

## E2. Verification status messages

Code, as shown in the screenshot:

```js
c = function(e) {
  return e.PENDING = "Your identity is being verified by the accredited issuer. This could take a few minutes but in some (rare) cases it could take a few days. Please check again soon.",
  e.FAIL = "The issuer, Averer, was not able to verify your identity. You may need to reach out to Averer directly.",
  e.RETRY = "The issuer, Averer, is not yet able to verify your identity. You may need to resubmit some information. If you continue having trouble however, you may need to reach out to Averer directly.",
```

What it shows:

| State | Message |
|---|---|
| PENDING | Usually a few minutes, in rare cases a few days. Check again soon. |
| FAIL | Averer was not able to verify you. You may need to reach out to Averer directly. |
| RETRY | Averer is not yet able to verify you. You may need to resubmit some information. If it continues, reach out to Averer directly. |

Note: these are internal state names (PENDING, FAIL, RETRY) and message text. The screen titles and button labels for each state are in other parts of the code. Read them before you quote them.

## E3. Button and screen labels (Part C)

Each string was found in `index-25986869981a8ae9.js`.

| Label | Where it appears |
|---|---|
| Connect wallet | button, `children:"Connect wallet"` |
| Get access credential | screen title |
| Begin identity verification | button, `begin-identification-button` |
| I understand | checkbox label, and the button of the link wallet notice |
| Continue with Averer | button, `continue-with-averer-button` |
| Interacting with averer.co | window title |
| Identity verification pending | screen title |
| Check verification status | button |
| Identity verification incomplete | screen title for the retry state |
| Retry identity verification | button |
| Identity verification failed | screen title for the failed state |
| CONTACT AVERER | link |
| Account status: Enabled / Not enabled | status chip |
| Enable account | button |
| It seems you haven't received the RBNT yet, which you will need to enable you account. Please wait a few minutes and try again. | warning (the portal text has the typo "you account") |
| Add another account | button, `add-another-account-button` |
| Link another wallet | button, `link-another-wallet-button` |

Link another wallet notice: "To link another wallet to your verified identity, you must use the Dynamic widget in the top right corner of the dApp to connect the additional wallet." Warning: "By linking another wallet, you will be accountable for all the actions taken by that wallet on the network."

Averer notice: "The identity verification process will be managed by Averer, an accredited issuer on Redbelly Network." and "This data is not shared with, nor stored on, Redbelly Network."
