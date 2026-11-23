import mysql.connector

def connection_database() :
    conn_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@123",
    database = "Leads_Basic_Details",
    )
    cursor_obj = conn_obj.cursor(dictionary=True)
    return conn_obj, cursor_obj

def education_wise(cursor_obj):
    query = f""" SELECT current_education as edu , COUNT(*) as lead_count FROM leads GROUP By current_education"""
    cursor_obj.execute(query)
    print("Current Education Wise Leads")
    data = []
    for row in cursor_obj.fetchall():
        data.append(row)
    print(data)

def main():
    conn_obj, cursor_obj = connection_database()
    education_wise(cursor_obj)
    conn_obj.close()

main()

