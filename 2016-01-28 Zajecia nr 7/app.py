#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import StringIO
import datetime

from flask import (
    Flask, 
    render_template, 
    session,
    make_response,
    request,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy

from utils import (
    get_cpu_stats,
    get_process_list,
    get_memory_stats,
)

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/lol.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CPU_SAMPLER_TIME'] = 1
app.config['CPU_GATHER_JOB_INTERVAL'] = 3
db = SQLAlchemy(app)


class Commentage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, nickname, comment):
        self.nickname = nickname
        self.comment = comment



class CpuStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avg_load = db.Column(db.Float, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, avg_load):
        if isinstance(avg_load, list):
            avg_load = sum(avg_load)/float(len(avg_load))
        self.avg_load = float(avg_load)



@app.route('/add_comment', methods=['GET', 'POST'])
def add_comment():
    res = make_response(":(")
    if request.method == 'POST':
        c = Commentage(
            nickname = request.form['nickname'],
            comment = request.form['commentage']
        )
        db.session.add(c)
        db.session.commit()
        res = redirect(url_for('hello'))
    else:
        res = make_response(render_template('add_comment_form.html'))

    return res


@app.route("/huefewhfoiw")
def download_csv():
    process_list = get_process_list()
    process_stio = StringIO.StringIO()

    w = csv.writer(process_stio)
    w.writerows(process_list)

    res = make_response(process_stio.getvalue())
    res.headers['Content-Type'] = 'text/csv'
    res.headers['Content-Disposition'] = 'attachment; filename=export.csv'
    return res


@app.route("/")
def hello():
    our_response = render_template(
        'show_stats.html', 
        cpu_data=enumerate(get_cpu_stats(
            app.config['CPU_SAMPLER_TIME'])),
        mem_data=get_memory_stats(),
        process_list=get_process_list(),
        comments=(Commentage.query.all()),
        cpu_history=(

            CpuStats.query.order_by(
                CpuStats.created.desc()
            ).limit(50)
            
        ),
    )

    return our_response


if __name__ == "__main__":
    app.run(debug=True)