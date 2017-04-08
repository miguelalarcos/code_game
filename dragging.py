# from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

v = None
w = None
pos = None
dragging = False

class MyButton(Button):
    def on_touch_move(self, touch):
        global pos
        if self.collide_point(*touch.pos) and dragging:
            self.background_color = [0, 1, 0, 1]
            p = [c for c in self.parent.children if c != w].index(self)
            if touch.pos[1] > self.pos[1] + self.size[1]/2.:
                p += 1
            if p != pos:
                print(p)
                v.remove_widget(w)
                v.add_widget(w, index=p)
                print('setting widget at pos', p)
                pos = p
        else:
            self.background_color = [.5, .5, .5, 1]


class MyWidget(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            #print(self.parent.children.index(self))
            touch.grab(self)
            self.deltax = 0#touch.pos[0]
            self.deltay = 0#touch.pos[1]
            global v, w, dragging
            #v.remove_widget(w)
            dragging = True

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            x = touch.pos[0] - self.deltax
            y = touch.pos[1] - self.deltay
            self.pos = (x, y)

    def on_touch_up(self, touch):
        global pos, dragging
        if touch.grab_current is self:
            touch.ungrab(self)
            v.remove_widget(w)
            v.add_widget(w, index=pos)
            dragging = False


class TestApp(App):
    def build(self):
        global v, w
        h = BoxLayout()
        v = BoxLayout(orientation='vertical')
        h.add_widget(v)
        h.add_widget(MyButton(text='Drop here'))
        w = MyWidget(text='Drag me!')
        v.add_widget(w)
        v.add_widget(MyButton(text='Drop here'))
        v.add_widget(MyButton(text='Drop here'))
        v.add_widget(MyButton(text='Drop here'))
        return h

TestApp().run()