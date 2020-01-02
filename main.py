from app import app_factory
import uvicorn

app = app_factory()


def main():
    uvicorn_config = {"host": "127.0.0.1",
                      "port": 5000}

    uvicorn.run("main:app", **uvicorn_config)


if __name__ == '__main__':
    main()
