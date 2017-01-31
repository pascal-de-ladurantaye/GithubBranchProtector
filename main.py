from aiohttp import web

from app import APP
from configs import PORT


if __name__ == '__main__':
    web.run_app(APP, port=PORT)
