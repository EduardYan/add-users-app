"""
This module have the queries
for make in the database.
"""

# queries for the database
INSERT_USER = 'INSERT INTO users VALUES(NULL, "{name_user}", {age_user}, "{description_user}")'
UPDATE_USER = 'UPDATE users SET name = "{name_user}", age = {age_user}, description = "{description_user}" WHERE(id = {id})'
DELETE_USER = 'DELETE FROM users WHERE(id = {id})'
SELECT_USERS = 'SELECT * FROM users'
SELECT_A_USER = 'SELECT * FROM users WHERE(id = {id})'