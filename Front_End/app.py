from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def upload_page():
    return render_template('upload_page.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    uploaded_file = request.files['file']
    uploaded_file.save('static/uploaded_image.png')  

    process = subprocess.Popen(['python3', 'final.py'], stdout=subprocess.PIPE, text=True)
    result = process.communicate()[0].strip() 
    lines = result.split('\n')
    lines = lines[-1]

    return render_template('result.html', result=lines)

@app.route('/token.html')  # New route for op.html
def op_page():
    return render_template('token.html')

if __name__ == '__main__':
    app.run(debug=True)
