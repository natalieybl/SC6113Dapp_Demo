from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=["get","post"])
def index():
    return render_template('index.html')

@app.route('/store_money',methods=["get","post"])
def store_money():
    return render_template('store_money.html')

@app.route('/transfer_money',methods=["get","post"])
def transfer_money():
    return render_template('transfer_money.html')

@app.route('/loop',methods=["get","post"])
def loop():
    return render_template('loop.html')

if __name__=='__main__':
    app.run()
    #app.run(host='0.0.0.0', port=8000, debug=True)
