# Занятие 24. Практика обучения GAN

Занятие провел: Оганов Александр (tg: @welmud)

Материалы составили: Оганов Александр (tg: @welmud), Находнов Максим (nakhodnov17@gmail.com)


### Источники:


- **Generative Adversarial Networks**: [Ian J. Goodfellow et al., 2014](https://arxiv.org/abs/1406.2661), примерно 94 тысячи цитирований &ndash; работа в которой была предложена идея генеративно состязательных сетей

- [Небольшая история о том, как появилась идея GAN](https://www.technologyreview.com/2018/02/21/145289/)

- **DCGAN**: [Alec Radford et al., 2016](https://arxiv.org/abs/1511.06434), примерно 22 тысячи цитирований &ndash; улучшение GAN модели с помощью выявления принципов обучение и подбора правильной архитектуры; одна из первых моделей качественной генерации цветных изображений разрешением 64 пикселей

- [Обзор на область генеративных моделей от автора DCGAN на конференции ICLR 2026](https://iclr.cc/virtual/2026/test-of-time/10020471) &ndash; обзор идей, методов, истории их появлений и науке; **таймкод 35:40**, может потребоваться регистрация

- **Towards Principled Methods for Training Generative Adversarial Networks**: [Martin Arjovsky and Leon Bottou, 2017](https://arxiv.org/abs/1701.04862), примерно 3400 цитирований


- **Wasserstein GAN**: [Martin Arjovsky et al., 2017](https://arxiv.org/abs/1701.07875), примерно 22 тысячи цитирований &ndash; использование расстояния Вассерштейна для оценки похожести распределений (вместо KL дивергенции)

- **WGAN-GP**: [Ishaan Gulrajani et al., 2017](https://arxiv.org/abs/1704.00028), примерно 15 тысяч цитирований &ndash; появление gradient penalty для соблюдения необходимого условия модели критика

- **R3GAN**: [Yiwen Huang et al., 2025](https://arxiv.org/abs/2501.05441), примерно 100 цитат (май 2026) &ndash; современный подход к стабильному обучению GAN моделей с высоким разнообразием и теоретическими гарантиями

- **f-GAN**: [Sebastian Nowozin et al., 2016](https://arxiv.org/abs/1606.00709), примерно 2300 цитирований

- **About KL Divergences**: [Alan Chan et al., 2022](https://arxiv.org/abs/2107.08285), 61 цитирование

- **How to Train GAN**: [GitHub](https://github.com/soumith/ganhacks)

- **From GAN to WGAN**: [GitHub](https://lilianweng.github.io/posts/2017-08-20-gan/)

- **Разные реализации**: [GitHub](https://github.com/eriklindernoren/PyTorch-GAN/tree/master)

- [Greedification Operators for Policy Optimization: Investigating Forward and Reverse KL Divergences](https://jmlr.org/papers/volume23/21-054/21-054.pdf)


- [Часть материала основана на курсе "Глубокого обучения" ВМК МГУ](https://github.com/Dyakonov/DL/blob/47f2efbadfd15f8d0a5f5cb209386aba64326eb6/2020/DL2020_053gan_13n.pdf)

- [Часть материала основана на семинаре НИУ ВШЭ](https://github.com/nakhodnov17/HSE_DPO_DL/tree/40bee88bfae8c601f1068d8d70ad0d04078286dd/Seminars/Seminar%2007)

- [Часть материала основана на курсе "Глубокие генеративные модели" AIMasters](https://github.com/r-isachenko/2024-DGM-AIMasters-course/blob/5aa2879d9d4091cbed6b8d86900ee36e47489767)



## Аннотация

[По ссылке](https://wandb.ai/nakhodnov17/mmp_practicum_spring_2024%7CSeminar%2011%7CWGAN-GP/runs/o7qnv1aq?nw=nwusernakhodnov17) можно посмотреть логи `wandb` для всех экспериментов.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/24-gan-practice/24-gan-practice.ipynb)
