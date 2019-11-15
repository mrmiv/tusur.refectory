    // preloader
  $(window).on('load', function () {
    var $preloader = $('#page-preloader'),
        $spinner   = $preloader.find('#pizza');
    $spinner.fadeOut();
    $preloader.fadeOut();
    
    $('body', 'html').removeClass('overflow')

    // scroll animations

    parallaxScroll();
    $(window).bind('scroll',function(){
        parallaxScroll();
    });

});