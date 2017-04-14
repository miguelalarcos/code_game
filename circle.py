from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.graphics import *


class TestApp(App):
    def borrar(self, evt):
        #self.fl.canvas.remove(self.i1)
        self.circle.pos = (500, 0)
        self.circle.size = (10, 10)

    def build(self):
        self.fl = fl = FloatLayout()
        butt = Button(text='borrar', size_hint=(0.1,0.1))
        butt.bind(on_press=self.borrar)
        self.i1 = i1 = InstructionGroup()
        i1.add(Color(1., 0, 0))
        self.circle = circle = Ellipse(pos=(10, 10), size=(100, 100))
        i1.add(circle)
        fl.canvas.add(i1)

        fl.add_widget(butt)
        return fl

TestApp().run()

