const {Client} = require('pg');

const DBClient  = new Client({
    host:"localhost",
    user :"postgres",
    port :"5432",
    database : "test"
});

DBClient.connect();

DBClient.query(

    `SELECT * FROM person`, (err,res)=>{
        if(!err){
            console.log(res.rows);
        }else{
            console.log(err.message);
        }
        DBClient.end;
    }
)



// CREATE TABLE person(Id INT, Name VARCHAR(50), Age INT, City VARCHAR(50));
// INSERT INTO person VALUES(1, 'John', 25, 'New York');
// INSERT INTO person VALUES(2, 'Johnny', 27, 'Clarksville');

