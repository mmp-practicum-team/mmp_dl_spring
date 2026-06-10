# Занятие 31. CLIP

Занятие провел: Ильясов Эрик (@erikotoz)

Материалы составили: Оганов Александр (@welmud), Ильясов Эрик (@erikotoz)

### Источники:

- **CLIP**: [Alec Radford et al., 2021](https://arxiv.org/abs/2103.00020), примерно 33000 цитирований

- [Пост про CLIP от создателей](https://openai.com/research/multimodal-neurons)

- [Официальная реализация](https://github.com/openai/CLIP)

- Часть примеров взята [из источника](https://medium.com/@kerry.halupka/getting-started-with-openais-clip-a3b8f5277867)

- [Contrastive Representation Learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/)

## Аннотация

На занятии обсудим:
- зачем это может быть нужно;
- как из этого построить классификатор и модель сегментации;
- как оценивать качество сгенерированных изображений.

По сути дела увидим, что мультимодальные модели, а точнее извлекаемые ими признаки, крайне полезны на практике. Если раньше у нас был fine-tuning, потом были PEFT методы, то сейчас будем говорить про zero-shot подходы (когда нет обучающей выборки и примеров)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/31-clip/31-clip.ipynb)
