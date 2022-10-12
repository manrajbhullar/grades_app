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


app.get('/', function(req, res) {

    MongoClient.connect(url, function(err, db) {
      if (err) throw err;
      var dbo = db.db("grades_app");
      var query = {}; // empty = everything
      
      // dbo.collection("course_stats").find(query).toArray(function(err, result) {
      dbo.collection("results").find(query).limit(1).sort({$natural:-1}).toArray(function(err, result) {
          if (err) throw err;
          console.log(result);
          db.close();
          
          dbo.collection("course_stats").find(query).toArray(function(err, courses) {
            if (err) throw err;
            console.log(courses);
            db.close();
            
            if (result.length == 0) {
              var locals = {
                body: 'There are no Classes in the Database'
              }
              res.render("layout", locals);
            } 
            else {
              var locals = {
                body: info=courses,
                update: result,
                body_length: info.length,
                update_length: result[0].courses.length
              };
              res.render("layout2", locals);
            }
            

          });

          
      });
  });  


});

app.listen(PORT, function(){
    console.log('Your node js server is running on PORT:',PORT);
});