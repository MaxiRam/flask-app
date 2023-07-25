from app.db import db, BaseModelMixin


class Dream(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)

    def __init__(self, topic):
        self.topic = topic

    def __repr__(self):
        return f'Dream({self.topic})'

    def __str__(self):
        return f'{self.Topic}'
