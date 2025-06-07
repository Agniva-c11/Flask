# TEMPLATES AND HTML
from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = "GreyKnight"
    myresult = 10 + 20
    mylist = [1, 2, 3, 4]
    return render_template('index.html', myvalue = myvalue, myresult = myresult, mylist = mylist)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5002, debug = True)