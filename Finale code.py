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

import sqlite3


#Define our different screens
class TitleMenu(Screen):
    pass

class StudentLogin(Screen):
    textinput= ObjectProperty(None)
##    username= ObjectProperty(None)
##    password= ObjectProperty(None)
##Creating 'show password' function
    def showpassword(self):
        if self.textinput.password == True:
            self.textinput.password = False

        elif self.textinput.password == False:
            self.textinput.password = True

        else:
            print('')

##    def press(self):
##        username= self.username.text
##        password= self.password.text
##        ## Create Database or connect to one
##        conn = sqlite3.connect('login.db')
##        c= conn.cursor()
##
##        sql= ("INSERT INTO login")
##        conn.commit()
##        conn.close()

    
                       
class StudentRegister(Screen):
    textinput= ObjectProperty(None)
##    username= self.username.text
##    password= self.password.text

    ## Writing to database
    
    


##Creating 'show password' function
    def showpassword(self):
        if self.textinput.password == True:
            self.textinput.password = False

        elif self.textinput.password == False:
            self.textinput.password = True

        else:
            print('')


class StudentMainMenu(Screen):
    pass

class Biology(Screen):
    pass

class Chemistry(Screen):
    pass

class Physics (Screen):
    pass

class Maths (Screen):
    pass

class Progress (Screen):
    pass

class MentalHealth (Screen):
    pass

class StudyTips (Screen):
    pass


class WindowManager(ScreenManager):
    pass


           
#Desginate our kv file 
kv = Builder.load_file('revisepro.kv')
 

class MyApp(App):
    def build(self):
        #Customising background color
        Window.clearcolor= (129/255, 125/255, 255/255)
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
    




	
