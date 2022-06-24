FROM python:3.8-slim-buster

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000


# CMD ["python", "app.py"]
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
# CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5000", "main:app"]


# ENTRYPOINT ["python"]
# ENTRYPOINT ["docker-entrypoint.sh"]
# CMD ["flask", "run", "--host=localhost", "--port=5001"]