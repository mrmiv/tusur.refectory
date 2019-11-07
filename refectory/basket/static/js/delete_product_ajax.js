$('.delete_product').on('click',function(e){
    // console.log('helo')
    var product_id = $(this).attr('data-product_id');

    // console.log(product_id)
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: 'delete',
        dataType: 'json',
        data: {
            product_id
            },
        success: function(data){
            console.log('it worked');
            // console.log($('li[data-product_li ='+ product_id+']'))
            $('li[data-product_li ='+product_id+']').remove()
            if (data.empty) {
                $('.order_in_basket').remove()
                $("#content").load();  
            }
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