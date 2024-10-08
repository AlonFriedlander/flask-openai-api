from flask import Flask
from app import create_app

# Create the Flask application instance using the application factory pattern.
app: Flask = create_app()


def main() -> None:
    """
    Runs the Flask web server on host '0.0.0.0' and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)


# Ensures the app only runs when this script is executed directly.
if __name__ == '__main__':
    main()
