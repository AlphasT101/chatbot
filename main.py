# if you get this error : AttributeError: module 'time' has no attribute 'clock'
# then replace the required lines with time.perf_counter()

import os
from aiml import Kernel
import sys

pc_folder_windows = "E:/.vscode/chatbot/database"
aiml_folder = ""

folder_select = input("Enter 1 to select PC folder(windows): ")


if folder_select == "1" :
    aiml_folder = pc_folder_windows
else:
    print("FOLDER PATH ERROR")
    sys.exit()

class SimpleChatbot:
    def __init__(self):
        self.kernel = Kernel()

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
