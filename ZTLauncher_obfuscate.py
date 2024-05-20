import webbrowser
from selenium import webdriver
from pathlib import Path
from tkinter import Tk, Canvas, END, Text, Button, PhotoImage, messagebox
import requests
import subprocess
import pyperclip
import webbrowser

import os, subprocess, sys, requests, time, httpx
from pystyle import System
from discord_webhook import DiscordWebhook
from secrets import token_hex
from os import popen, environ
from subprocess import call
from PIL import ImageGrab
import tkinter.messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\UI\.img")  # เปลี่ยนด้วย ที่อยู่รูปภาพ

discord = "https://discord.com/users/1119676900462313572"

# เพิ่มฟังก์ชันการส่งแจ้งเตือนผ่าน LINE
def send_line_notify(message):
    line_notify_token = '5hBpSkLVXX5ryunQVB946nfCMkjUYZ7ApWsKPce2f79'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    data = {'message': message}
    requests.post(line_notify_api, headers=headers, data=data)

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        return response.json()["ip"]
    except requests.RequestException:
        return "ไม่สามารถดึง IP ได้"

def get_hwid():
    try:
        return subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    except subprocess.CalledProcessError:
        return "ไม่สามารถดึง HWID ได้"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

processes = []

def R1():
    proc = subprocess.Popen(['C:\\Program Files\\Information Luncher\\ZEROTWO.exe'])
    processes.append(proc)
    webbrowser.open(discord)
    messagebox.showwarning("error", f"- โปรแกรมมีปัญหากรุณารออัพเดต\n\n- ERR404 Please Contact Annart X\n\n- HWID: {hwid}")

def R2():
    proc = subprocess.Popen(['C:\\Program Files\\Information Luncher\\ZEROTWO AIM&SPC Launcher.exe'])
    processes.append(proc)
    messagebox.showwarning("success", "- เปิดใช้งานโปรแกรมเสร็จสิ้น")

def R3():
    window_1.destroy()

def on_closing():
    for proc in processes:
        proc.terminate()
    window_1.destroy()

def start_move(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def stop_move(event):
    x_offset = None
    y_offset = None

def on_motion(event):
    x = event.x_root - x_offset
    y = event.y_root - y_offset
    window_1.geometry(f'+{x}+{y}')

window_1 = Tk()
window_1.config(bg="#FFFFFF")

# ตั้งค่าขนาดและตำแหน่งของหน้าต่าง
width_of_window_1 = 802
height_of_window_1 = 397
screen_width = window_1.winfo_screenwidth()
screen_height = window_1.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window_1 / 2)
y_coordinate = (screen_height / 2) - (height_of_window_1 / 2)
window_1.geometry("%dx%d+%d+%d" % (width_of_window_1, height_of_window_1, x_coordinate, y_coordinate))

# ตั้งชื่อและไอคอนของหน้าต่าง
window_1.title("ZT Launcher 2.0")
window_1.iconbitmap(relative_to_assets("C:\Program Files\Information Luncher\.img\main.ico"))  # เปลี่ยน path ให้ถูกต้องตามที่อยู่ของไฟล์ icon.ico

# ผูกเหตุการณ์การลากหน้าต่าง
window_1.bind("<ButtonPress-1>", start_move)
window_1.bind("<ButtonRelease-1>", stop_move)
window_1.bind("<B1-Motion>", on_motion)

canvas_2 = Canvas(
    window_1,
    bg="#FFFFFF",
    height=900,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas_2.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("Zerotwo.png"))
image_1 = canvas_2.create_image(401.0, 200.0, image=image_image_1)

button_image_1 = PhotoImage(file=relative_to_assets("start1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: R1(),
    relief="flat"
)
button_1.place(
    x=614.0,
    y=222.0,
    width=189.0,
    height=43.0
)

button_image_2 = PhotoImage(file=relative_to_assets("start2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: R2(),
    relief="flat"
)
button_2.place(
    x=614.0,
    y=278.0,
    width=189.0,
    height=43.0
)

window_1.resizable(False, False)
window_1.protocol("WM_DELETE_WINDOW", on_closing)

# ส่งการแจ้งเตือนเมื่อโปรแกรมเปิดขึ้น
ip_address = get_public_ip()
hwid = get_hwid()
send_line_notify(f"โปรแกรม ZT Launcher ถูกเปิดใช้งาน\nIP: {ip_address}\nHWID: {hwid}")

window_1.mainloop()
