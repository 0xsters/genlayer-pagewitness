# GenLayer Portal submission, ready to paste

Form: Submit Contribution (portal.genlayer.foundation)

- Contribution Type: Builder
- Category: Intelligent Contracts
- Contribution Date: 11/10/2026
- Title: PageWitness: consensus-backed answers about what a web page says, with verbatim proof
- Evidence 1, type "GitHub Repository": https://github.com/0xsters/genlayer-pagewitness
- Evidence 2, type "GenLayer Explorer Contract": https://explorer-studio.genlayer.com/address/0xBBE090C5c5cCd8a93A899867DE41a5c13a8f628D

## Notes / Description (paste exactly, under the 1,000 character limit)

PageWitness is a GenLayer Intelligent Contract that answers questions about what a public web page actually says, with validator consensus and verbatim proof. Anyone registers a page URL and one plain-language question, for example a deadline, an eligibility rule, or a price. Resolving the question fetches the live page, and an LLM answers using only what the page says, returning a short answer plus a quote copied word for word from the page. The answer is stored only after validators agree through run_nondet_unsafe with a custom validator: the validator's own reading must reach the same outcome, the leader's quote must be found word for word in the validator's own copy of the page, and the two answers must state the same fact. It includes a prompt-injection guard, input validation, readable source, 8 passing direct tests, and full documentation, so builders can reuse it wherever a claim about a web page needs to be checkable.

## Verification evidence (already run locally)

- `genvm-lint check contracts/page_witness.py`: lint passed, validation passed, contract PageWitness, 4 methods (2 view, 2 write).
- `pytest tests/direct -v`: 8 passed.
