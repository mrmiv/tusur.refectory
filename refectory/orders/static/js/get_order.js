$('.get_order_link').on('click',function(e){
    // console.log('helo')
    var order_to_get = $(this).attr('data-order-to-get');

    console.log(order_to_get)
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: $(this).attr('href'),
        dataType: 'json',
        data: {
            order_to_get
            },
        success: function(data){
            // console.log(data)
            console.log('it worked');
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