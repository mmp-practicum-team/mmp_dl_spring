# Занятие 13. Эмбединги слов, дистрибутивная гипотеза, word2vec


Занятие провёл: Денисов Егор (mail: denisov.official72@gmail.com)

Материалы составили Денисов Егор (mail: denisov.official72@gmail.com), Ким Роман (tg: @karman_rim), Оганов Александр (tg: @welmud)

### Источники:
- Часть материалов основана на курсе [Математические методы анализа текстов, кафедра ММП](https://github.com/mmta-team/mmta_2021_fall/blob/main/cmc/slides/02_word_embeddings.pdf)

- [Конспект по основам NLP](https://github.com/mmp-practicum-team/mmp_practicum_spring_2024/blob/main/Seminars/Seminar%2007/%D0%AF%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8.%20Torchtext.ipynb), который подготовили: Феоктистов Дмитрий, Хисматуллин Владимир

- Часть материалов основана на [NLP Course](https://lena-voita.github.io/nlp_course.html)

- **Distributional Structure**: [Zellig S. Harris, 1954](https://www.tandfonline.com/doi/pdf/10.1080/00437956.1954.11659520), примерно 8400 цитирований
- **A Synopsis of Linguistic Theory**: [J. Firth, 1957](https://www.scirp.org/reference/ReferencesPapers?ReferenceID=1846447), примерно 5700 цитирований
- **Count-based methods**: [Peter D. Turney and Patrick Pantel, 2010](https://arxiv.org/abs/1003.1141), примерно 4200 цитирований
- **GloVe**: [Jeffrey Pennington et al., 2014](https://nlp.stanford.edu/pubs/glove.pdf), примерно 50 тысяч цитирований
- **Word2Vec**: [Tomas Mikolov et al., 2013](https://arxiv.org/abs/1301.3781), примерно 52 тысячи цитирований
- **Negative sampling and other acceleration methods**: [Tomas Mikolov et al., 2013](https://arxiv.org/abs/1310.4546), примерно 50 тысяч цитирований
- **FastText**: [Piotr Bojanowski et al., 2017](https://arxiv.org/abs/1607.04606), примерно 15 тысяч цитирований

- Для большинства изображений указан источник, откуда оно взято, как правило, являющийся статьей
- 
## Аннотация
В этом ноутбуке мы постараемся познакомиться с задачей обработки естественного языка (natural language processing/NLP). В частности на данной лекции будут разобраны методы получения векторных представлений слов &ndash; от простых статистических до нейросетевых подходов. Кроме того, вспомним о том, что такая токенизация, и какой она бывает.

**Оффтоп**: не стоит думать, что NLP ограничивается только большими моделями, в начале развития были использованы **колоссальные труды** лингвистов и людей с филологическим образованием. Гигантские команды формулировали различные логические правила на основе знаний о синтаксисе языка.
Например, вы можете изучить [национальный корпус русского языка](https://ruscorpora.ru/), в котором собирались знания многих специалистов о русском языке. Каждый текст имеет: стиль, автора, год, при этом корпус содержит более 2 миллиардов слов (что в **10000 раз больше**, чем в книге "Война и мир").

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/13-embedding/13-embedding.ipynb)
