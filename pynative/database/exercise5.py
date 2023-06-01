import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    # breakpoint()
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


def Update_doctors_experience(doctor_id, experience):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_update_query = """update Doctor set Experience = %s where Doctor_Id =%s"""
        sql_select_query = """select * from Doctor where Doctor_Id =%s"""
        cursor.execute(sql_update_query, (experience, doctor_id ))
        cursor.execute(sql_select_query, (doctor_id, ))
        records = cursor.fetchall()
        print("Printing Update Doctor Experience record")
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

Update_doctors_experience(104, 15)