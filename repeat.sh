#!/bin/bash

# Use este script para criar vários daods
# para o banco de dados sem utilizar uma amostra
# muito grande.

for i in {1..20}
do
  python3 main.py
done
