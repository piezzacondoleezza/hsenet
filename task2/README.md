1. поиск мин MTU в канале между локальным пользователем и хостом
2. обернуто в докер

### Тестирование:
копируем репозиторий
```
$ git clone https://github.com/piezzacondoleezza/hsenet.git
```
запуск:
```
$ docker build . -f Dockerfile -t MTU
$ docker run MTU
```
