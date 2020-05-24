from marshmallow import fields, Schema
import datetime
from . import db

class SongsModel(db.Model):
    """
    Songs model
    """
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.String(100), unique=True, nullable=False)
    song_name = db.Column(db.String(200), nullable=False, default='')
    artist_id = db.Column(db.String(100), nullable=True, default='')
    artist_name = db.Column(db.String(100), nullable=True, default='')
    genre = db.Column(db.String(100), nullable=True, default='')
    album_id = db.Column(db.String(100), nullable=True, default='')
    album_name = db.Column(db.String(100), nullable=True, default='')
    thumbnail_id = db.Column(db.String(100), nullable=True, default='')
    duration = db.Column(db.Integer, nullable=False, default=0)
    listen_count = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.song_id = data.get('song_id')
        self.song_name = data.get('song_name')
        self.artist_id = data.get('artist_id')
        self.artist_name = data.get('artist_name')
        self.genre = data.get('genre')
        self.album_id = data.get('album_id')
        self.album_name = data.get('album_name')
        self.thumbnail_id = data.get('thumbnail_id')
        self.duration = data.get('duration')
        self.listen_count = data.get('listen_count')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)

        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def get_all_songs():
        return SongsModel.query.all()

    @staticmethod
    def get_one_song(id):
        return SongsModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)



class SongsSchema(Schema):
    """
    Songs Schema
    """
    id = fields.Int(dump_only=True)
    song_id = fields.Str(required=True)
    song_name = fields.Str(dump_only=True)
    artist_id = fields.Str(dump_only=True)
    artist_name = fields.Str(dump_only=True)
    genre = fields.Str(dump_only=True)
    album_id = fields.Str(dump_only=True)
    album_name = fields.Str(dump_only=True)
    thumbnail_id = fields.Str(dump_only=True)
    duration = fields.Int(dump_only=True)
    listen_count = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)