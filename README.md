# julia-trancou
Um bot no Twitter que twitta diariamente sobre meu status acadêmico. Tranquei ou não a faculdade?

A ideia veio de uma brincadeira entre amigos sobre meu descontentamento com o curso de Medicina e desejo de seguir na área de Computação e Desenvolvimento de Software. Decidi seguir adiante e executar o projeto.



![tweet](https://user-images.githubusercontent.com/85142222/140836287-61fa9d40-4166-4855-9d75-46e1e6782bba.png)

## O que aprendi com esse projeto?
- Sobre o uso de APIs, no caso a do Twitter. Tive que fazer uma requisição para uso em projetos de hobby e entender como o wrapper Tweepy funciona.

- Como lidar com credenciais privadas em projetos públicos.
  - Nos testes locais, achei interessante salvar em um arquivo separado e listá-lo sob o .gitignore.
  -  No servidor, usando variáveis de ambiente.

- Como fazer o deploy de uma aplicação para um servidor.
  - Utilizando a versão gratuita do Heroku.
  - Compreender qual o consumo de "dynos" do meu app, visto que a versão gratuita tem um limite de horas de uso.

- Manipular arquivos com Python.


## O que ainda falta?
- ~~Adicionar foto de perfil e capa ao perfil.~~

- ~~Adaptá-lo ao modelo Heroku Scheduler, que economizará no número de horas.~~

- ~~Script deverá ser executado uma vez por dia, postando um Tweet que informa se tranquei ou não, dia e mês.~~

- ~~O mês não deverá ser um número, mas sim por extenso (Novembro, em vez de mês 11).~~

- Devo ainda implementar toda a parte de pedir resposta do usuário, e para isso deve usar base de dados do heroku.


## O que devo estudar mais:
- Git e Github,version control.
- Deploying applications.
