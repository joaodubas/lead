$(function(){
   $('.redirect').click(function(){
        window.location=$(this).attr('rel');
   });
});
