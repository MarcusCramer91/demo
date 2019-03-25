import connexion
from waitress import serve
import os
import time

app = connexion.App(__name__, specification_dir="spec")

app.add_api('/Users/marcuscramer/FlaskDemo/swagger/swagger_definitions.yml')

if __name__ == "__main__":

    # app.run(host="0.0.0.0", threaded=False, processes=5)
    serve(app, host="0.0.0.0", port=5000)