#!/usr/bin/python3
import datetime
import psycopg2
import sys


def q_one():
    """Return three most popular articles of all time."""
    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        print("Connected!")
    c = db.cursor()
    c.execute("""
        select title, count(*) as views
        from articles
        join log on replace(path, '/article/', '') = slug
        group by title
        order by views desc limit 3;""")
    bestreads = c.fetchall()
    db.close()
    print('{article} - {count} views'.format(article=bestreads[0], count=bestreads[1]))


def q_two():
    """Return the most popular article authors of all time."""
    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        print("Connected!")
    c = db.cursor()
    c.execute("""
        select title, views
        from articles
        inner join
            (select path, count(path) as views
            from log
            group by log.path) as log
        on log.path = '/article/' || articles.slug
        order by views desc
        limit 3""")
    bestwriters = c.fetchall()
    db.close()
    print(bestwriters)


def q_three():
    """Return days with more than 1 percent of requests lead to errors."""
    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        print("Connected!")
    c = db.cursor()
    c.execute("select * from dailyerrorp where error_percentage >= 1.00;")
    worstdays = c.fetchall()
    db.close()
    print(worstdays)


if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')


q_one()
q_two()
q_three()
