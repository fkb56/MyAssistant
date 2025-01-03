import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

from myassistant.openai_chat import model

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatBot:
    def __init__(self, engine: str = "gpt-3.5-turbo") -> None:
        self.model = engine
        self.conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]

    def send_message(self, message: str) -> str:
        assistant_response = ""
        self.conversation_history.append({"role": "user", "content": message})
        # Creates a completion for the provided prompt and parameters.
        try:
            response = client.chat.completions.create(model=self.model,
            messages=self.conversation_history)
            # Extract the generated response from the API response.
            assistant_response = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
        except openai.AuthenticationError as error:
            print("error: {0}".format(error.args))
        except openai.RateLimitError as error:
            print("error: {0}".format(error.args))
        except openai.InvalidRequestError as error:
            print("error: {0}".format(error.args))
        except openai.PermissionError as error:  # Occurred when you are not allowed to sample a model
            print("error: {0}".format(error.args))
        return assistant_response


def main():
    print("Welcome to ChatBot! Type 'quit' to exit.")
    chatbot = ChatBot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.send_message(user_input)
        print("ChatBot:", response)


if __name__ == "__main__":
    main()