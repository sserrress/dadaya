from flask import Flask
app =FLask(__name__)
@app.route('/')
def index():
return "Привет, мир!"
app.rin(port='8000')
