# Занятие 19. Обработка звука

Занятие провела: Кравцова Ольга

Материалы составил: Находнов Максим (nakhodnov17@gmail.com), Алексеев Илья (@voorhs)


### Источники:

- [Torchaudio documentation](https://pytorch.org/audio/stable/index.html)
- [Librosa documentation](https://librosa.org/doc/latest/index.html)
- [AudioMNIST dataset repository](https://github.com/soerenab/AudioMNIST)
- [Whisper in Transformers](https://huggingface.co/docs/transformers/model_doc/whisper)


## Аннотация

В первой части последовательно разбираются физика звука, работа микрофона, дискретизация, квантизация, PCM, ряд и преобразование Фурье, DFT/FFT, частота Найквиста, алиасинг, STFT, оконные функции, спектрограмма, фаза, mel и MFCC. Во второй части те же идеи переводятся в практику: анализ waveform, простой VAD, построение спектральных признаков, мини-классификация на AudioMNIST, аугментации и знакомство с ASR на Whisper.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmp-practicum-team/mmp_dl_spring/blob/mipt_2026/Seminars/19-audio/19-audio.ipynb)
