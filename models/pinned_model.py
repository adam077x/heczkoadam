from sqlalchemy import ForeignKey
from app import db

class PinnedProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey("project.id"))
    
class PinnedPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey("post.id"))
    