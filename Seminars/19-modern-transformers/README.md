# Занятие 19. Современные трансформеры

Занятие провел: Мелихов Дмитрий (@dmitrymelikhov)

Материалы составил: Мелихов Дмитрий (@dmitrymelikhov)

### Источники:

- [D2L book](https://d2l.ai) &ndash; учебник по DL, где можно найти базу по Attention и трансформерам и многим другим интересным темам.
- [IBM blog про MHA/MQA/GQA](https://www.ibm.com/think/topics/grouped-query-attention) &ndash; Объяснение реализаций attention.
- [Medium blog про Pre-Norm vs Post-Norm](https://medium.com/@ashutoshs81127/why-pre-norm-became-the-default-in-transformers-4229047e2620) &ndash; пояснение про порядок нормализаций
- [HF blog про MoE](https://huggingface.co/blog/moe) &ndash; блог HuggingFace про Mixture of Experts

## Аннотация
На этом занятии:
- KV-cache
- Sliding window attention
- Разбираем оптимизации механизма внимания: MQA, GQA
- MLA из DeepSeek. 
- Смотрим на Mixture of Experts — как модель учится не «думать всеми головами сразу» и почему это позволяет масштабироваться без пропорционального роста вычислений. 
- Позиционные кодирования: классический sinusoidal PE, ALiBi, относительное кодирование и RoPE — стандарт в современных LLM. 
- Нормализации (LayerNorm, RMSNorm, Pre/Post-Norm) 
- Активации (GELU, SwiGLU)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/19-modern-transformers/19-modern-transformers.ipynb)
