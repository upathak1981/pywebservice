from flask import Flask, request, abort
app = Flask(__name__)
@app.route('/')
def rootfunction():
    return 'First Python app on Heroku'    
if __name__=='__main__':
    app.run(debug=True)
    app.run()
