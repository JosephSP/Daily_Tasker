from kivy import platform
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
import sqlite3


class MainGuiApp(App):
    headers = ["Prioridad", "Actividad", ""]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWidget(Widget):
    pass

MainGuiApp().run()