from flask import Flask , render_template
app = Flask(__name__)

name = '茱萸'
blogs = [
    {'title':'Python学习笔记-Flask' , 'text':''},
    {'title':'Scrapy复习' , 'text':''}
]



@app.route('/')
def hello():
    return render_template('index.html' , name=name , blogs=blogs)


