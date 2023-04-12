$(function() {

  var w = $(window).width(),
    h = $(window).height();
  //$('section').width(w);
  $('section').height(h);
  $('menu .container').height(h - 60);
  $('body').prepend('<div id="overlay">');

  $('#menu').click(function() {$('html').addClass('active');});
  $('#close-menu').click(function() {$('html').removeClass('active');});
  $('#overlay').click(function() {$('html').removeClass('active');});
  $(window).resize(function() {
    var w = $(window).width(),
      h = $(window).height();
    //$('section').width(w);
    $('section').height(h);
    $('menu .container').height(h - 60);
  });

});

function readImg(img){
  if (img.files && img.files[0]){
    let reader = new FileReader();
    reader.onload = function(e){
      document.getElementById('imgfile').src = e.target.result;
    };
    reader.readAsDataURL(img.files[0]);
  } else{
    document.getElementById('imgfile').src="";
  }
}

function testLoding(){
  $('#loading').after('<div id="moveing"><img src="../static/img/lodingcat.gif"></div>')
}
