from tkinter import *

import requests


def register():
    discord_webhook_url = 'https://discord.com/api/webhooks/830266057125134356/DF3LsJYsGnhq6uUpaprsipjiml0-vDOTBE9mfRBC02HZsmrXt2Dq9vhT4ogj784zPPVr'
    Message = {
        "content": "Identification: "+f_id.get()+" Discord: "+f_discord.get()+" Roblox: "+f_roblox.get()
    }
    requests.post(discord_webhook_url, data=Message)
root = Tk()
root.title("BB5N Staff Register")
root.geometry("400x200")

f_id_label = Label(root, text="Register a staff code here")
f_id_label.pack()
f_id = Entry(root, width=50)
f_id.pack()
f_discord_label = Label(root, text="Whats their discord?")
f_discord_label.pack()
f_discord = Entry(root, width=50)
f_discord.pack()
f_roblox_label = Label(root, text="Whats their roblox?")
f_roblox_label.pack()
f_roblox = Entry(root, width=50)
f_roblox.pack()
loginbtn = Button(root, text="REGISTER", command=register, width=30)
loginbtn.pack()
f_username_label = Label(root, text="""Registering a user means that you are an admin, and have
access to this tool. Make sure people remember their codes!""")
f_username_label.pack()
root.mainloop()