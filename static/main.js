$( document ).ready(function() {
    $( "#image-upload" ).change(function() {
            if (this.files && this.files[0]) {
                var reader = new FileReader();
    
                reader.onload = function (e) {
                    $('#uploaded')
                        .attr('src', e.target.result)
                        .width(450)
                        .height(600);
                };
    
                reader.readAsDataURL(this.files[0]);
            }
    });
});