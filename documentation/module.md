# module

## module

###

- Laboratory: Un laboratory est un git qui contient des modules sous forme de submodules git.
    L'objectif d'un laboratory est de pouvoir gerer les modules de facon centraliser.
    Les types d'action que l'on peut faire sur un laboratory sont les suivants:
    - Creer un module
    - Supprimer un module
    - Mettre a jour un module avec le code recuperer sur un Project.
    - Suivre le niveaux d'evolution des modules installer sur un ensemble de project.
 
- Module: Un module est un git qui contient un code source, qui peut etre injecter dans un ou plusieurs projets.
    L'objectif d'un module est de pouvoir etre reutiliser dans plusieurs projets.
    Les types d'action que l'on peut faire sur un module sont les suivants:

- Project: Un project est un git ainsi qu'un dossier qui contient des modules injecter sans suivie de version git.
    Un projet est un livrable client. 
    Les types d'action que l'on peut faire sur un project sont les suivants:
    - Creer un project
    - Supprimer un project
    - Mettre a jour un project avec le code module centraliser sur le laboritory.
    - Locker un module sur une version specifique, pour permettre une customisation du module, a destination du client.
      Sans affecter en aucun cas le module centraliser sur le laboritory.

### \[INTRODUCTION]

La conception de tout projet dépend souvent de librairies et de modules qui sont potentiellement réutilisables. `gpm` (Git plug module) permet leur gestion dans les cas de figures suivants:

* Administration de la base de données de code.
* Le numéro de version est directement récupéré du MD5 généré par Git de la base de code en cours.

#### \[INSTALLATION]

Pour installer `gpm`, exécutez la commande suivante:

```
pip install gpm
```

Apres l'installation du module il faut initialiser ou importer, un environnement de travail.

Pour creer un nouvelle workspace !

```
$ gpm newworkspace ./sethere
```

Autrement pour indiquer un workspace qui existe deja voici la commande.

```
$ gpm remote newworkspace ./sethere 
```

Un ordinateur ne peut avoir en cour d'execution qu'un seul workspace pour savoir lequel est en cours d'execution faire

``` 
    gpm remote workspace
```

#### \[PROCESS]

<<<<<<< HEAD
x. En premier lieux ont met en place un laboratory, qui est un git qui contiendra les modules sous le format submodules git.
x.  
=======
x. La premiere etape consiste en la creation d'un espace de travail au sein duquel l'ont pourra
>>>>>>> a6f3eec74411d396a60e9d66c29092474e097d38

#### \[CREATE\_NEW\_MODULE]

Pour creer une nouveaux module il faut taper la commande suivante.

```console
    gpm new module
```

Explication de la commande. @input.name -> Le nom que va prendre le module.\
@input.gitadress -> L'adress que doit prendre ce module. @input.project -> Demande a qu'elle projet est-ce que je suis lier.

\-------- \[CODE-PROCESS] x. Verifier s'il existe un module dans le dossier actuelle. x. \*IF S'il n'existe pas de module alors ont n'ent creer une x. \*ELSE Ont indique a l'utilisateurs que le module n'existe pas

```json
{ 
    'module__name': "chatroom", 
    'version__md5': "aoeuaoetunsaousaoeuhaoeu", 
    "version__module": "1.22.234 (main)",
}
```

#### \[MANAGER]

<<<<<<< HEAD

### \[CREATE\_NEW\_MODULE]

<<<<<<< HEAD
La gestion&#x20;
=======
## \[MANAGER]&#x20;

## &#x20;Qu'elle est le but de GPM ? Avant d'interagir avec le \[END]

\=======

### Qu'elle est le but de GPM ? Avant d'interagir avec le

> > > > > > > b204f20b584b49b0c58e04f118d78f6d6c3083ac

#### \[CREATE\_JSON\_FILE]

La gestion
>>>>>>> a6f3eec74411d396a60e9d66c29092474e097d38

```json
{
    'module__name': "chatroom",
    'version__md5': "aoeuaoetunsaousaoeuhaoeu",
    "version__module": "1.22.234 (main)",
}
```

<<<<<<< HEAD
### \[CREATE\_NEW\_MODULE]

Qu'elle est le but de GPM ? Avant d'interagir avec le&#x20;

=======
#### \[CREATE\_NEW\_MODULE]

Qu'elle est le but de GPM ? Avant d'interagir avec le
>>>>>>> a6f3eec74411d396a60e9d66c29092474e097d38
