from tkinter import *
from tkinter import ttk
import pyshorteners
from tkinter import messagebox
import pyperclip
from pyshorteners.exceptions import *
import qrcode
from PIL import ImageTk
from tkinter import filedialog


BACKGROUND_THEME = "#333333"
URL_PLACEHOLDER = "https://www.example.com/"


def shorten_url():
    """Shorten the URL using one of the available services which the user chooses"""
    url = url_entry.get()

    if url == "" or url == URL_PLACEHOLDER:
        messagebox.showerror(title="Error", message="Enter a valid URL")
        return

    if shortener_choice.get() not in shorteners:
        messagebox.showerror(title="Error", message="You need to select a Shortener service")
        return

    short = pyshorteners.Shortener()
    service = shortener_choice.get()

    shortener_methods = {
        "TinyURL": short.tinyurl.short,
        "Clck.ru": short.clckru.short,
        "Chilp.it": short.chilpit.short,
        "Git.io": short.gitio.short,
        "OSDB": short.osdb.short,
        "Ow.ly": short.owly.short,
        "Da.gd": short.dagd.short
    }

    try:
        shortened_url = shortener_methods[service](url)
        short_url_entry.delete(0, END)
        short_url_entry.insert(0, shortened_url)
        generate_qr(shortened_url)

    except (BadAPIResponseException, ShorteningErrorException, ExpandingErrorException):
        messagebox.showerror(title="Error", message="An unexpected error occurred. Try another service.")

    except BadURLException:
        messagebox.showerror(title="Error", message="Please enter a valid URL")


def generate_qr(url):
    """Generate QR code from the shortened URL"""
    qr = qrcode.QRCode(version=1, box_size=5, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    global qr_image
    qr_image = qr.make_image(fill_color="black", back_color="white")

    qr_link = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_link)
    qr_label.image = qr_link

    save_qr_btn.grid(row=6, column=1, sticky="w", pady=10)
    clear_btn.grid(row=6, column=2, sticky="e", pady=10)

    window.update_idletasks()
    window.geometry("")


def save_qr():
    """Save the QR code as image on user-chosen path"""
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
    )
    if save_path:
        qr_image.save(save_path)


def clean_url():
    """Clear everything to prepare for another use"""
    url_entry.delete(0, END)
    url_entry.insert(END, URL_PLACEHOLDER)
    url_entry.config(fg="gray")

    shortener_choice.set("Select a Shortener Service")
    short_url_entry.delete(0, END)

    qr_label.config(image="")
    save_qr_btn.grid_forget()
    clear_btn.grid_forget()
    # resize back
    window.update_idletasks()
    window.geometry("")


def on_entry_click(event):
    """Clear the URL Placeholder when the user click in the entry widget """
    if url_entry.get() == URL_PLACEHOLDER:
        url_entry.delete(0, END)
        url_entry.config(fg="black")


def out_entry_click(event):
    """Restore the URL Placeholder"""
    if url_entry.get() == "":
        url_entry.insert(END, URL_PLACEHOLDER)
        url_entry.config(fg="gray")


def on_click_copy(event):
    """Copy shortened URL to clipboard"""
    if short_url_entry.get():
        pyperclip.copy(short_url_entry.get())
        status_label.config(text="✓ Copied to clipboard!", fg="#00FF00")
        window.after(3000, lambda: status_label.config(text=""))


# ---------------- UI ----------------

window = Tk()
window.title("URL Shortener")
window.config(bg=BACKGROUND_THEME, padx=20, pady=20)

frame = Frame(window, bg=BACKGROUND_THEME)
frame.pack(padx=30, pady=30)

url_shortener_label = Label(
    frame, text="URL Shortener",
    bg=BACKGROUND_THEME, fg="#FF3399",
    font=("Arial", 30)
)
url_shortener_label.grid(row=0, column=1, columnspan=2, pady=30)

Label(frame, text="URL", bg=BACKGROUND_THEME, fg="white", font=("Arial", 16)).grid(row=1, column=0)
Label(frame, text="Shortening Service", bg=BACKGROUND_THEME, fg="white", font=("Arial", 16)).grid(row=2, column=0)
Label(frame, text="Shortened URL", bg=BACKGROUND_THEME, fg="white", font=("Arial", 16)).grid(row=3, column=0)

url_entry = Entry(frame, width=35, fg="gray")
url_entry.insert(0, URL_PLACEHOLDER)
url_entry.bind("<FocusIn>", on_entry_click)
url_entry.bind("<FocusOut>", out_entry_click)
url_entry.grid(row=1, column=1, pady=15)

# Shortener services available to use
shorteners = ["TinyURL", "Clck.ru", "Chilp.it", "Git.io", "OSDB", "Ow.ly", "Da.gd"]

shortener_choice = ttk.Combobox(frame, values=shorteners, state="readonly", width=34)
shortener_choice.set("Select a Shortener Service")
shortener_choice.grid(row=2, column=1)

short_url_entry = Entry(frame, width=35)
short_url_entry.bind("<FocusIn>", on_click_copy) # copy URL just by clicking in the entry
short_url_entry.grid(row=3, column=1, pady=15)

Button(
    frame, text="Shorten URL",
    bg="#FF3399", fg="white",
    font=("Arial", 16),
    command=shorten_url
).grid(row=4, column=1, pady=20, columnspan=2)

qr_label = Label(frame, bg=BACKGROUND_THEME)
qr_label.grid(row=5, column=1, columnspan=2, pady=15)

save_qr_btn = Button(
    frame, text="Save QR",
    bg="#FF3399", fg="white",
    font=("Arial", 14),
    command=save_qr
)

clear_btn = Button(
    frame, text="Clear",
    bg="#FF3399", fg="white",
    font=("Arial", 14),
    command=clean_url
)

status_label = Label(window, text="", bg=BACKGROUND_THEME, fg="white")
status_label.pack(side=BOTTOM, fill=X)

window.mainloop()
