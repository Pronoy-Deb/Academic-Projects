from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            column_data=[
                ("Serial", dp(20)),
                ("Name", dp(30)),
                ("Status", dp(50)),
                ("Price (TK)", dp(30)),
                ("Quantity", dp(30)),
            ],
            row_data=[
                (
                    "1",
                    "Gaming RAM",
                    "Available",
                    "3550",
                    "1",
                ),
                (
                    "2",
                    "RAM",
                    "Available",
                    "8600",
                    "1",
                ),
                (
                    "3",
                    "Casing Fan",
                    "Unavailable",
                    "2000",
                    "1",
                ),
                (
                    "4",
                    "Tube Clamp",
                    "Unavailable",
                    "180",
                    "1",
                ),
                (
                    "5",
                    "HDC",
                    "Available",
                    "850",
                    "1",
                ),
                (
                    "6",
                    "Sound Card",
                    "Available",
                    "1050",
                    "1",
                ),
                (
                    "7",
                    "Rotary",
                    "Unavailable",
                    "1100",
                    "1",
                ),
                (
                    "8",
                    "Tube Reamer",
                    "Available",
                    "1300",
                    "1",
                ),
                (
                    "9",
                    "SSD",
                    "Available",
                    "2200",
                    "1",
                ),
                (
                    "10",
                    "Mother Board",
                    "Available",
                    "11900",
                    "1",
                ),
                (
                    "11",
                    "HDD",
                    "Available",
                    "3700",
                    "1",
                ),
                (
                    "12",
                    "Cooling Fan",
                    "Available",
                    "999",
                    "1",
                ),
            ],
        )
        layout.add_widget(data_tables)
        return layout

Example().run()