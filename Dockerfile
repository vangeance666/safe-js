FROM nikolaik/python-nodejs:python3.10-nodejs14

WORKDIR /safe-js
COPY . .

RUN pip3 install -r requirements.txt

RUN npm install box-js --global

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]