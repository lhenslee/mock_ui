from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.metrics import inch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget


black = (0, 0, 0, 1)
white = (1, 1, 1, 1)
grey = (.8, .8, .8, 1)
Window.clearcolor = white
header_height = inch(.6)
row_height = inch(.4)
large_font = '20px'


class ColorWidget(Widget):
    rectangle = Rectangle()

    def __init__(self, background_color=grey, **kwargs):
        super(ColorWidget, self).__init__(**kwargs)
        with self.canvas:
            r, g, b, a = background_color
            Color(r, g, b, a)
            self.rectangle = Rectangle(size=self.size, pos=self.pos)

    def on_size(self, *args):
        self.rectangle.size = self.size

    def on_pos(self, *args):
        self.rectangle.pos = self.pos


class BlackLabel(Label):

    def __init__(self, **kwargs):
        kwargs['color'] = (0, 0, 0, 1)
        super(BlackLabel, self).__init__(**kwargs)


class Hamburger(Image):

    def __init__(self, **kwargs):
        kwargs['source'] = 'hamburger.png'
        kwargs['size_hint_x'] = None
        kwargs['width'] = header_height
        super(Hamburger, self).__init__(**kwargs)


class ShoppingCart(Image):

    def __init__(self, **kwargs):
        kwargs['source'] = 'shopping-cart.png'
        kwargs['size_hint_x'] = None
        kwargs['width'] = header_height
        super(ShoppingCart, self).__init__(**kwargs)
        
        
class Add(Image):
    
    def __init__(self, **kwargs):
        kwargs['source'] = 'plus.png'
        kwargs['size_hint'] = (None, None)
        kwargs['size'] = (row_height-10, row_height-10)
        super(Add, self).__init__(**kwargs)


class Header(BoxLayout, ColorWidget):

    def __init__(self, **kwargs):
        kwargs['height'] = header_height
        kwargs['size_hint_y'] = None
        kwargs['orientation'] = 'horizontal'
        super(Header, self).__init__(**kwargs)
        self.add_widget(Hamburger())
        self.add_widget(BlackLabel(text='A La QaRte', font_size=large_font))
        self.add_widget(ShoppingCart())


class MenuItem(BoxLayout):

    def __init__(self, title, price, **kwargs):
        kwargs['height'] = row_height
        kwargs['size_hint_y'] = None
        kwargs['orientation'] = 'horizontal'
        super(MenuItem, self).__init__(**kwargs)
        self.add_widget(BlackLabel(text=title, size_hint_x=.8))
        self.add_widget(BlackLabel(text=f'${price}', size_hint_x=.2))
        self.add_widget(Add())


class MenuHeader(BlackLabel):

    def __init__(self, **kwargs):
        kwargs['size_hint_y'] = None
        kwargs['height'] = header_height
        kwargs['font_size'] = large_font
        super(MenuHeader, self).__init__(**kwargs)


class MenuBody(BoxLayout):

    def __init__(self, **kwargs):
        kwargs['orientation'] = 'vertical'
        kwargs['size_hint_y'] = None
        kwargs['height'] = 0
        super(MenuBody, self).__init__(**kwargs)
        self.add_widget(MenuHeader(text='Lit Burgers'))
        self.add_widget(MenuItem('Western Burger', 12))
        self.add_widget(MenuItem('Steph Burger', 30))
        self.add_widget(MenuItem('Kobe Burger', 24))
        self.add_widget(MenuItem('Goku Burger', 9000))
        self.add_widget(MenuItem('Travis Scott Burger', 3500))
        self.add_widget(MenuItem('Hawaiian Burger', 12))
        self.add_widget(MenuItem('Huncho Burger', 10000))
        self.add_widget(MenuHeader(text='Salads'))
        self.add_widget(MenuItem('Steak Salad', 7))
        self.add_widget(MenuItem('Taco Salad', 9))
        self.add_widget(MenuItem('Fruit Salad', 9))
        self.add_widget(MenuItem('Chicken Salad', 6))

        for child in self.children:
            self.height += child.height


class Layout(BoxLayout):

    def __init__(self, **kwargs):
        kwargs['orientation'] = 'vertical'
        super(Layout, self).__init__(**kwargs)
        self.add_widget(Header())
        self.add_widget(MenuBody())
        self.add_widget(Widget())


class ALaQaRte(App):

    def build(self):
        return Layout()


ALaQaRte().run()

