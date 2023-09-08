
## Primeiros passos

O ideal é criar um ambiente de desenvolvimento virtual para rodar o projeto. Geralmente, é recomendado o uso do `virtualenv`.

## Como rodar o projeto

1. Clone o repositório;
2. Crie um ambiente de desenvolvimento;
3. Ative o ambiente do passo anterior;
4. Instale as dependências presentes no arquivo requirements.txt;
5. Faça as migrações;
6. Inicie o servidor.

Usando o módulo `venv` para a criação do ambiente virtual, os passos serão esses

```bash
cd django-rest-api-exemplo
python3 -m venv venv
source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## OpenAPI

Para ver a documentação da API, abra o link http://localhost:8000/api/docs no seu navegador.


## Referências

- https://www.django-rest-framework.org/
- https://django-ninja.rest-framework.com/