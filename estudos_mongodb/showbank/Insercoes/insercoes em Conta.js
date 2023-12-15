// Insert por registro e varios registro em Conta
db.Conta.insertOne({
    "Numero_Conta": "04938-1",
    "Agência": "5575",
    "Tipo": "Conta salário",
    "Cpf": "207.588.703-96",
    "Valor": 308
});

db.Conta.insert({
    "Numero_Conta": "0265177-7",
    "Agência": "0944",
    "Tipo": "Conta salário",
    "Cpf": "426.239.760-23",
    "Valor": "1411"
});


db.Conta.insertMany([
    {"Numero_Conta": "0189393-9", 
     "Agência": "0289", 
     "Tipo": "Conta salário",
     "Cpf": "208.862.381-70", 
     "Valor": 5242
    }, 
    {"Numero_Conta": "67314-4", 
     "Agência": "7147", 
     "Tipo": "Conta poupança", 
     "Cpf": "520.233.763-94"
    }
]);

db.Conta.find();