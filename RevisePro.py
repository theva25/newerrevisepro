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
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty
from time import strftime
from kivy.core.text import LabelBase
import sqlite3
from kivy.factory import Factory
from kivy.uix.popup import Popup
import re

## Importing the '.otf' files for font to be used
## Assigning name of font for programmer to use
LabelBase.register(name='Amaranth-Regular',
    fn_regular= 'Amaranth-Regular.otf'
    )

LabelBase.register(name='Bainsley_Roman',
    fn_regular= 'Bainsley_Roman.otf'
    )

LabelBase.register(name='sforsoncasualmedium',
    fn_regular= 'sforsoncasualmedium.ttf'
    )

LabelBase.register(name='sforsoncasualshaded',
    fn_regular= 'sforsoncasualshaded.ttf'
    )

## Allows kivy window to open maximised in default
Window.maximize()


## Error Popup when register password hasnt met requirements
class Error(Popup):
    pass

class Error2(Popup):
    pass

class Logout(Popup):
    pass

## Eukaryotic cells multiple choice
class Cells1(Popup):

    ## Variable holding the score of the user. Updated later.
    score = 0

    def right1(self):
        if self.ids.right1.active == True:
            self.ids['wrong1'].active = False
            self.ids['wrong2'].active = False
            self.ids['wrong3'].active = False
            self.ids['nucleus'].outline_color = (0/255, 150/255, 255/255,255/255)
        else:
            self.ids['nucleus'].outline_color = (0,0,0)

    def wrong1(self):
        if self.ids.wrong1.active == True:
            self.ids['right1'].active = False
            self.ids['wrong2'].active = False
            self.ids['wrong3'].active = False
            self.ids['mitochondria1'].outline_color = (0/255, 150/255, 255/255,255/255)
        else:
            self.ids['mitochondria1'].outline_color = (0,0,0)

    def wrong2(self):
        if self.ids.wrong2.active == True:
            self.ids['right1'].active = False
            self.ids['wrong1'].active = False
            self.ids['wrong3'].active = False
            self.ids['cytoplasm'].outline_color = (0/255, 150/255, 255/255,255/255)
        else:
            self.ids['cytoplasm'].outline_color = (0,0,0)

    def wrong3(self):
        if self.ids.wrong3.active == True:
            self.ids['right1'].active = False
            self.ids['wrong1'].active = False
            self.ids['wrong2'].active = False
            self.ids['ribosomes1'].outline_color = (0/255, 150/255, 255/255,255/255)
        else:
            self.ids['ribosomes1'].outline_color = (0,0,0)
            
##    def deactivate1(self):
##        ## When checkbox is clicked, other checkbox are updated to be false
##        self.ids['wrong1'].active = False
##        self.ids['wrong2'].active = False
##        self.ids['wrong3'].active = False
##
    def change1(self):
        ## Text of the corresponding checkbox updates color if active
        ## Chosen text changes to a baby blue colour, rbga value below
        self.ids['nucleus'].color = (0/255, 105/255, 146/255,255/255)
        self.ids['mitochondria'].color = (0,0,0,0)
        self.ids['cytoplasm'].color = (0,0,0,0)
        self.ids['ribosomes'].color = (0,0,0,0)
        
##    def deactivate2(self):
##        self.ids['right1'].active = False
##        self.ids['wrong2'].active = False
##        self.ids['wrong3'].active = False
##
##    def change2(self):
##        self.ids['nucleus'].color = (0,0,0,0)
##        self.ids['mitochondria'].color = (0/255, 105/255, 146/255,255/255)
##        self.ids['cytoplasm'].color = (0,0,0,0)
##        self.ids['ribosomes'].color = (0,0,0,0)
##        
##    def deactivate3(self):
##        self.ids['wrong1'].active = False
##        self.ids['right1'].active = False
##        self.ids['wrong3'].active = False
##
##    def change3(self):
##        self.ids['nucleus'].color = (0,0,0,0)
##        self.ids['mitochondria'].color = (0,0,0,0)
##        self.ids['cytoplasm'].color = (0/255, 105/255, 146/255,255/255)
##        self.ids['ribosomes'].color = (0,0,0,0)
##        
##    def deactivate4(self):
##        self.ids['wrong1'].active = False
##        self.ids['wrong2'].active = False
##        self.ids['right1'].active = False
##
##    def change4(self):
##        self.ids['nucleus'].color = (0,0,0,0)
##        self.ids['mitochondria'].color = (0,0,0,0)
##        self.ids['cytoplasm'].color = (0,0,0,0)
##        self.ids['ribosomes'].color = (0/255, 105/255, 146/255,255/255)
    pass

## Eukaryotic cells Fill in the blanks
class Cells2(Popup):
    pass

#Define our different screens
class TitleMenu(Screen):
    pass

class StudentLogin(Screen):
##Creating 'show password' function
    def showpassword(self):
        ## On_active, the masking is removed
        if self.password.password == True:
            ## Masking =  False so characters are shown
            self.password.password = False   

        ## When no active masking= true
        elif self.password.password == False:
            self.password.password = True

        ## Else returns print statement 
        else:
            print('')

    def validate(self):
        check = 0
        ## IF password doesnt match confirmpassword
        if self.password.text == '':
            check = 1
        if self.username.text == '':
            check = 1
        ## IF password meets conditions 
        if(check == 0):
            print('Password is valid')
            self.ids.password.text = ''
            self.ids.username.text = ''
            self.ids.showpassword.active = False
            ## Transits user to mainmenu
            self.manager.current = 'studentmainmenu'
            ## Transition animation
            self.manager.transition.direction='up'
        else:
            print('Password isnt valid')
            ## Display error popup message
            Error2().open()

            
    ## Clear all/reset widgets 
    def clear(self):
        ## Username textinput is empty
        self.ids.password.text = ''
        ## Password textinput is empty
        self.ids.username.text = ''
        ## Show password is disabled
        self.ids['showpassword'].active = False
                 
class StudentRegister(Screen):
    ##Creating 'show password' function
    def showpassword(self):
        ## On_active, the masking is removed
        if self.password.password == True:
            ## Masking = False so characters are shown
            self.password.password = False
            
        ## When not active masking - True 
        elif self.password.password == False:
            self.password.password = True

        else:
            print('')

    def showconfirmpassword(self):
        ## On_active, the masking is removed
        if self.confirmpassword.password == True:
            ## Masking =  False so characters are shown
            self.confirmpassword.password = False   

        ## When not active masking= true
        elif self.confirmpassword.password == False:
            self.confirmpassword.password = True

        ## Else returns print statement 
        else:
            print('')

    ## Password Validation function
    def validate(self):
        ## Condition variable
        check = 0
        ## IF input doesnt have lowercase letter
        if not re.search('[a-z]',self.password.text):
            ## Label turns red if not found
            self.ids['lowercase'].color= (244/255, 46/255, 23/255,255/255)
            check= 1
        else:
            ## Label turns green if found
            self.ids['lowercase'].color = (50/255, 205/255, 50/255)
            
        ## IF input doesnt have a digit
        if not re.search('[0-9]',self.password.text):
            ## Label turns red if not found
            self.ids['number'].color= (244/255, 46/255, 23/255,255/255)
            check = 1
        else:
            ## Label turns green if found
            self.ids['number'].color = (50/255, 205/255, 50/255)
            
        ## IF input doesnt have an uppercase letter
        if not re.search('[A-Z]',self.password.text):
            ## Label turns red if not found
            self.ids['uppercase'].color = (244/255, 46/255, 23/255,255/255)
            check = 1
        else:
            ## Label turns green if found
            self.ids['uppercase'].color = (50/255, 205/255, 50/255)
            
        ## IF input doesnt have special characters
        if not re.search('[$@#!-]',self.password.text):
            ## Label turns red if not found
            self.ids['special'].color = (244/255, 46/255, 23/255,255/255)
            check = 1
        else:
            ## Label turns green if found
            self.ids['special'].color = (50/255, 205/255, 50/255)
            
        ## IF passsword length < 6
        if len(self.password.text)<6:
            ## Label turns red if not found
            self.ids['characters'].color = (244/255, 46/255, 23/255,255/255)
            check = 1
        else:
            ## Label turns green if found
            self.ids['characters'].color = (50/255, 205/255, 50/255)
     
        ## IF password doesnt match confirmpassword
        if self.password.text != self.confirmpassword.text:
            check = 1
        ## IF password meets conditions 
        if(check == 0):
            print('Password is valid')
            ## Transits user to mainmenu
            self.manager.current = 'studentmainmenu'
            ## Transition animation
            self.manager.transition.direction='up'
            ## Label turns white if all requirements are met
            self.ids['lowercase'].color = (1,1,1)
            self.ids['uppercase'].color = (1,1,1)
            self.ids['number'].color = (1,1,1)
            self.ids['characters'].color = (1,1,1)
            self.ids['special'].color = (1,1,1)
            self.ids.showpassword.active = False
            self.ids.password.text = ''
            self.ids.confirmpassword.text = ''
            self.ids.username.text = ''
        else:
            print('Password isnt valid')
            ## Display error popup message
            Error().open()
            
    ## Clear all/reset widgets 
    def clear(self):
        ## Username textinput is empty
        self.ids.password.text = ''
        ## Password textinput is empty
        self.ids.username.text = ''
        ## Confirm password textinput is empty
        self.ids.confirmpassword.text = ''        
        ## Show password is disabled
        self.ids['showpassword'].active = False
        ## Password requirement text colour returns to white
        self.ids['lowercase'].color = (1,1,1)
        self.ids['uppercase'].color = (1,1,1)
        self.ids['number'].color = (1,1,1)
        self.ids['characters'].color = (1,1,1)
        self.ids['special'].color = (1,1,1)
        

class StudentMainMenu(Screen):
    def submit(self):
        goal1= self.one.text
        goal2= self.two.text
        goal3= self.three.text
        goal4= self.four.text
        goal5= self.five.text
            
        if goal1 == '' and  goal2 == '' and goal3 == '' and  goal4 == '' and goal5 == '':
            self.ids.one.text = self.ids.goals.text
            self.ids.goals.text = ''
            self.ids.task1.disabled = False
        else:
            print('')

        if goal2 == '' and goal3 == '' and  goal4 == '' and goal5 == '':
            self.ids.two.text = self.ids.goals.text
            self.ids.goals.text = ''
            self.ids.task2.disabled = False
        else:
            print('')

        if goal3 == '' and  goal4 == '' and goal5 == '':
            self.ids.three.text = self.ids.goals.text
            self.ids.goals.text = ''
            self.ids.task3.disabled = False
        else:
            print('')

        if goal4 == '' and goal5 == '':
            self.ids.four.text = self.ids.goals.text
            self.ids.goals.text = ''
            self.ids.task4.disabled = False
        else:
            print('')
            
        if goal5 == '':
            self.ids.five.text = self.ids.goals.text
            self.ids.goals.text = ''
            self.ids.task5.disabled = False
        else:
            print('')

    def tasks(self):
        goal1= self.one.text
        
        if not goal1 == '':
            self.ids.notasks.text = ''
        else:
            print()

    def clear(self):
        self.ids.one.text = ''
        self.ids.two.text = ''
        self.ids.three.text = ''
        self.ids.four.text = ''
        self.ids.five.text = ''
        self.ids.notasks.text = 'Currently no \ntasks'
        self.ids.task1.disabled = True
        self.ids.task2.disabled = True
        self.ids.task3.disabled = True
        self.ids.task4.disabled = True
        self.ids.task5.disabled = True
        self.ids.task1.active = False
        self.ids.task2.active = False
        self.ids.task3.active = False
        self.ids.task4.active = False
        self.ids.task5.active = False

    def task1(self):
        if self.ids.task1.active == True:
            self.ids.one.color = (0/255, 230/255,64/255,255/255)
        elif self.ids.task1.active == False:
            self.ids.one.color = (1,1,1)
        else:
            print('')

    def task2(self):
        if self.ids.task2.active == True:
            self.ids.two.color = (0/255, 230/255,64/255,255/255)
        elif self.ids.task2.active == False:
            self.ids.two.color = (1,1,1)
        else:
            print('')

    def task3(self):
        if self.ids.task3.active == True:
            self.ids.three.color = (0/255, 230/255,64/255,255/255)
        elif self.ids.task3.active == False:
            self.ids.three.color = (1,1,1)
        else:
            print('')

    def task4(self):
        if self.ids.task4.active == True:
            self.ids.four.color = (0/255, 230/255,64/255,255/255)
        elif self.ids.task4.active == False:
            self.ids.four.color = (1,1,1)
        else:
            print('')
            
    def task5(self):
        if self.ids.task5.active == True:
            self.ids.five.color = (0/255, 230/255,64/255,255/255)
        elif self.ids.task5.active == False:
            self.ids.five.color = (1,1,1)
        else:
            print('')
            
        
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

class Organs (Screen):
    pass

class Plants (Screen):
    pass

class Diseases (Screen):
    pass

class Genes (Screen):
    pass

class CellsDivision(Screen):
    pass

class Membrane(Screen):
    pass

class Specialised(Screen):
    pass

class Digestive (Screen):
    pass

class Circulatory (Screen):
    pass

class Nervous  (Screen):
    pass

class Respiration (Screen):
    pass

class Atoms (Screen):
    pass

class Period (Screen):
    pass 



## Manages multiple screens of the program
class WindowManager(ScreenManager):
    pass
           
#Desginate our kv file 
main= Builder.load_file('main.kv')
popup= Builder.load_file('popup.kv')

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
        return main
        return popup
##        return chemistry
##        return physics
##        return maths

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
    




	
