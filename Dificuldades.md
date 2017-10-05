### Dificuldade #1
Como instalar o python 3.2 / Deixar o Python 3 como padrão?

### Dificuldade #2
IDLE para Python 3

Ao instalar o IDLE através do terminal (sudo apt-get install IDLE) e depois rodar o IDLE ele inicia com o Python 2.
Não estou conseguindo iniciar o IDLE com o Python 3, estou procurando na net como fazer:

" sudo apt-get install IDLE3 " - para conseguir instalar o IDLE para Python 3.x

### Dificuldade #3
Invalid syntax e um ")"
Fiquei quase 40 minutos procurando o erro e me perguntando porque o código não funcionava corretamente, até a quebra de linha com o enter estava estranha, até que percebi que era a falta de fechar o o bendito parêntese.

Código:

  letras.append(input("Letra: ") **)**
  
  i += 1
  
  O que me fez ficar perdido foi o fato do erro apontar para o "i" na linha do acumulador e não na linha do erro em si.

### Dificuldade #4
O exercicio 4 da lista IIIb - Desafios
"Dado um número inteiro positivo, determine a sua decomposição em fatores primos calculando também a multiplicidade de cada fator."
Fiquei muito tempo pensando como eu faria para achar o próximo primo para fazer a divisão, sem me dar conta que ao tentar dividir por um número não primo, já tendo dividido por um número menor que faz sua divisão ele não seria divisivel por aquele número.
Quase cai da cadeira quando vi um código lindo de 3 ou 4 linhas para resolver esse exercicio.
