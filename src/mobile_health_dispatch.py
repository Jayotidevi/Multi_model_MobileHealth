"""Single-model baseline for mobile health unit dispatch."""

from pathlib import Path

PROMPT_PATH = (
    Path(__file__).resolve().parent.parent
    / "prompts"
    / "mobile_health"
    / "system_prompt.md"
)


def load_system_prompt():
    """Load the project-specific system prompt."""
    return PROMPT_PATH.read_text(encoding="utf-8")


def prepare_request(user_message):
    """Prepare a request for a model; this function makes no API calls."""
    if not isinstance(user_message, str) or not user_message.strip():
        raise ValueError("Please provide a non-empty service request.")

    return {
        "system_prompt": load_system_prompt(),
        "user_message": user_message.strip(),
    }


def format_mock_response(user_message):
    """Return a deterministic placeholder for local testing only."""
    request = prepare_request(user_message)

    return {
        "Request Summary": request["user_message"],
        "Service Need": "Requires coordinator review",
        "Urgency Indicators": "Not assessed by the mock baseline",
        "Missing Information": "Confirm location, service, and availability",
        "Recommended Next Step": "Have a coordinator review the request",
        "Human Review Required": "Yes",
    }
