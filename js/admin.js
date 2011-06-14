$(function(){
	
	// Fix forms
	$('#mainContainer label').wrap('<div class="labelForm" />');
	$('#mainContainer input:text').wrap('<div class="labelInputText" />');
	$('#mainContainer select').wrap('<div class="labelSelect" />');
	$('#mainContainer textarea').wrap('<div class="labelTextare" />');
	
	// Active the #main
	$('#container').css('display', 'block');
});