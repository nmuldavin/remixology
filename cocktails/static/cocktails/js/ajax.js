$(document).ready(function() {

    var slug = $("#recipe_container").attr("data-group");
    var rank = parseInt($("#recipe_container").attr("data-rank"));

    function loadrecipe(groupslug, reciperank) {
        $("#recipe_container").html('').load(
            "/cocktails/"+ groupslug + "/" + String(reciperank)
        );
    };

    loadrecipe(slug, rank);

    $("#next").click(function() {
        rank = rank + 1;
        loadrecipe(slug, rank);
    });

    $("#previous").click(function() {
        rank = rank - 1;
        loadrecipe(slug, rank);

    });
});


