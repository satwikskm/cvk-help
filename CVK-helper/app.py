from flask import Flask,render_template

from gui import *
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/index',methods=['POST'])
def index():
    
    return render_template('./index.html',name=output)
if __name__ == '__main__':
    app.run()