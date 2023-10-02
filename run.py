import requests
import json
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

app = Tk()
app.title("Dev (Parody)")
app.iconbitmap('icon.ico')
row_no = 12

logo_img = ImageTk.PhotoImage(Image.open('gigachad.png'))

def insultfr():
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    response = requests.get(url)
    data = response.json()
    insultapi = data["insult"]
    return insultapi

def send():
    global row_no
    webhook_url = webhook_entry.get()
    user_id = target_entry.get()
    profile_pic_url = profile_pic_entry.get()
    insult = insultfr()
    message = {
        'content': f"<@{user_id}> {insult}",
        'username': botname_entry.get(),
        'avatar_url': profile_pic_url
    }

    payload = json.dumps(message)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=payload.encode('utf-8'), headers=headers)

    if response.status_code == 204:
        msg = (
            "[" + datetime.now().strftime('%H:%M:%S') + "] [" + "INFO" + "] " + "Insult sent successfully" + f"\n{insult}")
        print_label = Label(app, text=msg, fg="green")
    else:
        msg = (
            f"[{datetime.now().strftime('%H:%M:%S')}] [INFO] Failed to send message. Status code: {response.status_code}")
        print_label = Label(app, text=msg, fg="red")
    print_label.grid(row=row_no, column=2)
    row_no += 2

def send_custom():
    global row_no
    webhook_url = webhook_entry.get()
    user_id = target_entry.get()
    profile_pic_url = profile_pic_entry.get()
    cust_msg = custom_msg_entry.get('1.0', 'end-1c')

    message = {
        'content': f"<@{user_id}> {cust_msg}",
        'username': botname_entry.get(),
        'avatar_url': profile_pic_url
    }

    payload = json.dumps(message)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=payload.encode('utf-8'), headers=headers)

    if response.status_code == 204:
        print_label = Label(app, text="Message sent successfully", fg="green")
    else:
        resp_print = (f'Failed to send message. Status code: {response.status_code}')
        print_label = Label(app, text=resp_print, fg="red")
    print_label.grid(row=row_no, column=2)
    row_no += 1

webhook_entry = Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
webhook_entry.insert(0, "dewebhook")
webhook_entry.grid(row=1, column=2)

profile_pic_entry = Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
profile_pic_entry.insert(0, "pp")
profile_pic_entry.grid(row=2, column=2)

botname_entry = Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
botname_entry.insert(0, "Dev (Parody)")
botname_entry.grid(row=3, column=2)

target_entry = Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
target_entry.insert(0, "uid")
target_entry.grid(row=4, column=2)

custom_msg_entry = Text(app, borderwidth=4, bg="#D2CDCC", width=100, height=5)
custom_msg_entry.grid(row=5, column=2, rowspan=3)

giga_chad = Label(app, image=logo_img)
giga_chad.grid(row=0, column=0)

welcome = Label(app, text="""
███████╗░█████╗░██╗░░░░░░█████╗░░█████╗░███╗░░██╗███████╗░░███╗░░░░███╗░░░█████╗░░░███╗░░
██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗████╗░██║╚════██║░████║░░░████║░░██╔══██╗░████║░░
█████╗░░███████║██║░░░░░██║░░╚═╝██║░░██║██╔██╗██║░░░░██╔╝██╔██║░░██╔██║░░╚█████╔╝██╔██║░░
██╔══╝░░██╔══██║██║░░░░░██║░░██╗██║░░██║██║╚████║░░░██╔╝░╚═╝██║░░╚═╝██║░░██╔══██╗╚═╝██║░░
██║░░░░░██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║░░██╔╝░░███████╗███████╗╚█████╔╝███████╗
╚═╝░░░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚══════╝""")
welcome.grid(row=0, column=1, columnspan=8)

ask_webhook = Label(app, text="What's your webhook? ", fg="blue", font=('Times New Roman', 15, 'bold'))
ask_webhook.grid(row=1, column=0)

ask_botprofile_pic = Label(app, text="Enter URL for Profile pic for your bot: ", fg="blue", font=('Times New Roman', 15, 'bold'))
ask_botprofile_pic.grid(row=2, column=0)

ask_bot_name = Label(app, text="Enter name for Bot: ", fg="blue", font=('Times New Roman', 15, 'bold'))
ask_bot_name.grid(row=3, column=0)

ask_target = Label(app, text="Enter Target User ID: ", fg="blue", font=('Times New Roman', 15, 'bold'))
ask_target.grid(row=4, column=0)

ask_custom_msg = Label(app, text="Enter Custom Message: ", fg="blue", font=('Times New Roman', 15, 'bold'))
ask_custom_msg.grid(row=5, column=0)

send_button = Button(app, text="Send Insult", fg="white", bg="blue", padx=50, pady=5, command=send)
send_button.grid(row=8, column=2, pady=(5, 5))

cus_send_button = Button(app, text="Send Custom", fg="white", bg="blue", padx=50, pady=5, command=send_custom)
cus_send_button.grid(row=9, column=2, pady=(5, 0))

app.mainloop()
