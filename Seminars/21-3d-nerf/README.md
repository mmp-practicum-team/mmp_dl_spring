# Занятие 21. Неявные представления в 3Д

Занятие провёл: Алиев Мишан (mail: maliev@hse.ru)

Материалы основаны на лекции Струминского Кирилла Алексеевича


### Источники:


- [Мишан Алиев](https://www.hse.ru/org/persons/885876805/), [Кирилл Струминский](https://www.hse.ru/org/persons/165140955)

- [Лекция  Струминского Кирилла Алексеевича на курсе "3D CV" факультета ФКН](https://github.com/struminsky/hse_3dcv/blob/2024/week_6/lecture/lecture_6.pdf)

- **DeepSDF**: [Park J.J. et al., 2019](https://arxiv.org/abs/1901.05103), примерно 4200 цитирований

- **NeRF**: [Mildenhall B. et al., 2021](https://arxiv.org/abs/2003.08934), примерно 11800 цитирований

- **SIREN**: [Sitzmann V. et al., 2020](http://arxiv.org/abs/2006.09661), примерно 3000 цитирований

- **Plenoxels**: [Yu A. et al., 2021](https://arxiv.org/abs/2112.05131), примерно 200 цитирований.

- **Instant NGP**: [Müller T. et al., 2022](https://arxiv.org/abs/2201.05989), примерно 4300 цитирований.

- **pixelNeRF**: [Yu A. et al., 2021](https://arxiv.org/abs/2012.02190), примерно 1900 цитирований.

- **LERF**: [Kerr J. et al., 2023](https://arxiv.org/abs/2303.09553), примерно 400 цитирований.

- **NerfAcc**: [Li R. et al., 2022](https://arxiv.org/abs/2210.04847), примерно 100 цитирований.

- **Mip-NeRF**: [Barron J.T. et al., 2021](https://arxiv.org/abs/2103.13415), примерно 2200 цитирований.

- **Mip-NeRF 360**: [Barron J.T. et al., 2022](https://arxiv.org/abs/2111.12077), примерно 1900 цитирований.

- **NeRF++**: [Zhang K. et al., 2020](https://arxiv.org/abs/2010.07492), примерно 1100 цитирований.

- **Zip-NeRF**: [Barron J.T. et al., 2023](https://arxiv.org/abs/2304.06706), примерно 500 цитирований.

- **CamP**: [Park K. et al., 2023](https://arxiv.org/abs/2308.10902), примерно 60 цитирований.|


## Аннотация

Лекция посвящена неявным 3D-представлениям и тому, как они используются для моделирования сцен. Рассматриваются воксельные, нейросетевые и гибридные представления (hash grids, Instant-NGP) как компромисс между качеством, скоростью и памятью. Основной пример &ndash; Neural Radiance Fields (NeRF), где сцена задается полем плотности и излучения, а изображение получается интегрированием вдоль лучей. Обсуждаются методы ускорения и улучшения качества: разреживание, иерархическое сэмплирование, anti-aliasing (Mip-NeRF, Mip-NeRF-360, Zip-NeRF). Отдельный блок посвящен улучшению геометрии с помощью SDF, Eikonal loss и последующему извлечению мешей (Marching Cubes)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/21-3d-nerf/21-3d-nerf.ipynb)
