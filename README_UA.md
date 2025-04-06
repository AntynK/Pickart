# Pickart
#### [English version](https://github.com/AntynK/Pickart/blob/main/README.md)

Pickart - це формат файлу який використовує гра [Colouring art](https://github.com/AntynK/ColouringArt) для збереження зображень.

Назва 'Pickart' - походить від комбінування слів ['pickle'](https://docs.python.org/3.9/library/pickle.html) та 'art'.


## Про формат
Коренем .pickart файлу є словник серіалізований за допомогою [pickle](https://docs.python.org/3.9/library/pickle.html) та стиснений за допомогою [gzip](https://docs.python.org/3.9/library/gzip.html).

Структура файлу(версії 1.0.0):
``` Python
{
    "info":{
        "size": (1, 1),
        "version": 1
    },
    "palette":[(red, green, blue, alpha), ...],
    "pixels": [
        [(colour_index, is_painted), ...]
    ]
}
```

`"info"` - зберігає розмір зображення та версію Pickart файлу.
`"palette"` - зберігає палітру кольорів. Кожен колір це кортеж з цілих чисел в діапазоні від 0 до 255(включно), `alpha` - не обов'язковий. 


`"pixels"` - це двовимірний список який зберігає `colour_index`(int) та прапорець `painted`(bool). 

`colour_index` - це індекс кольору в палітрі, якщо цей піксель прозорий(`alpha` = 0) то індекс стає `None`, вказуючи що це порожній піксель.

`painted` - прапорець який вказує чи зафарбований піксель. Якщо його значення істина то піксель буде кольоровим, інакше відтінком сірого.


Модуль [pickle](https://docs.python.org/3.9/library/pickle.html) має проблеми з безпекою, гра використовує нестандартну версію pickle.load(), a [обмежений завантажувавч](https://docs.python.org/3/library/pickle.html#restricting-globals) який дозволяє зберігати лише базові типи(Неповний перелік: int, str, list, dict, tuple, set). Якщо файл містить зовнішній тип(будь-який об'єкт який потрібно імпортувати), то програма видасть помилку `UnpicklingError` з повідомленням `There is something strange in the file, do not trust it!`(переклад: `У файлі є щось дивне не довіряйте йому!`).

## Інтерфейс командного рядка
Цей модуль дає можливість конвертувати .png файли в .pickart і навпаки.

Команда яка показує доступні аргументи:

**Windows:**
```bash
python -m pickart -h
```
**Для Linux та MacOS**
```bash
python3 -m pickart -h
```

### Основні аргументи
`-i "шлях"` - вказує папку в якій знаходяться файли для конвертації(за замовчуванням 'input'), вказана папка має існувати.

`-o "шлях"` - вказує папку в якій будуть збереженні ковертовані файли(за замовчуванням 'output'), якщо папки не існує вона буде автоматично створена.

`-m "режим"` - вказує режим конвертації, можливі режими: 
* `to_pickart` - .png файли в .pickart файли;
* `to_png` - .pickart файли в .png файли;