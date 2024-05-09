#!/bin/bash

venv_dir="venv"

if [ ! -d "$venv_dir" ]; then
  echo "Não foi possível encontrar venv dir, criando."

  python -m venv venv
fi

source venv/bin/activate

pip install -r requirements.txt

if [ $# -eq 0 ]; then
  echo "Não foi passado nenhum argumento para iniciar, para usar a aplicação python src/main.py argumentos..."
  exit 0
fi

args="$@"

python src/main.py $args