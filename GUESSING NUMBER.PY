
import tkinter as tk
from tkinter import ttk
import random
import winsound


DIFFICULTIES = {
    "Easy": {"limit": 20, "attempts": 8},
    "Medium": {"limit": 50, "attempts": 7},
    "Hard": {"limit": 100, "attempts": 6}
}


class NumberGuessingGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Number Quest - Guessing Game")
        self.root.geometry("520x590")
        self.root.resizable(False, False)
        self.root.configure(bg="#101827")

        self.score = 0
        self.secret_number = 0
        self.attempts_left = 0
        self.max_attempts = 0
        self.game_over = False

        self.create_widgets()
        self.new_game()

    # WIN SOUND
    def play_win_sound(self):
        try:
            winsound.Beep(700, 150)
            winsound.Beep(900, 150)
            winsound.Beep(1100, 300)
        except RuntimeError:
            pass

    # LOSE SOUND
    def play_lose_sound(self):
        try:
            winsound.Beep(350, 350)
            winsound.Beep(250, 450)
        except RuntimeError:
            pass

    def create_widgets(self):
        tk.Label(
            self.root,
            text="NUMBER QUEST",
            font=("Arial", 25, "bold"),
            bg="#101827",
            fg="#38BDF8"
        ).pack(pady=(22, 4))

        tk.Label(
            self.root,
            text="Can you find the secret number?",
            font=("Arial", 11),
            bg="#101827",
            fg="#CBD5E1"
        ).pack(pady=(0, 18))

        tk.Label(
            self.root,
            text="CHOOSE DIFFICULTY",
            font=("Arial", 10, "bold"),
            bg="#101827",
            fg="#A5B4FC"
        ).pack()

        self.difficulty = ttk.Combobox(
            self.root,
            values=["Easy", "Medium", "Hard"],
            state="readonly",
            font=("Arial", 11),
            width=15
        )
        self.difficulty.set("Medium")
        self.difficulty.pack(pady=8)

        self.range_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            bg="#101827",
            fg="#CBD5E1"
        )
        self.range_label.pack(pady=5)

        self.score_label = tk.Label(
            self.root,
            text="Total Score: 0",
            font=("Arial", 12, "bold"),
            bg="#101827",
            fg="#FACC15"
        )
        self.score_label.pack(pady=8)

        self.attempts_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11, "bold"),
            bg="#101827",
            fg="#FB7185"
        )
        self.attempts_label.pack(pady=5)

        self.guess_entry = tk.Entry(
            self.root,
            font=("Arial", 18),
            justify="center",
            width=12,
            bg="#F8FAFC",
            fg="#111827",
            relief="flat"
        )
        self.guess_entry.pack(pady=12)
        self.guess_entry.bind(
            "<Return>", self.check_guess
        )

        self.guess_button = tk.Button(
            self.root,
            text="GUESS NUMBER",
            command=self.check_guess,
            font=("Arial", 11, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=20,
            pady=9
        )
        self.guess_button.pack(pady=5)

        self.message_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            bg="#101827",
            fg="#34D399",
            wraplength=430
        )
        self.message_label.pack(pady=18)

        self.new_button = tk.Button(
            self.root,
            text="NEW GAME / PLAY AGAIN",
            command=self.new_game,
            font=("Arial", 10, "bold"),
            bg="#059669",
            fg="white",
            activebackground="#047857",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=24,
            pady=9
        )
        self.new_button.pack(pady=4)

        tk.Label(
            self.root,
            text="Think smart. Guess right. Earn points!",
            font=("Arial", 9, "italic"),
            bg="#101827",
            fg="#94A3B8"
        ).pack(side="bottom", pady=12)

        self.difficulty.bind(
            "<<ComboboxSelected>>",
            self.new_game
        )

    def new_game(self, event=None):
        level = self.difficulty.get()
        settings = DIFFICULTIES[level]

        self.secret_number = random.randint(
            1, settings["limit"]
        )
        self.max_attempts = settings["attempts"]
        self.attempts_left = self.max_attempts
        self.game_over = False

        self.range_label.config(
            text=f"Guess a number from 1 to {settings['limit']}"
        )
        self.attempts_label.config(
            text=f"Chances left: {self.attempts_left}"
        )
        self.score_label.config(
            text=f"Total Score: {self.score}"
        )
        self.message_label.config(
            text="Your adventure starts now!",
            fg="#34D399"
        )

        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state="normal")
        self.guess_entry.focus_set()

    def check_guess(self, event=None):
        if self.game_over:
            return

        value = self.guess_entry.get().strip()

        try:
            guess = int(value)
        except ValueError:
            self.message_label.config(
                text="Enter a valid whole number!",
                fg="#FB7185"
            )
            return

        limit = DIFFICULTIES[
            self.difficulty.get()
        ]["limit"]

        if guess < 1 or guess > limit:
            self.message_label.config(
                text=f"Choose a number from 1 to {limit}.",
                fg="#FB7185"
            )
            return

        self.attempts_left -= 1
        self.attempts_label.config(
            text=f"Chances left: {self.attempts_left}"
        )
        self.guess_entry.delete(0, tk.END)

        if guess == self.secret_number:
            points = 100 + self.attempts_left * 10
            self.score += points
            self.score_label.config(
                text=f"Total Score: {self.score}"
            )
            self.message_label.config(
                text=(
                    f"YOU WON! Secret number: "
                    f"{self.secret_number}\n"
                    f"You earned {points} points!"
                ),
                fg="#34D399"
            )

            self.end_game()
            self.play_win_sound()

        elif self.attempts_left == 0:
            self.message_label.config(
                text=(
                    f"Game over! The number was "
                    f"{self.secret_number}.\n"
                    f"Press Play Again to try again."
                ),
                fg="#FB7185"
            )

            self.end_game()
            self.play_lose_sound()

        elif guess < self.secret_number:
            self.message_label.config(
                text="Too low! Try a BIGGER number.",
                fg="#FACC15"
            )

        else:
            self.message_label.config(
                text="Too high! Try a SMALLER number.",
                fg="#FACC15"
            )

    def end_game(self):
        self.game_over = True
        self.guess_button.config(state="disabled")
        self.guess_entry.config(state="disabled")


if __name__ == "__main__":
    window = tk.Tk()
    game = NumberGuessingGame(window)
    window.mainloop()
