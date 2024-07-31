const {Client} = require('pg');
const client  = new Client({
    host:"localhost",
    user :"postgres",
    port :"5432",
    database : "test"
})

client.connect();

client.query(

    `SELECT * FROM person`, (err,res)=>{
        if(!err){
            console.log(res.rows);
        }else{
            console.log(err.message);
        }
        client.end;
    }
)

// CREATE TABLE person(Id INT, Name VARCHAR(50), Age INT, City VARCHAR(50));
// INSERT INTO person VALUES(1, 'John', 25, 'New York');
// INSERT INTO person VALUES(2, 'Johnny', 27, 'Clarksville');

