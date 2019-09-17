Trabalho da disciplina de Sistemas Inteligentes - Algoritmos de Busca no GRID

Executar o arquivo Labirinto.py no terminal utilizando python 3 (na minha máquina foi utilizada a versão 3.7.3). No terminal aparecerá o mapa lido do arquivo e as opções, digitar 1 para executar o algoritmo de busca A* e 2  para executar o best first, A e D são os comandos para girar o agente para o sentido horário ou antihorário e W para se mover na direção para a qual o agente está virado, Q para encerrar o programa.

Foram utilizadas as bibliotecas heapq e math do python 3

O programa lê como entrada o arquivo mapa.txt, em que as duas primeiras linhas são números inteiros representando a altura(a) e a largura(l) do mapa e as a linhas seguintes possuem l caracteres que indicam a posição inicial do agente, pontos sem obstáculos, asteriscos representando obstáculos e um X indicando a posição final que o agente deve chegar.

Os custos das transições de estado são: "1" para rotação 45 graus sentido horário ou anti-horário, "1" para progressão para "frente" na mesma linha, ou na mesma coluna, e "1.5" para progressão em diagonal.

Os algoritmos A* e best first retornam o caminho e o custo para chegar ao destino, contanto que exista um caminho entre o agente e o destino percorrendo o mapa.

Os algoritmos estão implementados em dois arquivos diferentes, a_star.py e best_first.py, e não precisam ser executados, pois são importados no arquivo Labirinto.py.