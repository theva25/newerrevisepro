#Importing the modules for code
import kivy
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.picker import MDDatePicker
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty
from time import strftime
from kivy.clock import Clock
from kivy.core.text import LabelBase
import sqlite3
from kivy.factory import Factory
from kivy.uix.popup import Popup
import re

LabelBase.register(name='Bainsley_Roman',
    fn_regular= 'Bainsley_Roman.otf'
    )

LabelBase.register(name='sforsoncasualmedium',
    fn_regular= 'sforsoncasualmedium.ttf'
    )

LabelBase.register(name='sforsoncasualshaded',
    fn_regular= 'sforsoncasualshaded.ttf'
    )

LabelBase.register(name='Amaranth-Regular',
    fn_regular= 'Amaranth-Regular.otf'
    )

Window.size = (950, 550)


#Define our different screens
class TitleMenu(Screen):
    pass

class Error(Popup):
    pass


class StudentLogin(Screen):
    popup= ObjectProperty(None)
    textinput1= ObjectProperty(None)
##    username= ObjectProperty(None)
##    password= ObjectProperty(None)
    
##Creating 'show password' function
##    def showpassword(self):
##        if self.textinput.password == True:
##            self.textinput.password = False
##
##        elif self.textinput.password == False:
##            self.textinput.password = True
##
##        else:
##            print('')
##            
##        if self.textinput.password == True:
##            self.textinput.password = False
##
##        elif self.textinput.password == False:
##            self.textinput.password = True
##
##        else:
##            print('')
            
##    def press(self):

##        self.ids.username.text= ''
##        self.ids.password.text= ''
        
##    def validate(self):
##        password= self.ids.password.text
##        Popup= ObjectProperty(None)
##        while True:
##            if len(password) < 8:
##                self.popup
##            elif not password.isdigit():
##                MyPopup.open()
##            elif not password.isupper(): 
##                MyPopup.open()
##            else:
##                MyPopup.open()
##                break

     

##    def validate(self):
##        password= self.password.text
##        def invalidLogin(self):
##            pop = Error()
##            pop.open()
##
##        return invalidLogin(self)

##        pattern= re.compile(r'')
##        while True:
##            if(len(password)<6):
##                print('too short')
##                break
##            elif re.search(r'[!@#$%&]',password) is None:
##                print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
##            elif re.search(r'\d',password) is None:
##                print('heheheheehehehehheeh')
##            elif re.search('[A-Z]',password) is None:
##                print('Capital letter')
##            elif re.match(r'[a-z A-Z 0-9 !@#$%&]{6}',password):
##                pattern= re.compile(r'[a-z A-Z 0-9 !@#$%&]{6}',password)
##                result=pattern.match(password)
##                print('password valid')
##                break
##            else:
##                print('Password invalid')
                
            
                         




        
##        while True:
##            if len(password) < 8:
##                self.invalidLogin()
##            elif not password.isdigit():
##                self.invalidLogin()
##            elif not password.isupper():
##                self.invalidLogin()
##            else:
##                self.invalidLogin()
##                break     

                     
class StudentRegister(Screen):
    textinput= ObjectProperty(None)
##    username= self.username.text
##    password= self.password.text

    ## Writing to database
    
##Creating 'show password' function
##    def showpassword(self):
##        if self.textinput.password == True:
##            self.textinput.password = False
##
##        elif self.textinput.password == False:
##            self.textinput.password = True
##
##        else:
##            print('')
##
##    def press(self):
##
##        self.ids.username.text= ''
##        self.ids.password.text= ''
##
##    def validate(self):
##        password= self.ids.password.text
##        
##        while True:
##            if len(password) < 8 and password.digit() and password.isupper():
##                Factory.MyPopup().open()
##            else:
##                print("Your password seems fine")
##                break
##

class StudentMainMenu(Screen):
    pass

class Biology(Screen):
    background_color= (50/255, 205/255, 50/255)
    pass

class Chemistry(Screen):
    background_color= (255/255, 139/255, 40/255)
    pass

class Physics (Screen):
    background_color= (119/255, 55/255, 191/255)
    pass

class Maths (Screen):
    pass

class Progress (Screen):
    pass

class MentalHealth (Screen):
    pass

class StudyTips (Screen):
    pass

class Cells (Screen):
    pass


class WindowManager(ScreenManager):
    pass


           
#Desginate our kv file 
kv = Builder.load_file('revisepro.kv')

##obj = StudentLogin() 

class MyApp(App):

    def build(self):
        title= 'RevisePro'
        #Customising background color
##        Window.clearcolor= (129/255, 125/255, 255/255)
        ## Create Database or connect to one
        conn = sqlite3.connect('login.db')

        ## Create a cursor
        c = conn.cursor()

        ## Create a table
        c.execute(""" CREATE TABLE if not exists login(
            username text,
            password text)
        """)

        ## Commit out changes
        conn.commit()

        ## Close our connection
        conn.close()
        return kv

    def submit(self):
        conn = sqlite3.connect('login.db')

        ## Create a cursor
        c = conn.cursor()

        ## add a record
        c.execute("INSERT INTO login VALUES(:first)",
            {
                'first': self.root.username.text,

            })
        

        ## Commit out changes
        conn.commit()

        ## Close our connection
        conn.close()
    
if __name__== '__main__':
    MyApp().run()
    StopWatchApp().run()
    




	
