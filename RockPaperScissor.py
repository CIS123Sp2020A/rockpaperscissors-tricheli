#Tenisce Richelieu 
#CIS 123


#Assignment: Create a GUI that will simulate the game Rock Paper Scissors using radio buttons


import tkinter
import tkinter.messagebox as box

#import random
import random

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x100")

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        # self.middle_frame = tkinter.Frame(self.main_window)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar()
        self.radioVars = tkinter.StringVar()
        self.resultVar = tkinter.StringVar()

        #Create radio buttons labeled Rock Paper Scissors; rock paper scissors radio frame
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Rock', variable=self.radioVar, value='Rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Paper', variable=self.radioVar, value='Paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Scissors', variable=self.radioVar, value='Scissors')

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #Create play and quit buttons; ok and quit button frame
        self.okButton = tkinter.Button(self.buttonFrame, text='OK', command=self.displayInfo)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.okButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    #Have the computer make a random move out of the selections Rock Paper or Scissors Rock(0), Paper(1) or Scissors (2);
    #this will be displayed with your selection as well(message box)
    def displayInfo(self):
        self.randomNum = random.randint(0,2)

        if self.randomNum == 0:
            self.radioVars.set('Rock')
        elif self.randomNum == 1:
            self.radioVars.set('Paper')
        else:
            self.radioVars.set('Scissors')

    #Create if/else statements around whether the player wins or not, attached to text which tells the action of their moves; message box
    #if rock beats scissors - rock crushes scissors. (Player) Wins
    #if paper beats rock - paper covers rock. (Player) Wins
    #if scissors beats paper - scissors cuts paper. (Player) Wins

        
        box.showinfo('Selection',('Computer selected: ' + self.radioVars.get(),
                                  'You selected: ' + self.radioVar.get()))
        if ((self.radioVars.get() == 'Rock') and (self.radioVar.get() == 'Scissors')):
            self.resultVar.set('Rock crushes Scissors: You Lose :(')
        elif ((self.radioVars.get() == 'Scissors') and (self.radioVar.get() == 'Rock')):    
            self.resultVar.set('Rock crushes Scissors: You Win! :)')   
        elif ((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Rock')):
            self.resultVar.set('Paper covers Rock: You Lose :(')
        elif ((self.radioVars.get() == 'Rock') and (self.radioVar.get() == 'Paper')):
            self.resultVar.set('Paper covers Rock: You Win! :)')  
        elif ((self.radioVars.get() == 'Scissors') and (self.radioVar.get() == 'Paper')):
            self.resultVar.set('Scissors beats Paper: You Lose :(')
        else:
            self.resultVar.set('Scissors beats Paper: You Win! :)')

        box.showinfo('Winner',(self.resultVar.get()))


demoGUI = MyGUI()
