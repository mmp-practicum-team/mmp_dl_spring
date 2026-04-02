# Занятие 14. Рекуррентные нейронные сети


Занятие провел: Булкин Антон (@pochti_chekhov)

Материалы составили: Дегтев Василий (@vasco_de_gtev), Феоктистов Дмитрий (@trandelik), Алексеев Илья (@voorhs), Оганов Александр (@welmud) на основе материалов Хисматуллина Владимира (s02190724@gse.cs.msu.ru)

### Источники:

- **Simple Recurrent Networks (Elman)**: [Elman J. L., 1991](https://link.springer.com/content/pdf/10.1007/BF00114844.pdf), примерно 2 тысячи цитирований
- **LSTM**: [Hochreiter S., Schmidhuber J., 1997](https://www.bioinf.jku.at/publications/older/2604.pdf), примерно 146 тысяч цитирований
- **GRU**: [Cho K. et al., 2014](https://arxiv.org/abs/1406.1078), примерно 40 тысяч цитирований
- **Foundaments of RNN and LSTM**, [Alex Shertinsky,2023 ](https://arxiv.org/pdf/1808.03314.pdf), примерно 5 тысяч цитирований
- [Beam search](https://d2l.ai/chapter_recurrent-modern/beam-search.html)
- [Подсчет градиентов для разных видов RNN](https://mmuratarat.github.io/2019-02-07/bptt-of-rnn)
- [Открытй гитхаб курса по DL на coursera](https://github.com/amanchadha/coursera-deep-learning-specialization/tree/master/C5%20-%20Sequence%20Models)


## Аннотация
Данный семинар будет посвящен практическому применению RNN в различных задачах по обработке последовательностей. Семинар будет состоять из трех частей: вводная теоретическая часть, практика с различными видами RNN и обучение посимвольной языковой модели на основе RNN. В начале вспомним основные свойста RNN и какие типы задач они решают, разберем проблемы затухания и взрыва градиентов и как с ними бороться. Далее вспомним архитектуры GRU и LSTM и в чем их преимущество по сравнению с классической RNN Эламана. В практической части напишем цикл обучения с клипингом градиета и логгированием нормы градиента, обучим и сравним RNN Элмана, LSTM, GRU в различных задачах. В последней части вспомним задачу Causal Language Modeling и познакомимся со стратегиями декодирования: greedy, beam search и top-k sampling. В конце обучим собственную посимвольную языковую модель на текстах шекспира и реализуем жадное декодирование.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/14-rnn-practice/14-rnn-practice.ipynb)
