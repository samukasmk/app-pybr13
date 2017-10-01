from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
import webbrowser


class ScreenFeedback(Screen):
    Builder.load_string('''
<ScreenFeedback>
    name: 'ScreenFeedback'
''')
    def on_pre_enter(self):
        webbrowser.open('https://2017.pythonbrasil.org.br')

    def on_enter(self):
        app = App.get_running_app()
        app.go_back_in_history()
