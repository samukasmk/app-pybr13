from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from functools import partial

import webbrowser


class ScreenCoC(Screen):
    Builder.load_string('''
<ScreenCoC>
    spacing: dp(9)
    name: 'ScreenCoC'
    ScrollView
        id: scroll
        ScrollGrid
            BackLabel
                text: 'Código de Conduta do Evento Python Brasil'
                size_hint: 1, None
                height: dp(20)
                font_size:dp(18)
            BackLabel
                id: comm_desc
            FloatLayout
                size_hint_y: None
                height: dp(45)
                ActiveButton
                    id: but
                    text: "Consulte online"
                    size_hint: None, None
                    width: dp(200)
                    center_x: comm_desc.center_x
                    top: comm_desc.y - dp(10)
        ''')

    def on_pre_enter(self):
        self.ids.scroll.opacity = 0

    def on_enter(self, onsuccess=False):
        from network import get_data
        coc = get_data('coc', onsuccess=onsuccess)

        if not coc:
            return

        coc = coc.get('0.0.1')[0]

        self.ids.but.on_released = partial(webbrowser.open, coc['website'])

        self.ids.comm_desc.text = coc['coc']
        self.ids.comm_desc.halign = 'left'

        Factory.Animation(opacity=1, d=.5).start(self.ids.scroll)
