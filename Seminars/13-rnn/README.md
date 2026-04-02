# Занятие 13. Рекуррентные нейронные сети

Занятие провела: Загатин Даниил (@ZagatinDaniil)

Материалы составили: Овсиенко Олеся (@Olesya_Ovsienko), Алексеев Илья (@voorhs)

### Источники:

- [Советуем так же ознамиться с материалами предыдущих лет](https://github.com/mmp-practicum-team/mmp_practicum_spring_2024/blob/main/Seminars/Seminar%2006/%D0%A0%D0%B5%D0%BA%D1%83%D1%80%D1%80%D0%B5%D0%BD%D1%82%D0%BD%D1%8B%D0%B5%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%A1%D0%B5%D1%82%D0%B8.ipynb)

- **Simple Recurrent Networks (Elman)**: [Elman J. L., 1991](https://link.springer.com/content/pdf/10.1007/BF00114844.pdf), примерно 2 тысячи цитирований
- **Vanishing/Exploding Gradients in RNN**: [Pascanu R. et al., 2013](https://arxiv.org/abs/1211.5063), примерно 9 тысяч цитирований
- **LSTM**: [Hochreiter S., Schmidhuber J., 1997](https://www.bioinf.jku.at/publications/older/2604.pdf), примерно 146 тысяч цитирований
- **GRU**: [Cho K. et al., 2014](https://arxiv.org/abs/1406.1078), примерно 40 тысяч цитирований
- **Batch Normalization**: [Ioffe S., Szegedy C., 2015](https://arxiv.org/abs/1502.03167), примерно 67 тысяч цитирований
- **Layer Normalization**: [Ba J. L., Kiros J. R., Hinton G. E., 2016](https://arxiv.org/abs/1607.06450), примерно 18 тысяч цитирований
- **Instance Normalization**: [Ulyanov D., Vedaldi A., Lempitsky V., 2016](https://arxiv.org/abs/1607.08022), примерно 5 тысяч цитирований
- **Bahdanau Attention**: [Bahdanau D., Cho K., Bengio Y., 2014](https://arxiv.org/abs/1409.0473), примерно 43 тысячи цитирований

Реализации:

- **RNN (PyTorch)**: [https://pytorch.org/docs/stable/generated/torch.nn.RNN.html](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)
- **Gradient clipping (PyTorch)**: [https://docs.pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html](https://docs.pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html)
- **BatchNorm1d (PyTorch)**: [https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html)
- **LayerNorm (PyTorch)**: [https://pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html](https://pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)
- **GRU (PyTorch)**: [https://pytorch.org/docs/stable/generated/torch.nn.GRU.html](https://pytorch.org/docs/stable/generated/torch.nn.GRU.html)
- **LSTM (PyTorch)**: [https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)

## Аннотация
Это занятие будет посвящено рекуррентным нейронным сетям (RNN) и их эволюции от простой ячейки до современных gated-моделей. Мы начнём с ограничений статических эмбеддингов (word2vec), разберём базовую RNN-ячейку, проблему vanishing/exploding gradients при Backpropagation Through Time и практические решения: gradient clipping, Layer Normalization (почему BatchNorm не подходит для текстов), правильную токенизацию. Далее подробно рассмотрим LSTM и GRU &ndash; как внутренние гейты и skip-connections решают проблему длинных зависимостей. Обсудим ключевые задачи последовательного моделирования: классификация текстов, causal language modeling (next-token prediction как первый пример self-supervised learning), распознавание именованных сущностей (BIO-разметка), машинный перевод с encoder-decoder архитектурой. Затронем модификации (bidirectional RNN, stacked layers, residual connections) и введём механизм внимания (Bahdanau attention). Мы опираемся на ключевые статьи по каждой теме, а количество цитирований указано для того, чтобы дать представление о масштабе области и вовлеченности научного сообщества, а не для прямого сравнения статей друг с другом.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/13-rnn/13-rnn.ipynb)
