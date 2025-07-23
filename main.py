from app import create_app
import subprocess
import os

app = create_app()

if __name__ == '__main__':

    # Aquí arrancas Flask
    app.run(port=5555, debug=True)
