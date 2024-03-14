from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Mad Libs Generator in Python')
root.geometry('800x800+200+100')

root.resizable(False, False)
fg1 = '#262c5f'
bg1 = '#addbed'

f = Frame(root, bd=10, bg="cyan", relief=RIDGE, width=800, height=800)

f.pack()

name_var = StringVar()
skil_var = StringVar()
dream_var = StringVar()
profession_var = StringVar()
game_var = StringVar()
study_var = StringVar()

# ================================ Imformations ======================
im_lable = Frame(f, width=740, bg='#addbed', height=380, bd=8, relief=RIDGE)
im_lable.place(x=20, y=20)

name_label = Label(im_lable, text="Name:", font=("Arial", 15, 'bold'), fg="#262c5f", bg="#addbed", bd=1)
name_label.place(x=40, y=40)

name_entry = Entry(im_lable, font=("Arial", 15, 'bold'), textvariable=name_var, relief=RIDGE, bd=1, width=35)
name_entry.place(x=300, y=40)

profession_label = Label(im_lable, text="Profession :", bd=0, font=("Arial", 15, 'bold'), fg=fg1, bg=bg1, relief=RIDGE)
profession_label.place(x=40, y=90)

profession_entry = Entry(im_lable, font=("Arial", 15, 'bold'), textvariable=profession_var, relief=RIDGE, bd=1,
                         width=35)
profession_entry.place(x=300, y=90)

study_label = Label(im_lable, text="Study of Subject:", bd=0, font=("Arial", 15, 'bold'), fg=fg1, bg=bg1, relief=RIDGE)
study_label.place(x=40, y=140)

study_entry = Entry(im_lable, font=("Arial", 15, 'bold'), textvariable=study_var, relief=RIDGE, bd=1, width=35)
study_entry.place(x=300, y=140)

dream_label = Label(im_lable, text="Dream :", bd=0, font=("Arial", 15, 'bold'), fg=fg1, bg=bg1, relief=RIDGE)
dream_label.place(x=40, y=190)

dream_entry = Entry(im_lable, font=("Arial", 15, 'bold'), textvariable=dream_var, relief=RIDGE, bd=1, width=35)
dream_entry.place(x=300, y=190)

skil_label = Label(im_lable, text="Skil :", bd=0, font=("Arial", 15, 'bold'), fg=fg1, bg=bg1, relief=RIDGE)
skil_label.place(x=40, y=240)

skil_entry = Entry(im_lable, font=("Arial", 15, 'bold'), relief=RIDGE, bd=1, textvariable=skil_var, width=35)
skil_entry.place(x=300, y=240)

game_label = Label(im_lable, text="Outside Game :", bd=0, font=("Arial", 15, 'bold'), fg=fg1, bg=bg1, relief=RIDGE)
game_label.place(x=40, y=290)

game_entry = Entry(im_lable, font=("Arial", 15, 'bold'), relief=RIDGE, bd=1, width=35, textvariable=game_var)
game_entry.place(x=300, y=290)

text1 = "Story Loading..."


# ================================== Story post ======================
story_lable = Frame(f, width=740, height=300, bg='#addbed', bd=8, relief=RIDGE)
story_lable.place(x=20, y=460)
story_title = Label(story_lable, text="Story:", font=("Arial", 15, 'bold'), relief=RIDGE, bd=0, bg=bg1)
story_title.place(x=350, y=10)

textbox = Text(story_lable, width=73, height=9, font=("Arial", 12, 'bold'), bd=5, relief=RIDGE)
textbox.place(x=30, y=50)
textbox.insert(END, text1)


def story_sub():
    if name_entry.get() == '':
        messagebox.showinfo("Error", "Please enter your Name")

    elif dream_entry.get() == '':
        messagebox.showinfo("Error", "please enter your Dream Name")
    elif skil_entry.get() == '':
        messagebox.showinfo("Error", "Please enter your Skil Name")
    elif profession_entry.get() == '':
        messagebox.showinfo("Error", "Please enter your professions")
    elif game_entry.get() == '':
        messagebox.showinfo("Error", "Please enter your Outside Game Name")

    else:
        text_story = (
            f"My name is {name_var.get()}, and I am a dedicated {profession_var.get()} pursuing a degree in {study_var.get()}. My dream is to obtain a {dream_var.get()} degree in my field of study, and I am fully committed to achieving this goal. My passion lies in {skil_var.get()}, and I devote much of my time to studying various {study_var.get()}. Outside of academics, I find joy in playing {game_var.get()}, which not only keeps me physically active but also fosters teamwork and camaraderie. While my primary focus is on my studies and {skil_var.get()} work, I always make time for the things that bring me happiness and fulfillment.")

        textbox.delete(1.0, END)
        textbox.insert(END, text_story)


button_fream = Frame(f, width=740, height=50, bd=8, relief=RIDGE, bg=bg1)
button_fream.place(x=20, y=405)
button_submit = Button(button_fream, text="Submit", font=("Arial", 10, 'bold'), bg=bg1, fg='blue', command=story_sub)

button_submit.place(x=340, y=3)

root.mainloop()
