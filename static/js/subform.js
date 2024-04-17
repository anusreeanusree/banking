//<script>
//$(document).ready(function(){
//    $('#id_district').change(function(){
//        var district = $(this).val();
//        $.ajax({
//            url: '/get_branches/',
//            type: 'GET',
//            data: {'district': district},
//            success: function(data){
//                $('#id_branch').empty();
//                $.each(data, function(key, value){
//                    $('#id_branch').append($('<option></option>').attr('value', value).text(key));
//                });
//            }
//        });
    });
});
</script>
