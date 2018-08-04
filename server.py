from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'cod3f34fv34vd2224s'

@app.route('/')  # Register the 'http://localhost:5000 **/** ' route to this function.
def route_index():  # Just a normal function, I named it this way for cleaner code
    story_title = None
    user_story = None
    criteria = None
    business = None
    estimotion = None

    if 'story_title' in session:
        story_title = session['story_title']

    if 'user_story' in session:
        user_story = session['user_story']

    if 'criteria' in session:
        criteria = session['criteria']

    if 'business' in session:
        business = session['business']

    if 'estimotion' in session:
        estimotion = session['estimotion']

        print(story_title)
    return render_template('list.html', story_title=story_title, user_story=user_story, criteria=criteria, business=business, estimotion=estimotion)


@app.route('/form')  # Registering GET requests sent to 'http://localhost:5000 **/edit-note** ' to this function
def route_edit():
    note_text = None
    if 'note' in session:  # If we something already stored, then use that
        note_text = session['note']
    return render_template('form.html', note=note_text)


@app.route('/form', methods=['POST'])
def route_save():
    print('POST request received!')
    session['story_title'] = request.form['story_title']
    session['user_story'] = request.form['user_story']
    session['criteria'] = request.form['criteria']
    session['business'] = request.form['business']
    session['estimotion'] = request.form['estimotion']

    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
