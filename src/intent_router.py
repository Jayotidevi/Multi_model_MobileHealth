"""Local mock intent classification and routing for Chapter 2."""

ALLOWED_INTENTS = {
    "routine_service_request",
    "resource_navigation",
    "dispatch_coordination",
    "potentially_urgent",
    "general_question",
    "unclear",
}


def classify_intent_mock(message):
    """Return a simple test classification without calling an AI model."""
    text = message.lower()

    # Safety-first routing: illustrative keywords, not a medical detector.
    urgent_terms = (
        "chest pain",
        "can't breathe",
        "cannot breathe",
        "severe bleeding",
        "unconscious",
    )
    if any(term in text for term in urgent_terms):
        return {"intent": "potentially_urgent", "confidence": 0.99}

    if any(term in text for term in ("allocate", "competing requests", "unit availability")):
        intent = "dispatch_coordination"
    elif any(term in text for term in ("clinic", "find a service", "available services")):
        intent = "resource_navigation"
    elif any(term in text for term in ("checkup", "health visit", "mobile health service")):
        intent = "routine_service_request"
    elif any(term in text for term in ("what is", "how does", "general question")):
        intent = "general_question"
    else:
        intent = "unclear"

    return {"intent": intent, "confidence": 0.80}


def route_request(classification):
    """Choose a route based on the classification and confidence."""
    intent = classification.get("intent", "unclear")
    confidence = classification.get("confidence", 0.0)

    if intent not in ALLOWED_INTENTS or not isinstance(confidence, (int, float)):
        return "human_review"

    if intent == "potentially_urgent":
        return "emergency_escalation"

    if confidence < 0.70 or intent == "unclear":
        return "human_review"

    if intent in {"routine_service_request", "general_question"}:
        return "simple_response"

    if intent in {"resource_navigation", "dispatch_coordination"}:
        return "planning_assistant"

    return "human_review"
