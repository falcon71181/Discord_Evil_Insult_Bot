import requests
import json
import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime

# Create the main application window
app = tk.Tk()
app.title("Dev (Parody)")
app.iconbitmap('icon.ico')

# Initialize row number for grid layout
row_no = 12

# Load the logo image
logo_img = ImageTk.PhotoImage(Image.open('gigachad.png'))

# Function to fetch a random insult from the API
def fetch_random_insult():
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    response = requests.get(url)
    data = response.json()
    insult = data["insult"]
    return insult

# Function to send a message using the Discord webhook
def send_message():
    global row_no

    webhook_url = webhook_entry.get()
    user_id = target_entry.get()
    profile_pic_url = profile_pic_entry.get()
    insult = fetch_random_insult()

    message = {
        'content': f"<@{user_id}> {insult}",
        'username': botname_entry.get(),
        'avatar_url': profile_pic_url
    }

    payload = json.dumps(message)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(webhook_url, data=payload.encode('utf-8'), headers=headers)

    if response.status_code == 204:
        msg = f"[{datetime.now().strftime('%H:%M:%S')}] [INFO] Insult sent successfully\n{insult}"
        print_label = tk.Label(app, text=msg, fg="green")
    else:
        msg = f"[{datetime.now().strftime('%H:%M:%S')}] [INFO] Failed to send message. Status code: {response.status_code}"
        print_label = tk.Label(app, text=msg, fg="red")

    print_label.grid(row=row_no, column=2)
    row_no += 2

# Function to send a custom message using the Discord webhook
def send_custom_message():
    global row_no

    webhook_url = webhook_entry.get()
    user_id = target_entry.get()
    profile_pic_url = profile_pic_entry.get()
    custom_msg = custom_msg_entry.get('1.0', 'end-1c')

    message = {
        'content': f"<@{user_id}> {custom_msg}",
        'username': botname_entry.get(),
        'avatar_url': profile_pic_url
    }

    payload = json.dumps(message)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(webhook_url, data=payload.encode('utf-8'), headers=headers)

    if response.status_code == 204:
        print_label = tk.Label(app, text="Message sent successfully", fg="green")
    else:
        resp_print = f'Failed to send message. Status code: {response.status_code}'
        print_label = tk.Label(app, text=resp_print, fg="red")

    print_label.grid(row=row_no, column=2)
    row_no += 1

# Create and configure tkinter widgets
webhook_entry = tk.Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
webhook_entry.insert(0, "https://discord.com/api/webhooks/your_webhook_url_here")
webhook_entry.grid(row=1, column=2)

profile_pic_entry = tk.Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
profile_pic_entry.insert(0, "https://example.com/your_bot_image.png")
profile_pic_entry.grid(row=2, column=2)

botname_entry = tk.Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
botname_entry.insert(0, "Dev (Parody)")
botname_entry.grid(row=3, column=2)

target_entry = tk.Entry(app, borderwidth=4, bg="#D2CDCC", width=100)
target_entry.insert(0, "715602301632643177")
target_entry.grid(row=4, column=2)

custom_msg_entry = tk.Text(app, borderwidth=4, bg="#D2CDCC", width=100, height=5)
custom_msg_entry.grid(row=5, column=2, rowspan=3)

giga_chad = tk.Label(app, image=logo_img)
giga_chad.grid(row=0, column=0)

welcome = tk.Label(app, text="""
 /¯¯¯¯\/¯¯¯¯¯¯\        |\¯¯¯¯¯\  |\¯¯¯¯¯\'    |\¯¯¯¯¯¯\    /¯¯¯¯¯ /|     °          
|                      |       |;|         | |;|         |    |;|          |   |          |:'|                
|         |\ _____ /|'      |/         /  |/        /|'‚   |;|          |   \          \;|                
'\         \/¯¯¯¯¯¯\'     /          /  /        /;'|'‚   |/          /|‘   \          \|                
 |        |\______ /|‘   |           \/         /;;:|   /          /;;|'    \          \‘               
 |        |/¯¯¯¯¯¯¯\‚   |\                   /;;;;;|   |          |;'/°      \          \/¯¯¯¯¯¯\'‚
 |\____/\ ______/|'   |;;\ ________ /;;;;;/‘   |\_____\/‘         |                      |'‚
 |;||¯¯¯||'||¯¯¯¯¯|;'|‘   |;;;||¯¯¯¯¯¯¯||;;;;'/      |;||¯¯¯¯||'         /______/\_____/|‘ 
 |;||     ||'||         |;'|‘    \;;||            ||;;'/        |;||       ||'         ||¯¯¯¯¯||;||¯¯¯¯||;|°
 '\||___||'||_____|'/‘       \||_______||/    °      \||____||°        ||         ||;||       ||;| 
    ¯¯     ¯¯¯¯¯°             ¯¯¯¯¯ ‘                ¯¯¯¯°          ||_____||;||____||/  
               '                                    '                °             ¯¯¯¯      ¯¯¯¯‘   
      '                               '                     '‚                              ‘               
                  '        '                                   by '‚falcon71181‘                             
          '                                     '                     '‚                                   ‘
""", fg="#FF7801")
welcome.grid(row=0, column=1, columnspan=8)

# Labels for input fields
label_texts = [
    "What's your webhook? ",
    "Enter URL for Profile pic for your bot: ",
    "Enter name for Bot: ",
    "Enter Target User ID: ",
    "Enter Custom Message: ",
]

for i, text in enumerate(label_texts):
    label = tk.Label(app, text=text, fg="blue", font=('Times New Roman', 15, 'bold'))
    label.grid(row=i + 1, column=0)

# Buttons to send insults and custom messages
send_button = tk.Button(app, text="Send Insult", fg="white", bg="blue", padx=50, pady=5, command=send_message)
send_button.grid(row=8, column=2, pady=(5, 5))

cus_send_button = tk.Button(app, text="Send Custom", fg="white", bg="blue", padx=50, pady=5, command=send_custom_message)
cus_send_button.grid(row=9, column=2, pady=(5, 0))

# Start the tkinter main loop
app.mainloop()
