from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from functools import partial

import webbrowser


class ScreenAboutApp(Screen):
    Builder.load_string('''
<ScreenAboutApp>
    spacing: dp(9)
    name: 'ScreenAboutApp'
    ScrollView
        id: scroll
        BoxLayout
            orientation: 'vertical'
            BackLabel
                text: 'Sobre esse App'
                size_hint: 1, None
                height: dp(20)
                font_size:dp(18)
            BackLabel
                id: comm_desc
                spacing: dp(13)
            BoxLayout
                orientation: 'vertical'
                spacing: dp(13)
                ActiveButton
                    id: github
                    text: "Veja o Código-fonte"
                ActiveButton
                    id: contato
                    text: "Contato"

        ''')

    def on_pre_enter(self):
        self.ids.scroll.opacity = 0

    def on_enter(self, onsuccess=False):
        from network import get_data
        aboutapp = get_data('aboutapp', onsuccess=onsuccess)

        if not aboutapp:
            return

        aboutapp = aboutapp.get('0.0.1')[0]

        self.ids.contato.on_released = partial(webbrowser.open, aboutapp['contato'])
        self.ids.github.on_released = partial(webbrowser.open, aboutapp['github'])

        self.ids.comm_desc.text = aboutapp['aboutapp']
        self.ids.comm_desc.halign = 'left'

        Factory.Animation(opacity=1, d=.5).start(self.ids.scroll)
