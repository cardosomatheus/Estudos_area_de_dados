db.createCollection("Produto",{
    validator:{
        $jsonSchema:{
            bsonType:"object",
            required:["ID","Descrição","Embalagem","Quantidade","Preço"],
            properties:{
                ID:{
                    bsonType:"int",
                    description:"Tipo inteiro"
                    },
                Descrição:{
                    bsonType:"string",
                    description:"Tipo string"
                },
                Embalagem:{
                    bsonType:"string",
                    description:"Tipo string"
                },
                Quantidade:{
                    bsonType:"int",
                    description:"Tipo inteiro"
                },
                Preço:{
                    bsonType:"double",
                    description:"Tipo double"
                }
            }
        }
    }
});




db.Produto.find();

