# 使用官方Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录
COPY . /app

# 安装所需的Python包和iputils-ping
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    pip install --no-cache-dir flask

# 暴露应用运行端口
EXPOSE 8080

# 运行Flask应用
CMD ["python", "ping_server.py"]
