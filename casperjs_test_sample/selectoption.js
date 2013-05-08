
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

casper.start('selectoption.html', function(){
    this.test.assertExists('#memberActionOption1', 'the memberActionOption1 menu exists');
});

casper.then(function(){
	this.fill('form[name="formName"]', {
    	'memberActionOption1': 'Option1'
    }, true);
});

casper.wait(1000, function(){
	this.capture("selectoption.png");
});

casper.run(function() {
    console.log(this.getCurrentUrl()); // 2498
    this.exit();
});



