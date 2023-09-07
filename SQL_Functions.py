import sqlite3

    # conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    # c = conn.cursor()
    # c.execute()
    # conn.commit()
    # conn.close()

### ===> Table Creation <===
def Create_New_table(tablename:str, list_of_headers:list):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()
    header_string = ''
    counter = 1
    for headers in list_of_headers:
        if counter == len(list_of_headers):
            header_string += str(headers) + ' text'
            break
        header_string += str(headers) + ' text, '
        counter +=1
    create_comand = "CREATE TABLE " + tablename + " (" + header_string + ")"
    c.execute(create_comand)

    conn.commit()
    conn.close()

def Insert_Rows(tablename:str, rows_to_insert:list):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()
    values_string = ""

    counter = 1
    for values in rows_to_insert:
        if counter == len(rows_to_insert):
            values_string += "'" + str(values) + "'"
            break
        values_string += "'" + str(values) + "', "
        counter +=1
    
    create_command = "INSERT INTO " + tablename + " VALUES (" + values_string + ")"
    c.execute(create_command)

    conn.commit()
    conn.close()

def Insert_Many_Rows(tablename:str, list_rows_to_insert:list):
    for rows in list_rows_to_insert:
        Insert_Rows(tablename, rows)


### ===> Table Reading <===
def Get_Data_In_Table(tablename):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM " + tablename)

    data_in_table = str(c.fetchall())

    conn.commit()
    conn.close()
    
    return data_in_table

def Get_Table_Sorted_By(tablename, colum_to_sort:str, order = "ASC"):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM " + tablename + " ORDER BY " + colum_to_sort + " " + order)

    data_in_table = str(c.fetchall())

    conn.commit()
    conn.close()
    
    return data_in_table

def Get_Table_Filtered_By(tablename, colum_to_filter:str, parameter_to_filter):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM " + tablename + " WHERE " + colum_to_filter + " LIKE '" + str(parameter_to_filter) + "'")

    data_in_table = str(c.fetchall())

    conn.commit()
    conn.close()
    
    return data_in_table


### ===> Table Updating <===
def Update_Table_By_ID(tablename:str, id:int, Objective_colum:str, data):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()

    c.execute("UPDATE " + tablename + " SET " + Objective_colum + " = '" + str(data) + "' WHERE rowid = " + str(id))

    conn.commit()
    conn.close()

def Update_Table_By_Data(tablename:str, parse_colum:str, data_parse, Objective_colum:str, data_change):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()

    c.execute("UPDATE " + tablename + " SET " + Objective_colum + " = '" + str(data_change) + "' WHERE " + parse_colum + " = '" + str(data_parse) + "'")

    conn.commit()
    conn.close()


### ===> Table Deleting <===
def Delete_The_Table_From_Existence(tablename:str):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()

    c.execute("DROP TABLE " + tablename)

    conn.commit()
    conn.close()


def Delete_Row_By_ID(tablename:str, id:int):
    conn = sqlite3.connect('Daily_Tasker\\' + tablename +'.db')
    c = conn.cursor()

    c.execute("DELETE FROM " + tablename + " WHERE rowid = " + str(id))

    conn.commit()
    conn.close()



list_of_headers = ["task_key", "actividad", "prioridad", "tiempo_utilizado"]
list_of_values = ["value " + str(x) for x in range(4)]
list_of_rows = [["value "+ str(y) + ',' + str(x) for x in range(4)] for y in range(3)]

# print(list_of_rows)
# Create_New_table("hello", list_of_headers)
# Insert_Rows("hello", list_of_values)
# Insert_Many_Rows("hello", list_of_rows)

# Delete_Row_By_ID("hello", 2)
# Delete_The_Table_From_Existence("hello")
# print(Get_Table_Sorted_By("hello", "actividad"))
print(Get_Data_In_Table("hello"))