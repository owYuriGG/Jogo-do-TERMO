# <h1 align="center"> **Trabalho Avaliativo G2 S2 2023** </h1>

<p align="center">
  <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png">
</p>



<p align="center">
  Sistemas de Informações - AMF
</p>
<p align="center">
  Segundo semestre - 2023
</p>

## **Descrição do Repositório**
<p align="justify"> Neste repositório, encontra-se meu trabalho avaliativo da segunda etapa do segundo semestre, onde fui desafiado a programar 100% em Python o jogo do Termo (https://term.ooo), jogado diretamente do console. </p


## <h2>**Requisitos do Sistema** </h2>
<p align="justify">  Ao ser dado o trabalho de desenvolver este jogo, diversos requisitos, técnicos e/ou funcionais foram passados, tais como: </p>
<ol>
<li>Criação de um arquivo contendo todas as possibilidades de palavras a serem utilizadas no
jogo.</li>
<li>Elaboração de um arquivo com registro das palavras já utilizadas, garantindo que uma
palavra não seja sorteada mais de uma vez.</li>
<li>Utilização de listas, exceções, modularização e manipulação de arquivos no
desenvolvimento do sistema.</li>
<li>Caso o usuário não acerte a palavra durante um jogo, ela poderá aparecer futuramente.</li>
<li>Implementação de funcionalidade que permita ao usuário redefinir as palavras já usadas no
jogo.</li>
<li>Garantia de que uma palavra não possa ser digitada duas vezes durante uma mesma partida.</li>
<li>As palavras devem possuir obrigatoriamente 5 letras para serem válidas.</li>
<li>As palavras sorteadas devem possuir 5 letras.</li>
<li>O sistema não deve aceitar palavras com números ou espaços em branco.</li>
<li>Desenvolvimento de uma interface amigável.</li>
</ol>

<h2> Arquitetura do Sistema </h2>
<p align="justify"> O programa é subdividido em 7 arquivos diferentes, sendo 1 o arquivo central, o main, outros 4 são módulos do programa, divididos cada um em um grupo de funções organizadas e mais 2 arquivos de texto para armazenação de informações.</p>
<h3>Módulos: </h3>
<dl>
  <dt>main</dt>
  <dd>Neste módulo, é realizada a integração geral do sistema, junto com os outros módulos e funções além da jogatina em si.</dd>
  <dt>game</dt>
    <dd>Neste módulo se concentra o core do jogo do Termo em si.</dd>
  <dt>menu_module</dt>
    <dd>Neste módulo está o menu principal do programa.</dd>
  <dt>asnwer_checker</dt>
    <dd>Neste módulo se encontra a função principal do jogo, onde é realizada a verificação da palavra dada pelo usuário em comparação com a palavra do jogo</dd>
  <dt>utilities</dt>
    <dd>Neste módulo se encontra as funções utilitárias, onde é realizada a verificação e tratamento de exceções, além de claro, o sorteio da palavra do dia.</dd>
</dl>
<h3>Arquivos: </h3>
<d1>
  <dt>words</dt>
  <dd>Este arquivo contém 100 palavras, de 5 letras, cujo quais são utilizadas para serem sorteadas no jogo</dd>
  <dt>used_words</dt>
  <dd>Este arquivo armazena as palavras já utilizadas, que foram acertadas, nos jogos.</dd>
</d1>


<h2 align="left"> Desenvolvido por:</h2>
Yuri Garcia  - aluno do curso Sistemas de Informações na Antonio Meneguetti Faculdade
<h3>Minhas redes sociais:</h3>

> Instagram: @yuri.garciia


> Discord: yuri.garciia
