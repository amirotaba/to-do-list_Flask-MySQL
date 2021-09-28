from flask import Flask, render_template, request
import mysql.connector
import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SXd6mBhFshUFY@R",
  database="to_do_list"
)

c = mydb.cursor()


x = datetime.datetime.now()

d = int(x.strftime("%d"))
m = int(x.strftime("%m"))
y = int(x.strftime("%Y"))

date2 = datetime.date(y, m, d)


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=["POST", "GET"])
def todolist():
    if request.method == "POST":
        if request.form.get("add-task"):
            v1 = request.form["task"]
            if v1 == "":
                sql_show = "SELECT * from tasks"

                c.execute(sql_show)

                data = c.fetchall()

                for row in data:
                    id = row[0]
                    # get date1
                    sql_date1 = "SELECT date FROM tasks WHERE id =%s"
                    c.execute(sql_date1, [id])

                    # convert the irregular date to regular
                    not_date = str(c.fetchall())
                    irreg_date = not_date[2: -3]
                    tr = -1
                    for w in irreg_date:
                        tr = tr + 1
                        if w == "(":
                            start = tr + 1
                        if w == ")":
                            end = tr
                    reg_date = irreg_date[start: end]
                    year = int(reg_date[0:4])
                    tr = -1
                    list = []
                    for n in reg_date:
                        tr = tr + 1
                        if n == ",":
                            list.append(tr)
                    month = int(reg_date[list[0] + 2: list[1]])
                    day = int(reg_date[list[1] + 2: len(reg_date) + 1])
                    date1 = datetime.date(year, month, day)

                    # change the diff to days
                    irreg_diff = str(date2 - date1)
                    if irreg_diff[0] == "0":
                        diff = 0
                    else:
                        list = []
                        tr = -1
                        for w in irreg_diff:
                            tr = tr + 1
                            if w == " ":
                                list.append(tr)
                        diff = int(irreg_diff[0: list[0]])

                    c.execute("UPDATE tasks SET datediff=%s WHERE id=%s", (diff, id))

                    mydb.commit()

                sql_show = "SELECT * from tasks"

                c.execute(sql_show)

                data = c.fetchall()

                return render_template("show-task-dis.html", data=data)
            else:
                v1 = request.form["task"]
                sql = "INSERT INTO tasks (task, done) VALUES (%s, %s)"
                val = (v1, "")
                c.execute(sql, val)

                mydb.commit()
                sql_show = "SELECT * from tasks"

                c.execute(sql_show)

                data = c.fetchall()

                for row in data:
                    id = row[0]
                    # get date1
                    sql_date1 = "SELECT date FROM tasks WHERE id =%s"
                    c.execute(sql_date1, [id])

                    # convert the irregular date to regular
                    not_date = str(c.fetchall())
                    irreg_date = not_date[2: -3]
                    tr = -1
                    for w in irreg_date:
                        tr = tr + 1
                        if w == "(":
                            start = tr + 1
                        if w == ")":
                            end = tr
                    reg_date = irreg_date[start: end]
                    year = int(reg_date[0:4])
                    tr = -1
                    list = []
                    for n in reg_date:
                        tr = tr + 1
                        if n == ",":
                            list.append(tr)
                    month = int(reg_date[list[0] + 2: list[1]])
                    day = int(reg_date[list[1] + 2: len(reg_date) + 1])
                    date1 = datetime.date(year, month, day)

                    # change the diff to days
                    irreg_diff = str(date2 - date1)
                    if irreg_diff[0] == "0":
                        diff = 0
                    else:
                        list = []
                        tr = -1
                        for w in irreg_diff:
                            tr = tr + 1
                            if w == " ":
                                list.append(tr)
                        diff = int(irreg_diff[0: list[0]])

                    c.execute("UPDATE tasks SET datediff=%s WHERE id=%s", (diff, id))

                    mydb.commit()

                sql_show = "SELECT * from tasks"

                c.execute(sql_show)

                data = c.fetchall()

                return render_template("show-task-dis.html", data=data)
        elif request.form.get("show-tasks"):
            sql_show = "SELECT * from tasks"

            c.execute(sql_show)

            data = c.fetchall()

            for row in data:
                id = row[0]
                # get date1
                sql_date1 = "SELECT date FROM tasks WHERE id =%s"
                c.execute(sql_date1, [id])

                #convert the irregular date to regular
                not_date = str(c.fetchall())
                irreg_date = not_date[2: -3]
                tr = -1
                for w in irreg_date:
                    tr = tr + 1
                    if w == "(":
                        start = tr + 1
                    if w == ")":
                        end = tr
                reg_date = irreg_date[start: end]
                year = int(reg_date[0:4])
                tr = -1
                list = []
                for n in reg_date:
                    tr = tr + 1
                    if n == ",":
                        list.append(tr)
                month = int(reg_date[list[0]+2: list[1]])
                day = int(reg_date[list[1]+2: len(reg_date)+1])
                date1 = datetime.date(year, month, day)

                #change the diff to days
                irreg_diff = str(date2 - date1)
                if irreg_diff[0] == "0":
                    diff = 0
                else:
                    list = []
                    tr = -1
                    for w in irreg_diff:
                        tr = tr + 1
                        if w == " ":
                            list.append(tr)
                    diff = int(irreg_diff[0: list[0]])

                c.execute("UPDATE tasks SET datediff=%s WHERE id=%s", (diff, id))

                mydb.commit()

            sql_show = "SELECT * from tasks"

            c.execute(sql_show)

            data = c.fetchall()

            return render_template("show-task-dis.html", data=data)
        elif request.form.get("delete"):
            delete_id = request.form.get("delete")

            c.execute("DELETE from tasks WHERE id = %s", [delete_id])

            mydb.commit()

            sql_show = "SELECT * from tasks"

            c.execute(sql_show)

            data = c.fetchall()

            for row in data:
                id = row[0]
                # get date1
                sql_date1 = "SELECT date FROM tasks WHERE id =%s"
                c.execute(sql_date1, [id])

                # convert the irregular date to regular
                not_date = str(c.fetchall())
                irreg_date = not_date[2: -3]
                tr = -1
                for w in irreg_date:
                    tr = tr + 1
                    if w == "(":
                        start = tr + 1
                    if w == ")":
                        end = tr
                reg_date = irreg_date[start: end]
                year = int(reg_date[0:4])
                tr = -1
                list = []
                for n in reg_date:
                    tr = tr + 1
                    if n == ",":
                        list.append(tr)
                month = int(reg_date[list[0] + 2: list[1]])
                day = int(reg_date[list[1] + 2: len(reg_date) + 1])
                date1 = datetime.date(year, month, day)

                # change the diff to days
                irreg_diff = str(date2 - date1)
                if irreg_diff[0] == "0":
                    diff = 0
                else:
                    list = []
                    tr = -1
                    for w in irreg_diff:
                        tr = tr + 1
                        if w == " ":
                            list.append(tr)
                    diff = int(irreg_diff[0: list[0]])

                c.execute("UPDATE tasks SET datediff=%s WHERE id=%s", (diff, id))

                mydb.commit()

            sql_show = "SELECT * from tasks"

            c.execute(sql_show)

            data = c.fetchall()

            return render_template("show-task-dis.html", data=data)
        elif request.form.get("check"):
            button_id = int(request.form.get("check"))

            sql_check = "UPDATE tasks SET done = 'Y' WHERE id = %s"

            c.execute(sql_check, [button_id])

            mydb.commit()
            sql_show = "SELECT * from tasks"

            c.execute(sql_show)

            data = c.fetchall()

            for row in data:
                id = row[0]
                # get date1
                sql_date1 = "SELECT date FROM tasks WHERE id =%s"
                c.execute(sql_date1, [id])

                # convert the irregular date to regular
                not_date = str(c.fetchall())
                irreg_date = not_date[2: -3]
                tr = -1
                for w in irreg_date:
                    tr = tr + 1
                    if w == "(":
                        start = tr + 1
                    if w == ")":
                        end = tr
                reg_date = irreg_date[start: end]
                year = int(reg_date[0:4])
                tr = -1
                list = []
                for n in reg_date:
                    tr = tr + 1
                    if n == ",":
                        list.append(tr)
                month = int(reg_date[list[0] + 2: list[1]])
                day = int(reg_date[list[1] + 2: len(reg_date) + 1])
                date1 = datetime.date(year, month, day)

                # change the diff to days
                irreg_diff = str(date2 - date1)
                if irreg_diff[0] == "0":
                    diff = 0
                else:
                    list = []
                    tr = -1
                    for w in irreg_diff:
                        tr = tr + 1
                        if w == " ":
                            list.append(tr)
                    diff = int(irreg_diff[0: list[0]])

                c.execute("UPDATE tasks SET datediff=%s WHERE id=%s", (diff, id))

                mydb.commit()

            sql_show = "SELECT * from tasks"

            c.execute(sql_show)

            data = c.fetchall()

            return render_template("show-task-dis.html", data=data)
    elif request.method == 'GET':
        return render_template("home.html")


if __name__ == '__main__':
    app.run()
