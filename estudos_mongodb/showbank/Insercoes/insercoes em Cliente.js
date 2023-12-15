db.Cliente.insertOne({
    "Nome": "Allana Esther Lara Monteiro",
    "Cpf": "207.588.7003-96",
    "Data_nascimento": "15/03/1962",
    "Genero": "Feminino",
    "Profissao": "Servente de obras",
    "Endereco": "Rua Deputado João Moura Santos, número 155, Matadouro, Teresina, PI, 64004-340",
    "Status_civil": "Divorciado(a)"
});

db.Cliente.insert({
    "Nome": "Cauê Luan da Paz",
    "Cpf": "426.239.760-23",
    "Data_nascimento": "16/02/1967",
    "Genero": "Masculino", 
    "Profissao": "Vendedor em comércio atacadista", 
    "Endereco": "Rua Vinte e Quatro, número 121, Três Vendas, Pelotas, RS, 96071-380", 
    "Status_civil": "Casado(a)"
});


db.Cliente.insertMany([
    {"Nome": "Juliana Eloá Brito", 
     "Cpf": "208.862.381-70",
     "Data_nascimento": "26/06/1991", 
     "Genero": "Feminino", 
     "Profissao": "Trabalhador de serviços de limpeza", 
     "Endereco": "Rua Euza D'Aparecida Roriz dos Anjos, número 617, Setor Leste, Luziânia, GO, 72803-590", 
     "Status_civil": "Solteiro(a)"
    },
    
    {"Nome": "Luan Caio da Silva", 
    "Cpf": "520.233.763-94", 
    "Data_nascimento": "14/10/1949", 
    "Genero": "Masculino", 
    "Profissao": "Atendente de farmácia", 
    "Endereco": "Rua João Alberto, número 224, Santa Clara, São Luís, MA, 65058-623", 
    "Status_civil": "Viúvo(a)"
    }
]);

db.Cliente.find();