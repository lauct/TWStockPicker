
var casper = require('casper').create({
	verbose: true,
	logLevel: "info",
	viewportSize: {width: 1024, height: 768},
	onError: function(self, m) {   // Any "error" level message will be written
        console.log('FATAL:' + m); // on the console output and PhantomJS will
        self.exit();               // terminate
    },
	onError: function(self, m) {   // Any "error" level message will be written
        console.log('FATAL:' + m); // on the console output and PhantomJS will
        self.exit();               // terminate
    },	
});

casper.start('http://www.cnyes.com/twstock/finreport/2498.htm', function(){
    this.test.assertExists('#ctl00_ContentPlaceHolder1_tb1', 'the table exists');
});
casper.wait(1000, function(){
	this.capture("cs.png");	
});

casper.run(function() {
    console.log(this.getCurrentUrl()); // 2498
    this.exit();
});