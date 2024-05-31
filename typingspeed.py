import tkinter as tk
import random
import time

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes perfect.",
    "Coding is fun and challenging.",
    "Hello, World! This is a speed typing test.",
]

class SpeedTypingTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speed Typing Test")
        self.geometry("600x400")

        self.sentence_label = tk.Label(self, text="", wraplength=500)
        self.sentence_label.pack(pady=20)

        self.input_entry = tk.Entry(self, width=50)
        self.input_entry.pack(pady=10)

        self.start_button = tk.Button(self, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.results_label = tk.Label(self, text="")
        self.results_label.pack(pady=20)

        self.current_sentence = ""
        self.start_time = 0
        self.is_test_running = False

    def start_test(self):
        if not self.is_test_running:
            self.current_sentence = random.choice(SENTENCES)
            self.sentence_label.config(text=self.current_sentence)
            self.input_entry.delete(0, tk.END)
            self.start_time = time.time()
            self.input_entry.focus()
            self.is_test_running = True
            self.start_button.config(text="Stop")
            self.results_label.config(text="")

        else:
            self.calculate_results()
            self.is_test_running = False
            self.start_button.config(text="Start")

    def calculate_results(self):
        typed_text = self.input_entry.get()
        elapsed_time = time.time() - self.start_time
        words_per_minute = len(typed_text.split()) / (elapsed_time / 60)
        accuracy = self.calculate_accuracy(typed_text)

        results_text = f"Time: {elapsed_time:.2f} seconds\n"
        results_text += f"Speed: {words_per_minute:.2f} words per minute\n"
        results_text += f"Accuracy: {accuracy:.2f}%"
        self.results_label.config(text=results_text)

    def calculate_accuracy(self, typed_text):
        correct_chars = sum(a == b for a, b in zip(self.current_sentence, typed_text))
        total_chars = len(self.current_sentence)
        return (correct_chars / total_chars) * 100

if __name__ == "__main__":
    app = SpeedTypingTest()
    app.mainloop()