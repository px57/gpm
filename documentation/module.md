# [VOCABULAIRE]

[END]

# [INTRODUCTION]

La conception de tout projet dépend souvent de librairies et de modules qui sont potentiellement réutilisables. `gpm` (Git plug module) permet leur gestion dans les cas de figures suivants:
- Administration de la base de données de code.
- Le numéro de version est directement récupéré du MD5 généré par Git de la base de code en cours.

[END]

# [INSTALLATION]

Pour installer `gpm`, exécutez la commande suivante:
    
    $ pip install gpm

[END]
# [INSTALLATION]

Pour installer gpm faire la commande suivante.

Apres l'installation du module il faut initialiser ou importer, un environnement de travail.

Pour creer un nouvelle workspace !
    $ gpm newworkspace ./sethere

Autrement pour indiquer un workspace qui existe deja voici la commande.

    $ gpm remote newworkspace ./sethere 

Un ordinateur ne peut avoir en cour d'execution qu'un seul workspace pour savoir lequel est en cours d'execution faire 

    $ gpm remote workspace

[END]
[CREATE_NEW_MODULE] 
Pour creer une nouveaux module il faut taper la commande suivante.

    $ gpm newmodule
        @input.name -> Le nom que va prendre le module.   
        @input.gitadress -> L'adress que doit prendre ce module.
        @input.project -> Demande a qu'elle projet est-ce que je suis lier.

-------- [CODE-PROCESS]
x. Verifier s'il existe un module dans le dossier actuelle.
    x. *IF S'il n'existe pas de module alors ont n'ent creer une 
    x. *ELSE Ont indique a l'utilisateurs que le module n'existe pas 
-------- [END]

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [CREATE NEW MODULE] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [END] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [CREATE JSON FILE] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
{
    'module__name': "chatroom",
    'version__md5': "aoeuaoetunsaousaoeuhaoeu",
    "version__module": "1.22.234 (main)",
}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[END]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [MANAGER] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Qu'elle est le but de GPM ? 
Avant d'interagir avec le 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[END]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>