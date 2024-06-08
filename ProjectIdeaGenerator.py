import json
import random

class ProjectIdeaGenerator:
    def __init__(self, dataset_path):
        self.dataset = self.load_dataset(dataset_path)
        self.default_message = "Sorry. I'm not sure how to respond to that. Can you please rephrase?"

    def load_dataset(self, path):
        with open(path, 'r') as file:
            return json.load(file)

    def get_response(self, message):
        message = message.lower()
        for category in self.dataset:
            for key in self.dataset[category]:
                if key in message:
                    return random.choice(self.dataset[category][key])
        return self.default_message

    def create_training_file(self, output_path):
        with open(output_path, 'w') as file:
            for category in self.dataset:
                file.write(f"Category: {category}\n")
                for key, responses in self.dataset[category].items():
                    file.write(f"  Key: {key}\n")
                    for response in responses:
                        file.write(f"    Response: {response}\n")
                file.write("\n")

if __name__ == "__main__":
    bot = ProjectIdeaGenerator('dataset.json')
    bot.create_training_file('training_file.txt')
    print("Training file created successfully.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("PIG: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"PIG: {response}")
