from tkinter import *
from textblob import TextBlob

root = Tk()
root.title('Spelling Checker')  # setting the title of the window which will appear in the top-left corner of the window
root.geometry('700x400')  # determining the length and width of the window
root.config(background='#48C9B0')  # setting the background color of the window after initialization

def check_spelling():
    word = enter_text.get()  # getting text from the enter_text box wsing .get() method
    chk = TextBlob(word)
    right = str(chk.correct())

    cs = Label(root, text= 'Correct spelling is: ', font=('poppins', 20), bg='#48C9B0', fg='#364971')
    cs.place(x=100, y=250)
    spell.config(text=right)  # config or configure is used to access an object's attributes after its initialisation


heading = Label(root, text='Spelling Checker !', font=('times new roman', 40, 'bold'), bg='#48C9B0', fg='#1F618D')
heading.pack(pady=(50, 0))  # managing layout using .pack()

enter_text = Entry(root, justify='center', width= 30, font=('poppins, 30'), bg='white', border= 2)
enter_text.pack(pady=10)  # an entry widget created
enter_text.focus()  # Focus is used to refer to the widget or window which is currently accepting input

button = Button(root, text='Check', font=('arial', 20, 'bold'), fg='#48C9B0', bg='#E74C3C', command=check_spelling)
button.pack()  # .pack() used to place the button accurately on the window

spell = Label(root, font=('arial', 20), bg='#dae6f6', fg='#364971')
spell.place(x=350, y=250)  # used to place the reply accurately on the window


root.mainloop()

# note: Tkinter has three Layout Managers that use geometric methods to position widgets in an application frame:
# pack, place, grid. Each method has different coding requirements. Note that if a widget is added to a frame without
# using a Layout Manager the code may not produce an error, but the widget will not be displayed correctly in the frame.
