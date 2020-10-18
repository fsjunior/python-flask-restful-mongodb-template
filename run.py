from app.app import create_app
from app.common import settings

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=settings.app_port)
