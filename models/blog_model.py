from app import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(256))
    content = db.Column(db.Text)
    published = db.Column(db.Integer)
    