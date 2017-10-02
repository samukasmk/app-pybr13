'''Ticket:
Display the explara link for the ticket page.
'''
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ScreenTicket(Screen):


    Builder.load_string('''
    #:import webbrowser webbrowser
<ScreenTicket>
    name: 'ScreenTicket'
    BoxLayout
        padding: dp(12)
        spacing: dp(12)
        orientation: 'vertical'
        BoxLayout
            size_hint_y: None
            height: dp(50)
            spacing: dp(5)
            ActiveButton
                text: 'Comprar ingressos'
                on_release:
                    webbrowser.open('http://2017.pythonbrasil.org.br/#tickets')
            ActiveButton
                text: 'Pagina do Sympla'
                on_release:
                    webbrowser.open('https://www.sympla.com.br/pythonbrasil13--pybr13__148343')
        BackLabel:
            id: comm_desc
        BackLabel:
            id: sample_email
        Image:
            source: 'data/images/ticket.png'
            allow_stretch: True
            size: root.size
            opacity: 1
''')

    def on_enter(self, onsuccess=False):
        self.ids.comm_desc.backcolor = 0, 0, 0, 0
        self.ids.comm_desc.text = 'A confirmação de compra do seu ingresso é enviado ao seu email, imprima e leve no dia.\nSegue um exemplo do email.'

        self.ids.sample_email.halign = 'left'
        self.ids.sample_email.text = 'Assunto: Confirmação de compra para PythonBrasil[13] · #pybr13 - Pedido XPT2017\nConteúdo: Na imagem abaixo.'
