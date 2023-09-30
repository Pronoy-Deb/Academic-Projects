 
from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_file('animation.kv')

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0,0,1,1),
            duration=1, opacity=1
            )
        animate += Animation(
            size_hint=(1,1))
        
        animate += Animation(
            size_hint=(.5,.5))
        animate += Animation(
            pos_hint={"center_x":1})
        animate += Animation(
            pos_hint={"center_x":0.5})
        
        animate.start(widget)
        

class MyApp(App):
	def build(self):
	    return MyLayout()


if __name__=='__main__':
	MyApp().run()