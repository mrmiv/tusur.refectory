$(document).ready(function(){
    parallaxScroll();
    $(window).bind('scroll',function(){
        parallaxScroll();
    });
})

function parallaxScroll(){
    var scrolled = $(window).scrollTop();
    console.log(scrolled)
    // Нижнее поле
    console.log($('.block-info').offset().top-$(window).height())
    if (scrolled>=$('.block-info').offset().top-$(window).height()) {
        $('.block-text-info').addClass('pulse');
    }

    //Поле по середине
    if (scrolled>=$('.block-about').offset().top-$(window).height()) {
        $('.text-about').addClass('animated fadeIn');
    }


    //Вторая картинка
    if (scrolled>=$('.second-img').offset().top-$(window).height()) {
        $('.second-img').addClass('flipInX');
    }

    if (scrolled>=$('.animated-tomato').offset().top-$(window).height()) {
        $('.animated-tomato').addClass('fadeIn');
    }
    
};