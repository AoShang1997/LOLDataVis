from app import app, db
from flask_migrate import Migrate
if __name__ == '__main__':
    db.drop_all()
    db.create_all()