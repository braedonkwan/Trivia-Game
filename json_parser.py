import json


class Parser:
    def __init__(self, file_names):
        self.questions = []
        for file_name in file_names:
            file = self.load_data(file_name)
            for question in file["results"]:
                parsed = self.parse_question(question)
                if parsed not in self.questions:
                    self.questions.append(parsed)
        with open("questions.json", "w") as file:
            json.dump((self.questions), file, indent=4)

    def load_data(self, file_name):
        with open("data/" + file_name, "r") as file:
            return json.load(file)

    def parse_question(self, question):
        return {
            "category": question["category"],
            "difficulty": question["difficulty"],
            "question": question["question"],
            "correct_answer": question["correct_answer"],
            "incorrect_answers": question["incorrect_answers"],
        }


if __name__ == "__main__":
    FILE_NAMES = {
        "general_knowledge.json",
        "books.json",
        "film.json",
        "music.json",
        "television.json",
        "video_games.json",
        "science_&_nature.json",
        "sports.json",
        "geography.json",
        "history.json",
        "animals.json",
    }
    Parser(FILE_NAMES)
