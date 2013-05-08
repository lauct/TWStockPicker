
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

casper.start('http://blog.lauct.org', function(){
    this.test.assertExists('#cat', 'the categories menu exists');
});

casper.then(
	this.clickLabel("Web開發", "a");
    this.wait(1000, function(){
    	this.capture('blog.png');	
    });    
);


casper.run();