$(document).ready(function() {
    var slug = document.getElementById('recipe_container').getAttribute('data-group');
    var recipes = parseInt(document.getElementById('recipe_container').getAttribute('data-recipes'));
    var rank = parseInt(document.getElementById('recipe_container').getAttribute('data-reciperank'));
    var standard = saveStandardRecipe();

    hideButtons(rank, recipes);


    $("#next").click(function() {
        rank = rank + 1;
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            $("#previous").css('visibility','visible');
            hideButtons(rank, recipes);
        });
    });

    $("#previous").click(function() {
        rank = rank - 1;
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            $("#next").css('visibility','visible');
            hideButtons(rank, recipes);
        });
    });

    $("#edit_recipe").click(function() {
        standard = saveStandardRecipe();
        loadRecipeForm(slug, rank, function() {
            $("#controls_container").children().css('visibility', 'hidden');
            populateForm(standard);
            formControlListeners();
            formSubmitListener();
        });
    });

    $("#add_recipe").click(function() {
        rank = recipes + 1;
        loadRecipeForm(slug, rank, function() {
            $("#controls_container").children().css('visibility', 'hidden');
            populateForm(standard);
            formControlListeners();
            formSubmitListener();
        });
    });

    $(".recipe_button").click(function() {
        rank = parseInt((this).innerHTML);
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            hideButtons(rank, recipes);
        });
    });




});