
function unhide() {
    var hid = document.getElementsByClassName("hidden");
    // Emulates jQuery $(element).is(':hidden');
    if(hid[0].offsetWidth > 0 && hid[0].offsetHeight > 0) {
        hid[0].style.visibility = "visible";
    }
}

function typewrite () {
  document.getElementById('typeabout').classList.add("typewriter-text");
}



$(function() {
  $('a[href*=#]').on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top}, 500, 'linear');
  });
});
