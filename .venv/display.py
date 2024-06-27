from kivy.graphics import Line, Color
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import BooleanProperty,StringProperty

class Display(RelativeLayout):
    num1 = None
    num2 = None
    result = None

    unuse_op = None
    operate = None

    AC = BooleanProperty(False)
    calc = BooleanProperty(False)
    res_onscreen = BooleanProperty(True)

    def on_AC(self, *args):
        if self.AC == True:
            self.reset()
        self.AC = False

    def reset(self):
        self.num1 = None
        self.num2 = None
        self.operate = None
        self.clrscr()

    def clrscr(self):
        self.scr.text = ""

    def on_calc(self, *args):
        if self.calc == True:
            if self.num1 == None:
                self.num1 = float(self.scr.text)
                self.clrscr()

            if self.num1 != None and self.unuse_op != None and self.num2 == None:
# Always make sure the operator has been updated, or else do_calc with be trigger right away
                self.num2 = float(self.scr.text)
                self.clrscr()

# Update operator
            if self.unuse_op == None:
                self.unuse_op = self.operate

# Make calculation if all conditions are fulfilled
            if self.num1 != None and self.num2 != None:
                self.do_calc()
# Reset state of calculation
        self.calc = False

    def do_calc(self):
        num1 = self.num1
        num2 = self.num2

        if self.unuse_op == '/':
            self.result = num1 / num2
        if self.unuse_op == 'x':
            self.result = num1 * num2
        if self.unuse_op == '+':
            self.result = num1 + num2
        if self.unuse_op == '-':
            self.result = num1 - num2

        if self.operate != '=':
            self.unuse_op = self.operate
        else:
            self.unuse_op = None
        self.scr.text = str(self.result)
        self.res_onscreen = True

        self.num1 = self.result
        self.num2 = None


