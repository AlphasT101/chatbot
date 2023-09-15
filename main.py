import os
from aiml import Kernel

class SimpleChatbot:
    def __init__(self):
        self.kernel = Kernel()

        aiml_folder = "C:\AlphasT101\coding files\own_made_aiml_bot\database"  # Change this to the folder path where your AIML files are located

        # Load AIML files from the specified folder
        for file in os.listdir(aiml_folder):
            if file.endswith(".aiml"):
                aiml_file = os.path.join(aiml_folder, file)
                self.kernel.learn(aiml_file)

    def get_response(self, user_input):
        response = self.kernel.respond(user_input)
        return response

if __name__ == "__main__":
    chatbot = SimpleChatbot()

    print("Chatbot: Hi there! How can I help you? Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)
