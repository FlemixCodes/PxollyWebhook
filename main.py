from src import app
from src.database import load_db
from src.setup import Setup


if __name__ == "__main__":
    setup = Setup()
    if setup.check_setup():
        load_db()
        app.run(debug=True)
    else:
        setup.setup()

