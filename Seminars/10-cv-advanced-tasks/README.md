# Занятие 10. Computer Vision: детекция и семантическая сегментация

Занятие провел: Загатин Даниил (@ZagatinDaniil)

Материалы составили: Иванов Егор (@e1vanov), Загатин Даниил(@ZagatinDaniil), Находнов Максим (nakhodnov17@gmail.com), Глеб Афанасьев, Варламова Арина, Солдатов Владислав

### Источники:

- **R-CNN**: [Ross Girshick et al., 2013](https://arxiv.org/abs/1311.2524v5), примерно 46 тысяч цитирований

- **Fast R-CNN**: [Ross Girshick, 2015](https://arxiv.org/abs/1504.08083), примерно 44 тысячи цитирований

- **Faster R-CNN**: [Shaoqing Ren et al., 2015](https://arxiv.org/abs/1506.01497), примерно 58 тысяч цитирований

- **YOLO**: [Joseph Redmon et al., 2015](https://arxiv.org/abs/1506.02640), примерно 73 тысячи цитирований

- **U-Net**: [Olaf Ronneberger et al., 2015](https://arxiv.org/abs/1505.04597), примерно 135 тысяч цитирований

-  **Link-Net**: [Abhishek Chaurasia, Eugenio Culurciello, 2017](https://arxiv.org/abs/1707.03718), примерно 2500 цитирований

- **U-shaped Neural Operator**: [Md Ashiqur Rahman et al., 2022](https://arxiv.org/abs/2204.11127), примерно 267 цитирований

- Под каждым изображением есть ссылка на источник, как правило являющийся статьей по теме


## Аннотация
Мы уже изучили методы классификации изображений, теперь мы обсудим более сложные задачи и подходы к их решению. Мы пройдем путь от моделей, которые решали задачу и требовали множество ресурсов, до способов обработки изображений в режиме реального времени. Обсудим, как сегментировать изображения и как это связано с глобальным контекстом. Кроме того, обсудим применение архитектур из компьютерного зрения в других областях, например, нейронных операторов.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/10-cv-advanced-tasks/10-cv-advanced-tasks.ipynb)
