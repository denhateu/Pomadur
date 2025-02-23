# Pomadur

Охуенная програ для запуска таймера Pomodoro в терминале.

## Установка

Пока что инструкция по установке и запуску есть только для Linux.

### Linux

#### Для ленивых

<details>
  <summary>Click me</summary>

  Я сделал скрипт для автоматического скачивания зависимостей и запуска.
  Но перед этим нужно [клонировать репозиторий](https://github.com/denhateu/Pomadur#для-не-ленивых) к себе на комп.

  ```
  ./run.sh
  ```
</details>

#### Для не ленивых

1. Клонирование репозитория

```
git clone https://github.com/denhateu/Pomadur
```

2. Переход в директорию с проектом

```
cd Pomadur
```

3. Создание виртуального окружения

```
python3 -m venv venv
```

4. Активация виртуального окружения

```
source venv/bin/activate
```

5. Установка зависимостей

```
pip3 install -r requirements.txt
```

6. Запуск скрипта

```
python3 scripts/main.py
```

## Зависимости

* Python 3.6.9
* pip3 9.0.1
* pyinstaller 3.6
