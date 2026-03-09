# Занятие 12. Решение дифференциальных уравнений с помощью нейронных сетей. PINN, DeepONet, FNO


Занятие провел: Иванов Егор (@e1vanov)

Материал составил: Иванов Егор (@e1vanov)

### Источники:

- Статья 1 по **PINN**. Решение ДУ: [Maziar Raissi et al., 2017](https://arxiv.org/abs/1711.10561), примерно 2200 цитирований
- Статья 2 по **PINN**. Обратные задачи: [Maziar Raissi et al., 2017](https://arxiv.org/abs/1711.10566), примерно 2200 цитирований
- **DeepONet**: [Lu Lu et al., 2019](https://arxiv.org/abs/1910.03193), примерно 1200 цитирований
- Neural Operator (**FNO, LNO, ...**): [Nikola Kovachki et al., 2021](https://arxiv.org/abs/2108.08481), примерно 2000 цитирований

- Теорема об универсальной аппроксимации операторов. [Chen, Chen, 1995](https://www.researchgate.net/profile/Tianping-Chen/publication/3302007_Universal_approximation_to_nonlinear_operators_by_neural_networks_with_arbitrary_activation_functions_and_its_applications_to_dynamic_systems/links/5580152308aeea18b77a8dd0/Universal-approximation-to-nonlinear-operators-by-neural-networks-with-arbitrary-activation-functions-and-its-applications-to-dynamic-systems.pdf), примерно 1800 цитирований

- Обучение операторов. Обзор: [Nicolas Boullé, Alex Townsend, 2023](https://arxiv.org/abs/2312.14688), примерно 140 цитирований

## Аннотация
Обсудим, как можно научить нейронную сеть физике и как с помощью этого можно построить альтернативу классическим численным солверам ОДУ и обратных задач.
Кроме того, на прошлых лекциях вы узнали, что нейронные сети являются универсальными аппроксиматорами функций. В этот раз мы повысим ставки и поговорим о том, могут ли нейронные сети аппроксимировать отображения между бесконечномерными пространствами - операторы, например, отображающие функции, задающие ДУ, в его решение.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/12-pinn/12-pinn.ipynb)
