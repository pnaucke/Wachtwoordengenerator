FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "Wachtwoordengenerator.py"]

EXPOSE 8000