$(document).ready(function(){
    parallaxScroll();
    
    console.log($('.block-info').offset().top-$(window).height()*0.9)
    // console.log(
    //     $('.block-text-info').offset().top-$(window).height()
    // )
    $(window).bind('scroll',function(){
        parallaxScroll();
    });
})

function parallaxScroll(){
    var scrolled = $(window).scrollTop();
    console.log(scrolled)
    // Нижнее поле
    if (scrolled>=$('.block-info').offset().top-$(window).height()*0.9) {
        $('.block-text-info').addClass('animated flipInX');
    }
    else{
        // $('.block-text-info').css('opacity', '0');
    }
    //Поле по середине
    if (scrolled>=$('.block-about').offset().top-$(window).height()*0.9) {
        $('.text-about').addClass('animated fadeIn');
    }
    else{
        $('.text-about').css('opacity', '0');
    }
    //Вторая картинка
    if (scrolled>=$('.block-img.second-img').offset().top-$(window).height()*0.9) {
        $('.block-img.second-img').addClass('animated flipInX');
    }
    else{
        //$('.block-img.second-img').css('opacity', '0');
    }
    
};