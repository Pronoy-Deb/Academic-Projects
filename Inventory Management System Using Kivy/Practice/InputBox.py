import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
       
        self.cols = 2
        self.add_widget(Label(text="Name:"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text="Favorit food:"))
        self.food = TextInput(multiline=False)
        self.add_widget(self.food)

        self.add_widget(Label(text="Favorit color:"))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)
        
        self.submit = Button(text="submit", font_size=50)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name= self.name.text
        food= self.food.text
        color= self.color.text
        #print(f'Hello {name}, you like {food}')
        self.add_widget(Label(text=f'Hello {name}, you like {food}'))
        self.name.text=""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()

        
if __name__ == '__main__':
    MyApp().run()