# Занятие 22. Parameter-Efficient Fine-Tuning

Занятие провел: Владимир Богачев (@bogachevvTG)

Материалы составил: Владимир Богачев (@bogachevvTG)


### Источники:

- **GPT-3 / few-shot learning**: [Brown et al., 2020](https://arxiv.org/abs/2005.14165), примерно 70 тысяч цитирований
- **Prompt Tuning**: [Lester et al., 2021](https://arxiv.org/abs/2104.08691), примерно 7000 цитирований
- **Prefix Tuning**: [Li, Liang, 2021](https://arxiv.org/abs/2101.00190), примерно 7000 цитирований
- **Adapters**: [Houlsby et al., 2019](https://arxiv.org/abs/1902.00751), примерно 8000 цитирований
- **LoRA**: [Hu et al., 2022](https://openreview.net/forum?id=nZeVKeeFYf9), примерно 20 тысяч цитирований
- **rsLoRA**: [Kalajdzievski, 2023](https://arxiv.org/abs/2312.03732), примерно 200 цитирований
- **LoRA+**: [Hayou et al., 2024](https://arxiv.org/abs/2402.12354), примерно 200 цитирований
- **PiSSA**: [Meng et al., 2024](https://arxiv.org/abs/2404.02948), примерно 400 цитирований
- **QLoRA**: [Dettmers et al., 2023](https://arxiv.org/abs/2305.14314), примерно 6500 цитирований
- **Intrinsic dimensionality**: [Aghajanyan et al., 2021](https://arxiv.org/abs/2012.13255), примерно 1000 цитирований
- **DoRA**: [Liu et al., 2024](https://arxiv.org/abs/2402.09353), примерно 1300 цитирований


## Аннотация

На этой паре поговорим о том, как работать с LLM без долгого и дорогого дообучения. Разберём zero-shot и few-shot подходы, затем посмотрим, что такое prompt tuning и как он помогает адаптировать модель под задачу. Отдельно обсудим LoRA и другие методы PEFT &ndash; современные и практичные способы тонкой настройки больших моделей.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/22-peft/22-peft.ipynb)
