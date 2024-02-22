#Django já tem uma função para gerar secret_key automaticamente
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key()) #vamos rodar a função utilizando o print, capturar a chave e colar em nossa variável de ambiente

#para gerar basta ir no terminal, entrar na pasta scripts e executar o comando:  python secret_key_generator.py