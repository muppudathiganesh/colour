
from flask import Flask, render_template, request
import webbrowser
import threading

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def color_picker():
    # Default color is red
    color = '#ff0000'
    if request.method == 'POST':
        # Get color from form input
        color = request.form.get('color', color)
    return render_template('color.html', color=color)

# Auto-open browser after starting the server
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    # Delay browser opening slightly so server starts first
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
