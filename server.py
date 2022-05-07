
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response


@app.route('/client_views',method=['POST'])
def views_by_client():
    num = int(request.form['clicks'])
    session['clicks'] += num
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear() # clears all keys
    return redirect('/')

    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

