from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """ Serves the homepage for this app """
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
