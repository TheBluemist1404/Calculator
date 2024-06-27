from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import RoundedRectangle, Color, Line
from kivy.properties import ListProperty, StringProperty


class Keys(StackLayout):
    pass

class CustomWidget(AnchorLayout):
    # Define properties
    text_content = StringProperty('Default Text')
    text_color = ListProperty([1, 1, 1, 1])  # Default: white text color
    background_color = ListProperty([0.2, 0.6, 0.8, 1])  # Default: blue background color

    def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs)
        # Add a Label widget
        self.init_color = None
        self.label = Label()
        self.add_widget(self.label)

        # Bind properties to update widget appearance
        self.bind(text_content=self.update_text)
        self.bind(text_color=self.update_color)
        self.bind(background_color=self.update_background)
        self.bind(size=self.update_background, pos=self.update_background)
        self.bind(size=self.update_label, pos=self.update_label)


    def update_text(self, *args):
        self.label.text = self.text_content

    def update_color(self, *args):
        self.label.color = self.text_color

    def update_background(self, *args):
        self.canvas.before.clear()
        if self.init_color == None:
            self.init_color = self.background_color
        with self.canvas.before:
            # Unpack the background_color list into separate arguments
            Color(*self.background_color)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[self.height/2])

    def update_label(self, *args):
        self.label.size = self.size
        self.label.pos = self.pos
        self.label.font_size = self.height/2.5
        self.label.font_name = 'Roboto-Regular.ttf'

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.change_color()
            self.parent.display.scr.text += self.text_content
            if self.parent.display.res_onscreen == True:
                self.parent.display.scr.text = self.text_content
                self.parent.display.res_onscreen = False

    def change_color(self):
        self.background_color = (.5,.5,.5,1)

    def on_touch_up(self, touch):
        self.reset_color()

    def reset_color(self):
        self.background_color = self.init_color

class ACWidget(CustomWidget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.change_color()
            self.AC()

    def AC(self, *args):
        self.parent.display.AC = True

class NegWidget(CustomWidget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
# We will indeed use exception handle here, but not for now
            self.change_color()
            text = self.parent.display.scr.text
            if text[0] == '-':
                self.parent.display.scr.text = text[1:]
            else:
                self.parent.display.scr.text = "-"+text

class PercentWidget(CustomWidget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
# We will indeed use exception handle here, but not for now
            self.change_color()
            text = self.parent.display.scr.text
            value = float(text)
            value /= 100
            self.parent.display.scr.text = str(value)

class ZeroWidget(CustomWidget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.change_color()
            if self.parent.display.scr.text != "":
                self.parent.display.scr.text = self.parent.display.scr.text+'0'
            if self.parent.display.res_onscreen == True:
                self.parent.display.scr.text = ""
                self.parent.display.res_onscreen = False

class DotWidget(CustomWidget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.change_color()
            text = self.parent.display.scr.text
            if  text == "":
                self.parent.display.scr.text = self.parent.display.scr.text+'0.'
            elif text.count('.') == 1:
                print("too many dots")
            else:
                self.parent.display.scr.text = self.parent.display.scr.text + '.'
            if self.parent.display.res_onscreen == True:
                self.parent.display.scr.text = "0."
                self.parent.display.res_onscreen = False

class Operators(CustomWidget):
    def __init__(self, **kwargs):
        super(Operators,self).__init__(**kwargs)


    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.change_color()
            self.parent.display.operate = self.text_content
            self.parent.display.calc = True
        else:
            self.reset_color()

    def on_touch_up(self, touch):
        pass

class EqWidget(CustomWidget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.change_color()
            self.parent.display.operate = self.text_content
            self.parent.display.calc = True
