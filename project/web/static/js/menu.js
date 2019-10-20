// $(document).ready(function(){
//     var form = $('.form-buy')
//     // console.log(form);
//     // Кнопка подверждения (добавления в корзину)
//     form.on('submit', function(e){
//         e.preventDefault()
//         // console.log('123');
//         // Аттрибут id текущей формы
//         var i = $(this).attr("id");
//         // console.log(i);
//         // Количество тарелок
//             // var number = $("[data-id="+i+"]").val();
//         // console.log(number);
//         // Получение названия объекта еды через его id
//         var submit = $("#btn_"+i);
//         var product_name = submit.data("name");
//         // console.log(product_name);
//         $(".shop-list").append('<li>'+product_name+'</li>')
//     })
// });