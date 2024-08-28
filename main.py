from tkinter import *
import requests
from api_key import API_KEY
from tkinter import messagebox  # Import messagebox

def Generate():
    category = 'happiness'  # Set a default category or use input
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    
    if response.ok:
        quotes_data = response.json()
        if quotes_data:  # Check if there are quotes
            # Display the first quote from the list
            quote_info = quotes_data[0]
            quote = quote_info.get('quote', 'No quote available')
            author = quote_info.get('author', 'Unknown author')
            messagebox.showinfo("Quote", f"Quote: {quote}\nAuthor: {author}")
        else:
            messagebox.showinfo("Quote", "No quotes found.")
    else:
        messagebox.showerror("Error", f"Error: {response.status_code} - {response.text}")

# Initialize Tkinter window
win = Tk()
win.title("Quote Generator")

win.geometry("300x150")
win.tk.call('tk', 'scaling', 3.0)

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)
win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=1)
win.grid_rowconfigure(2, weight=1)

# Create and place the button
bntGen = Button(win, text="Generate", command=Generate)
bntGen.grid(column=1, row=1, sticky="nsew")

win.mainloop()
