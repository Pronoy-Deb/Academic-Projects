from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('tabs.kv')

class MyLayout(TabbedPanel):
    pass
    #def spinner_clicked(self, value):
        #self.ids.click_label.text=f'You Selected {value}'

class MyApp(App):
	def build(self):
	    return MyLayout()


if __name__=='__main__':
	MyApp().run()