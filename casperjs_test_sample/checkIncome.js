var casper = require("casper").create();                       //新建一個頁面

function getOptionValues() {
    var datevalue = document.querySelectorAll('option');
    return Array.prototype.map.call(datevalue, function(e) {
        return e.getAttribute('value')
    });
}

casper.start('html.html', function(){
	this.test.assertExists("#color", "colorOptionList is here!");
});  //http://www.cnyes.com/twstock/finreport/2498.htm
// casper.thenClick('#color'); //#ctl00_ContentPlaceHolder1_DropDownList1

casper.wait(500, function() {  
	this.echo("I clicked DropDownList1");
	this.capture("screenshot.png");
});


casper.then(function() {
    datevalue = this.evaluate(getOptionValues);
    this.echo(datevalue);
});

// <select name="ctl00$ContentPlaceHolder1$DropDownList1" onchange="javascript:setTimeout('__doPostBack(\'ctl00$ContentPlaceHolder1$DropDownList1\',\'\')', 0)" id="ctl00_ContentPlaceHolder1_DropDownList1" style="font-size:Small;width:120px;">
// 	<option value="2012年1~12月">2012年1~12月</option>
// 	<option value="2012年1~9月">2012年1~9月</option>
// 	<option value="2012年1~6月">2012年1~6月</option>
// 	<option value="2012年1~3月">2012年1~3月</option>
// 	<option value="2011年1~12月">2011年1~12月</option>
// 	<option value="2011年1~9月">2011年1~9月</option>
// 	<option value="2011年1~6月">2011年1~6月</option>
// 	<option value="2011年1~3月">2011年1~3月</option>
// 	<option value="2010年1~12月">2010年1~12月</option>
// 	<option value="2010年1~9月">2010年1~9月</option>
// 	<option value="2010年1~6月">2010年1~6月</option>
// 	<option value="2010年1~3月">2010年1~3月</option>
// 	<option value="2009年1~12月">2009年1~12月</option>
// 	<option value="2009年1~9月">2009年1~9月</option>
// 	<option value="2009年1~6月">2009年1~6月</option>
// 	<option value="2009年1~3月">2009年1~3月</option>
// 	<option value="2008年1~12月">2008年1~12月</option>
// 	<option value="2008年1~9月">2008年1~9月</option>
// 	<option value="2008年1~6月">2008年1~6月</option>
// 	<option value="2008年1~3月">2008年1~3月</option>
// 	<option value="2007年1~12月">2007年1~12月</option>
// 	<option value="2007年1~9月">2007年1~9月</option>
// 	<option value="2007年1~6月">2007年1~6月</option>
// 	<option value="2007年1~3月">2007年1~3月</option>
// 	<option value="2006年1~12月">2006年1~12月</option>
// 	<option value="2006年1~9月">2006年1~9月</option>
// 	<option value="2006年1~6月">2006年1~6月</option>
// 	<option value="2006年1~3月">2006年1~3月</option>
// 	<option value="2005年1~12月">2005年1~12月</option>
// 	<option value="2005年1~9月">2005年1~9月</option>
// 	<option value="2005年1~6月">2005年1~6月</option>
// 	<option value="2005年1~3月">2005年1~3月</option>
// 	<option value="2004年1~12月">2004年1~12月</option>
// 	<option value="2004年1~6月">2004年1~6月</option>
// 	<option value="2004年1~3月">2004年1~3月</option>
// 	<option value="2003年1~12月">2003年1~12月</option>
// 	<option value="2003年1~9月">2003年1~9月</option>
// 	<option value="2003年1~6月">2003年1~6月</option>
// 	<option value="2003年1~3月">2003年1~3月</option>
// 	<option value="2002年1~12月">2002年1~12月</option>
// 	<option value="2002年1~9月">2002年1~9月</option>
// 	<option value="2002年1~6月">2002年1~6月</option>
// 	<option value="2002年1~3月">2002年1~3月</option>
// 	<option value="2001年1~12月">2001年1~12月</option>
// 	<option value="2000年1~12月">2000年1~12月</option>
// 	<option value="1999年1~12月">1999年1~12月</option>
// 	<option selected="selected" value="1998年1~12月">1998年1~12月</option>

// </select>