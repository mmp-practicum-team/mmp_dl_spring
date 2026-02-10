## Стиль оформления занятия


1. В папке `Seminars` сделать подпапку `{номер занятия}-{название на англ. краткое}`. Например, `01-intro`
2. В папке занятия:
    - `README.md` с названием пары, кто провел, кто сделал материалы, аннотация, источники
    - ноутбук
    - версия ноутбука в pdf (так как очень часто ноутбуки после обновления GitHub битые и с мобильной версией открыть удобно pdf). Скрипт для конвертации в pdf:
      ```
      jupyter-nbconvert --to webpdf --allow-chromium-download Seminars/01-intro.ipynb
      ```
    - ноутбук в виде бейджа: `[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/<your-lecture>.ipynb)`
    - **Важно:** все изображения внутри ноутбука перевести в base64, чтобы не было ссылок на файлы (ноутбук должен содержать в себе всё необходимое). Можно воспользоваться [скриптом](./tutors/embed_notebook_images.py). Желательно избегать `svg` изображений, они не отображаются в веб версии
3. [В основную таблицу](./README.md) добавить ссылку на подпапку занятия, в ней будет отображаться `README.md` со всей необходимой информацией


[Пример оформления занятия 1](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/01-intro). Пример оформления с курса [DL2 ВШЭ](https://github.com/thecrazymage/DL2_HSE/tree/main/week_01). 
