from app import app
# from flask_migrate import Migrate,MigrateCommand
from flask.ext.script import Manager

manager=Manager(app)

# migrate=Migrate(app,db)
# manager.add_command('db',MigrateCommand)

if __name__== '__main__':
    manager.run()