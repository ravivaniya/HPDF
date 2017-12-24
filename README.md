#HPDF TASKS
###Description
  This repository contains tasks that I have worked on during HPDF Week 1.
###Getting Started
  To know the project tasks just [Click Here](https://docs.google.com/document/d/1cnCbFkgn-A7pSONDTX9AlIzaqyWlZFZAT4xncfAYXcc/edit?ts=5a1e8781#heading=h.mobob3mkdw86).The list of these tasks are given to us(fellow interns) just to improve our fundamental knowledge of Python & Flask and communication with other interns.I started with the references below.
###Prerequisites
- Python 3.x
- Flask
###How to use
1. Download python from [here](https://www.python.org/downloads/) and install it.
2. Then go to your command prompt and type
'''
$ pip install Flask
'''
then click enter to install flask on your computer. This command to install flask is for Windows only. Now install virtual environment into the Scripts folder of Python package. First open Scripts folder in the command prompt and type the command "pip install virtualenv" and then click enter. You also need to install flask and virtual environment directly into your project folder. Now you all set to go.
Tasks
1. Add an endpoint at / that displays Hello World along with your first name (and slack username)
2. Add and endpoint at /authors which fetches a list of authors and count of their posts using the given JSON data available via URLs https://jsonplaceholder.typicode.com/users and https://jsonplaceholder.typicode.com/posts
3. Add an endpoint at /setcookie which sets a cookie with values name=<your-first-name> and age=<your-age if not set already.
4. Add an endpoint at /getcookies which displays the values of the cookie that has been set with /setcookie endpoint.
5. Deny request to /robots.txt endpoint with 403 (Forbidden) status code.
6. Add an endpoint at /html displaying some placeholder HTML text. Lorem Ipsum was used here.
7. Display a form containing a textbox at /input endpoint.
8. Upon submitting the form at /input, send the data via a POST request to /input endpoint. This /input endpoint should display the text data received via the request instead of the form. Also log the received data to STDOUT.
References
https://www.tutorialspoint.com/flask 
http://flask.pocoo.org/docs/0.12/tutorial/ 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world 
https://docs.python.org/3/tutorial/
