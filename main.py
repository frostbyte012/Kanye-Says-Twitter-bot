from tkinter import *
import requests

def get_final_quote():
    quote=get_quote()
    canvas.itemconfig(quote_text, text=quote)

def get_quote():
        request=requests.get(url="https://api.kanye.rest")
        quote=request.json()["quote"]
        request.raise_for_status()
        return quote




window = Tk()
window.title("Kanye Says")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
first_quote=get_quote()
quote_text = canvas.create_text(150, 207, text=first_quote, width=250, font=("Arial", 30, "bold"), fill="green")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_final_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()