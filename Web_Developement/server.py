from crypt import methods
from distutils.log import error
import email
from email import message
from unicodedata import name
from flask import Flask, render_template, request,redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:

          data = request.form.to_dict()
          print(data)
          write_to_csv(data)
          return redirect('/thankyou.html')#data
        except:
          return "Something went wrong to save data!"   

    else:
        return "Something went wrong!"

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



''' 
@app.route("/works.html")
def works():
    return render_template('./works.html')


@app.route("/about.html")
def about():
    return render_template('./about.html')
'''

''' 
@app.route("/<username>/<int:post_id>")
def hello_world(username=None,post_id=None):
    return render_template('./index.html',name=username,post_id=post_id)

'''
