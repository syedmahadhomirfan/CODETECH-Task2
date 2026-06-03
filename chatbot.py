import re

RESPONSES = [
    (r"\b(hours|open|closing|close|schedule)\b",
     "We're open from 9 AM to 6 PM, Monday to Friday. If you need weekend hours, please ask."),
    (r"\b(refund|return|money back|cancel)\b",
     "You can request a refund within 30 days of purchase. I can also help with return status if you provide your order number."),
    (r"\b(contact|support|help|email|phone)\b",
     "You can reach our support team at support@example.com or call +1-800-123-4567."),
    (r"\b(price|cost|payment|pricing)\b",
     "Our pricing varies by product and plan. Please visit our website for the latest pricing or ask me about a specific item."),
    (r"\b(order|shipping|delivery|track)\b",
     "For order and shipping updates, I can help with tracking status, delivery times, and shipping options."),
    (r"\b(account|login|password|signup|register)\b",
     "I can help with account issues like login, password reset, and registration."),
    (r"\b(thank|thanks|appreciate|goodbye|bye)\b",
     "You're welcome! If you need anything else, just ask."),
]

DEFAULT_RESPONSE = (
    "I'm sorry, I didn't understand that. "
    "Try asking about hours, refunds, contact, pricing, order status, or account support."
)


def chatbot_response(user_input: str) -> str:
    normalized = user_input.strip().lower()
    if not normalized:
        return "Please type your question so I can help."

    for pattern, response in RESPONSES:
        if re.search(pattern, normalized):
            return response

    return DEFAULT_RESPONSE


def is_exit_command(user_input: str) -> bool:
    return re.search(r"\b(quit|exit|bye|goodbye)\b", user_input.strip().lower()) is not None


if __name__ == "__main__":
    print("Customer Service Chatbot — Professional mode")
    print("Type a question or 'quit' to exit.")

    while True:
        user = input("You: ")
        if is_exit_command(user):
            print("Bot: Goodbye! Have a pleasant day.")
            break
        print("Bot:", chatbot_response(user))
