
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [VOCABULAIRE] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [END] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [INTRODUCTION] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
La conception de tout projet depend souvent de librairie, et de module qui sont potentiellement reutillisable 
gpm(Git plug module) permet leur gestion dans les cas de figures suivant: 
x. Administration de la base de donne de code.
x. Le numero de version est directement recuperer du md5 generer par git de la base de code en cours.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[END]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [INSTALLATION] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Pour installer gpm faire la commande suivante.

Apres l'installation du module il faut initialiser ou importer, un environnement de travail.

Pour creer un nouvelle workspace !
>>> gpm newworkspace ./sethere

Autrement pour indiquer un workspace qui existe deja voici la commande.

>>> gpm remote newworkspace ./sethere 

Un ordinateur ne peut avoir en cour d'execution qu'un seul workspace pour savoir lequel est en cours d'execution faire 

>>> gpm remote newworkspace

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[END]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [CREATE NEW MODULE] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Pour creer une nouveaux module il faut taper la commande suivante.

>>> gpm newmodule
    @input.name -> Le nom que va prendre le module.   
    @input.gitadress -> L'adress que doit prendre ce module.
    @input.project -> Demande a qu'elle projet est-ce que je suis lier.

-------- [CODE-PROCESS]
x. Verifier s'il existe un module dans le dossier actuelle.
    x. *IF S'il n'existe pas de module alors ont n'ent creer une 
    x. *ELSE Ont indique a l'utilisateurs que le module n'existe pas 
-------- [END]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[END]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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