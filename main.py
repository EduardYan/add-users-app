"""
This is the principal file for
execute the server.
"""

from flask import Flask, render_template, redirect, flash, request, url_for

# creating the server
app = Flask(__name__)

# settings for see the messages
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
@app.route('/home')
def home():
  """"
  This is the initial
  route for the server.
  """

  return render_template('index.html')


@app.route('/add-user', methods = ['POST'])
def add_user():
  """
  This route is for add a user in
  the database.
  """

  return redirect(url_for('home'))

if __name__ == '__main__':
  # running the server
  app.run(host = '0.0.0.0', port = 3000, debug = True)