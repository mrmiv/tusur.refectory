function toggle_menu() { 
    $('.categories').toggleClass('d-table');
 }

$('#button-categories').click(function () {
    toggle_menu()
});

var products = document.getElementsByClassName('add_product_form')
// console.log($('[data-category-product]'))
$('.category-item').click(function () {
    $(".active").removeClass("active"); 
    $(this).addClass('active');
    var attr = ($(this).attr('data-category'))

    toggle_menu()

    if (attr=='all'){

     // console.log('true')
    $(products).each(function(){
        $(this).fadeIn()
    })  

    } else {
        // console.log('false')
        $(products).each(function(){
            $(this).hide()
        });

    var category = $(this).attr('data-category')
    $('[data-category-product').each(function(){
        if ($(this).attr('data-category-product')==category){
        // console.log(this)
        $(this).fadeIn()
        }
    });

    };
});