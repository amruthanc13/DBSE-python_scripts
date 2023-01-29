import pymysql

def get_bag_of_words_from_db(task_id):

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="dbse_project")
    cursor = connection.cursor()
    query = "select bow_id, bow from bag_of_words where task_id =  {} ".format(task_id)
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()
   
    bows = []
    for row in rows:
        bow = {
                "bow_id" : row[0],
                "bow" : row[1],
                }
        bows.append(bow)
    return bows