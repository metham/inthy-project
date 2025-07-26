FROM python:3.10
WORKDIR /app
RUN pwd
RUN ls
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pwd
RUN ls
CMD ["python", "consumption_app/main.py"]