def get_bot_reply(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message or "hey" in message:
        return "Hello! 👋 Welcome to DRABZ. How can I help you with your trading education?"

    if "forex" in message:
        return "Forex is the foreign exchange market, where currencies are traded. Check Lesson 1: Introduction to Forex to learn the basics."

    if "risk" in message:
        return "Risk management helps traders control how much they could lose on a trade. Never risk money you cannot afford to lose."

    if "buy" in message:
        return "A Buy trade means you are taking a position expecting the price to rise."

    if "sell" in message:
        return "A Sell trade means you are taking a position expecting the price to fall."

    if "lesson" in message:
        return "You can find your trading lessons on the Lessons page. Start with Lesson 1: Introduction to Forex."

    if "drabz" in message:
        return "DRABZ is a trading education platform created to help people learn trading fundamentals before putting real money at risk."

    if "help" in message:
        return "I can help with basic Forex concepts, Buy/Sell, risk management, and finding lessons on DRABZ."

    return "I'm still learning. Try asking me about Forex, risk management, Buy, Sell, or DRABZ."
