const express = require('express');
const router = express.Router();

// Get a list of ? from database
router.get('/crypto', (req, res) => res.send({type:'GET'}));

// Add a new ? to the database
router.post('/crypto', function(req, res) {
    console.log(req.body);
    res.send({type:'POST'});
});

// Update an existing ? in the database
router.put('/crypto/:id', (req, res) => res.send({type:'PUT'}));

// Delete a ? from in the database
router.delete('/crypto/:id', (req, res) => res.send({type:'DELETE'}));

// Gotta export stuff
module.exports = router;