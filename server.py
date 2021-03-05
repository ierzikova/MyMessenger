from flask import Flask
import time


app = Flask('Bananagram')
stat={
        "status" : True,
        "name"   : "Bananagram",
        "server_time"   : time.time()}

@app.route("/")
def hello():
    return "<b>Hello, World!</b>, <br> " \
           "<a href=page2> Страница 2 </a>  <br>" \
           "<a href=status> Статус сервера</a> "

@app.route("/page2")
def page2():
    return "<b>'это Page 2</b>"

@app.route("/status")
def status():
    return stat


app.run()

