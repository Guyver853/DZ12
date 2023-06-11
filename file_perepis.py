from pathlib import Path

root_dir = Path('E:\Технология Прибыльных Сайтов (2020)')

repl = '[SuperSliv.biz]'

files = [x for x in root_dir.rglob('*') if repl in str(x)]
files.reverse()

for file in files:
    parent = file.parent
    name = file.name.replace(repl, '')
    file.replace(f'{parent}/{name}')
