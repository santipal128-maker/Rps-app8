from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RPSApp(App):
    def build(self):
        self.you = 0
        self.computer = 0

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.result = Label(
            text="Rock Paper Scissors\nFirst to 2 Wins!",
            font_size=22
        )

        self.score = Label(text="You: 0   Computer: 0", font_size=20)

        self.layout.add_widget(self.result)
        self.layout.add_widget(self.score)

        rock = Button(text="Rock")
        paper = Button(text="Paper")
        scissors = Button(text="Scissors")

        rock.bind(on_press=lambda x: self.play(1))
        paper.bind(on_press=lambda x: self.play(2))
        scissors.bind(on_press=lambda x: self.play(3))

        self.layout.add_widget(rock)
        self.layout.add_widget(paper)
        self.layout.add_widget(scissors)

        return self.layout

    def play(self, choice):
        com = random.randint(1, 3)
        names = {1: "Rock", 2: "Paper", 3: "Scissors"}

        if choice == com:
            msg = f"Computer: {names[com]}\nDraw!"
        elif (choice == 1 and com == 3) or \
             (choice == 2 and com == 1) or \
             (choice == 3 and com == 2):
            self.you += 1
            msg = f"Computer: {names[com]}\nYou Win!"
        else:
            self.computer += 1
            msg = f"Computer: {names[com]}\nComputer Wins!"

        self.result.text = msg
        self.score.text = f"You: {self.you}   Computer: {self.computer}"

        if self.you == 2:
            self.result.text += "\n🏆 You won the Best of 3!"
        elif self.computer == 2:
            self.result.text += "\n💻 Computer won the Best of 3!"

RPSApp().run()
