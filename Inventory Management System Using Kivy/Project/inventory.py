from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
import json

class show(ScreenManager):
    def signup(self):
        file = open("file.json")
        x = file.read()
        lis = list(json.loads(x))
        data = {"username": self.ids.name.text, "email": self.ids.mail.text, "password": self.ids.pas.text}
        lis.append(data)
        jsonString = json.dumps(lis, indent=4)
        jsonFile = open("file.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Submitted Successfully!!!")
        self.ids.name.text = ""
        self.ids.mail.text = ""
        self.ids.pas.text = ""

    def checkUser(self):
        file = open("file.json")
        x = file.read()
        data = json.loads(x)

        for info in data:
            if(info["username"] == self.ids.ckname.text and info["password"] == self.ids.ckpas.text):
                toast("Welcome to the System!!!")
                self.ids.ckname.text = ""
                self.ids.ckpas.text = ""
                self.get_screen('first').manager.current = 'first'
                break
        else:
            toast("Invalid Username or Password!!!")

    def add1(self):
        file = open("file.json")
        x = file.read()
        lis = list(json.loads(x))
        data = {"id": self.ids.id.text, "name": self.ids.nam.text,
                "catagory": self.ids.cat.text, "quantity": self.ids.quan.text, "totalprice": self.ids.totprice.text}
        lis.append(data)
        jsonString = json.dumps(lis, indent=4)
        jsonFile = open("file.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Added Successfully!!!")
        self.ids.id.text = ""
        self.ids.name.text = ""
        self.ids.cat.text = ""
        self.ids.quan.text = ""
        self.ids.totprice.text = ""

    def add2(self):
        file = open("file.json")
        x = file.read()
        lis = list(json.loads(x))
        data = {"id": self.ids.oid.text, "name": self.ids.onam.text,
                "catagory": self.ids.ocat.text, "quantity": self.ids.oquan.text, "totalprice": self.ids.totprice.text}
        lis.append(data)
        jsonString = json.dumps(lis, indent=4)
        jsonFile = open("file.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Placed Successfully!!!")
        self.ids.oid.text = ""
        self.ids.onam.text = ""
        self.ids.ocat.text = ""
        self.ids.oquan.text = ""
        self.ids.ototprice.text = ""

    def add3(self):
        file = open("file.json")
        x = file.read()
        lis = list(json.loads(x))
        data = {"id": self.ids.sid.text, "name": self.ids.snam.text,
                "address": self.ids.sadd.text}
        lis.append(data)
        jsonString = json.dumps(lis, indent=4)
        jsonFile = open("file.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Added Successfully!!!")
        self.ids.sid.text = ""
        self.ids.snam.text = ""
        self.ids.sadd.text = ""

    def add4(self):
        file = open("file.json")
        x = file.read()
        lis = list(json.loads(x))
        data = {"id": self.ids.cid.text, "name": self.ids.cnam.text, "contact": self.ids.ccon.text,
                "address": self.ids.cadd.text}
        lis.append(data)
        jsonString = json.dumps(lis, indent=4)
        jsonFile = open("file.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Added Successfully!!!")
        self.ids.cid.text = ""
        self.ids.cnam.text = ""
        self.ids.ccon.text = ""
        self.ids.cadd.text = ""

    def add5(self):
        file = open("file.json")
        x = file.read()
        lis = list(json.loads(x))
        data = {"id": self.ids.pid.text, "name": self.ids.pnam.text, "type": self.ids.ptype.text,
                "quantity": self.ids.pquan.text, "price": self.ids.pprice.text}
        lis.append(data)
        jsonString = json.dumps(lis, indent=4)
        jsonFile = open("file.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Added Successfully!!!")
        self.ids.pid.text = ""
        self.ids.pnam.text = ""
        self.ids.ptype.text = ""
        self.ids.pquan.text = ""
        self.ids.pprice.text = ""

    def add6(self):
        file = open("file.json")
        x = file.read()
        lis = list(json.loads(x))
        data = {"id": self.ids.sid.text, "name": self.ids.snam.text, "type": self.ids.stype.text,
                "quantity": self.ids.squan.text, "price": self.ids.sprice.text}
        lis.append(data)
        jsonString = json.dumps(lis, indent=4)
        jsonFile = open("file.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Added Successfully!!!")
        self.ids.sid.text = ""
        self.ids.snam.text = ""
        self.ids.stype.text = ""
        self.ids.squan.text = ""
        self.ids.sprice.text = ""

    # def tab(self):
    #     class Tab(MDApp):
    #         def build(self):
    #             screen = Screen()
    #             table = MDDataTable(
    #                 pos_hint={'center_x': 0.5, 'center_y': 0.5},
    #                 size_hint=(0.9, 0.6),
    #                 column_data=[
    #                     ("First Name", dp(30)),
    #                     ("Last Name", dp(30)),
    #                     ("Email Address", dp(30)),
    #                     ("Phone Number", dp(30))
    #                 ],
    #                 row_data=[
    #                     ("John", "Elder", "john@codemy.com", "(123) 456-7891"),
    #                     ("Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
    #                 ]
    #             )
    #             # self.theme_cls.theme_style = "Light"
    #             # self.theme_cls.primary_palette = "BlueGray"
    #             screen.add_widget(table)
    #             return screen
    #     return Tab()
        # Tab().run()



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        Builder.load_file("inventory.kv")
        return show()

MainApp().run()
