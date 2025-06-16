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

- git status