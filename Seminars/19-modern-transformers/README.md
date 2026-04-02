# Занятие 19. Современные трансформеры

Занятие провел: Мелихов Дмитрий (@dmitrymelikhov)

Материалы составил: Мелихов Дмитрий (@dmitrymelikhov)

## Аннотация
На этом занятии:
- Разбираем оптимизации механизма внимания: MQA, GQA
- MLA из DeepSeek. 
- Смотрим на Mixture of Experts — как модель учится не «думать всеми головами сразу» и почему это позволяет масштабироваться без пропорционального роста вычислений. 
- Позиционные кодирования: классический sinusoidal PE, ALiBi, относительное кодирование и RoPE — стандарт в современных LLM. 
- Нормализации (LayerNorm, RMSNorm, Pre/Post-Norm) 
- Активации (GELU, SwiGLU)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/main/Seminars/19-modern-transformers/19-modern-transformers.ipynb)
