"""
The flask application package.
"""

from flask import Flask ,render_template
import pymysql
app = Flask(__name__)
#conn =pymysql.connect('score','name','','pass')


@app.route("/")
def hello():

	return render_template('EE.html',rr=0)

if __name__ == '__main__':
   app.run(debug=True)