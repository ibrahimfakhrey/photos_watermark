from tkinter import *
from PIL import Image, ImageFont, ImageDraw

root = Tk()

root.geometry("1000x1000")


# Add Text To Image
def add_it():
    # Open our image
    my_image = Image.open("car-967387_1280.png")
    # Define The Font
    text_font = ImageFont.truetype("arial.ttf", 46)
    # Get text to add to image
    text_to_add = my_entry.get()

    # Edit the Image
    edit_image = ImageDraw.Draw(my_image)
    edit_image.text((150, 300), text_to_add, ("green"), font=text_font)

    # Save The Image
    my_image.save("/Users/Admin/hopper2.jpeg")

    # Clear the entry box
    my_entry.delete(0, END)
    my_entry.insert(0, "Saving File...")

    # Wait a couple seconds and then show image
    my_label.after(2000, show_pic)


def show_pic():
    # Show New Image
    global aspen2
    aspen2 = PhotoImage(file="/Users/Admin/hopper2.jpeg")
    my_label.config(image=aspen2)

    # Clear the entry box
    my_entry.delete(0, END)


# Define Image
aspen = PhotoImage(file="car-967387_1280.png")
# Create A Label
my_label = Label(root, image=aspen)
my_label.pack(pady=20)

# Entry Box
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# Button
my_button = Button(root, text="Add Text To Image",
                   command=add_it, font=("Helvetica", 24))
my_button.pack(pady=20)

root.mainloop()