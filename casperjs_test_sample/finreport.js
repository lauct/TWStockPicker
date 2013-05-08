
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

var INFO = "INFO";

casper.start('http://www.cnyes.com/twstock/finreport/2498.htm', function(){
	// this.debugPage();
    // this.download(url, 'finreport_2498.html');
    this.wait(1000);
    this.test.assertExists('#aspnetForm', 'the aspnetForm exists');
    this.test.assertExists('#ctl00_ContentPlaceHolder1_DropDownList1', 'the dropdown menu exists');
    this.echo(this.getHTML('div[class="mbx bd3"]')); // => '宏達電簡明財報'

});

casper.then(function(){
	this.fill('form[name="aspnetForm"]', {
    	'ctl00$ContentPlaceHolder1$DropDownList1': '2009年1~12月'
    }, true);
});

casper.wait(1000, function(){
	this.capture("good.png");
});

casper.run(function() {
    console.log(this.getCurrentUrl(), INFO); // 2498
    this.exit();
});



