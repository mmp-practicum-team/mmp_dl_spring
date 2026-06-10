# Занятие 17. Трансформеры

Занятие провел: Ким Роман (@karman_rim)

Материалы составили: Алексеев Илья (@voorhs), Ким Роман (@karman_rim)

### Источники:

- **Attention**: [Ashish Vaswani et al., 2017](https://arxiv.org/abs/1706.03762), примерно 244 тысяч цитирований
- **FlashAttention**: [Tri Dao et al., 2022](https://arxiv.org/abs/2205.14135), примерно 5 тысяч цитирований


## Аннотация
Сегодня мы разберём архитектуру **трансформера**, предложенную в работе [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017). На момент весны 2025 года у этой статьи более **230000+  цитирований** &ndash; это одна из самых влиятельных работ в истории машинного обучения, определившая облик практически всех современных языковых моделей.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/17-transformers/17-transformers.ipynb)
