$(document).ready(function(){
    parallaxScroll();
    $(window).bind('scroll',function(){
        parallaxScroll();
    });
})

function parallaxScroll(){
    var scrolled = $(window).scrollTop();
    // console.log(scrolled)
    if (scrolled>300) {
        $('.name_degree').addClass('animated fadeIn');
        $('.cards-degree').addClass('animated fadeIn');
    }
    else{
        $('.name_degree').css('opacity', '0');
        $('.cards-degree').css('opacity', '0');
    }
};