from flask import Flask
import subprocess
import getpass
import datetime

app = Flask(__name__)

@app.route('/htop')  
def htop():
    full_name = "Parth Gupta" 
    username = getpass.getuser()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")


    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

