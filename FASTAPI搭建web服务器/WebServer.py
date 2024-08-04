import fastapi
from fastapi import Response
import uvicorn

app = fastapi.FastAPI()


# {path}用于获取图片的名称，如0.jpg、1.jpg
# http://127.0.0.1:8000/images/0.jpg => /images/0.jpg路径
@app.get('/images/{path}')
def get_pic(path: str):
    with open(f'source/images/{path}', 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='jpg')


# 使用路由装饰器进行信息收发
@app.get('/')
def main():
    with open('source/html/index.html', 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='text/html')


@app.get('/{path}')
def main(path: str):
    with open(f'source/html/{path}', 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='text/html')


uvicorn.run(app, host='127.0.0.1', port=8000)
