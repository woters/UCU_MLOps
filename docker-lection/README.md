Тестовий проект, щоб показати як користуватися докером:
``````
docker build -t ihor-p/docker-lection:0.0.1 . 
docker images
docker run -p 8080:5000 ihor-p/docker-lection:0.0.1
# detached mode
docker run -p 8080:5000 -d ihor-p/docker-lection:0.0.1
``````
Список контейнерів (```-a```) для стопнутих)

```
docker ps -a
```
Подивитися логи контейнера (```-f``` щоб приатачитися):
```
docker logs
```

Памʼять вижирається дуже швидко. Щоб все почистити:
```
docker system prune -a
docker volume prune
```

Якщо щось зайняло порт (для мак ос):
```
lsof -i tcp:<PORT>
kill -15 <PID>
kill -9 <PID>
```