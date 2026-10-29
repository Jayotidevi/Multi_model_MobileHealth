import unittest

from src.intent_router import classify_intent_mock, route_request


class IntentRouterTests(unittest.TestCase):

    def test_routine_request(self):
        result = classify_intent_mock("I need a routine health checkup.")
        self.assertEqual(result["intent"], "routine_service_request")
        self.assertEqual(route_request(result), "simple_response")

    def test_resource_navigation(self):
        result = classify_intent_mock("Help me find a clinic.")
        self.assertEqual(result["intent"], "resource_navigation")
        self.assertEqual(route_request(result), "planning_assistant")

    def test_dispatch_coordination(self):
        result = classify_intent_mock("We need to allocate one available unit.")
        self.assertEqual(result["intent"], "dispatch_coordination")
        self.assertEqual(route_request(result), "planning_assistant")

    def test_potential_emergency(self):
        result = classify_intent_mock("A person reports severe chest pain.")
        self.assertEqual(result["intent"], "potentially_urgent")
        self.assertEqual(route_request(result), "emergency_escalation")

    def test_low_confidence_goes_to_review(self):
        self.assertEqual(
            route_request({"intent": "dispatch_coordination", "confidence": 0.4}),
            "human_review",
        )

    def test_unknown_intent_goes_to_review(self):
        self.assertEqual(
            route_request({"intent": "unknown", "confidence": 0.99}),
            "human_review",
        )


if __name__ == "__main__":
    unittest.main()
