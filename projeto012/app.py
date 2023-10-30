import flask
app = flask.Flask(__name__)

@app.route("/")
def OlaMundo ():
        return "<p>Ola Mundo</p>"
