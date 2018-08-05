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
        if request.form['action'] == "add_row":
            id_of_story = get_last_id('stores.csv')
            story_title = request.form['story_title']
            user_story = request.form['user_story']
            criteria = request.form['criteria']
            business = request.form['business']
            estimotion = request.form['estimotion']
            plan_list = request.form['plan_list']

            data_to_write = [id_of_story, story_title, user_story, criteria, business, estimotion, plan_list]
            add_to_list('stores.csv', data_to_write)

            list_data = get_from_file('stores.csv')
            return render_template("list.html", list_data=list_data)

        elif request.form['action'] == "del_row":
            delete_story_id = request.form['delete_story']

            delete_from_list('stores.csv', delete_story_id)

            print(delete_story_id)
            list_data = get_from_file('stores.csv')
            return render_template("list.html", list_data=list_data)


@app.route('/story', methods=['GET', 'POST'])
def route_save():
    if request.method == 'GET':
        print('GET request received!')
        return render_template("form.html")

    elif request.method == 'POST':
        print('POST request received!')
        return render_template("form.html")


@app.route('/story/<story_id>', methods=['POST', 'GET'])
def update(story_id=None):
    print("fdsf")
    return render_template("form.html")


# get the last max ID from the file, then add +1 and return


def get_last_id(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        i = len(lines)
    return str(i + 1)


def get_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        data = [element.replace("\n", "").split(";") for element in lines]
    return data


def add_to_list(file_name, data_to_write):
    list_where_to_add = get_from_file(file_name)
    list_where_to_add.append(data_to_write)
    write_to_file(file_name, list_where_to_add)


def delete_from_list(file_name, id_to_delete):
    list_where_to_del = get_from_file(file_name)
    for i, row in enumerate(list_where_to_del):  # count in which row, list element is the ID, we want to remove
        if id_to_delete in str(row[0]):
            del list_where_to_del[i]  # delete exact row from the table according the provided ID
    write_to_file(file_name, list_where_to_del)


def write_to_file(file_name, list_to):
    with open(file_name, "w") as file:
        for record in list_to:
            row = ';'.join(record)
            file.write(row + "\n")


if __name__ == '__main__':
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )