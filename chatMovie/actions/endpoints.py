action_endpoint:
  url: "http://localhost:5055/webhook"

tracker_store:
  type: redis
  url: "localhost"
  port: 6379
  db: 0
  password: "123456"
  use_ssl: false

# Se quiser usar MongoDB em vez de Redis, substitua a configuração acima por esta:
# tracker_store:
#   type: mongod
#   url: "mongodb://localhost:27017"
#   db: "rasa"
#   username: "<usuário_para_autenticação>"
#   password: "<senha_para_autenticação>"
