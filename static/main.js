$( document ).ready(function() {
    var imageLink = $('#imageLink').val();
    $( "#submit-btn" ).click(function() {
        console.log($('#imageLink').val());
    });
});