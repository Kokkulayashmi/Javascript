from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

# Redirect to next.html
@app.route('/next')
def next_page():
    return render_template('next.html')

# Redirect to gift.html
@app.route('/gift')
def gift_page():
    return render_template('gift.html')
@app.route('/video')
def video_page():
    return render_template('end.html')

if __name__ == '__main__':
  app.run(debug=True)
