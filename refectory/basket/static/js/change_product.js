$('a[data-q-minus]').on('click',function(e){
    // console.log($(this).attr('data-q-minus'));
    var product_id = $('li.product-in-basket[data-product-li = '+$(this).attr('data-q-minus')+']');
    // console.log(product_id)

    e.preventDefault(); 
    $.ajax({
        type: "POST",
        url: $(this).attr('href'),
        dataType: 'json',
        data: {
            product_id 
            },
        success: function(){
            // console.log(data)
            console.log('it worked');
            // console.log($('li[data-product_li ='+ product_id+']'))
            // если получить обратно data, то можно добавить условие, при котором удалится блок заказа
        },
        error: function(){
            console.log('error')
        }
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});