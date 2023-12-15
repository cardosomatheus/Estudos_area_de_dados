//Cria um novo database
use showbank;

// criação da Coleção Cliente junto com suas validações.
db.createCollection("Cliente",{
    validator:{
        $jsonSchema:{
            bsonType:"object",
            required:["Nome","Cpf","Data_nascimento","Status_civil","Endereco"],
            properties:{
                    Nome:{
                    bsonType:"string",
                    description:"O campo é do tipo string, insira coretamento o nome"
                    },
                    Cpf:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira coretamento o cpf"
                    },
                    Data_nascimento:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira a data no formato dd/mm/yyyy"
                    },
                    Status_civil:{
                        bsonType:"string",
                        enum:["Solterio(a)", "Casado(a)", "Viúvo(a)", "Separado(a)", "Divorciado(a)", "Noivo(a)", "Outro"],
                        description:"Solterio(a), Casado(a), Viúvo(a), Separado(a), Divorciado(a), Noivo(a), Outro"
                    },
                    Endereco:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira coretamento o endereco"
                    },
                    
                }
            }
        }
    }
);



//visualizar as coleções
show tables;


// Alterações no schema de validação do cliente.
db.runCommand({collMod:"Cliente",
       validator:{
        $jsonSchema:{
            bsonType:"object",
            required:["Nome","Cpf","Data_nascimento","Status_civil","Endereco"],
            properties:{
                    Nome:{
                    bsonType:"string",
                    maxLength:150,
                    description:"O campo é do tipo string, insira coretamento o nome"
                    },
                    Cpf:{
                        bsonType:"string",
                        maxLength:14,
                        minLength:14,
                        description:"O campo é do tipo string, insira coretamento o cpf"
                    },
                    Data_nascimento:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira a data no formato dd/mm/yyyy"
                    },
                    Status_civil:{
                        bsonType:"string",
                        enum:["Solterio(a)", "Casado(a)", "Viúvo(a)", "Separado(a)", "Divorciado(a)", "Noivo(a)", "Outro"],
                        description:"Solterio(a), Casado(a), Viúvo(a), Separado(a), Divorciado(a), Noivo(a), Outro"
                    },
                    Endereco:{
                        bsonType:"string",
                        description:"O campo é do tipo string, insira coretamento o endereco"
                    },
                    
                }
            }
        }
    } 
});