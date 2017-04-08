from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        is_inside = self.collide_point( *touch.pos )
        message = "Button {0} touch down. Pos {1}, is inside {2}."
        print(message.format(self.text, touch.pos, is_inside))

    def on_press(self):
        message = "Button {0} pressed."
        print(message.format(self.text))

def box_layout_td(text, instance, touch):
    is_inside = instance.collide_point( *touch.pos )
    message = "{0} BoxLayout touch down. Pos {1}, is inside {2}."
    print(message.format(text, touch.pos, is_inside))


def root_td(instance, touch):
    is_inside = instance.collide_point( *touch.pos )
    message = "Root BoxLayout touch down. Pos {0}, is inside {1}."
    print(message.format(touch.pos, is_inside))


def row1_td(instance, touch):
    is_inside = instance.collide_point( *touch.pos )
    message = "Row 1 BoxLayout touch down. Pos {0}, is inside {1}."
    print(message.format(touch.pos, is_inside))


def row2_td(instance, touch):
    is_inside = instance.collide_point( *touch.pos )
    message = "Row 2 BoxLayout touch down. Pos {0}, is inside {1}."
    print(message.format(touch.pos, is_inside))


class LayoutDemoApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        root.bind(on_touch_down=root_td)

        r1 = BoxLayout()
        button11 = MyButton(text='R1C1')
        button12 = MyButton(text='R1C2')
        r1.bind(on_touch_down=row1_td)

        r1.add_widget(button11)
        r1.add_widget(button12)

        r2 = BoxLayout()
        r2.bind(on_touch_down=row2_td)
        button21 = MyButton(text='R2C1')
        button22 = MyButton(text='R2C2')
        r2.add_widget(button21)
        r2.add_widget(button22)

        root.add_widget(r1)
        root.add_widget(r2)
        return root

if __name__ == '__main__':
    LayoutDemoApp().run()