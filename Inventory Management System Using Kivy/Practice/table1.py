from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class MainApp(MDApp):
	def build(self):
		screen = Screen()
		table = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.9, 0.6),
                    column_data=[
                        ("First Name", dp(30)),
                        ("Last Name", dp(30)),
                        ("Email Address", dp(30)),
                        ("Phone Number", dp(30))
                    ],
                    row_data=[
                        ("John", "Elder", "john@codemy.com", "(123) 456-7891"),
                        ("Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                    ]
                )
		# self.theme_cls.theme_style = "Light"
		# self.theme_cls.primary_palette = "BlueGray"
		screen.add_widget(table)
		return screen
MainApp().run()
