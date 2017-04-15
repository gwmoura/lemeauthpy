import requests

class LemeAuth(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        data = {'user':self.username, 'pass':self.password}
        r = requests.post('http://api.lememilitar.com/users/login/', data)
        json_data = r.json()
        if(json_data['user'] is None):
          return False
        else:
          self.user = json_data['user']
          self.email = json_data['email']
          self.nome = json_data['nome']
          self.codfornecedor = json_data['codfornecedor']
          self.setor = json_data['setor']
          return True

