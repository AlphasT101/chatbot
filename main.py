import os
from aiml import Kernel

folder_select = int(input("Enter 1 to select laptop folder or enter 2 to select PC folder: "))
laptop_folder = "C:/Users/User/Documents/coding files/chatbot/database"
pc_folder = "E:/AlphasT101/coding files/chatbot/database"
aiml_folder = ""

if folder_select == 1:
    aiml_folder = laptop_folder
elif folder_select == 2:
    aiml_folder = pc_folder

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
