Python Brasil [13] 2017 Application
=============================

Fala Pessoal,

Andei brincando com o Kivy aqui e fiz um aplicativo (DE EXEMPLO) da PythonBrasil, com a grade, e coisas simples.

#### Segue o Pacote APK para android:
 - [PythonBrasil-2017-Alternativo-0.1.apk](https://github.com/samukasmk/pythonbrasil_mobile/blob/master/PythonBrasil-2017-Alternativo-0.1.apk)

## Lembrando que esse não tem a intenção de ser oficial!

ESSE APLICATIVO É APENAS PARA ESTUDO, E SE ISENTA DE QUALQUER RESPONSABILIDADE COM A VERACIDADE.

**PARA TOTAL CONFIABILIDADE UTILIZE O APP OFICIAL DA PYTHONBRASIL13:**
- https://play.google.com/store/apps/details?id=br.org.pythonbrasil.pybr13


## ABAIXO Segue mais informações do aplicativo original da comunidade PyDelhi


> Mobile App for Python Brasil [13] 2017

![Alt text](screen.png?raw=true "Optional Title")

## Kivy Installation:
- https://kivy.org/docs/installation/installation.html

## Make sure you build the theme before using the app.
   - Make sure you have `pillow` installed. `pip install pillow --user`
   - Paste/change the image in PythonBrasilConf/tools/theming
   - Change your directory to PythonBrasilConf
   - Run command ``make theming``

### To test install kivy and run the following::

    $ python appconf/main.py -m screen:droid2,portrait -m inspector

### Help on screens
- https://kivy.org/docs/api-kivy.modules.screen.html


This command will aggregate all the png images in your file to one atlas
from which the images are loaded.

## to make apk **prefer linux**

1. Install buildozer: pip install buildozer
2. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step.
3. Connect your mobile, enable usb debugging, Then goto appconf
   folder and type `make apk`

Link to a existing vm that can be re-used will be added for convenience.

## to make ipa for ios **

1. Install XCode with latest updates & latest command line tools
2. pip install buildozer
3. goto the app folder and do `buildozer init`
4. edit the buildoze.spec and add details for ios
5. run `buildozer ios debug`

**How to add a screen**

Step 1: Create a new file, add the following Template for a clean Screen

	'''Module XYZ:
	This is the documentation for the Module that explains the
	main usecase of this Module and details it's usage.
	'''

	from kivy.uix.screenmanager import Screen
	from kivy.lang import Builder

	class ScreenSponsor(Screen):
	    '''This is the documentation for the Screen that explains
	    the main usecase of this Screen and details it's usage.
	    '''

	    # Here we define the UI of this screen.
	    Builder.load_string('''
<ScreenSponsor>
	name: 'ScreenSponsor'
	# your Widgets here,  we just use 2 buttons in boxlayout as demo
	BoxLayout
	    Button
	    Button
	''')

Take special note of the names::

    The `name: ScreenSponsor`, in this same as the class name `class ScreenSponsor(...)`.


Step 2: Save the file as `screensponsor.py` in the folder `<PythonBrasilConf/appconf/uix/screens>`. Take note to name the file same as the class name,  in our case `ScreenSponsor` in lowercase with .py appended at end.

That's it. Now to load this screen::

    Button:
    	on_release:
            app.load_screen('ScreenSponsor', manager=app.navigation_manager)

`manager=` is a optional parameter, which specifies which `ScreenManager` to load this screen in.
If it is omitted this screen will be loaded into the main Screen Manager Which is responsobile for loading `StartupScreen` and `NavigationScreen`.


***   Enjoy   ***
