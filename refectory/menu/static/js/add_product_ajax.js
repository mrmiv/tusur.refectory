    $('.add_product_form').on('submit',function(e){
        // console.log('helo')
        var product_id = $(this).find("button[type=submit]").attr('data-id');
        // console.log(product_id)
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: $('.add_product_form').attr('action'),
            dataType: 'json',
            data: {
                product_id
                },
            success: function(data){
                console.log('it worked');
                // $('ul.allusers').append('<li> user: '+data['name']+'<br> email: '+ data['email']+'</li>')
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