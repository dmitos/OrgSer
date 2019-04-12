from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.formatted_text import HTML
from pathlib import Path


def bottom_toolbar(text):
    return HTML('es un barra ' + text)


dire = Path.cwd()
directorio = PathCompleter(only_directories=True, expanduser=False)

d = prompt(
    '> ', completer=directorio, bottom_toolbar=bottom_toolbar(str(dire)))

p = Path(d)
print(p.exists())
