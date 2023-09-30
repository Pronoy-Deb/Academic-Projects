# import kivy
# from kivy.app import App
# import all the relevant classes
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


# class to call the popup function
class PopupWindow(Widget):
	def btn(self):
		popFun()

# class to build GUI for a popup window
class P(FloatLayout):
	pass

# function that displays the content
def popFun():
	show = P()
	window = Popup(title = "popup", content = show,
				size_hint = (None, None), size = (300, 300))
	window.open()

# class to accept user info and validate it
class loginWindow(Screen):
	email = ObjectProperty(None)
	pwd = ObjectProperty(None)


# class to accept sign up info
class signupWindow(Screen):
	name2 = ObjectProperty(None)
	email = ObjectProperty(None)
	pwd = ObjectProperty(None)

# class to display validation result
class logDataWindow(Screen):
	pass

# class for managing screens
class windowManager(ScreenManager):
	pass


# kv file
kv = Builder.load_file('login.kv')
sm = windowManager()

# adding screens
sm.add_widget(loginWindow(name='login'))
sm.add_widget(signupWindow(name='signup'))
sm.add_widget(logDataWindow(name='logdata'))

# class that builds gui
class loginMain(App):
	def build(self):
        return Label(text="Hello world", font_size=72)
		return sm

class MyApp(App):
        
    def build(self):
        
# if __name__ == '__main__':

# driver function
if __name__=="__main__":
    # MyApp().run()
	loginMain().run()
