from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivymd.uix.screen import Screen
import datetime
import json

class Demo(ScreenManager):
    def registerUser(self):
        file=open("userdata.json")
        x=file.read();
        aList=json.loads(x)
        data={"id":self.ids.i.text,"name":self.ids.n.text,"contact_number":self.ids.cn.text,"password":self.ids.pas.text}
        aList.append(data)
        jsonString = json.dumps(aList,indent=4)
        jsonFile = open("userdata.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        file.close()
        toast("Registation Completed..")
        self.ids.i.text=""
        self.ids.n.text=""
        self.ids.cn.text=""
        self.ids.pas.text=""
        
    def checkUser(self):
        '''file=open("userdata.json")
        x=file.read();
        data=json.loads(x)
    
        for d in data:
            if(d["id"]==self.ids.cid.text and d["password"]==self.ids.cpas.text):
                toast("Welcome")
                self.ids.cid.text=""
                self.ids.cpas.text=""
                self.get_screen('adminpanel').manager.current='adminpanel'
                break
        else:
            toast("Wrong Information")'''
        self.get_screen('adminpanel').manager.current='adminpanel'
        
    def addmem(self):
        pass
    def purcoupon(self):
        pass
        
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        Builder.load_file("all.kv")
        return Demo()
    
        
MainApp().run()