$('a.category-link').click(function (e) { 
    e.preventDefault();
    category = $(this).attr('data-category')
    console.log(category)
    $.ajax({
        type: "GET",
        cache: false, 
        url: $(this).attr('href'),
        dataType: "json",
        data: {
            category
        },
        success: function (response) {
            console.log(response)
        }
    });    
});