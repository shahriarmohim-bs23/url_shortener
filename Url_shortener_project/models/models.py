from core import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from random import choices
import string
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)
class Link(db.Model):
     __tablename__ = 'link'
     id = db.Column(db.Integer,primary_key = True)
     original_url = db.Column(db.String(512))
     short_url = db.Column(db.String(3),unique=True)
     visits = db.Column(db.Integer,default=0)
     date_created = db.Column(db.DateTime,default= datetime.now)
     def __init__(self,original_url ) -> None:
        super().__init__()
        self.original_url = original_url
        self.short_url = self.generate_short_link()
     def generate_short_link(self):
         characters = string.digits + string.ascii_letters
         short_url = ''.join(choices(characters,k=3))
         link = self.query.filter_by(short_url=short_url).first()
         if link:
             return self.generate_short_link()
         
         return short_url



def create_link(original_url):
    short_url = Link(original_url)
    

    db.session.add(short_url)
    db.session.commit()
    return short_url

def search_link(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits + 1
    db.session.commit()
    return link
def query():
    return Link.query.all()