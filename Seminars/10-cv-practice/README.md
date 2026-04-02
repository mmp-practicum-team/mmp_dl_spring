# Занятие 10. Практика решения задач компьютерного зрения

Занятие провел: Загатин Даниил (@ZagatinDaniil)

Материалы составили: Загатин Даниил (@ZagatinDaniil), Федоров Артем, Оганов Александр (@welmud), Солдатов Владислав, Глеб Афанасьев, Максим Находнов, Варламова Арина

### Источники:

- [Лекция Detection and Segmentation с курса cs231, Standford](https://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf)

- Сегментация объектов видео: [Wenguan Wang et al., 2017](https://arxiv.org/abs/1702.00871), примерно 700 цитирований

- Ортогональная регуляризации свёрток: [Jiayun Wang et al., 2019](https://arxiv.org/abs/1911.12207), примерно 300 цитирований

- Детекция заболиваний растений: [Ameer Tamoor Khan et al., 2023](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2023.1308528/), примерно 80 цитирований

- Все логи comet_ml доступны по [ссылке](https://www.comet.com/enteralt/cv-mmp-2026/view/new/panels). Все логи wandb с 2025 года доступны по [ссылке](https://wandb.ai/3145tttt/ImageSegmentationPrac/workspace).
- Чекпоинт модели сегментации находится по [ссылке](https://huggingface.co/3145tttt/segmentation).

## Аннотация
На занятии мы на практике реализуем полный цикл обучения модели сегментации изображений &ndash; от предобработки данных до цикла обучения. Разберем, какие метрики и параметры важно логировать для контроля качества сегментации. Также рассмотрим инференс (применение) предобученных моделей детекции и сегментации. Отдельно на примере ортогональной регуляризации сверточных слоев обсудим, как подходить к проектированию дизайна эксперимента, как выборать архиктеры, данные и как отразить это в цикле обучения.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/10-cv-practice/10-cv-practice.ipynb)
