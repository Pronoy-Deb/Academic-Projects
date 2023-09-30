 
from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('dropdown.kv')

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text=f'You Selected {value}'

class MyApp(App):
	def build(self):
	    return MyLayout()


if __name__=='__main__':
	MyApp().run()