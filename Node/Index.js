// import express from 'express';
// import hello from './One';

const { hello } = require('./One');
// hello();
const express = require('express');
const app = express();
const port  = 4000;


app.listen(port, () => {

    hello();
    console.log(`Server started on port ${port}`);
});
app.get('/get', (req, res) => {
    res.send('Hello World');
});
