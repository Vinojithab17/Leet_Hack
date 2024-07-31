const {Client} = require('pg');

const DBClient  = new Client({
    host:process.env.DB_HOST,
    user :process.env.DB_USER,
    port :process.env.DB_PORT,
    database : process.env.DB_NAME,
});


DBClient.connect()
  .then(() => console.log('Connected to PostgreSQL'))
  .catch(err => console.error('Connection error', err.stack));

//   DBClient.query(

//     `SELECT * FROM person`, (err,res)=>{
//         if(!err){
//             console.log(res.rows);
//         }else{
//             console.log(err.message);
//         }
//         DBClient.end;
//     }
// )


module.exports = {DBClient};

