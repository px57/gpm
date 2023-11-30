# module

## module

###

#### \[VOCABULAIRE]

#### \[INTRODUCTION]

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

```console
    gpm remote workspace
```

#### \[PROCESS]

x. La premiere etape consiste en la creation d'un espace de travail au sein duquel l'ont pourra

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

## \[MANAGER]&#x20;

## &#x20;Qu'elle est le but de GPM ? Avant d'interagir avec le <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\[END]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

\=======

### Qu'elle est le but de GPM ? Avant d'interagir avec le

> > > > > > > b204f20b584b49b0c58e04f118d78f6d6c3083ac

#### \[CREATE\_JSON\_FILE]

La gestion

```json
{
    'module__name': "chatroom",
    'version__md5': "aoeuaoetunsaousaoeuhaoeu",
    "version__module": "1.22.234 (main)",
}
```

#### \[CREATE\_NEW\_MODULE]

Qu'elle est le but de GPM ? Avant d'interagir avec le
