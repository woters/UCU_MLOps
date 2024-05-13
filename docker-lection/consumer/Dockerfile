# https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.11-slim-bookworm

# Копіюємо файл з залежностями, створюється новий шар
COPY requirements.txt requirements.txt

# Встановлюємо залежності вказалі requirements.txt - теж новий шор
RUN pip install --no-cache-dir -r requirements.txt

# Додаємо наш код - створили новий шар. таким чином при ребілді не потрібно заново ставити залежності при змані коду
ADD . .

# Run app.py when the container launches
# https://spacelift.io/blog/docker-entrypoint-vs-cmd
ENTRYPOINT [ "python" ] 
CMD ["-u", "consumer.py"]
