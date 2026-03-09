# Занятие 09. Цикл обучения


Занятие провел: Оганов Александр (@welmud)

Материалы составили: Оганов Александр (@welmud), Находнов Максим (nakhodnov17@gmail.com)

### Источники:

- [Сборка нейронной сети PyTorch](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html#sphx-glr-beginner-blitz-neural-networks-tutorial-py)

- [Обучение классификатора для CIFAR-10](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py)

- [Reproducibilty PyTorch](https://pytorch.org/docs/stable/notes/randomness.html)

- [Подробное описание получения state-of-the-art (SOTA) результатов.](https://pytorch.org/blog/how-to-train-state-of-the-art-models-using-torchvision-latest-primitives/)

- Ноутбук во многом опирается на [этот конспект](https://github.com/mmp-practicum-team/mmp_dl_spring_2025/blob/main/Seminars/08-training/08-training.ipynb)

## Аннотация
В этом ноутбуке вы познакомитесь с тем, как писать цикл обучения нейронных сетей с помощью библиотеки PyTorch. В процессе обучения вы будете наблюдать изменение метрик, значений функций потерь и других показателей, для отслеживания которых их нужно правильно логировать. В ноутбуке вы обучите свёрточную нейронную сеть (CNN) для классификации датасета **[Imagenette](https://github.com/fastai/imagenette.git)** и сравните с transfer learning.  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/09-training/09-training.ipynb)
