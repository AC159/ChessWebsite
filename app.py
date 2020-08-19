import csv
import os
import bcrypt

from itsdangerous import TimedJSONWebSignatureSerializer
from flask import Flask, flash
from flask import render_template, redirect, url_for, session
from forms import RegistrationForm, LoginForm, ForgotPasswordForm, NewPasswordForm
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_mail import Message, Mail
from Top_Players import TopPlayers, CreateTable, CreateTableItems

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inmyf69y3p3v9q8yrctnuv5yp938tusi;htvpw'
login_manager = LoginManager()
login_manager.login_view = '/login'
app.config['USE_SESSION_FOR_NEXT'] = True
login_manager.init_app(app)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='chessnation748@gmail.com',
    MAIL_DEFAULT_SENDER='chessnation748@gmail.com',
    MAIL_PASSWORD=os.environ['MAIL_PASSWORD']
)
mail = Mail(app)
# Initializing a JWS object with the secret key and an expiration time:
s = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'], salt='forgot-password', expires_in=600)  # Lifetime of


# the token is 10 minutes.


@app.route('/')
def home():
    contents = TopPlayers.top_10_players()
    count = 1
    items = []
    for item in contents:  # Using a for loop in case there are less than 10
        items.append(CreateTableItems(ranking=count, username=item["Username"], rating=item["Rating"]))
        if count == 10:
            break
        count += 1

    # items = [CreateTableItems(ranking=1, username=contents[0]["Username"], rating=contents[0]["Rating"]),
    #         CreateTableItems(ranking=2, username=contents[1]["Username"], rating=contents[1]["Rating"]),
    #        CreateTableItems(ranking=3, username=contents[2]["Username"], rating=contents[2]["Rating"]),
    #       CreateTableItems(ranking=4, username=contents[3]["Username"], rating=contents[3]["Rating"]),
    #      CreateTableItems(ranking=5, username=contents[4]["Username"], rating=contents[4]["Rating"]),
    #     CreateTableItems(ranking=6, username=contents[5]["Username"], rating=contents[5]["Rating"]),
    #    CreateTableItems(ranking=7, username=contents[6]["Username"], rating=contents[6]["Rating"]),
    #    CreateTableItems(ranking=8, username=contents[7]["Username"], rating=contents[7]["Rating"]),
    #   CreateTableItems(ranking=9, username=contents[8]["Username"], rating=contents[8]["Rating"]),
    #  CreateTableItems(ranking=10, username=contents[9]["Username"], rating=contents[9]["Rating"])]

    table = CreateTable(items)
    return render_template("HomePageChess.html", table=table)


class User(UserMixin):
    def __init__(self, username, email, rating, password=None):
        self.id = username
        self.email = email
        self.rating = rating
        self.password = password

    def get_forgot_password_token(self):
        token = s.dumps({'id': self.id}, salt='forgot-password').decode('utf-8')  # The token will contain the user's ID
        return token

    @staticmethod
    def verify_reset_password_token(token):
        try:
            decoded_id = s.loads(token, salt='forgot-password')['id']  # Lifetime of the token is 10 minutes.
        except:
            return None
        return decoded_id


def send_password_reset_email(user):
    token = user.get_forgot_password_token()
    send_email(subject='Reset Your ChessNation Password', sender='chessnation748@gmail.com', recipients=[user.email],
               text_body=render_template('PasswordReset.txt', user=user, token=token))


def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    mail.send(msg)


@app.route('/ResetPasswordFail')
def ResetPasswordFail():
    return render_template('ResetPasswordConfirmationFail.html')


@app.route('/Reset_Password_Confirmation/<token>', methods=['GET', 'POST'])
def ResetPasswordConfirmation(token):
    user = User.verify_reset_password_token(token)  # This statement returns the id inside the token in the url.
    if not user:
        flash('Sorry, your verification token expired!', category='danger')
        return redirect(url_for('ResetPasswordFail'))
    form = NewPasswordForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(form.password.data.encode(), salt)  # Hashing the new password
        list_users = []  # List to copy the users.csv file and we will rewrite to it in order to change the password.
        with open("users.csv", "r", newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                list_users.append(line)
                if line[0] == user:
                    line[3] = password.decode('utf-8')  # Writing the new password to the list
                #  Decode to utf-8 is necessary because otherwise it will return a string of bytes.
        with open("users.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(list_users)
        flash('Your password was successfully changed!', category='info')
        return redirect(url_for('Reset_Password_Confirmation_Response'))
    return render_template("ResetPasswordConfirmation.html", form=form)


@app.route('/ResetPasswordConfirmationResponse')
def Reset_Password_Confirmation_Response():
    return render_template('ResetPasswordConfirmationResponse.html')


@login_manager.user_loader
def find_user(user_id):
    with open('users.csv') as f:
        for user in csv.reader(f):
            if user_id == user[0]:
                return User(user[0], user[1], user[2], user[3])  # We could use the User(*user) notation
    return None


@app.route('/login', methods=['GET', 'POST'])
def website_chessboard():
    if current_user.is_authenticated:
        return redirect(url_for('home'))  # If the user is already logged in, do not allow him to login again.
    form = LoginForm()
    if form.validate_on_submit():
        user = find_user(form.username.data)
        if user and bcrypt.checkpw(form.password.data.encode(), user.password.encode()):  # Verifying if the hashed
            # password is the same
            login_user(user)
            next_page = session.get('next', '/')
            session['next'] = '/'
            return redirect(next_page)
        else:
            flash('Incorrect username or password!')
    return render_template("Website(chessboard)3.0.html", form=form)


@app.route('/logout')
@login_required  # The user must be logged in to be able to logout.
def logout():
    logout_user()
    return redirect(url_for('website_chessboard'))


@app.route('/About')
def about_only_chess():
    return render_template("AboutOnlyChess.html")


@app.route('/play')
def play():
    return render_template("PlayChess.html")


@app.route('/history')
def history():
    return render_template("History.html")


@app.route('/engines')
def engines():
    return render_template("Engines.html")


@app.route('/store')
@login_required
def store():
    return render_template("Store.html")


@app.route('/api')
def api():
    return render_template("APIPlay.html")


@app.route('/NewUser')
def new_user():
    return render_template("New_User.html")


@app.route('/sign_in_response/<username>/<email>')
def sign_in_response(username, email):
    return render_template("Sign_in_Response.html", username=username, email=email)


@app.route('/registration_form', methods=['GET', 'POST'])
def handle_sign_in_forms():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Checking if the user already exists:
        user = find_user(form.username.data)
        if not user:
            with open("users.csv", "a", newline='') as f:
                salt = bcrypt.gensalt()
                password = bcrypt.hashpw(form.password.data.encode(), salt)
                writer = csv.writer(f)
                writer.writerow([form.username.data, form.email.data, 1250, password.decode()])  # The number
                # represents the user's initial rating when he registers to the website.
                flash(
                    f'Account successfully created for {form.username.data}! Thank you for registering to ChessNation!',
                    'success')
            return redirect(url_for("sign_in_response", username=form.username.data, email=form.email.data))
        else:
            flash("This username already exists!")
    return render_template("New_User.html", form=form)


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password_form():
    form = ForgotPasswordForm()
    if current_user.is_authenticated:  # Making sure the user is not logged in.
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = find_user(form.username.data)  # Checking if the user exists.
        if user:
            send_password_reset_email(user)
            flash('Check your email for the instructions to reset your password!', 'success')
            return redirect(url_for('password_reset_response'))
    return render_template("ForgotPassword.html", form=form)


@app.route('/password_reset_response')
def password_reset_response():
    return render_template('PasswordResetResponse.html')


if __name__ == '__main__':
    app.run()
