from fastapi import FastAPI
from fastapi import Response
import urllib.parse
import uvicorn

"""
FastAPI框架可以封装web开发，具有更为简介完善的框架
"""
# 创建FastAPI框架对象
app = FastAPI()


# 通过@app装饰器收发数据
# @app.get(url)通过get方式获取数据
# 要实现多个页面请求，则写多个响应函数就可以
@app.get(urllib.parse.unquote('/html中的表单标签.html'))
def main():
    with open('D:/AIProject/Project/HTML_and_CSS/html中的表单标签.html', 'rb') as f:
        data = f.read()
    # 响应数据，这边接收ip传来的请求，并响应数据
    return Response(content=data, media_type='text/html')


# 持续运行框架对象
uvicorn.run(app, host='127.0.0.1', port=8000)
