from .celery import app
import platform
from random import randint

@app.task
def get_random_number():
    """Gets a random number and the name of the node.

    Returns:
        {"random_number": number, "node_name": string}: A random number and the name of the node it came from.
    """
    nodename = platform.node()
    random_number = randint(0, 1000)

    return {"random_number": random_number, "node_name": nodename}