FROM python:3.9-alpine

WORKDIR /app

COPY ./backend/requirements.txt requirements.txt


# requirements.txtにリストされたパッケージをインストールする
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# ADD main.py ./backend/
# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]