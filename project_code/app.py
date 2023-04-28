from db.run_sql import run_sql

with open("db/MOCK_MEMBERS.sql", "r") as sql_file:
    for line in sql_file:
        run_sql(line)