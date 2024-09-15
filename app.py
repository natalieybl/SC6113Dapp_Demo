from flask import Flask,render_template,request
import sqlite3
import datetime

app=Flask(__name__)

@app.route('/',methods=["get","post"])
def index():
    return render_template('index.html')

@app.route('/main',methods=["get","post"])
def main():
    r = request.form.get("q")
    #print('back from view.html')
    #print(r)
    if r == None: 
        pass
    else:
        current_time = datetime.datetime.now()
        conn = sqlite3.connect('dapp.db')
        c = conn.cursor()
        c.execute('insert into user values(?,?)', (r, current_time))
        conn.commit()
        c.close()
        conn.close()
    
    return render_template('main.html', r = r)

@app.route('/store_money',methods=["get","post"])
def store_money():
    return render_template('store_money.html')

@app.route('/transfer_money',methods=["get","post"])
def transfer_money():
    return render_template('transfer_money.html')

@app.route('/loop',methods=["get","post"])
def loop():
    return render_template('loop.html')

@app.route('/admin',methods=["get","post"])
def admin():
    return render_template('admin.html')

@app.route('/viewDB',methods=["get","post"])
def viewDB():
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    # Execute a SELECT statement to retrieve all records from the table
    c.execute('SELECT * FROM user')

    # Fetch all the records
    rows = c.fetchall()

    # Get the column names
    column_names = [description[0] for description in c.description]
    r = ""
    # Create the HTML table
    html_table = '''
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            {}
        </tr>
        {}
    </table>
    '''

    # Create the table header row
    table_header_row = '<th>{}</th>'.format('</th><th>'.join(column_names))

    # Create the table rows
    table_rows = ''
    for row in rows:
        table_row = '<td>{}</td>'.format('</td><td>'.join(str(value) for value in row))
        table_rows += '<tr>{}</tr>'.format(table_row)

    # Assemble the HTML table
    html_table = html_table.format(table_header_row, table_rows)

    # Print the HTML table
    print(html_table)

    # Close the connection
    conn.close()
    '''
    c.execute('select * from user')
    r = ""
    for row in c.fetchall():
        r = r + str(row) + "\n"
    print(r)
    conn.commit()
    c.close()
    conn.close()
    '''
    return render_template('view.html', r = r, html_table = html_table)

@app.route('/delDB',methods=["get","post"])
def delDB():
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute("delete from user")
    conn.commit()
    c.close()
    conn.close()
    return render_template('delete.html')

if __name__=='__main__':
    app.run()
    #app.run(host='0.0.0.0', port=8000, debug=True)
