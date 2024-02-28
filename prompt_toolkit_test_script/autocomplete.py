from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Liste des options
options = ['pomme', 'banane', 'orange', 'raisin', 'cerise']

# Créer un compléteur avec nos options
options_completer = WordCompleter(options)

# Demander à l'utilisateur de faire une sélection
selection = prompt('Choisissez un fruit: ', completer=options_completer)

print(f'Vous avez choisi: {selection}')
