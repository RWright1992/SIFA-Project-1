FROM python:3.6

COPY . .

RUN pip3 install -r requirements.txt

ENV DATABASE_URI=mysqlite:///data.db MY_SECRET_KEY=shhhhhhh

RUN ["python3", "create.py"]

ENTRYPOINT ["python3", "app.py"]