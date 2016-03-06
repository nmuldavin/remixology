$(document).ready(function() {

    var slug = $("#recipe_container").attr("data-group");
    var rank = parseInt($("#recipe_container").attr("data-rank"));
    var current = [];
    var standard = [];

    function getRecipe() {
        var recipe = [];
        $('.recipe-entry').each(function() {
            var entry = []
            $(this).children('.entry-data').each(function() {
                entry.push($(this).html());
            });
            recipe.push(entry);
        });
        return recipe;
    };

    function loadrecipe(groupslug, reciperank, init) {
        $("#recipe_container").html('').load(
            "/cocktails/"+ groupslug + "/" + String(reciperank), function() {
                current = getRecipe();
                if(init) {
                    standard = current;
                    console.log(standard);
                }
                console.log(current);
            });
    };



    loadrecipe(slug, rank, true);

    $("#next").click(function() {
        rank = rank + 1;
        loadrecipe(slug, rank, false);
    });

    $("#previous").click(function() {
        rank = rank - 1;
        loadrecipe(slug, rank, false);

    });
});


