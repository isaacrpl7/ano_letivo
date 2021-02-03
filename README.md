# ano_letivo

Link do projeto funcionando: https://ano-letivo.herokuapp.com

## Resumo da aplicação
Aplicação web de registro de ano letivo em escolas. A aplicação possui 6 tabelas: Aluno, Disciplina, Escola, Habilidade, Professor e Turma. Cada uma possui as relações que foram indicadas na orientação do projeto, porém, decidi fazer pequenas modificações. Em Aluno adicionei os campos, Disciplina, Escola, Professor e Habilidade adicionei o campo 'nome', para que ficasse mais fácil a distinção de cada objeto. Em disciplinas, adicionei os campos 'habilidades_requeridas' e 'habilidades_ofertadas', que ligam em uma relação "ManyToMany" a tabela Disciplina e Habilidade. Além disso, os alunos possuem uma relação 'ManyToMany' com as habilidades também.

É possível listar, editar e criar novos conceitos. Além disso, é possível "detalhar" os Alunos, Disciplinas, Escolas e Turmas, para ver informações mais específicas de cada um desses. Ao detalhar uma escola, é possível ver as turmas que estão cadastradas naquela escola. Ao detalhar uma turma, é possível ver as disciplinas e os alunos que estão matriculados naquela turma, ao detalhar uma disciplina, pode-se ver as habilidades que a disciplina requer e oferta, junto com os professores daquela disciplina.

No detalhe dos alunos, decidi listar as habilidades que ele tem e colocar a opção de adicionar mais habilidades e de remover a que quiser.

### Detalhes de um aluno teste
![Imgur](https://i.imgur.com/PfNJOrr.png)

Com relação às turmas, decidi adicionar um botão no detalhamento da turma que permite a "conclusão" daquela turma. Isto é, ao apertar esse botão, todas as habilidades que a turma oferece vão para as habilidades dos alunos matriculados nessa turma, e a turma é deletada. Além disso, ao matricular um aluno em uma nova turma (o que pode ser feito na página de listagem dos alunos), o sistema verifica se os alunos possui as habilidades requeridas das disciplinas da turma. Se não possuir alguma, o aluno não pode entrar na turma.

### Detalhes de uma turma
![Imgur](https://i.imgur.com/1GbSBFI.png)

## Dificuldades durante o desenvolvimento
A primeira dúvida que surgiu foi se eu deveria fazer um sistema que atendesse a demana de uma única rede de ensino, ou seja, qualquer usuário cadastrado seria supostamente um membro da rede de ensino, e teria acesso a todas as escolas, alunos, etc, ou se eu deveria fazer um sistema de login de forma que cada usuário possuísse suas únicas escolas, alunos, etc, o que atenderia a várias redes de ensinos. A segunda opção foi a escolhida, uma vez que atenderia a um maior público de pessoas.

A segunda dificuldade que encontrei ao realizar o desenvolvimento, foi na hora da modelagem dos conceitos em relação às habilidades dos alunos. Pensei primeiro em fazer relação 'ManyToMany' entre alunos e habilidades, e até aí tudo bem. Mas na hora de listar as habilidades que uma disciplina precisa e oferta fiquei na dúvida se deveria criar algum modelo adicional para fazer a ligação, ou se já dava para ligar. Após alguns testes e análise, decidi ligar sem modelo adicional, até para deixar o código menor e menos robusto.

O terceiro grande desafio veio na hora de fazer o upload para o heroku, uma vez que deu muitos erros, mas mais tarde descobri que eram erros relacionados aos Assets e que foram resolvidos após mudar algumas configurações.

## Organização do código
Para melhorar o visual do código, decidi separar cada template em pastas, coloquei as views dentro de uma pasta também, e criei a pasta "controller" para colocar funções específicas daqueles conceitos. Além disso, tentei ao máximo evitar repetição de código, separando funções como 'comparar_habilidades', que é usada em quase 4 classes de views e deixaria o código muito mais robusto se não fosse encurtada, sempre tentando fazer o melhor algoritmo possível (nessa função foi um O(n²)). Também comentei o código nas partes de view para melhor compreensão.
