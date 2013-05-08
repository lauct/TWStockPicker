var casper = require("casper").create();
casper.start("http://www.google.fr/", function() {
    // this.download("http://www.google.fr/images/srpr/logo3w.png", "logo.png");
});

var currentTime = new Date();
var month = currentTime.getMonth() + 1;
var day = currentTime.getDate();
var year = currentTime.getFullYear();
var myfile = "data-"+year + "-" + month + "-" + day+".html";

var fs = require('fs');

var myData = "my data";
fs.write(myfile, myData, 'w');

casper.run();