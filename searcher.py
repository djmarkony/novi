from __future__ import print_function


from main import mysql
import  notepad



def get_all_categories():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM category ''')
    category = cursor.fetchall()
    return category

def get_videos():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM category c INNER JOIN videos v ON c.id_category = v.id_category WHERE v.approved = 0 ORDER BY c.id_category''')
    data = cursor.fetchall()
    return data

def get_approved_videos():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT * FROM category c INNER JOIN videos v ON c.id_category = v.id_category WHERE v.approved = 1 ORDER BY c.id_category''')
    data = cursor.fetchall()
    print (data)
    return data

def get_approved_videos_by_category(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    if id == '0':
        cursor.execute('''SELECT * FROM category c INNER JOIN videos v ON c.id_category = v.id_category WHERE v.approved = 1 ORDER BY c.id_category''')
    else:
        cursor.execute('''SELECT * FROM category c INNER JOIN videos v ON c.id_category = v.id_category WHERE c.id_category = %s AND v.approved = 1 ORDER BY c.id_category''', id)
    data = cursor.fetchall()
    # print (data)
    return data


def get_videos_by_category(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    if id == '0':
        cursor.execute('''SELECT * FROM category c INNER JOIN videos v ON c.id_category = v.id_category WHERE v.approved = 0 ORDER BY c.id_category''')
    else:
        cursor.execute('''SELECT * FROM category c INNER JOIN videos v ON c.id_category = v.id_category WHERE c.id_category = %s AND v.approved = 0 ORDER BY c.id_category''', id)
    data = cursor.fetchall()
    # print (data)
    return data

def approveVideos(ids):
    conn = mysql.connect()
    cursor = conn.cursor()



    for i in ids:
        # print(i)
        query = "UPDATE videos SET approved= 1  WHERE id= %s"
        cursor.execute(query, (i))
        conn.commit()

        querySelect = "SELECT * FROM category c INNER JOIN videos v ON c.id_category = v.id_category WHERE v.approved = 1 ORDER BY c.id_category"
        cursor.execute(querySelect)
        dataSelect = cursor.fetchall()
        print (dataSelect)
        notepad.addPost(dataSelect[6], 'https://youtu.be/'+dataSelect[5],  querySelect[2], querySelect[7], 'publish'+querySelect[12])
    data = get_videos()
    return data

# def select_video():
#     category = 'Animation'
#     cursor = mysql.get_db().cursor()
#     cursor.execute('''SELECT id_category FROM category WHERE category_name like %s''', category)
#     row = cursor.fetchone()
#     print(json.dumps(row))
#     return str(row)
