FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY . /app

ENV TZ=Asia/Ho_Chi_Minh

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

RUN pip uninstall -y uvicorn
RUN pip install uvicorn[standard]

RUN apt-get update -y

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]