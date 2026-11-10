import json


QUESTION = "What is the last day to submit a proposal?"
PAGE_BODY = (
    "<html><body><h1>Grant program</h1>"
    "<p>The last day to submit a proposal is March 15, 2027.</p>"
    "<p>Applications open on January 10, 2027.</p></body></html>"
)
ANSWER_JSON = json.dumps(
    {
        "outcome": "answered",
        "answer": "March 15, 2027",
        "quote": "The last day to submit a proposal is March 15, 2027.",
    }
)


def _deploy(direct_deploy):
    return direct_deploy("contracts/page_witness.py")


def _ask(contract):
    return contract.ask("https://example.com/grants", QUESTION)


def _mock_page_and_llm(direct_vm, llm_json):
    direct_vm.mock_web(
        r".*example\.com/grants.*",
        {"status": 200, "body": PAGE_BODY},
    )
    direct_vm.mock_llm(r".*page witness.*", llm_json)


def test_create_and_read(direct_vm, direct_deploy, direct_alice):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_alice

    query_id = _ask(contract)
    assert query_id == 0
    assert contract.total_queries() == 1

    record = json.loads(contract.get_query(0))
    assert record["page_url"] == "https://example.com/grants"
    assert record["question"] == QUESTION
    assert record["status"] == "open"
    assert record["outcome"] is None


def test_answer_answered(direct_vm, direct_deploy, direct_alice):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_alice
    _ask(contract)
    _mock_page_and_llm(direct_vm, ANSWER_JSON)

    contract.answer_query(0)

    record = json.loads(contract.get_query(0))
    assert record["status"] == "answered"
    assert record["outcome"] == "answered"
    assert record["answer"] == "March 15, 2027"
    assert record["quote"] == "The last day to submit a proposal is March 15, 2027."


def test_answer_unanswerable(direct_vm, direct_deploy, direct_bob):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_bob
    _ask(contract)
    _mock_page_and_llm(
        direct_vm,
        json.dumps({"outcome": "unanswerable", "answer": "", "quote": ""}),
    )

    contract.answer_query(0)

    record = json.loads(contract.get_query(0))
    assert record["status"] == "answered"
    assert record["outcome"] == "unanswerable"
    assert record["answer"] == ""


def test_ask_rejects_short_question(direct_vm, direct_deploy, direct_alice):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_alice

    with direct_vm.expect_revert("too short"):
        contract.ask("https://example.com/grants", "When?")


def test_ask_rejects_bad_url(direct_vm, direct_deploy, direct_alice):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_alice

    with direct_vm.expect_revert("must be an http"):
        contract.ask("ftp://example.com/grants", QUESTION)


def test_answer_unknown_query_reverts(direct_vm, direct_deploy, direct_alice):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_alice

    with direct_vm.expect_revert("Unknown query id"):
        contract.answer_query(999)


def test_get_unknown_query_reverts(direct_vm, direct_deploy, direct_alice):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_alice

    with direct_vm.expect_revert("Unknown query id"):
        contract.get_query(999)


def test_answer_twice_reverts(direct_vm, direct_deploy, direct_alice):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_alice
    _ask(contract)
    _mock_page_and_llm(direct_vm, ANSWER_JSON)

    contract.answer_query(0)

    with direct_vm.expect_revert("already answered"):
        contract.answer_query(0)
