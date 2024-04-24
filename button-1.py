import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute-script')
def execute_script():
    # Execute the Bash command to run the Python script
    subprocess.Popen(['python', 'exe2html.py'])
    return 'Script executed successfully'

if __name__ == '__main__':
    # Install Chrome and ChromeDriver using Bash command
    subprocess.Popen(['bash', 'install_chrome_and_chromedriver.sh'])

    # Run Flask application
    app.run(debug=True)
