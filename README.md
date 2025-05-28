## StreamVibe
![image](https://github.com/user-attachments/assets/2dedbaf4-2ff6-47da-a44c-8db018956a46)


StreamVibe é uma plataforma de streaming web desenvolvida com Django, projetada para oferecer uma experiência de visualização de filmes e séries similar aos serviços populares. O projeto foca em uma interface de usuário intuitiva e um backend robusto para gerenciamento de conteúdo.

## 🌟 Recursos
Página Inicial Dinâmica: Apresenta uma vasta coleção de filmes e séries.
Navegação por Categoria: Organize e explore o conteúdo por filmes, séries e gêneros.
Funcionalidade de Busca: Encontre rapidamente seus títulos favoritos.
Minha Lista (Watchlist): Permite que os usuários salvem conteúdo para assistir mais tarde.
Páginas de Detalhes: Informações detalhadas sobre cada filme ou série.
Interface Amigável: Design limpo e responsivo para uma ótima experiência do usuário.
Pé de Página Abrangente: Links para suporte, planos de assinatura e informações de contato.
## 🚀 Tecnologias Utilizadas
Backend:
Python: Linguagem de programação principal.
Django: Framework web de alto nível para desenvolvimento rápido e seguro.
Banco de Dados: SQLite (para desenvolvimento), configurável para PostgreSQL/MySQL para produção.
Frontend:
HTML5: Estrutura da página.
CSS3: Estilização e layout.
JavaScript: Interatividade (se aplicável para funcionalidades como carrosséis ou filtros dinâmicos).
Outros:
Git: Controle de versão.
## 🛠️ Instalação e Configuração
Siga estas instruções para configurar e executar o projeto localmente:

Clone o repositório:

Bash

git clone https://github.com/HallanBoy/Py.Django.git # Assumindo este é o seu repositório
cd Py.Django # Ou o nome da pasta do seu projeto Django
Crie e ative um ambiente virtual:

Bash

python -m venv venv
## No Windows
venv\Scripts\activate
## No macOS/Linux
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt # Certifique-se de ter um arquivo requirements.txt
Se você não tiver um requirements.txt, você pode instalar o Django e outras bibliotecas manualmente:
Bash

pip install Django
# Outras bibliotecas que você pode ter usado, como Pillow, crispy-forms, etc.
Configure o banco de dados e execute as migrações:

Bash

python manage.py makemigrations
python manage.py migrate
Crie um superusuário (para acessar o painel de administração):

Bash

python manage.py createsuperuser
Siga as instruções no terminal para criar um nome de usuário e senha.

Execute o servidor de desenvolvimento:

Bash

python manage.py runserver
Acesse a aplicação:
Abra seu navegador e vá para http://127.0.0.1:8000/.

## 🖥️ Como Usar
Página Inicial: Ao acessar http://127.0.0.1:8000/, você verá a página inicial com a biblioteca de filmes e séries.
Navegação: Use a barra de navegação superior para ir para "Home", "Filmes", "Séries" ou "Minha lista".
Busca: Utilize a barra de busca no canto superior direito para pesquisar por títulos.
Administração: Acesse o painel de administração do Django em http://127.0.0.1:8000/admin/ e faça login com as credenciais do superusuário que você criou.
## 🤝 Contribuição
Contribuições são bem-vindas! Se você quiser melhorar o StreamVibe, por favor:

Faça um fork do repositório.
Crie uma nova branch (git checkout -b feature/sua-feature).
Faça suas alterações e commit (git commit -m 'Adiciona nova feature X').
Envie para a branch (git push origin feature/sua-feature).
Abra um Pull Request.
## 📄 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 📧 Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

[Meu GitHub](https://github.com/HallanBoy) <br>
[Meu e-mail](hallanlisboa1993@gmail.com) <br>
[Meu Linkedin](https://www.linkedin.com/in/hallann-eloi-22233a310/) <br>

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
