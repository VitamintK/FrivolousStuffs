var express = require('express');
var app = express();

//We aren't specifying a route here, so it will apply to all of them
app.use(function(req, res, next) {
    console.log('Time:', Date.now(), req.url);
    next();
});

//We'll make an Array to save the words in
var wordHistory = []; 
//This middleware will only apply to the one we care about
app.use('/say/:word', function(req, res, next) {
    wordHistory.push(req.params.word);
    console.log("Word History:", wordHistory);
    next();
});

//Put this above your server declaration!
app.use(function (req, res) {
  res.status(404).send('Nothing to see here!');
});

app.route('/').get(function (req, res) {
  res.send('Hello World!');
});

app.route('/say/:word').get(function (req,res) {
  user_word = req.params.word;
  res.send('You said: ' + user_word);
});

var server = app.listen(1337, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Example app listening at http://%s:%s', host, port);
});

