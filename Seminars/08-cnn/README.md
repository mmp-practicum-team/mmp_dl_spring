# Занятие 08. Свёрточные архитектуры


Занятие провел: Оганов Александр (@welmud)

Материалы составил: Оганов Александр (@welmud)

Материалы основаны на лекции Садртдинова Ильдуса Рустемовича

### Источники:
- [Лекция Садртдинова Ильдуса Рустемовича на курсе "Введение в глубокое обучение" факультета ФКН](https://github.com/isadrtdinov/intro-to-dl-hse/blob/1fd3f9bf82fc7aa8e0475210318423559f02f582/lecture-notes/notes-05-cnn.pdf)

- **LeNet**: [Yann LeCun et al., 1998](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf), примерно 84 тысячи цитирований
- **ImageNet**: [O.Russakovsky et al., 2015](https://arxiv.org/abs/1409.0575), примерно 49 тысяч цитирований
- **AlexNet**: [Krizhevsky et al., 2012](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf), примерно 150 тысяч цитирований
- **VGG**: [Simonyan and Zisserman, 2014](https://arxiv.org/abs/1409.1556), примерно 160 тысяч цитирований
- **GoogLeNet (a.k.a. Inception)**: [Szegedy et al., 2014](https://arxiv.org/abs/1409.4842), примерно 71 тысяча цитирований
- **ResNet**: [He et al., 2015](https://arxiv.org/abs/1512.03385), примерно 310 тысяч цитирований
- Ландшафт функции потерь при skip connections: [Hao Li et al., 2017](https://arxiv.org/abs/1712.09913), примерно 3 тысячи цитирований
- [Ландшафты функций потерь](https://losslandscape.com/videos/)
- Ансамблирование в skip connections: [Veit et al., 2016](https://arxiv.org/abs/1605.06431), примерно 1500 цитирований
- **DenseNet**: [Huang et al., 2016](https://arxiv.org/abs/1608.06993), примерно 60 тысяч цитирований
- **MobileNet**: [Howard et al., 2017](https://arxiv.org/abs/1704.04861), примерно 37 тысяч цитирований
- **NASNet**:  [Zoph et al., 2017](https://arxiv.org/abs/1707.07012), примерно 9 тысяч цитирований
- **EfficientNet**: [Tan and Le, 2019](https://arxiv.org/abs/1905.11946), примерно 35 тысяч цитирований
- **ConvNet**: [Liu et al., 2022](https://arxiv.org/abs/2201.03545), примерно 12 тысяч цитирований

## Аннотация
Это занятие будет посвящено развитию сверточных архитектур. Мы проследим, как проверялись различные гипотезы и как менялась область с течением времени, опираясь на ключевые статьи. Для каждой работы мы разберем, какую проблему она решала, обсудим роль бенчмарков, а также идеи, которые впоследствии перешли в другие области, и способы их интерпретации. Мы также затроним одну из самых важных идей для глубинного обучения &ndash; перенос знаний (transfer learning). Количество цитирований указано для того, чтобы дать представление о масштабе области и вовлеченности научного сообщества, а **не** для прямого сравнения статей друг с другом.


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/08-cnn/08-cnn.ipynb)
