
import tkinter as tk
from tkinter import ttk
import random
import winsound


DIFFICULTIES = {
    "Easy": {"limit": 20, "attempts": 8},
    "Medium": {"limit": 50, "attempts": 7},
    "Hard": {"limit": 100, "attempts": 6}
}


class NumberQuest:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Quest")
        self.root.geometry("520x610")
        self.root.resizable(False, False)
        self.root.configure(bg="#101827")

        self.player_name = ""
        self.score = 0
        self.secret_number = 0
        self.attempts_left = 0
        self.game_over = False

        self.welcome_screen()

    # ---------------- WELCOME SCREEN ----------------

    def welcome_screen(self):
        self.welcome = tk.Frame(
            self.root, bg="#101827"
        )
        self.welcome.pack(fill="both", expand=True)

        tk.Label(
            self.welcome,
            text="🎮",
            font=("Arial", 42),
            bg="#101827",
            fg="white"
        ).pack(pady=(55, 5))

        tk.Label(
            self.welcome,
            text="NUMBER QUEST",
            font=("Arial", 27, "bold"),
            bg="#101827",
            fg="#38BDF8"
        ).pack(pady=5)

        tk.Label(
            self.welcome,
            text="A fun number guessing adventure!",
            font=("Arial", 11),
            bg="#101827",
            fg="#CBD5E1"
        ).pack(pady=5)

        tk.Label(
            self.welcome,
            text="ENTER YOUR NAME",
            font=("Arial", 11, "bold"),
            bg="#101827",
            fg="#A5B4FC"
        ).pack(pady=(30, 8))

        self.name_entry = tk.Entry(
            self.welcome,
            font=("Arial", 15),
            justify="center",
            width=22,
            bg="#F8FAFC",
            fg="#111827"
        )
        self.name_entry.pack(pady=5)
        self.name_entry.bind(
            "<Return>", self.start_game
        )

        tk.Label(
            self.welcome,
            text="CHOOSE DIFFICULTY",
            font=("Arial", 10, "bold"),
            bg="#101827",
            fg="#A5B4FC"
        ).pack(pady=(18, 5))

        self.difficulty = ttk.Combobox(
            self.welcome,
            values=["Easy", "Medium", "Hard"],
            state="readonly",
            font=("Arial", 11),
            width=15
        )
        self.difficulty.set("Medium")
        self.difficulty.pack(pady=5)

        self.welcome_message = tk.Label(
            self.welcome,
            text="",
            font=("Arial", 10),
            bg="#101827",
            fg="#FB7185"
        )
        self.welcome_message.pack(pady=8)

        tk.Button(
            self.welcome,
            text="START GAME",
            command=self.start_game,
            font=("Arial", 12, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=20,
            pady=10
        ).pack(pady=12)

        tk.Label(
            self.welcome,
            text="Guess smart. Have fun!",
            font=("Arial", 10, "italic"),
            bg="#101827",
            fg="#94A3B8"
        ).pack(pady=10)

        self.name_entry.focus_set()

    # ---------------- START GAME ----------------

    def start_game(self, event=None):
        name = self.name_entry.get().strip()

        if not name:
            self.welcome_message.config(
                text="Please enter your name first!"
            )
            return

        self.player_name = name
        self.score = 0

        self.welcome.destroy()
        self.game_screen()
        self.new_game()

    # ---------------- GAME SCREEN ----------------

    def game_screen(self):
        self.game_frame = tk.Frame(
            self.root, bg="#101827"
        )
        self.game_frame.pack(
            fill="both", expand=True
        )

        tk.Label(
            self.game_frame,
            text="NUMBER QUEST",
            font=("Arial", 24, "bold"),
            bg="#101827",
            fg="#38BDF8"
        ).pack(pady=(20, 3))

        self.greeting_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 13, "bold"),
            bg="#101827",
            fg="#A5B4FC"
        )
        self.greeting_label.pack(pady=5)

        tk.Label(
            self.game_frame,
            text="Find the secret number!",
            font=("Arial", 11),
            bg="#101827",
            fg="#CBD5E1"
        ).pack(pady=4)

        self.range_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 11),
            bg="#101827",
            fg="#CBD5E1"
        )
        self.range_label.pack(pady=5)

        self.score_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 12, "bold"),
            bg="#101827",
            fg="#FACC15"
        )
        self.score_label.pack(pady=7)

        self.attempts_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 11, "bold"),
            bg="#101827",
            fg="#FB7185"
        )
        self.attempts_label.pack(pady=5)

        self.guess_entry = tk.Entry(
            self.game_frame,
            font=("Arial", 18),
            justify="center",
            width=12,
            bg="#F8FAFC",
            fg="#111827"
        )
        self.guess_entry.pack(pady=12)
        self.guess_entry.bind(
            "<Return>", self.check_guess
        )

        self.guess_button = tk.Button(
            self.game_frame,
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
            self.game_frame,
            text="",
            font=("Arial", 12, "bold"),
            bg="#101827",
            fg="#34D399",
            wraplength=440
        )
        self.message_label.pack(pady=15)

        tk.Button(
            self.game_frame,
            text="PLAY AGAIN",
            command=self.new_game,
            font=("Arial", 10, "bold"),
            bg="#059669",
            fg="white",
            activebackground="#047857",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=22,
            pady=8
        ).pack(pady=4)

        tk.Button(
            self.game_frame,
            text="CHANGE PLAYER",
            command=self.change_player,
            font=("Arial", 9),
            bg="#475569",
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=22,
            pady=7
        ).pack(pady=5)

    # ---------------- SOUND EFFECTS ----------------

    def play_win_sound(self):
        try:
            winsound.Beep(700, 150)
            winsound.Beep(900, 150)
            winsound.Beep(1100, 300)
        except RuntimeError:
            pass

    def play_lose_sound(self):
        try:
            winsound.Beep(350, 350)
            winsound.Beep(250, 450)
        except RuntimeError:
            pass

    # ---------------- NEW ROUND ----------------

    def new_game(self):
        level = self.difficulty.get()
        settings = DIFFICULTIES[level]

        self.secret_number = random.randint(
            1, settings["limit"]
        )
        self.attempts_left = settings["attempts"]
        self.game_over = False

        self.greeting_label.config(
            text=f"Welcome, {self.player_name}!"
        )
        self.range_label.config(
            text=f"Guess a number from 1 to {settings['limit']}"
        )
        self.score_label.config(
            text=f"Your Score: {self.score}"
        )
        self.attempts_label.config(
            text=f"Chances left: {self.attempts_left}"
        )
        self.message_label.config(
            text="Your adventure starts now!",
            fg="#34D399"
        )

        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state="normal")
        self.guess_entry.focus_set()

    # ---------------- CHECK GUESS ----------------

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
                text=f"Your Score: {self.score}"
            )
            self.message_label.config(
                text=(
                    f"YOU WON, {self.player_name}!\n"
                    f"Secret number: {self.secret_number}\n"
                    f"You earned {points} points!"
                ),
                fg="#34D399"
            )

            self.end_game()
            self.play_win_sound()

        elif self.attempts_left == 0:
            self.message_label.config(
                text=(
                    f"Game over, {self.player_name}!\n"
                    f"The number was {self.secret_number}."
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

    # ---------------- END GAME ----------------

    def end_game(self):
        self.game_over = True
        self.guess_button.config(state="disabled")
        self.guess_entry.config(state="disabled")

    # ---------------- CHANGE PLAYER ----------------

    def change_player(self):
        self.game_frame.destroy()
        self.welcome_screen()


if __name__ == "__main__":
    window = tk.Tk()
    game = NumberQuest(window)
    window.mainloop()
