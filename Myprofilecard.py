"""
1) Add the file name and activity details.
   a) Mention the file name as `my-profile-card.py`.
   b) Mention the activity name as "My Profile Card".
   c) Mention the lesson topic and grade range.

2) Import Tkinter and create the main window.
   a) Import everything from the `tkinter` module.
   b) Create the main window using `Tk()`.
   c) Set the window title.
   d) Set the window size using `geometry()`.

3) Add the title label.
   a) Create a `Label` for the heading "My Profile Card".
   b) Add text colour, background colour, and width.
   c) Place it at the top using `grid()`.
   d) Use `columnspan` to make it stretch across two columns.

4) Add name and hobby input fields.
   a) Create a label for "Name".
   b) Create an `Entry` box for typing the name.
   c) Create a label for "Hobby".
   d) Create an `Entry` box for typing the hobby.
   e) Place all labels and entries using `grid()`.

5) Create the About Me section.
   a) Add a `Frame` to group the About Me content.
   b) Use border and relief to make the frame visible.
   c) Add an About Me label inside the frame.
   d) Add a `Text` box for writing a short description.
   e) Use `pack()` to place widgets inside the frame.

6) Add the submit button.
   a) Create a button with the text "Show My Card".
   b) Style it with background colour, text colour, and width.
   c) Place it using `grid()` across two columns.

7) Run the Tkinter window.
   a) Use `window.mainloop()` to keep the window open.
"""

from tkinter import *

window = Tk()
window.title("My Profile Card")
window.geometry("400x300")

# Ttile label
title_label = Label(window, text="My Profile Card", bg="blue", fg="white", width=30)
title_label.grid(row=0, column=0, columnspan=2)

# Name and hobby input fields
name_label = Label(window, text="Name:")
name_label.grid(row=1, column=0, )
name_entry = Entry(window)
name_entry.grid(row=1, column=1)

hobby_label = Label(window, text="Hobby:")
hobby_label.grid(row=2, column=0)
hobby_entry = Entry(window)
hobby_entry.grid(row=2, column=1)

# About me section
about_me_frame = Frame(window, bg="green", bd=5, relief="sunken")
about_me_frame.grid(row=3, column=0, columnspan=2, pady=10)

about_me_label = Label(about_me_frame, text="About Me", bg="green", fg="white")
about_me_label.pack()

about_me_text = Text(about_me_frame, height=5, width=30)
about_me_text.pack()

# Sumbit button
sumbit_button = Button(window, text="Show My card", bg="blue", fg="black", width=30)
sumbit_button.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()

