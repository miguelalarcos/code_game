from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

ancla = None
widget = None

class DragButton(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            global widget
            widget = self
            self.deltax = 0  # touch.pos[0]
            self.deltay = 0  # touch.pos[1]

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            x = touch.pos[0] - self.deltax
            y = touch.pos[1] - self.deltay
            self.pos = (x, y)
        elif self.collide_point(*touch.pos):
            self.background_color = [0, 1, 0, 1]
            global ancla
            if widget is not self:
                ancla = self
        else:
            self.background_color = [.5, .5, .5, 1]

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            global ancla, widget
            if ancla:
                self.pos = (ancla.pos[0], ancla.pos[1] - self.size[1])
                ancla = None
                widget = None



class TestApp(App):
    def build(self):
        layout = FloatLayout()
        b1 = DragButton(text='DB 1', size_hint=(0.2,0.1))
        b2 = DragButton(text='DB 2', size_hint=(0.1,0.2))
        layout.add_widget(b1)
        layout.add_widget(b2)
        return layout

TestApp().run()