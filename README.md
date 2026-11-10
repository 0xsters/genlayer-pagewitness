# PageWitness

A GenLayer Intelligent Contract that answers questions about what a public web page actually says, with the answer decided by validator consensus and backed by a verbatim quote from the page.

## The problem

Programs, protocols, and marketplaces state their rules on web pages: eligibility requirements, deadlines, prices, submission rules. Those pages change, and readers disagree about what they said. A screenshot proves nothing, and one person's reading is just an opinion.

## What PageWitness does

Anyone can register a question about a public page:

- **Page URL**: the page whose statement matters.
- **Question**: one plain-language question, for example "What is the last day to submit a proposal?" or "How much GEN must a validator stake?"

When the question is resolved, the contract:

1. Fetches the live page with `gl.nondet.web.render`.
2. Asks an LLM to answer using only what the page says, returning a short answer plus a **verbatim quote** copied word for word from the page (`gl.nondet.exec_prompt` with a JSON response format).
3. Stores the answer only after validators agree through `gl.vm.run_nondet_unsafe` with a custom validator.

A validator agrees only when:

- Its own reading of the page reaches the same outcome (answered or unanswerable).
- The leader's quote is found **word for word** in the validator's own copy of the page.
- The leader's answer and the validator's answer state the same fact (exact match after normalization, or a comparative equivalence check on the two answers).

Prompt-injection guard: the question and the page are passed as data only, and the grading prompt instructs the model to never follow instructions found inside them.

## Contract interface

| Method | Type | Description |
| --- | --- | --- |
| `ask(page_url, question)` | write | Register a question about a page. Returns the query id. |
| `answer_query(query_id)` | write | Fetch the page and store the consensus answer and quote. |
| `get_query(query_id)` | view | Return one query record as a JSON string. |
| `total_queries()` | view | Return how many queries have been registered. |

Input rules: the URL must start with `http://` or `https://`; the question must be 10 to 500 characters. A query can be answered only once.

## Repository layout

- `contracts/page_witness.py`: the Intelligent Contract.
- `tests/direct/`: direct-mode tests (8 tests) using mocked web pages and LLM responses.
- `SUBMISSION.md`: the GenLayer Portal submission text.

## Run the tests

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/genvm-lint check contracts/page_witness.py
.venv/bin/python -m pytest tests/direct -v
```

If a direct test fails while downloading `genvm-universal.tar.xz` with an HTTP 404, that is a known packaging quirk of the test runner: run the lint command first (it downloads the same bundle under a versioned name into `~/.cache/genvm-linter/`), then copy that file into `~/.cache/gltest-direct/` under both names the runner asks for (`genvm-universal-v0.3.0-rc7.tar.xz` and `genvm-universal.tar.xz`) and rerun the tests.

## License

MIT
