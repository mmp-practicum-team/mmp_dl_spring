# Занятие 05. Оптимизация в глубоком обучении


Занятие провел: Феоктистов Дмитрий (@trandelik)

Материалы составили: Феоктистов Дмитрий (@trandelik), Находнов Максим (nakhodnov17@gmail.com)

### Источники:

Источники:

- **RMSProp**: [Geoffrey Hinton, 2012](https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf), примерно 2.5 тысячи цитирований
- **AdaGrad**: [Duchi et al., 2011](https://jmlr.org/papers/volume12/duchi11a/duchi11a.pdf), примерно 16 тысяч цитирований
- **Adam**: [Kingma & Ba, 2014](https://arxiv.org/pdf/1412.6980), примерно 240 тысяч цитирований
- О неоптимальности глобального минимума: [Qingguang Guan](https://arxiv.org/abs/2407.16872v1), 1 цитирование
- Усреденение весов приводит к более широкому минимуму: [Izmailov et al., 2018](https://arxiv.org/pdf/1803.05407), примерно 2 тысячи цитирований
- О больших learning rate: [Lobacheva et al., 2023](https://arxiv.org/pdf/2311.11303), 4 цитирования
- О больших learning rate: [Sadrtdinov et al., 2024](https://arxiv.org/abs/2410.22113), 6 цитирований
- learing rate warmup и самостабилизация обучения: [Kalra & Barkeshli, 2024](https://arxiv.org/pdf/2406.09405), 69 цитирований
- learning rate warmup и обобщенная гладкость: [Riabinin et al., 2026](https://arxiv.org/pdf/2602.05813), пока без цитирований
- **AdamW**: [Loshchilov & Hutter, 2017](https://arxiv.org/abs/1711.05101), примерно 38 тысяч цитирований
- **AdEMAMix**: [Pagliardini et al., 2024](https://arxiv.org/abs/2409.03137), 31 цитирований
- **warmup-stable-decay scheduler**: [Hägele et al., 2024](https://arxiv.org/abs/2405.18392), 101 цитирований
- **Schedule-Free Optimizer** ([[Defazio et al., 2024]](https://arxiv.org/abs/2405.15682)), 146 цитирований
- **SignSGD** и **Signum**: [Bernstein et al., 2019](https://arxiv.org/abs/1802.04434), примерно 1.5 тысячи цитирований
- **Lion**: [Chen et al., 2023](https://arxiv.org/abs/2302.06675), 810 цитирований
- **Shampoo**: [Gupta et al., 2018](https://arxiv.org/abs/1802.09568), 430 цитирований
- **SOAP**: [Vyas et al., 2024](https://arxiv.org/abs/2409.11321), 148 цитирований
- **Muon**: [Jordan et al., 2024](https://kellerjordan.github.io/posts/muon/), 214 цитирований

## Аннотация
На этом занятии обсуждаем базовые методы оптимизации (SGD, AdaGrad, RMSProp, Adam, AdamW), как они устроены и почему, какие у них есть недостатки, почему одни методы лучше других. Также затрагиваем learning rate schedulers и зачем они нужны. Во второй части занятия уходим в сторону современных методов и их устройства, включая новый популярный оптимизатор Muon.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/05-optimization/05-optimization.ipynb)
