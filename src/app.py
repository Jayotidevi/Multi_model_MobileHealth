"""Command-line demo for mobile health dispatch."""

from src.intent_router import classify_intent_mock, route_request
from src.mobile_health_dispatch import format_mock_response


def main():
    print("Mobile Health Unit Dispatch — Local Demo")
    print("Enter a sample request, or type 'quit' to exit.")

    while True:
        message = input("\nRequest: ").strip()

        if message.lower() in {"quit", "exit"}:
            print("Demo ended.")
            break

        try:
            classification = classify_intent_mock(message)
            route = route_request(classification)

            print("\nIntent:", classification["intent"])
            print("Confidence:", classification["confidence"])
            print("Route:", route)

            if route == "simple_response":
                response = format_mock_response(message)
                for heading, content in response.items():
                    print(f"{heading}: {content}")
            elif route == "planning_assistant":
                print("Planning assistant selected (mock; not implemented yet).")
            elif route == "emergency_escalation":
                print(
                    "Potential emergency: contact appropriate emergency "
                    "services and seek immediate human review."
                )
            else:
                print("Human review required before proceeding.")

        except ValueError as error:
            print("Input error:", error)


if __name__ == "__main__":
    main()
