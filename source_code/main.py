from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy_garden.mapview import MapView

# Just load our .kv design stuff right here
Builder.load_string(open('main.kv', 'r').read())


class HomePage(Widget):
    pass


class THE_APP(App):
    def build(self):
        return HomePage()


if __name__ == '__main__':
    THE_APP().run()
