'''Navigation Screen
'''
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.navigationdrawer import NavigationDrawer
from kivy.factory import Factory

Factory.register('TouchRippleBehavior', module='uix.behaviors')


class NavigationScreen(Screen):
  '''
  '''

  Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition


<MenuButton@PyConButton>
    group: 'LeftPanel'
    on_released: app.navigationdrawer.toggle_state()

<LeftPanel@BoxLayout+Background>
    source: 'atlas://data/default/bg'
    orientation: 'vertical'
    padding: dp(7), dp(7)
    Image
        source: "atlas://data/default/logo"
        size_hint: 1, None
        height: dp(130)
        mipmap: True
    ScrollView
        GridLayout
            cols: 1
            size_hint_y: None
            height: self.minimum_height

            MenuButton
                id: bt_sched
                text: 'Programação'
                on_released: app.load_screen('ScreenSchedule', manager=app.navigation_manager)
            MenuButton
                text: 'Localização'
                on_released: app.load_screen('ScreenVenue', manager=app.navigation_manager)
            MenuButton
                text: 'Patrocinadores'
                on_released: app.load_screen('ScreenSponsor', manager=app.navigation_manager)
            MenuButton
                text: 'Ingressos'
                on_released: app.load_screen('ScreenTicket', manager=app.navigation_manager)
            MenuButton
                text: 'Sobre o evento'
                on_released: app.load_screen('ScreenAbout', manager=app.navigation_manager)
            MenuButton
                text: 'Código de Conduta'
                on_released: app.load_screen('ScreenCoC', manager=app.navigation_manager)
            MenuButton
                text: 'Contato'
                on_released: app.load_screen('ScreenCommunity', manager=app.navigation_manager)
            MenuButton
                text: 'Feedback'
                on_released: app.load_screen('ScreenFeedback', manager=app.navigation_manager)


<TopBar@BoxLayout>
    size_hint: None, None
    height: dp(45)
    width: dp(45)
    ImBut
        source: 'atlas://data/default/hamburger'
        size_hint_x: None
        size_hint_y: 1
        width: self.height
        allow_stretch: True
        on_released: app.navigationdrawer.toggle_state()


<RightPanel@BoxLayout+Background>
    source: 'app/data/images/background.jpg'
    orientation: "vertical"
    TopBar
    ScreenManager
        on_parent: app.navigation_manager = nav_sm
        id: nav_sm

<NavigationScreen>
    name: 'NavigationScreen'
    on_enter:
        import os
        scr = os.environ.get('PYTHONBRASIL_STARTUP_SCREEN','ScreenSchedule')
        app.load_screen(scr, manager=app.navigation_manager)
    NavigationDrawer
        id: navigationdrawer
        on_parent: app.navigationdrawer = navigationdrawer
        LeftPanel
            id: left_panel
        RightPanel
            opacity: 1.2-(self.x/root.right)
''')
