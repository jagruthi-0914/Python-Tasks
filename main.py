def read_file(file_name):
    with open(file_name,"r") as fp:
        lines = fp.readlines()
    return lines

def extract_values(lines):
    columns=lines[0].strip().split("\t")
    data = [ ]
    for line in lines[1:]:
        if line.strip()=="" :
            continue
        data.append(line.strip().split("\t"))
    return columns , data


import mysql.connector
def connection_database() :
    conn_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@123",
    database = "Leads_Basic_Details",
    )
    
    cursor_obj = conn_obj.cursor()
    return conn_obj, cursor_obj

def create_table(cursor_obj, columns):
    columns_definitions = ", ".join( f"`{col}` VARCHAR(255)" for col in columns)
    query = f""" CREATE TABLE IF NOT EXISTS leads ({columns_definitions})"""
    cursor_obj.execute(query)
    print(query)
    print("Table created successfully")

def insert_data(cursor_obj, conn_obj, columns, data):
    placeholder=",".join(["%s"]*len(columns))
    columns_names = ",".join(f"{col} " for col in columns)
    query = f"""INSERT INTO leads ({columns_names}) VALUES ({placeholder})"""
    cursor_obj.executemany(query, data)
    conn_obj.commit()
    print("Data inserted successfully")

def main():

    lines = read_file(r"D:\python_practice\leads_basic_details.txt")

    columns, data = extract_values(lines)

    print("Total lines in file:", len(lines))

    print("Total extracted rows:", len(data))

    conn_obj, cursor_obj = connection_database()

    create_table(cursor_obj, columns)

    insert_data(cursor_obj, conn_obj, columns, data)

    #cursor_obj.close()
    conn_obj.close()

main()


