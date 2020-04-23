from flask import Flask, render_template, redirect, request
import csv
app = Flask(__name__)

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/')
def landing_page():
    return render_template('./index.html')

@app.route('/<string:page>')
def render_page(page):
    return render_template(f'./{page}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return redirect('/contact.html')
    else:
        return redirect('/contact.html')