import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/time')
def get_current_time():
    # https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project
    # If you are surprised that you are not seeing a call to the jsonify() function from Flask,
    # you may not be aware that in recent releases of Flask your view function can return a
    # dictionary, which gets automatically JSONified by Flask.
    return {'time': time.time()}
    
# if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0')        