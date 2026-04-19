# Лабораторная работа №3  
## Настройка nginx

## Цель работы

Настроить веб-сервер nginx для обслуживания нескольких сайтов на одном сервере с использованием HTTPS.

## Ход работы

В ходе выполнения лабораторной работы были выполнены следующие действия:

- установлен и запущен nginx  
- сгенерирован самоподписанный SSL-сертификат  
- настроен HTTPS (порт 443)  
- реализован редирект HTTP → HTTPS (порт 80)  
- настроены виртуальные хосты:
  - `pet1.local`
  - `pet2.local`  
- реализован механизм `alias`  
- исправлена кодировка (UTF-8)  

## Структура проекта

devops-lab3/
│
├── nginx/
│ ├── pet1.conf
│ └── pet2.conf
│
├── sites/
│ ├── site1/index.html
│ ├── site2/index.html
│ └── shared/info.txt
│
├── screenshots/
│
└── README.md


## 🌐 Проверка работы

Доступные адреса:

- http://pet1.local - редирект на HTTPS  
- https://pet1.local  
- https://pet1.local/shared/info.txt  
- https://pet2.local  


## 📸 Результаты работы

### Первый сайт (pet1)
![pet1](screenshots/pet1.png)

### Второй сайт (pet2)
![pet2](screenshots/pet2.png)

### Проверка alias
![alias](screenshots/alias.png)

### Проверка редиректа HTTP → HTTPS
![redirect](screenshots/redirect.png)


## Вывод

В ходе первой части лабораторной работы был настроен веб-сервер nginx для обслуживания нескольких сайтов. Реализована работа через HTTPS, настроены виртуальные хосты и механизм alias.  
