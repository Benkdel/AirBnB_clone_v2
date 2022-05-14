web flask implementation


1) minimun application:
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

2) set up debugg mode for testing (to avoid restarting flask every time you change your code)
    export FLASK_ENV=development

3) Static Files
    folder static, if module next, if package inside

4) render templates using Jinja2
    folder templates/index.html
    render_template('index.html', name=name) --> second parameter if you neede it, u can add all the variables u want after the template  name
