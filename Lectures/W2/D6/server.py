from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "super secret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = ''
    
    session['process_gold'] = {
        "Farm" : random.randint(10,20),
        "Cave" : random.randint(5,10),
        "House" : random.randint(2,5),
        "Casino" : random.randint(-50,50)
    }
    
    locations = {
        "Farm" : "(earns 10-20 golds)",
        "Cave" : "(earns 5-10 golds)",
        "House" : "(earns 2-5 golds)",
        "Casino" : "(earns/takes 0-50 golds)"
    }
    return render_template('index.html', locations = locations)

@app.route('/process_money', methods=['post'])
def process_money():
    location = request.form['location']
    print(location)
    gold_proccessed = session['process_gold'][location]
    session['gold'] += gold_proccessed

    if gold_proccessed > 0:
        session['activities'] = "<p class='text-success'> You earned " + str(gold_proccessed) + " at " + location + "</p>" + session['activities']
    else:
        session['activities'] = "<p class='text-danger'> Entered a casino and lost " + str(gold_proccessed) + " gold at the " + location + "</p>" + session['activities']

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True)