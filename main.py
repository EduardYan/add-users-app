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

  return redirect(url_for('home'))

@app.route('/delete-user/<string:id>')
def delete_user(id):
  """
  This route is for delete
  the user in the database.
  And redirect to homa page.
  """

  id = int(id)

  db = DataBase(DB_PATH)
  db.delete(DELETE_USER.format(id = id))
  db.close()

  return redirect(url_for('home'))

@app.route('/update-user/<string:id>', methods = ['GET'])
def update_user(id):
  """
  This route is for show
  the page for update the user.
  """

  db = DataBase(DB_PATH)
  user = db.select(SELECT_A_USER.format(id = id))
  db.close()

  user = User(user[0][0], user[0][1], user[0][2], user[0][3])
  print(user.name)
  print(user.age)
  print(user.description)

  return render_template('update-user.html', user = user)


@app.route('/update-user', methods = ['POST'])
def update_a_user():
  """
  This route is for update a user
  in the database and redirect to home page.
  """

  id_user = request.form['id-user']
  name = request.form['new-name-user']
  age = request.form['new-age-user']
  description = request.form['new-description-user']

  db = DataBase(DB_PATH)
  print(UPDATE_USER.format(id = id_user, name_user = name, age_user = age, description_user = description))
  db.update(UPDATE_USER.format(id = id_user, name_user = name, age_user = age, description_user = description))
  db.close()

  return redirect(url_for('home'))

if __name__ == '__main__':
  # running the server
  app.run(host = '0.0.0.0', port = 3000, debug = True)