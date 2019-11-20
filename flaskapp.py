from flask import Flask, Response


flask_app = Flask('flaskapp')


@flask_app.route('/hello')
def hello_world():
    return Response(
        'Hello World from Flask! \n',
        content_type='text/plain',
    )


app = flask_app.wsgi_app