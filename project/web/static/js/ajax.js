// $('#result_form').on('submit',function(e){
//     e.preventDefault();
//     var result = $(this).find('input').val();
//     $.ajax({
//         type: 'GET',
//         url: '/results/',
//         data: {'result': result},
//         dataType: 'json',
//         success: function(response){ $('#response_msg').text(response.msg); }
//       });
// }); 




    $('#ajax_form').on('submit',function(e){
        // console.log('helo')
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: $('#ajax_form').attr('action'),
            dataType: 'json',
            data: {
                name: $('.name').val(),
                email:$('.email').val()
                },
            success: function(data){
                console.log('it worked');
                $('ul.allusers').append('<li> user: '+data['name']+'<br> email: '+ data['email']+'</li>')
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
