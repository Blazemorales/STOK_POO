# STOK-Made_in_FGA
Projeto Livre - OO - Prof. Henrique Moura

Resumo sobre o app:
  1. Criar um app de estoque que gerencia as lojas, os produtos destas lojas a partir de um usuário
  2. Fazer um portal para que usuários externos, que não têm o login, não tenham acesso ao app
  3. As funções do app são:
     a. Armazenar dados de lojas e mostrar quais lojas estão salvas no sistema (Gerenciar Lojas)
     b. Armazenar produtos de lojas e mostrar quais produtos estão cadastrados no sistema (Gerenciar Produtos)
     c. Sair do app (Sair)
     d. Criar uma janela de login (usuário: admin, senha: admin123)
  4. Para a interface, foi usado o tkinter
  5. Para a serialização dos dados, foi utilizado o json

Caso de uso - Iniciar app:

- Motivação: Executar o app para que o usuário possa utilizá-lo
- Quem faz? Usuário (chamado de admin)
- Como fazer?
  
  1. Abra o arquivo main.py, dentro do diretório onde está o documento no bash.
     (Ex.: cd ~/Downloads/Projeto_Livre
      python3 main.py)
  2. Dado o passo anterior, o app estará sendo executado. Você entrará na aba de login. Na aba de login, clique no campo ao lado de "Usuário" (preencha com admin). A seguir, faça o mesmo no campo ao lado de "Senha" (preencha com admin123).
  3. A seguir, você será redirecionado para o menu principal do app
     
- E se o usuário não digitar nada ou colocar dados cadastrais não registrados no sistema?
  O arquivo irá retornar um erro ou warning

Caso de uso - Cadastrar Lojas ou Produtos
- Motivação: Dentro do app, após o login, o usuário irá, efetivamente, cadastrar suas lojas e/ou produtos em cada um dos botões. Estes serão armazenados em um banco de dados
- Pré requisitos? "Logar" no app e clicar no botão da respectiva operação que você deseja realizar
- Quem faz? Usuário
- Como fazer?
  1. Clique no botão da operação que deseja (podendo inclusive sair do app)
  2. Se entrar em "Gerenciar Lojas" e/ou "Gerenciar Produtos", você irá digitar, em cada campo, os dados da sua loja nos campos em branco. Após, você clicará em salvar. Isso irá retornar uma mensagem de sucesso. Em "Gerenciar Produtos", na aba de características, se o produto for alimentício, diga se ele possui algum alergênico. Caso contrário, digite a cor do produto.
  3. Se quiser checkar se seus dados estão no banco, basta você clicar em dados salvos. Estes aparecerão abaixo dos campos de preenchimento. Cada coluna representa um dado específico de sua loja e ou produto.
  4. Depois de cadastrar seu produtos, clique em sair da aba (x no canto superior direito e volte para o menu inicial)
  5. Se você quiser sair do app, apenas clique em sair.
- E se o usuário não digitar nada ou então digitar alguma palavra em "quantidades"?
  Haverá um warning ou erro
