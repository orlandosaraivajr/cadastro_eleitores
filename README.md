# Cadastro Eleitores

Sistema de cadastro de eleitores desenvolvido para fins didáticos.

### Como desenvolver ?

1. Clone o repositório
2. Crie um virtualenv 
3. Ative a virtualenv
4. Instale as dependências
5. Configure a instância com o .env 
6. Execute os testes

```console
git clone https://github.com/orlandosaraivajr/cadastro_eleitores.git
cd cadastro_eleitores/
virtualenv venv -p python3
source venv/bin/activate
cd projeto/
pip install -r requirements.txt 
cp contrib/env-sample .env
python manage.py migrate
python manage.py test
python manage.py runserver
```
