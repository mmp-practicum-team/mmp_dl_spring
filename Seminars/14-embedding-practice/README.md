# Занятие 14. Эмбеддинги слов, классификация текстов

Занятие провёл: Денисов Егор (mail: denisov.official72@gmail.com)

Материалы составили Денисов Егор (mail: denisov.official72@gmail.com), Оганов Александр (tg: @welmud)

### Источники:

- [Конспект по основам NLP](https://github.com/mmp-practicum-team/mmp_practicum_spring_2024/blob/main/Seminars/Seminar%2007/%D0%AF%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8.%20Torchtext.ipynb), который подготовили: Феоктистов Дмитрий, Хисматуллин Владимир

- [Документация gensim](https://radimrehurek.com/gensim/models/word2vec.html)

- **UMAP**: [Leland McInnes et al., 2018](https://arxiv.org/abs/1802.03426), примерно 22 тысячи цитирований

- [Документация umap](https://umap-learn.readthedocs.io/en/latest/)

- [Выделение смысловых компонент слов с помощью Lasso](https://lars76.github.io/2021/06/16/operations-contextual-embeddings.html)

- [Датасет рецензий с Imdb](https://ai.stanford.edu/~amaas/data/sentiment/).

- [Документация CatBoost](https://catboost.ai/docs/en/concepts/python-reference_catboostclassifier)

- [Примеры датасетов для классификации текстов](https://lena-voita.github.io/nlp_course/text_classification.html#dataset_examples)

- [Документация fasttext](https://fasttext.cc/docs/en/python-module.html)

- [Документация tokenizers](https://huggingface.co/docs/tokenizers/index)

- [Документация datasets](https://huggingface.co/docs/datasets/index)

- Для большинства изображений указан источник, откуда оно взято, как правило, являющийся статьей


## Аннотация
На занятии мы попробуем на практике то, что изучили на лекции &ndash; посмотрим на операции с эмбеддингами, попробуем самостоятельно обучить word2vec и fasttext, а также решить с их помощью прикладную задачу классификации текстов. Кроме того, посмотрим на нейросетевой подход к решению данной задачи, а именно, как использовать MLP и сверточные сети для обработки текстов.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/14-embedding-practice/14-embedding-practice.ipynb)
