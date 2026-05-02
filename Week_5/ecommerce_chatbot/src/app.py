from chatbot import create_chatbot

def main():
    print("🛍️ E-commerce Chatbot Ready!")
    print("Ask anything about products, orders, shipping, or return policy.\n")

    bot = create_chatbot()

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting chatbot. Goodbye!")
            break

        response = bot.run(query)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
