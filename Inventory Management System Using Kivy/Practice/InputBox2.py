from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
       
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=150
        self.col_force_default= True
        self.col_default_width=200
        
        self.top_grid=GridLayout(row_force_default=True,
                                 row_default_height=50,
                                 col_force_default= True,
                                 col_default_width=200
                                 )
        self.top_grid.cols=2
        
        
        
        self.top_grid.add_widget(Label(text="Name:"))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        
        self.top_grid.add_widget(Label(text="Favorit food:"))
        self.food = TextInput(multiline=False)
        self.top_grid.add_widget(self.food)

        self.top_grid.add_widget(Label(text="Favorit color:"))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)
        
        self.add_widget(self.top_grid)
        
        
        self.submit = Button(text="submit", 
                             font_size=50,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=200
                             )
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name= self.name.text
        food= self.food.text
        color= self.color.text
        #print(f'Hello {name}, you like {food}')
        self.add_widget(Label(text=f'Hello {name}, your favourit food is {food}, And favourit color is {color}' ))
        self.name.text=""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()

        
if __name__ == '__main__':
    MyApp().run()