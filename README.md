# Simple Rule-Based Chatbot

A lightweight Python command-line chatbot that replies to basic customer service queries using keyword matching.

## Features

- Recognizes common topics such as business hours, refunds, support contact, pricing, order/shipping, and account issues
- Uses a simple rule list with regular expression matching for flexible keyword detection
- Runs interactively in the terminal until the user types `quit`, `exit`, `bye`, or `goodbye`
- No external dependencies required

## Requirements

- Python 3.7 or later

## Usage

From the folder containing `chatbot.py`, run:

```bash
python chatbot.py
```

Then type a message and press Enter. Example queries:

- `What are your hours?`
- `How do I request a refund?`
- `How can I contact support?`
- `What is your pricing?`

Type `quit`, `exit`, `bye`, or `goodbye` to exit the chatbot.

## How it works

The bot is driven by the `RESPONSES` list inside `chatbot.py`.
Each entry contains a regular expression pattern and a corresponding response.
The first matching rule is returned, or the default fallback message is shown if no pattern matches.

## Customization

To add or update responses, edit `chatbot.py` and modify the `RESPONSES` list.

Example entry:

```python
(r"\b(shipping|delivery|track)\b",
 "For order and shipping updates, I can help with tracking status, delivery times, and shipping options.")
```

You can also customize the default fallback reply by updating `DEFAULT_RESPONSE`.

## Example session

```text
Customer Service Chatbot — Professional mode
Type a question or 'quit' to exit.
You: What are your hours?
Bot: We're open from 9 AM to 6 PM, Monday to Friday. If you need weekend hours, please ask.
You: How do I get a refund?
Bot: You can request a refund within 30 days of purchase. I can also help with return status if you provide your order number.
You: quit
Bot: Goodbye! Have a pleasant day.
```

## Extension ideas

- Add more intent patterns and responses
- Use a natural language processing library for intent classification
- Persist conversation history to a log file
- Build a web or messenger interface around the chatbot
