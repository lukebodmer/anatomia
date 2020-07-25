$(document).ready(function(){

    $('form').on('submit',function (e) {
         $.ajax({
          type: 'post',
          url: '/buscar',
          data: $(this).serialize(),
           success: function (q) {
           }
          });
         e.preventDefault();
         });
    
    }
    // $('form').on('submit', function(event) {
    //     $.ajax({
    //         data: {
    //             userID: $('#userID').val(),
    //             name: $('#name').val()
    //         },
    //         type: 'POST',
    //         url: '/table_data'
    //     })
    // event.preventDefault();
    // });
}); 