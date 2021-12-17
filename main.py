"""
This is the principal file for
execute the server.
"""

from flask import Flask, render_template, redirect, flash, request, url_for
from models.database import DataBase, DB_PATH
from queries.queries import INSERT_USER, DELETE_USER, SELECT_USERS, UPDATE_USER, SELECT_A_USER
from models.user import User

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

  # connecting with the database for get alls the user for show
  db = DataBase(DB_PATH)
  users_list = db.select(SELECT_USERS)
  db.close()
  # converting in user objects
  users_list = list(map(lambda user: User(user[0], user[1], user[2], user[3]), users_list))

  return render_template('index.html', users_list = users_list)

@app.route('/about')
def about():
  """
  This route is for show the about
  page.
  """

  return render_template('about.html')

@app.route('/add-user', methods = ['POST'])
def add_user():
  """
  This route is for add a user in
  the database.
  """

  # gettings the values for save in the database
  name = request.form['name-user']
  age = request.form['age-user']
  description = request.form['description-user']

  # creating the connection with the database and save the new user
  db = DataBase(DB_PATH)
  db.insert(INSERT_USER.format(name_user = name, age_user = age, description_user = description))
  db.close()

  flash('User Added')

  # redirct to home
  return redirect(url_for('home'))

@app.route('/delete-user/<string:id>')
def delete_user(id):
  """
  This route is for delete
  the user in the database.
  And redirect to homa page.
  """

  id = int(id)

  # deleeting of the database
  db = DataBase(DB_PATH)
  db.delete(DELETE_USER.format(id = id))
  db.close()

  # showing messages and redirect to home
  flash('User Deleted')
  return redirect(url_for('home'))

@app.route('/update-user/<string:id>', methods = ['GET'])
def update_user(id):
  """
  This route is for show
  the page for update the user.
  """

  # selection according your id of the user
  db = DataBase(DB_PATH)
  user = db.select(SELECT_A_USER.format(id = id))
  db.close()

  # convert to user object
  user = User(user[0][0], user[0][1], user[0][2], user[0][3])

  return render_template('update-user.html', user = user)


@app.route('/update-user', methods = ['POST'])
def update_a_user():
  """
  This route is for update a user
  in the database and redirect to home page.
  """

  # getting the new data for the user
  id_user = request.form['id-user']
  name = request.form['new-name-user']
  age = request.form['new-age-user']
  description = request.form['new-description-user']

  # updating the user in the database
  db = DataBase(DB_PATH)
  db.update(UPDATE_USER.format(id = id_user, name_user = name, age_user = age, description_user = description))

  flash('User Updated')

  return redirect(url_for('home'))

if __name__ == '__main__':
  # running the server
  app.run(port = 3000, debug = True)