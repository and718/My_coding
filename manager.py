from flask_shop import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
app = create_app('develop')


manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)
'''
python manager.py db init 执行一次

python manager.py db migrate 生成表结构

python manager.py db upgrade 映射到数据库
'''


if __name__ == "__main__":
    app.run()
    # manager.run()