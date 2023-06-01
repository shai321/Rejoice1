import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    connection = psycopg2.connect(user=os.getenv('USER'),
                                  password=os.getenv('PASSWORD'),
                                  host=os.getenv('HOST'),
                                  port=os.getenv('PORT'),
                                  database=os.getenv('DATABASE'))
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        print("Postgres connection is closed")


def get_specialist_doctors_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Speciality = %s and Salary > %s"""
        cursor.execute(select_query, (speciality, salary))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
            print("\n")
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

print("Printing doctors whose specialty is Garnacologist and salary greater than 35000 ")
get_specialist_doctors_list("Garnacologist",35000)