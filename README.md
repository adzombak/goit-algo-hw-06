# goit-algo-hw-06

------------------# Завдання 1------------------ \
***Графічне зображення графу показано на малюнку Figure_1.png***

**Кількість вершин графа**: 9

**Кількість ребер графа**: [('Kyiv', 'Lviv'), ('Kyiv', 'Odesa'), ('Kyiv', 'Dnipro'), ('Kyiv', 'Ivano-Frankivsk'), ('Kyiv', 'Chernihiv'), ('Lviv', 'Odesa'), ('Lviv', 'Ivano-Frankivsk'), ('Dnipro', 'Donetsk'), ('Donetsk', 'Zaporizhia'), ('Zaporizhia', 'Kharkiv'), ('Kharkiv', 'Chernihiv')]

**Ваги ребер графа**: {('Kyiv', 'Lviv'): 540, ('Kyiv', 'Odesa'): 475, ('Kyiv', 'Dnipro'): 477, ('Kyiv', 'Ivano-Frankivsk'): 603, ('Kyiv', 'Chernihiv'): 150, ('Lviv', 'Odesa'): 826, ('Lviv', 'Ivano-Frankivsk'): 134, ('Dnipro', 'Donetsk'): 217, ('Donetsk', 'Zaporizhia'): 247, ('Zaporizhia', \ 'Kharkiv'): 330, ('Kharkiv', 'Chernihiv'): 300}

**Ступені вершин графа**:
Kyiv: 5
Lviv: 3
Odesa: 2
Dnipro: 2
Donetsk: 2
Zaporizhia: 2
Kharkiv: 2
Chernihiv: 2
Ivano-Frankivsk: 2

------------------# Завдання 2------------------ \
DFS рекурсивно обходить граф, глибоко проникаючи в кожну гілку перед тим, як перейти до наступної гілки. Це означає, що алгоритм DFS побудує шлях в довгу гілку графа, перш ніж він повернеться назад і розгляне іншу гілку \
У цьому прикладі DFS починається в Ivano-Frankivsk, а потім переходить до наступного доступного міста, Kyiv. З Києва він продовжує обхід, переходячи від одного міста до іншого, поки не відвідає всі міста. \
DFS-обхід:
Ivano-Frankivsk Kyiv Lviv Odesa Dnipro Donetsk Zaporizhia Kharkiv Chernihiv

BFS обходить граф широко, від вузла до сусідніх вузлів, а потім до їхніх сусідів, і так далі. Це означає, що алгоритм BFS спочатку відвідає всі вузли, які знаходяться на одному рівні від початкового вузла, перш ніж перейти до наступного рівня. \
У цьому прикладі BFS починається в Ivano-Frankivsk і спочатку відвідує всі міста, які безпосередньо пов'язані з Ivano-Frankivsk (Kyiv, Lviv), потім переходить до наступного "рівня" міст. \
BFS-обхід:
Ivano-Frankivsk Kyiv Lviv Odesa Dnipro Chernihiv Donetsk Kharkiv Zaporizhia

------------------# Завдання 3------------------ \
Найкоротші відстані від вершини Ivano-Frankivsk:
{'Kyiv': 603, 'Lviv': 134, 'Odesa': 960, 'Dnipro': 1080, 'Donetsk': 1297, 'Zaporizhia': 1383, 'Kharkiv': 1053, 'Chernihiv': 753, 'Ivano-Frankivsk': 0}
