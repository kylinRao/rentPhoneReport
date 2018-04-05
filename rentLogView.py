# coding=utf-8
from flask.ext.login import current_user

from __init__ import *
from wtforms.fields import SelectField

class RentLogView(ModelView):
    def is_accessible(self):
        return False
    # Disable model creation
    can_create = False
    can_delete = False
    can_edit = False

    # Override displayed fields
    # column_list = ('login', 'email')

    form_overrides = dict(status=SelectField)
    form_args = dict(
        # Pass the choices to the `SelectField`
        status=dict(
            choices=[(0, 1), (1, '出借中')]
        ))

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(RentLogView, self).__init__(rentlog, session, **kwargs)

class rentlog(db.Model):
    can_create = False
    can_delete = False
    id = db.Column(db.Integer, primary_key=True,unique=True)
    rentPhoneType = db.Column(db.String(80), unique=False)
    name =  db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(80), unique=False)
    deviceId = db.Column(db.String(80), unique=False)
    status = db.Column(db.Integer, unique=False)
    returnName = db.Column(db.Integer, unique=False)
    returnPhone = db.Column(db.Integer, unique=False)
    renttime = db.Column(db.DATETIME, unique=False)
    returntime = db.Column(db.DATETIME, unique=False)
    gameboxVersion =  db.Column(db.String(80), unique=False)
    hiappVersion = db.Column(db.String(80), unique=False)
    hmsVersion = db.Column(db.String(80), unique=False)

    column_list = ('name', 'phone')
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


    def __repr__(self):
        return '<rentLog %r>' % self.name