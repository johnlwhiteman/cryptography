"use strict";

const express = require('express');
const bodyParser = require('body-parser');
const app = express()
const port = 80

// Middleware
app.use(bodyParser.json());
app.use('/api',  require('./routes/crypto'));

app.get('/', (req, res) => res.send('Hello World!'))

app.get('/api', (req, res) => res.send('List of APIs go here!'))

app.listen(port, () => console.log(`Running @ http://localhost:${port}`))

