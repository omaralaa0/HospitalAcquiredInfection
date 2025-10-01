In order to run the flask application:

- Make sure you have the following dependencies:
flask
flask-sqlalchemy
sqlalchemy
psycopg2-binary
python-dotenv
joblib
numpy
scikit-learn


Steps to run the application:

- Make sure you are in Application directory (the exact folder called Application).
- Create a new postgres database, call it (SepsisDB).
- From Database dump folder, restore the SepsisDB.sql file in your database (or via executesql).
- Create a .env file in the root directory of the application (to avoid publishing database connection credentials for public deployment).
- In the .env file add the attribute of your DB connection; example: DATABASE_URL=postgresql://[username]:[password]@localhost:5432/SepsisDB - Don't edit the DATABASE_URL variable in the application since it's defined there.
- After making sure the database is up and running, all dependencies are installed, run the flaskapp.py file from any IDE.
- Open your browser and go to http://127.0.0.1:5000
- Navigate through the web app and try the different options.