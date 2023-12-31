from tkinter import *


ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#0B5A81')

f = ('Times', 14)
var = StringVar()
var.set('male')
loghead = Label(ws, text = "Register")
loghead.config(font=("Courier", 44))
loghead.place(x =250 , y = 10)





right_frame = Label(
    ws, 
    bd=2, 
    bg='#808080',
    relief=SOLID, 
    padx=100, 
    pady=100
    )

right_frame.place(x=220,y=100)

Label(
    right_frame, 
    text="Enter Name", 
    bg='#808080',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    bg='#808080',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    bg='#808080',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Gender", 
    bg='#808080',
    font=f
    ).grid(row=3, column=0, sticky=W, pady=10)




Label(
    right_frame, 
    text="Enter Password", 
    bg='#808080',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    bg='#808080',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#808080',
    padx=10, 
    pady=10,
    )


register_name = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f
    )

register_mobile = Entry(
    right_frame, 
    font=f
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    bg='#808080',
    variable=var,
    value='male',
    font=('Times', 10),
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#808080',
    variable=var,
    value='female',
    font=('Times', 10),
  
)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#808080',
    variable=var,
    value='others',
    font=('Times', 10)
   
)




register_pwd = Entry(
    right_frame, 
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command="None"
)


register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)

register_pwd.grid(row=4, column=1, pady=10, padx=20)
pwd_again.grid(row=5, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()
right_frame.place(x=200,y=100)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)


ws.mainloop()