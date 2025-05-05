from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start_page(): 
    return render_template('index.html')

@app.route("/legalnotice")
def legalnotice():
    return render_template("legalnotice.html")

@app.route("/privacypolicy")
def privacypolicy():
    return render_template("privacypolicy.html")

if __name__ == '__main__':
    app.run(debug=True)