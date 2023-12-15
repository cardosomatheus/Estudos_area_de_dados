db.createCollection("Contas",{
        validator:{
            $jsonSchema:{
                bsonType:"object",
                required:["Numero_conta","Agencia","Tipo","Cpf",],
                properties:{
                    Numero_conta:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira coretamento o numero da conta"
                    },
                    Agencia:{
                      bsonType:"string",
                      description:"O campo é do tipo string, insira coretamento a Agencia"
                    },
                    Tipo:{
                        bsonType:"string",
                        enum:["Conta corrente","Conta poupança", "Conta Salário"],
                        description: "Conta corrente,Conta poupança, Conta Salário"
                    },
                    Cpf:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira coretamento O Cpf"
                    }
                }
            }
        }
    }
);



show tables;

// Alterações no schema de validação da Conta.
db.runCommand({collMod:"Conta",
         validator:{
            $jsonSchema:{
                bsonType:"object",
                required:["Numero_conta","Agencia","Tipo","Cpf",],
                properties:{
                    Numero_conta:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira coretamento o numero da conta"
                    },
                    Agencia:{
                      bsonType:"string",
                      description:"O campo é do tipo string, insira coretamento a Agencia"
                    },
                    Tipo:{
                        bsonType:"string",
                        enum:["Conta corrente","Conta poupança", "Conta Salário"],
                        description: "Conta corrente,Conta poupança, Conta Salário"
                    },
                    Cpf:{
                        bsonType:"string",
                        maxLength:14,
                        minLength:14
                        description:"O campo é do tipo string, insira coretamento O Cpf"
                    },
                    Valor:{
                        bsonType:"double",
                        description:"Informe o valor corretamente."
                    }
                }
            }
        }
    }   
});
