import unittest

from src.mobile_health_dispatch import (
    format_mock_response,
    load_system_prompt,
    prepare_request,
)


class MobileHealthDispatchTests(unittest.TestCase):

    def test_system_prompt_loads(self):
        prompt = load_system_prompt()
        self.assertIn("Mobile Health Unit Dispatch Assistant", prompt)

    def test_request_is_prepared(self):
        request = prepare_request("  Request a routine mobile health visit  ")
        self.assertEqual(
            request["user_message"],
            "Request a routine mobile health visit",
        )
        self.assertIn("system_prompt", request)

    def test_empty_request_is_rejected(self):
        with self.assertRaises(ValueError):
            prepare_request("   ")

    def test_mock_response_has_required_sections(self):
        response = format_mock_response(
            "A resident needs a routine health checkup."
        )
        expected = {
            "Request Summary",
            "Service Need",
            "Urgency Indicators",
            "Missing Information",
            "Recommended Next Step",
            "Human Review Required",
        }
        self.assertEqual(set(response), expected)


if __name__ == "__main__":
    unittest.main()
