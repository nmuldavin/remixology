$(document).ready(function() {
    var slug = document.getElementById('recipe_container').getAttribute('data-group');
    var recipes = parseInt(document.getElementById('recipe_container').getAttribute('data-recipes'));
    var rank = parseInt(document.getElementById('recipe_container').getAttribute('data-reciperank'));
    var standard = saveStandardRecipe();

    setRecipeControls(rank, recipes);


    $("#next").click(function() {
        rank = rank + 1;
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            $("#previous").css('visibility','visible');
            setRecipeControls(rank, recipes);
        });
    });

    $("#previous").click(function() {
        rank = rank - 1;
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            $("#next").css('visibility','visible');
            setRecipeControls(rank, recipes);
        });
    });

    $("#edit_recipe").click(function() {
        standard = saveStandardRecipe();
        loadRecipeForm(slug, rank, function() {
            $("#controls_container").children().css('visibility', 'hidden');
            populateForm(standard);
            setFormControls();
            formControlListeners();
            formSubmitListener();
            $("#id_recipe_form-directions").elastic();
            $("#id_recipe_form-notes").elastic();
        });
    });

    $("#add_recipe").click(function() {
        rank = recipes + 1;
        loadRecipeForm(slug, rank, function() {
            $("#controls_container").children().css('visibility', 'hidden');
            populateForm(standard);
            setFormControls();
            formControlListeners();
            formSubmitListener();
            $("#id_recipe_form-directions").elastic();
            $("#id_recipe_form-notes").elastic();
        });
    });

    $("#cancel_form").click(function() {
        if (rank > recipes) {
            rank = 1;
        }
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            setRecipeControls(rank, recipes);
        });
    });

    $(".recipe_button").click(function() {
        rank = parseInt((this).innerHTML);
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            setRecipeControls(rank, recipes);
        });
    });




});