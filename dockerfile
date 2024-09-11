FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/app/src

# default commands
CMD ["python", "run.py", "github"]