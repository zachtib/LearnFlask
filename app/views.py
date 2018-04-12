from app import app

@app.route('/')
def home():
    app.logger.debug('Hello, World!')
    return 'Hello, World!'