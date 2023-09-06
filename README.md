# artist-album-catalog

[![Actions Status](https://github.com/ajib6ept/artist-album-catalog/workflows/api-check/badge.svg)](https://github.com/ajib6ept/artist-album-catalog/actions) [![Test Coverage](https://api.codeclimate.com/v1/badges/1192252f3a36d4862172/test_coverage)](https://codeclimate.com/github/ajib6ept/antibot-developer-trainee/test_coverage) [![Maintainability](https://api.codeclimate.com/v1/badges/1192252f3a36d4862172/maintainability)](https://codeclimate.com/github/ajib6ept/antibot-developer-trainee/maintainability)

Соберите с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры:

- Исполнитель
    - Название
- Альбом
    - Исполнитель
    - Год выпуска
- Песня
    - Название
    - Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.

В качестве площадки для демонстрации АПИ подключите к нему Swagger, чтобы можно было проверить работу АПИ через Postman

Результат присылайте в виде репозитория в GitHub с инструкцией по запуску. Бонусом будет, если проект будет запускаться через docker compose.

https://career.habr.com/vacancies/1000119444