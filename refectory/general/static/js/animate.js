$(document).ready(function(){
    parallaxScroll();
    // console.log(
    //     $('.block-text-info').offset().top-$(window).height()
    // )
    $(window).bind('scroll',function(){
        parallaxScroll();
    });
})

function parallaxScroll(){
    var scrolled = $(window).scrollTop();
    // console.log(scrolled)
    // когда пролистали до блока класса block-info
    if (scrolled>=$('.block-info').offset().top-$(window).height()*0.9) {
        // добавляем классы (animated обязательно) и название анимации блокам block-text-info
        // ссылку на названия анимации и где их няглядно потыкать кидал вк
        $('.block-text-info').addClass('animated fadeIn');
        // по аналогии накидать анимаций
    }
    else{
        $('.block-text-info').css('opacity', '0');
    }
};