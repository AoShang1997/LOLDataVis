from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, MigrateCommand

from app import app, db
from app.models import Team, Team_data

manager = Manager(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

def make_shell_context():
    return dict(app=app, db=db, Team=Team, Team_data=Team_data)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
