from flask import Flask  #flask->python package and Flask->class
from flask import render_template  #rendering any html page
from flask import request,make_response
from flask import redirect #url redirection
import requests

app = Flask(__name__) #app is an application object as an instance of class Flask

@app.route('/')  #@app.route() are known as decorators these are used as callbacks for certain events
@app.route('/index')
def index():
    return '<h2>Hello Friends! - My name is Ravi <br>This is my first Webapp based on flask</h2>'

@app.route('/authors',methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()  #fetch the json documents using get method
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']:{'name':d['name'],'count':0} for d in data} #list comprehension in python
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('authors.html',users=users)

@app.route('/givecookie')
def givecookie():
    return render_template('index.html')

@app.route('/setcookie',methods=['GET','POST'])
def setcookie():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        resp = make_response(render_template('cookieOutput.html'))
        resp.set_cookie('Name',name)
        resp.set_cookie('Age',age)
        return resp

@app.route('/getcookies',methods=['GET','POST'])
def getcookies():
    name = request.cookies.get('Name')
    age = request.cookies.get('Age')
    return '<h2>Welcome '+name+' you are '+age+' years old</h2>'

@app.route('/robots.txt')
def denyAccess():
    return redirect('http://httpbin.org/deny')

@app.route('/html')
@app.route('/image')
def renderHtmlPage():
    return render_template('test.html')

@app.route('/input')
def inputFile():
    return render_template('form.html')

@app.route('/output',methods=['GET','POST'])
def outputFile():
    text = request.form['txt']
    return render_template('output.html',text=text)

if __name__ == "__main__": #to run the app.
    app.run()