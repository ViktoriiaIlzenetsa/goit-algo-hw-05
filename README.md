# goit-algo-hw-05
Завдання 3
Результат виконання коду
|    text      |    pattern    |           kmp           |       boyer_moore       |       rabin_karp        |
|--------------|---------------|-------------------------|-------------------------|-------------------------|
|  article1    |     true      |  0.004346400499343872   |  0.0012118984013795853  |  0.008887700736522675   |
|              |     false     |  0.012706000357866287   |   0.00615210086107254   |  0.030829500406980515   |
|--------------|---------------|-------------------------|-------------------------|-------------------------|
|  article2    |     true      |  0.009083399549126625   |  0.0028641987591981888  |  0.020987600088119507   |
|              |     false     |  0.018295999616384506   |  0.008682001382112503   |   0.04675769992172718   |

Висновок. з результатів експерименту бачимо, що для обох статтей і не залежно від наявності в тексті патерну найщвидшим виявився алгоритм Боєра-Мура, а найгіршим - Рабіна-Карпа.
