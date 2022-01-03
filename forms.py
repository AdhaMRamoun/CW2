from wtforms import Form, StringField, DecimalField, IntegerField, TextAreaField, PasswordField, validators

#the form used to register users in the register page
class RegisterForm(Form):
    name = StringField('Full Name', [validators.Length(min=1,max=50)])
    username = StringField('Username', [validators.Length(min=4,max=25)])
    email = StringField('Email', [validators.Length(min=6,max=50)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')

#the form used in making transactions on the transaction page
class SendMoneyForm(Form):
    username = StringField('Username', [validators.Length(min=4,max=25)])
    amount = StringField('Amount', [validators.Length(min=1,max=50)])

#the form used in buying PyC from the buy page
class BuyForm(Form):
    amount = StringField('Amount', [validators.Length(min=1,max=50)])
