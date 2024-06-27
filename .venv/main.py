from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from display import Display
from keys import Keys

class Calculator(BoxLayout):
    pass

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()

