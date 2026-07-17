from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.display = TextInput(font_size=32, multiline=False)
        self.add_widget(self.display)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        grid = GridLayout(cols=4)

        for text in buttons:
            btn = Button(text=text, font_size=24)
            btn.bind(on_press=self.on_button)
            grid.add_widget(btn)

        self.add_widget(grid)

    def on_button(self, instance):
        text = instance.text
        if text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += text

class CalculatorApp(App):
    def build(self):
        return Calculator()

CalculatorApp().run()
