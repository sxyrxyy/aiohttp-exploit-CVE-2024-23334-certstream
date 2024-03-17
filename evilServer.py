# https://gist.github.com/W01fh4cker/2b570b1d0df40aa94808184c231d7ecb

import os
from aiohttp import web


def create_static_folder():
    current_directory = os.getcwd()
    
    static_folder_path = os.path.join(current_directory, "static")
    
    if not os.path.exists(static_folder_path):
        os.makedirs(static_folder_path)


async def index(request):
    return web.Response(text="Hello, World!")


create_static_folder()

app = web.Application()
app.router.add_routes([
    web.static("/static", "static/", follow_symlinks=True),
])
app.router.add_get('/', index)





if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8888)
