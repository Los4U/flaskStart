from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)
app.secret_key = 'cod3f34fv34vd2224s'


@app.route('/list', methods=['GET', 'POST'])
def get_list():
    if request.method == 'GET':
        list_data = get_from_file('stores.csv')
        return render_template("list.html", list_data=list_data)

    elif request.method == 'POST':
        list_data = get_from_file('stores.csv')
        story_title = None
        user_story = None
        criteria = None
        business = None
        estimotion = None
        plan_list = None

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
        if 'plan_list' in session:
            plan_list = session['plan_list']

            print(story_title)
    return render_template('list.html', story_title=story_title,
                                        user_story=user_story,
                                        criteria=criteria,
                                        business=business,
                                        estimotion=estimotion,
                                        plan_list=plan_list,
                                        list_data=list_data)


@app.route('/story', methods=['GET', 'POST'])
def route_save():
    if request.method == 'GET':
        print('GET request received!')
        return render_template("form.html")

    elif request.method == 'POST':
        print('POST request received!')
        '''
        session['story_title'] = request.form['story_title']
        session['user_story'] = request.form['user_story']
        session['criteria'] = request.form['criteria']
        session['business'] = request.form['business']
        session['estimotion'] = request.form['estimotion']
        session['plan_list'] = request.form['plan_list']
        '''
        story_title = request.form['story_title']
        user_story = request.form['user_story']
        criteria = request.form['criteria']
        business = request.form['business']
        estimotion = request.form['estimotion']
        plan_list = request.form['plan_list']

        data_to_write = [story_title, user_story, criteria, business, estimotion, plan_list]

        return redirect('/list')


def get_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        data = [element.replace("\n", "").split(";") for element in lines]
    return data


if __name__ == '__main__':
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )




# <input type="textarea" id="criteria" name="criteria" style="font-size:15pt;height:100px;width:650px;">
# <input type="text" id="user_story" name="user_story" style="font-size:15pt;height:100px;width:650px;"><br><br>