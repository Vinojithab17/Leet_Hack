

const { hello } = require('./One');
require('dotenv').config();
// hello();
const express = require('express');
const { DBClient } = require('./Database')
const app = express();
const port  = process.env.SERVER_PORT;


// Middleware
app.use(express.json()); 

app.listen(port, () => {

    hello();
    console.log(`Server started on port ${port}`);
});
app.get('/get', (req, res) => {
    res.send({"message":"Hello World"});
});


app.post('/create', async(req, res) => {

    try {
        console.log(req.body);
        const{todo_name, todo_description} = req.body;
        const response = await DBClient.query(
            `INSERT INTO todo(todo_name,todo_description) VALUES('${todo_name}', '${todo_description}') RETURNING *`,
        );
        res.json(response.rows[0]);

    } catch (error) {
        console.log(error.message);
    }
});

app.get('/getAllTodo', async(req, res) => {

    try {
    
        console.log("get all todo");
        const response = await DBClient.query(
            `SELECT * FROM todo`
        );
        res.json(response.rows);

    } catch (error) {
        console.log(error.message);
    }
});



app.get('/getTodo/:id', async(req, res) => {
    try {
        const {id} = req.params;
        const response = await DBClient.query(
            `SELECT * FROM todo WHERE todo_id = ${id}`
        );
        res.json(response.rows[0]);
    } catch (error) {
        console.log(error.message);
    }
});
function logger (req, res, next) {
    console.log("this is a middleware");
    next()
}