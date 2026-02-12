# Занятие 02. Инициализация и регуляризация нейросетей


Занятие провел: Голубев Роман (@Tetragrammaton_123)

Материалы составил: Алексеев Илья (@voorhs)

### Источники:

- **Dropout**: [Nitish Srivastava et al., 2014](https://jmlr.org/papers/v15/srivastava14a.html), примерно 61к цитирований
- **Batch Normalization**: [Sergey Ioffe, Christian Szegedy, 2015](https://arxiv.org/abs/1502.03167), примерно 65к цитирований
- **Xavier / Glorot initialization**: [Xavier Glorot, Yoshua Bengio, 2010](https://proceedings.mlr.press/v9/glorot10a.html), примерно 30к цитирований
- **ResNet (residual connections)**: [Kaiming He et al., 2015](https://arxiv.org/abs/1512.03385), примерно 300к цитирований
- Про симметрии и остаточные связи: https://habr.com/ru/articles/688350/
- Про сглаживание ландшафта функции потерь: [Hao Li et al., 2017](https://arxiv.org/abs/1712.09913), примерно 3к цитирований

## Аннотация
На этом занятии обсуждаем основные функции активации и их влияние на инициализацию нейронных сетей, а также способы увеличения стабильности обучения. Рассмотрим основные приёмы для регуляризации: dropout и влияние стохастической оптимизации.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/02-init-reg/02-init-reg.ipynb)
