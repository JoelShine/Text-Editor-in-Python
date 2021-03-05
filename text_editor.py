from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from PIL import ImageTk, Image
import webbrowser
from tkhtmlview import HTMLLabel


root = Tk()
root.title("My Text Editor")
root.iconbitmap("text.ico")

## below is the code for centering app in the screen
app_width = 1200
app_height = 565

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
	## above is the code for centering app in the screen (till above)


global open_status_name
open_status_name = False

global selected
selected = False

def new_file():
	my_text.delete("1.0", END)
	root.title("New File - My Text Editor")
	status_bar.config(text="New File        ")

	global open_status_name
	open_status_name = False

def open_file():
	my_text.delete("1.0", END)

	text_file = filedialog.askopenfilename(initialdir="C:/Users/joels/Desktop", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

	if text_file:
		global open_status_name
		open_status_name = text_file
		#name = name.replace("what do you want to replace", "")
		name = text_file
		status_bar.config(text=f"{name}        ")
		root.title(f"{name} - My Text Editor")

		text_file = open(text_file, 'r')
		stuff = text_file.read()

		my_text.insert(END, stuff)

		text_file.close()

def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/joels/Desktop", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
	if text_file:
		name = text_file
		root.title(f"{name} - My Text Editor (Saved)")
		status_bar.config(text=f"{name} Saved !        ")

		text_file = open(text_file, 'w')
		text_file.write(my_text.get(1.0, END))

		text_file.close()

def save_file():
	global open_status_name

	if open_status_name:
		text_file = open(open_status_name, 'w')
		text_file.write(my_text.get(1.0, END))

		text_file.close()
		status_bar.config(text=f"Saved : {open_status_name}        ")

	else:
		save_as_file()

def cut_text(e):
	global selected

	if e:
		selected = root.clipboard_get()

	else:
		if my_text.selection_get():
			selected = my_text.selection_get()
			my_text.delete("sel.first", "sel.last")
			root.clipboard_clear()
			root.clipboard_append(selected)

def copy_text(e):
	global selected
	if e:
		selected = root.clipboard_get()

	if my_text.selection_get():
		selected = my_text.selection_get()
		root.clipboard_clear()
		root.clipboard_append(selected)

def paste_text(e):
	global selected
	if e:
		selected = root.clipboard_get()

	else:
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position, selected) 

def bold_it():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	my_text.tag_configure("bold", font=bold_font)

	current_tags  = my_text.tag_names("sel.first")

	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		my_text.tag_add("bold", "sel.first", "sel.last")

def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	my_text.tag_configure("italic", font=italics_font)

	current_tags  = my_text.tag_names("sel.first")

	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		my_text.tag_add("italic", "sel.first", "sel.last")

def text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		color_font = font.Font(my_text, my_text.cget("font"))

		my_text.tag_configure("colored", font=color_font, foreground=my_color)

		current_tags  = my_text.tag_names("sel.first")

		if "colored" in current_tags:
			my_text.tag_remove("colored", "sel.first", "sel.last")
		else:
			my_text.tag_add("colored", "sel.first", "sel.last")

def bg_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

def all_text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)

def select_all(e):
	my_text.tag_add('sel', '1.0', 'end')

def clear_all():
	my_text.delete(1.0, END)

def night_on():
	main_color = "#000000"
	root_color = "#373737"
		
	root.config(bg=root_color)
	status_bar.config(bg=root_color, fg="white")
	my_text.config(bg=main_color, fg="white",insertbackground="white") ## insert background is the cursor position colour
	toolbar_frame.config(bg=root_color)
	bold_button.config(bg=main_color, fg="white")
	italics_button.config(bg=main_color, fg="white")
	undo_button.config(bg=main_color, fg="white")
	redo_button.config(bg=main_color, fg="white")
	color_text_button.config(bg=main_color, fg="white")
	search_button.config(bg=main_color, fg="white")

	file_menu.config(bg=main_color, fg="white")
	edit_menu.config(bg=main_color, fg="white")
	color_menu.config(bg=main_color, fg="white")
	options_menu.config(bg=main_color, fg="white")

def light_on():
	main_color = "white"
	root_color = "white"
		
	root.config(bg=root_color)
	status_bar.config(bg=root_color, fg="black")
	my_text.config(bg=main_color, fg="black",insertbackground="black") ## insert background is the cursor position colour
	toolbar_frame.config(bg=root_color)
	bold_button.config(bg=main_color, fg="black")
	italics_button.config(bg=main_color, fg="black")
	undo_button.config(bg=main_color, fg="black")
	redo_button.config(bg=main_color, fg="black")
	color_text_button.config(bg=main_color, fg="black")
	search_button.config(bg=main_color, fg="black")

	file_menu.config(bg=main_color, fg="black")
	edit_menu.config(bg=main_color, fg="black")
	color_menu.config(bg=main_color, fg="black")
	options_menu.config(bg=main_color, fg="black")

def my_popup(e):
	the_menu.tk_popup(e.x_root, e.y_root)

def Help():
	my_text.delete("1.0", END)

	help_file = "help.txt"

	if help_file:
		global open_status_name
		open_status_name = help_file
		#name = name.replace("what do you want to replace", "")
		name = help_file
		status_bar.config(text=f"{name}        ")
		root.title(f"{name} - My Text Editor")

		help_file = open(help_file, 'r')
		stuff = help_file.read()

		my_text.insert(END, stuff)

		help_file.close()

def google():
	s = my_text.selection_get()
	webbrowser.open(f"https://www.google.com/search?q={s}")

def github():
	webbrowser.open("https://github.com/JoelShine/Text-Editor-in-Python")


toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)
		
my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

my_text = Text(my_frame, width=97, height=20, font=("Helevetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

my_menu = Menu(root)
root.config(menu=my_menu)

## tearoff=False means that the line on the menu will be removed.

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut        ", command=lambda: cut_text(False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy        ", command=lambda: copy_text(False), accelerator="Ctrl+C")
edit_menu.add_command(label="Paste        ", command=lambda: paste_text(False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo        ", command=my_text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo        ", command=my_text.edit_redo, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all(True), accelerator="Ctrl+A")
edit_menu.add_command(label="Clear", command=clear_all, accelerator="Ctrl+Y")

color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text Color", command=text_color)
color_menu.add_command(label="All Text Color", command=all_text_color)
color_menu.add_command(label="Background Text Color", command=bg_color)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Themes", menu=options_menu)
options_menu.add_command(label="Light Mode", command=light_on)
options_menu.add_command(label="Dark Mode", command=night_on)

the_menu = Menu(my_menu, tearoff=False)
the_menu.add_command(label="Help", command=Help)
the_menu.add_command(label="Search in Google", command=google)
the_menu.add_separator()
the_menu.add_command(label="Exit", command=root.quit)

help_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help Readme", command=Help)
help_menu.add_command(label="Search in Google", command=google)

about_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Find us on Github", command=github)

status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-a>', select_all)
#root.bind('<Control-Key-+>', zoom_in)
#root.bind('<Control-Key-->', zoom_out)
root.bind('<Button-3>', my_popup)

bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=7)

italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5)

undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)

redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)

search_button = Button(toolbar_frame, text="Search", command=google)
search_button.grid(row=0, column=5, padx=5)

root.mainloop()
