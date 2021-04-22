def get_meter_data(mysql):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM meter_reader;''')
    rows = cur.fetchall()
    cur.close()
    return rows

def post_meter_data(mysql, consumption, production):
    cur = mysql.connection.cursor()
    print(consumption)
    cur.execute(f'''INSERT INTO meter_reader (consumption, production) VALUES ({consumption}, {production});''')
    print(cur.fetchall())
    mysql.connection.commit()
    return "SUCCESS"