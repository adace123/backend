from app import app, config

if __name__ == "__main__":
    app.run(host=config.Config.HOST, port=config.Config.PORT)
