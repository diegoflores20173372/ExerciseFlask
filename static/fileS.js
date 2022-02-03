$(document).ready(function() {
     
    $("#limpiar").click(function() {
        $("#name").val(null);
        $("#date").val(null);
        $("#aforo").val(null);
        $("#dojoLocation").val(null);
        $("#caractDojo1").prop("checked", false);
        $("#caractDojo2").prop("checked", false);
        $("#caractDojo3").prop("checked", false);
        $("#caractDojo4").prop("checked", false);
        $("#caractDojo5").prop("checked", false);
        $("#flexRadioDefault1").val(null);
        $("#comentarioDojo").val(null);

        console.log("limpieza");
    });

    $("#atras").click(function() {
         window.location.href="/";
    });
});