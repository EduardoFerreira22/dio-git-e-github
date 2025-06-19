O que é verisionamento de Código?

Tipos de Sistemas de Controle de Versão
Dentre os sistemas de controle de versão (VCS), temos:
VCS Centralizado (CVCS)
Ex: CVS, Subversion

VCS Distribuído (DVCS)
Ex: Git, Mercurial


VCS Centralizado (CVCS)
Sistema onde o contro de versão dos arquivos são armazenados em um servidor local

VCS Distribuído (DVCS)
São sistemas como Git e Mercurial.
Clona o repositório completo, o que inclui o histórico de versões.

Cada clone é como um backup;
Possibilita um fluxo de trabalho flexível;
Possibilidade de trabalhar sem conexão à rede.

> ## Oque é Git?
Sistema de controle de versão distribuído.
Gratuito e Open Source (Código Aberto);
Ramicações (Branching) e fusões (merging) eficientes;
Leve e rápido.

> ## CONFIGURANDO O GIT
Configurando o git para usar o mesmo e-mail para todos os repositórios utilizando o --global
- [git config --global user.name "Nome do Github"](https://git-scm.com/docs/git-config)
- [git config --global user.email "email do github"](https://git-scm.com/docs/git-config)


### caso tenha dúvidas do nome e e-mail que está configurado no git basta usar o comando:
- git config user.name ou user.email

- git config init.defaulBranch
retorna o nome da branch que está configurada como padrão


### para alterar a branch padrão basta usar o comando:
- git config --global init.defaultBranch main


## CRIANDO E CLONANDO REPOSITÓRIOS
Existem duas formas de obter um repositório Git na sua máquina:
1-Transformando um diretório que não está sob conrtole de versão, num
repositório Git;

## Clonando um repositório Git existente.
| Comando | Descrição |
|----------|----------|
| git init | Inicia um novo arquivo git no repositório local |
| git remote add origin "repositório remoto" | Cria uma conexão com o repositório remoto |
| git clone "url do repositório" | Comando para clonar um repositório remoto |
| git clone "url do repositório" --branch feature-1 --single-branch | para escolher de qual branch quer baixar |

## SALVANDO ALTERAÇÕES NO REPOSITÓRIO LOCAL
- git status - para verificar qual o status da nossa arvore de commits
```
"Untracked files" - são arquivos não rastreados
```

## DESFAZENDO ALTERAÇÕES NO REPOSITÓRIO REMOTO

### É sempre importante verificar em qual branch estamos e se realmente queremos apagar as ultimas alterações realizadas
- git log - para verificar quais commits estão salvos

- git status - verifica o status da arvore de trabalho do git

dá pra remover o arquivo .git - "não é recomendado pois irá remover tudo até as configuraçõe e credenciais".


- git restore - descarta todas as alterações realizadas localmente

altera a mensagem de um commit: git commit --amend -m"Nova mensagem de commit"
caso não passe no comando -m"mensagem de commit" será aberto um terminal para alterar manualmente

- git reset desfazer último commit 

- git reflog: traz o historico de alterações no repositório local

git reset --hard <hash do commit>: retorna para um determinado commit e suas alterações.

git reset <nome do arquivo>: isso removerá um arquivo do fila

git restore --staged <nome do arquivo>: esse comando fará a mesma coisa do comando a cima,
porém é mais recomendado pelo proprio git

git branch -M main: Esse comando renomeia a branch padrão master para a main


git push -u origin main : Envia as alterações locais para o Github


## Como usar o editor remoto do Github no navegador?

Dentro do diretório no Github clique em "."(ponto) que será aberto uma tela como se fosse o vc code onde podemos 
fazer edções.

## Trabalhando com Branches
- git checkout -b <nome da branch>: comando para criar uma nova branch

- git checkout <nome da branch>: muda para a branch informada

- git branch -v: mostra os últimos commits das branchs listadas

- git merge <nome da branch>: faz a fundição das alterações das duas branch's

- git branch -D <nome da branch>: comando para excluir uma branch

### Conflitos de Merge
### git pull
✅ O que faz:

    É um atalho para git fetch + git merge (por padrão).

    Busca as atualizações remotas e já tenta integrá-las ao seu branch atual.

🛠️ Exemplo de uso:

git pull origin main

🔎 Resultado:

    Atualiza o branch remoto e imediatamente mescla ao seu branch local.

📌 Quando usar:

    Quando você quer atualizar seu branch com as últimas alterações remotas de forma automática.

### git fetch
✅ O que faz:

    Busca as atualizações do repositório remoto, mas não altera seu branch atual.

    Traz apenas os dados (commits, branches remotos, tags...) para o repositório local.

🛠️ Exemplo de uso:

git fetch origin

🔎 Resultado:

    Atualiza os ponteiros de branches remotos, como origin/main, mas não incorpora essas mudanças no seu branch local (main ainda será o que era antes).

📌 Quando usar:

    Quando você quer inspecionar mudanças no remoto antes de integrá-las.

    Útil para revisar o que mudou antes de decidir aplicar.


### 🧑‍💻 Boas práticas

    Use git fetch seguido de git log origin/main ou git diff origin/main para ver o que mudou antes de aplicar com git merge.

    Evite git pull se estiver em meio a mudanças locais não finalizadas — pode causar conflitos ou confusão.

    Sempre faça commit ou stash antes de um pull para evitar perda de progresso.