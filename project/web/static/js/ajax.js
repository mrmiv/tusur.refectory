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