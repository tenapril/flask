from flask import Flask, session, redirect, url_for, escape, request
import paho.mqtt.publish as publish

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    msgs = [{'topic': "inTopicz", 'payload': "multiple 1"}, ("inTopicz", "multiple 2", 0, False), ("inTopicz", "multiple asu", 0, False)]
    publish.multiple(msgs, hostname="localhost")
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/tembak/<abc>')
def tembak(abc):
    publish.single("inTopicz", abc, hostname="mau.nyalainlampu.ga", port=8883, auth={'username':"testuser",'password':"testpassword"})
    # return redirect(url_for('index'))
    return 'Messagemu: %s' % abc

@app.route('/user_rec', methods=['POST'])
def user_rec():
    user_name = request.form.get('user_input')
    min_time = request.form.get('min_time')
    max_time = request.form.get('max_time')
    players = request.form.getlist('check')
    print(user_name, min_time, max_time, players)
    return redirect('/')


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
