$('.add_product_form').on('submit',function(e){
    // console.log('helo')

    function loading(data) {
        // пропадаед надпись
        // console.log(typeof(span.attr('data-in-basket')))
        $('.button-basket').fadeIn()
        span.fadeOut(function () {
            // если есть ошибка, возвращает ошибку в текст,
            if (data.error){
                setTimeout(function() {
                    span.html(String(data.error))
                }, 600);
            // если нет ошибки, возвращает успех
            } else {
                    if(button.attr("data-in-basket")=="0"){
                        // console.log('true worked - добавлено в корзину')
                        setTimeout(function() {
                            span.html("Добавлено в корзину!");
                            button.attr("data-in-basket","1")
                        }, 600);

                    }else{
                        // console.log('false worked')
                        setTimeout(function() {
                            span.html("Добавить в корзину")
                            button.attr("data-in-basket","0")
                        }, 600);
                        
                    };
                };
            })
        // появляется кольцо загрузки
        button.find("span.spinner-border").delay(300).fadeIn()
    }

    var product_id = $(this).find("button[type=submit]").attr('data-id');
    // var in_basket = $(this).find("button[type=submit] span").attr('data-in-basket') 
    // console.log(in_basket)
    var button = $(this).find("button[type=submit]")
    var span = button.find("span.button-val")
    // console.log(button.html())
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: $('.add_product_form').attr('action'),
        dataType: 'json',
        data: {
            product_id,
            // in_basket
            },
        success: function(data){
            console.log(data.error)
            // появляется загрузка и обновляется текст
            loading(data)
            console.log('ok')

            // пропадает загрузка 
            button.find("span.spinner-border").fadeOut(function () {
                // если есть ошибка, меняет цвет кнопки и возвращает через 2с в исходное состояние
                if (data.error){
                    button.css('background', "#811212")
                    setTimeout(function() {
                        if(button.attr("data-in-basket")!=="0"){
                            // console.log('true worked - добавлено в корзину')
                            span.html("Добавлено в корзину!");
                            button.css('background',"#fa983a")
                        }else{
                            // console.log('false worked')
                            span.html("Добавить в корзину")
                            button.css('background',"#1DA643")
                        };
                    },1500)
                }
                // если ошибки нет, выводит текст
                else{
                    span.fadeIn()
                }
                span.fadeIn()
            });
        },

        error: function(data){
            loading(data)
            button.find("span.spinner-border").delay(7000).fadeOut(function () {
                button.css('background', "#811212")
                
                span.html("Что-то пошло не так :(")
                span.fadeIn()
            });

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