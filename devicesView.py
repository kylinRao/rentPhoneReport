# coding=utf-8
from __init__ import *
from wtforms.fields import SelectField

class devices(db.Model):

    rentPhoneType = db.Column(db.String(80), unique=False)
    status = db.Column(db.Integer, unique=False)
    renterName =  db.Column(db.String(80), unique=False)

    deviceId = db.Column(db.String(80),primary_key=True, unique=False)

    gameboxVersion =  db.Column(db.String(80), unique=False)
    hiappVersion = db.Column(db.String(80), unique=False)
    hmsVersion = db.Column(db.String(80), unique=False)
    owner =  db.Column(db.String(80), unique=False)

    column_list = ('name', 'phone')
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


    def __repr__(self):
        return '<devices %r>' % self.name
class DevicesView(ModelView):
    # # Disable model creation
    can_create = True
    can_delete = False
    can_edit = True

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
        super(DevicesView, self).__init__(devices, session, **kwargs)