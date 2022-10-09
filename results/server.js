// server.js

const express = require('express');
var expressLayouts = require('express-ejs-layouts');
const app = express();

app.set('view engine', 'ejs');

app.use(expressLayouts);

const PORT = 8090;
const MongoClient = require('mongodb').MongoClient;
const DB_HOST = 'results_db'
const DB_PORT = 27017
const DB_NAME = 'grades_app'
const url = `mongodb://${DB_HOST}:${DB_PORT}/${DB_NAME}`;  
// const url = "mongodb://localhost:27017/mydb";
 

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    console.log("Connected");
    db.close();
  });

// Example database query - https://www.w3schools.com/nodejs/nodejs_mongodb_query.asp
// MongoClient.connect(url, function(err, db) {
//     if (err) throw err;
//     var dbo = db.db("mydb");
//     /*Return only the documents with the address "Park Lane 38":*/
//     var query = { address: "Park Lane 38" };
//     dbo.collection("customers").find(query).toArray(function(err, result) {
//         if (err) throw err;
//         console.log(result);
//         db.close();
//     });
// });

app.get('/', function(req, res) {
    var locals = {
        title: 'Page Title',
        description: 'Page Description',
        header: 'Page Header'
      };

    res.render("list", locals);
});

app.listen(PORT, function(){
    console.log('Your node js server is running on PORT:',PORT);
});