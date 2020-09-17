import requests
import os
import sqlite3
import argparse

from prettytable import PrettyTable

URL_SO_SEARCH = 'https://api.stackexchange.com/2.2/search'
URL_SO_ANSWERS = 'https://api.stackexchange.com/2.2/questions/{}/answers'
DATABASE_NAME = 'mydatabase'


def create_db(name):
    try:
        conn = sqlite3.connect("{}.db".format(name))
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS questions
                              (question_id int primary key ,
                              title text,
                              author text
                              )
                           """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS answers
                              (answer_id int primary key,
                               question_id int,
                               link text,
                               author text)
                           """)
        return conn, cursor

    except sqlite3.Error:
        print(sqlite3.Error)
        return False


def fill_db(questions, conn, cursor):
    for question in questions['items']:
        cursor.execute("""INSERT INTO questions(
                                                    question_id,
                                                    title,
                                                    author
                                                    ) 
                          VALUES(?,?,?);""",
                       (
                           question['question_id'],
                           question['title'],
                           question['owner']['display_name']
                       )
                       )
        if question["answer_count"]:
            answers = get_answers(question['question_id'])
            for answer in answers["items"]:
                cursor.execute("""INSERT INTO answers(answer_id,
                                                         question_id,
                                                         link,
                                                         author
                                                         )
                                    VALUES(?,?,?,?);""",
                               (
                                   answer['answer_id'],
                                   question['question_id'],
                                   answer['owner']['link'],
                                   answer['owner']['display_name']
                               )
                               )
        conn.commit()


def get_answers(question_id):
    params = {
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
    }
    response = requests.get(URL_SO_ANSWERS.format(question_id), params=params)
    response.raise_for_status()
    return response.json()


def render_table(rows):
    table = PrettyTable()
    table.field_names = ['Title', 'Author', 'Answered', 'Link']
    table.align['Title'] = 'l'
    table.align['Author'] = 'l'
    table.align['Answered'] = 'l'
    table.align['Link'] = 'l'
    table.max_width = 65
    for row in rows:
        table.add_row(list(row))
    return table


def main():
    parser = argparse.ArgumentParser(
        description="The script allows you to get data from stackexchange.com"
    )
    parser.add_argument('query', help='search query')

    params = {
        'order': 'desc',
        'sort': 'activity',
        'intitle': parser.parse_args().query,
        'filter': 'default',
        'site': 'stackoverflow',
        'run': 'true'
    }
    sql_request = """select t1.title, t1.author, t2.author, t2.link 
                          from questions as t1
                          join answers as t2 on t2.question_id=t1.question_id"""

    conn, cursor = create_db(DATABASE_NAME)
    print('loading...')
    try:
        response = requests.get(URL_SO_SEARCH, params=params)
        questions = response.json()
        if questions.get('items'):
            fill_db(questions, conn, cursor)
        else:
            print('Not data')
    except requests.exceptions.HTTPError:
        print('Request failed')

    cursor.execute(sql_request)
    print(render_table(cursor.fetchall()))
    os.remove('{}.db'.format(DATABASE_NAME))


if __name__ == '__main__':
    main()
