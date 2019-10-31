$(document).ready(function(){
    parallaxScroll();
    $(window).bind('scroll',function(){
        parallaxScroll();
    });
})

function parallaxScroll(){
    // var scrolled = $(window).scrollTop();
    // console.log(scrolled)
    // Нижнее поле
    if (scrolled>=$('.block-info').offset().top-$(window).height()) {
        $('.block-text-info').addClass('flipInX');
    }
    else{

    }


    //Поле по середине
    if (scrolled>=$('.block-about').offset().top-$(window).height()*0.9) {
        $('.text-about').addClass('animated fadeIn');
    }
    else{
        $('.text-about').css('opacity', '0');
    }


    //Вторая картинка
    if (scrolled>=$('.second-img').offset().top-$(window).height()*0.9) {
        $('.second-img').addClass('animated flipInX');
    }
    else{
        $('.second-img').css('opacity', '0');
    }
    
};