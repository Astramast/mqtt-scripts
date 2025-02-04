FROM python:3.10-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt
# Why Copy everything after ? Because Docker/Podman will not rebuild previous lines if requirements.txt has not changed. See Docker caching optimization.
COPY . .

CMD ["python", "listener.py"]
