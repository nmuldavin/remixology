$(document).ready(function() {

    var slug = $("#recipe_container").attr("data-group");
    var rank = parseInt($("#recipe_container").attr("data-rank"));

    $('#recipe_container').html('').load(
            "/cocktails/"+ slug + "/" + String(rank)
        );

    $("#next").click(function() {
        rank = rank + 1;
        $('#recipe_container').html('').load(
            "/cocktails/"+ slug + "/" + String(rank)
        );
    });

    $("#previous").click(function() {
        rank = rank - 1;
        $('#recipe_container').html('').load(
            "/cocktails/"+ slug + "/" + String(rank)
        );

    });
});


