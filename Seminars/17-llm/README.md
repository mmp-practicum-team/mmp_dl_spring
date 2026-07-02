# Занятие 17. Обучение LLM


Занятие провел: Феоктистов Дмитрий (tg: @trandelik)

Материалы составили: Марьясов Максим (tg: @oop_clon), Богачев Владимир (tg: @bogachevvTG)
### Источники:

- **Attention Is All You Need**: [Ashish Vaswani et al., 2017](https://arxiv.org/abs/1706.03762), примерно 240,000 цитирований &ndash; оригинальная работа, представившая архитектуру Transformer, которая стала основой всех современных LLM  

- **Deep Reinforcement Learning from Human Preferences**: [Paul Christiano et al., 2017](https://arxiv.org/abs/1706.03741), примерно 7,000 цитирований &ndash; базовый подход к обучению через человеческие предпочтения, лежащий в основе RLHF  

- **Improving Language Understanding by Generative Pre-Training (GPT)**: [Alec Radford et al., 2018](https://openai.com/research/language-unsupervised), примерно 20,000 цитирований &ndash; введение подхода generative pre-training: предобучение языковой модели с последующим fine-tuning под задачи  

- **Language Models are Unsupervised Multitask Learners (GPT-2)**: [Alec Radford et al., 2019](https://openai.com/research/better-language-models), примерно 24,000 цитирований &ndash; демонстрация того, что крупные языковые модели могут решать множество задач в zero-shot режиме без явного обучения на них  

- **Language Models are Few-Shot Learners**: [Tom B. Brown et al., 2020](https://arxiv.org/abs/2005.14165), примерно 70,000 цитирований &ndash; статья про GPT-3, где показано, что масштабирование моделей приводит к появлению in-context learning и позволяет решать задачи без fine-tuning  

- **Scaling Laws for Neural Language Models**: [Jared Kaplan et al., 2020](https://arxiv.org/abs/2001.08361), примерно 8,000 цитирований &ndash; эмпирические законы масштабирования: качество моделей предсказуемо улучшается при увеличении параметров, данных и вычислений

- **Training Compute-Optimal Large Language Models (Chinchilla)**: [Jordan Hoffmann et al., 2022](https://arxiv.org/abs/2203.15556), примерно цитирований &ndash; показано, что важен баланс между размером модели и объёмом данных; предложены compute-optimal scaling laws

- **Training language models to follow instructions with human feedback (InstructGPT)**: [Long Ouyang et al., 2022](https://arxiv.org/abs/2203.02155), примерно 24,000 цитирований &ndash;формализация RLHF-пайплайна: SFT $\to$ reward model $\to$ PPO для выравнивания модели с человеческими предпочтениями  

- **LLaMA: Open and Efficient Foundation Language Models**: [Hugo Touvron et al., 2023](https://arxiv.org/abs/2302.13971), примерно 25,000 цитирований &ndash; представлена линейка LLaMA: эффективные фундаментальные модели

- **Direct Preference Optimization (DPO)**: [Rafael Rafailov et al., 2023](https://arxiv.org/abs/2305.18290), примерно 8,500 цитирований &ndash; альтернатива RLHF без отдельной reward-модели и RL, сводящая обучение к прямой оптимизации предпочтений

- **Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient Descent as Meta-Optimizers**: [Damai Dai et al., 2022](https://arxiv.org/abs/2212.10559), примерно 330 цитирований &ndash; показывают, что механизм attention в трансформере имеет двойственную форму с градиентным спуском: модель порождает мета-градиенты на основе демонстрационных примеров и применяет их для построения ICL-модели

- **Transformers Learn In-Context by Gradient Descent**: [Johannes von Oswald, et al., 2022](https://arxiv.org/abs/2212.07677), примерно 230 цитирований &ndash; доказывают эквивалентность преобразований одного слоя linear self-attention и шага градиентного спуска на регрессионном лоссе; показывают, что трансформеры превосходят обычный GD за счёт обучения итеративной коррекции кривизны

## Аннотация
Цель данной лекции &ndash; разобрать полный цикл обучения современных LLM (Large Language Models): от предобучения на больших текстовых корпусах до дообучения под инструкции и выравнивания поведения модели под предпочтения человека.

В течение лекции мы узнаем следующее:

*  как формируется базовая языковая модель;
*  как обучить модель, чтобы она следовала нашим инструкциям;
*  почему правильный ответ не всегда хороший, и как научить модель их разделять;
*  как научить модель отвечать правильно без обучения;
*  как заставить модель думать перед ответом



[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/17-llm/17-llm.ipynb)
