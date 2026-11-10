# GenLayer Portal: Projects submission for PageWitness, ready to paste

Form: Submit Contribution, Contribution Type "Builder", Category "Projects" (Project Explorer application).
Status: contract ready, app and contract address are filled in after deployment (see markers).

## 01 Identity

- Logo: upload `logo.png` from this project folder (1024 x 1024 PNG).
- Project Name: PageWitness
- Primary Tag: AI & Agents
- Tag 1 and Tag 2: choose the two options closest to "Oracles" and "Research" in the list that appears. If unsure, send a screenshot of the open list.

## 02 One-liner (max 100 characters)

Ask what a web page actually says, and get a consensus answer with the quote to prove it.

## 03 Description (max 1,000 characters)

PageWitness answers questions about what a public web page actually says, and stores the answer on chain only after GenLayer validators agree on it. Programs and marketplaces state their rules on web pages: eligibility, deadlines, prices, submission rules. Those pages change, and readers disagree about what they said. With PageWitness, anyone registers a page URL and one plain-language question. Resolving it fetches the live page and asks an LLM to answer using only what the page says, returning a short answer plus a verbatim quote from the page. A validator agrees only when its own reading reaches the same outcome, the leader's quote is found word for word in the validator's own copy of the page, and the two answers state the same fact. The result is a witnessed answer with its proof attached, usable for program rules, deadlines, and prices. The app asks, resolves, and reads questions directly from the deployed Studionet contract, with 8 passing tests and documentation in GitHub.

## 04 Demo video (optional)

Leave empty, or add later.

## 05 Write the exact path (how-to steps)

Step 1, heading: "Open the app and connect a wallet"
Instruction: "Open https://pagewitness.vercel.app and click Connect wallet. If the GenLayer Studionet network (chain 61999) is not in your wallet yet, the app offers to add it. Approve the connection."

Step 2, heading: "Register a question about a page"
Instruction: "Paste the public page URL and write one plain-language question about what the page says, for example a deadline, a requirement, or a price. Click Ask and confirm the transaction in your wallet."

Step 3, heading: "Resolve the question"
Instruction: "In the Questions list, click Answer this question and confirm in your wallet. Validators fetch the page and check the answer and its quote. Finalization can take a minute or more."

Step 4, heading: "Read the witnessed answer"
Instruction: "Reload the page. The question now shows the stored answer and the verbatim quote from the page that supports it, or the outcome unanswerable when the page does not contain the information."

## 06 Prove the path works

Expected verification outcome (max 500 characters):

After following the steps, the Questions list shows the question as answered. Its answer box shows the short answer and a quote that can be found word for word on the linked page. The same record is stored in the contract at 0xBBE090C5c5cCd8a93A899867DE41a5c13a8f628D on GenLayer Studionet and can be checked in the explorer link below and by calling get_query with the question id. Before any question is created, the counter at the top of the app reads the live total from the contract.

Contract link 1 (optional): https://explorer-studio.genlayer.com/address/0xBBE090C5c5cCd8a93A899867DE41a5c13a8f628D

## 07 Project links

- Website (required): https://pagewitness.vercel.app
- GitHub: https://github.com/0xsters/genlayer-pagewitness

## Evidence and Supporting Information

- Add Evidence, type "GitHub Repository": https://github.com/0xsters/genlayer-pagewitness-app
  (A separate app repository is used here, because a repository URL that was already submitted once is rejected by the portal. The 07 GitHub field above keeps the contract repository.)

Then tick "I'm not a robot" and click Submit Contribution.
