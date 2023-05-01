# from db.run_sql import run_sql

from flask import Flask, render_template

from controllers.sessions_controller import sessions_blueprint
from controllers.members_controller import members_blueprint
from controllers.bookings_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(bookings_blueprint)
app.register_blueprint(sessions_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)

#Using Mockaroo.com I could feed mick member data into the database using this for loop and with open function:
# with open("db/members.sql", "r") as sql_file:
#     for line in sql_file:
#         run_sql(line)