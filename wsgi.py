from celery_app.tasks import get_random_number
from flask import Flask
# from tasks.random_numbers import get_random_number

app = Flask(__name__)

# app configuration
app.config['CELERY_BROKER_URL'] = "amqp://darth"
app.config["CELERY_RESULT_BACKEND"] = "rpc://darth"


NUMBER_OF_NUMS = 10


@app.route("/")
def root():
    result_vars = []
    for i in range(NUMBER_OF_NUMS):
        result_vars.append(get_random_number.delay())
    
    html_res = """
    <h1>Hello world!</h1>
    <ul>
    """

    for result in result_vars:
        result_body = result.wait()
        random_number = result_body["random_number"]
        node_name = result_body["node_name"]
        html_res += """
        <li>
            <b>Host: {}</b> Number {}
        </li>
        """.format(node_name, random_number)
    html_res += "</ul>"

    return html_res