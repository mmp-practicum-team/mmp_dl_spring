# Занятие 21. Как обучать LLM?

Занятие провел: Марьясов Максим (@oop_clon)

Материалы составил: Марьясов Максим (@oop_clon)

### Источники:

-  **Language Models are Few-Shot Learners**: [Tom B. Brown et al., 2020](https://arxiv.org/abs/2005.14165), примерно 70,000 цитирований &ndash; статья про GPT-3, где показано, что масштабирование моделей приводит к появлению in-context learning и позволяет решать задачи без fine-tuning  

- **Language Models are Unsupervised Multitask Learners (GPT-2)**: [Alec Radford et al., 2019](https://openai.com/research/better-language-models), примерно 24,000 цитирований &ndash; демонстрация того, что крупные языковые модели могут решать множество задач в zero-shot режиме без явного обучения на них  

- **Training language models to follow instructions with human feedback (InstructGPT)**: [Long Ouyang et al., 2022](https://arxiv.org/abs/2203.02155), примерно 24,000 цитирований &ndash; формализация RLHF-пайплайна: SFT → reward model → PPO для выравнивания модели с человеческими предпочтениями  

- **Deep Reinforcement Learning from Human Preferences**: [Paul Christiano et al., 2017](https://arxiv.org/abs/1706.03741), примерно 7,000 цитирований &ndash; базовый подход к обучению через человеческие предпочтения, лежащий в основе RLHF  

- **Direct Preference Optimization (DPO)**: [Rafael Rafailov et al., 2023](https://arxiv.org/abs/2305.18290), примерно 8,500 цитирований &ndash; альтернатива RLHF без отдельной reward-модели и RL, сводящая обучение к прямой оптимизации предпочтений


## Аннотация

Цель данного семинара &ndash; воспроизвести упрощённый, но концептуально полный пайплайн обучения современных языковых моделей.

Мы последовательно рассмотрим три этапа:
1. Базовая языковая модель (pre-training LM), обученная на задаче next-token prediction;
2. Supervised Fine-Tuning (SFT), в котором модель адаптируется к формату "инструкция → ответ";
3. Direct Preference Optimization (DPO), где модель обучается учитывать относительные предпочтения между ответами.

Главное, что наа всех этапах архитектура модели остаётся неизменной, изменяются только данные и функция потерь.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/21-llm-train/21-llm-train.ipynb)
