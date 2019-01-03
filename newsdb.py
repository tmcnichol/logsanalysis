#!/usr/bin/python3
import datetime
import psycopg2

DBNAME = "news"


def q_one():
    """Return three most popular articles of all time."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
        select title, count(*) as views
        from articles
        join log on replace(path, '/article/', '') = slug
        group by title
        order by views desc limit 3;""")
    bestreads = c.fetchall()
    db.close()
    print(bestreads)


def q_two():
    """Return the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select authors.name as author, count (*) as reads
        from authors, articles, log
        where authors.id = articles.author
        and replace(log.path, '/article/', '') = articles.slug
        group by name
        order by reads desc;""")
    bestwriters = c.fetchall()
    db.close()
    print(bestwriters)


def q_three():
    """Return days with more than 1 percent of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from dailyerrorp where error_percentage >= 1.00;")
    worstdays = c.fetchall()
    db.close()
    print(worstdays)


q_one()
q_two()
q_three()
