from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return render_template('index.html', name = "Jin", num = 15)

@app.route('/student/<name>/<other_name>')
def student_page(name, other_name):
    return "Hello " + name + " and " + other_name

@app.route('/index/<name>/<int:num>')
def index(name, num):
    return render_template('index.html', name = name, num = num)

@app.route('/example')
def example():
    return "example"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

