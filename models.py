from datetime import datetime
import peewee as pw

db = pw.SqliteDatabase('db.db')

class BaseModel(pw.Model):
    class Meta:
        database = db

class User(BaseModel):
    id = pw.AutoField()
    username = pw.CharField()
    password = pw.CharField()

class Article(BaseModel):
    id = pw.AutoField()
    title = pw.CharField()
    text = pw.CharField()
    author = pw.ForeignKeyField(User, related_name='articles')
    date = pw.DateTimeField(default=datetime.now())

if __name__ == '__main__':
    User.create_table()
    Article.create_table()
