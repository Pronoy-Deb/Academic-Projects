from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('lab.kv')
class MyGridLayout(Widget):
    

    def press(self):
        name= self.name.text
        food= self.food.text
        color= self.color.text
        self.name.text=""
        self.food.text=""
        self.color.text=f'Hello {name}, you like {food}'
        
class New(App):
    def build(self):
        return MyGridLayout()

        
if __name__ == '__main__':
    New().run()