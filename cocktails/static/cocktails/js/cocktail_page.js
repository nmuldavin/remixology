$(document).ready(function() {
    var slug = document.getElementById('recipe_container').getAttribute('data-group');
    var user_directory = document.getElementById('groupname').getAttribute('data-user_directory')
    var recipes = parseInt(document.getElementById('recipe_container').getAttribute('data-recipes'));
    var rank = parseInt(document.getElementById('recipe_container').getAttribute('data-reciperank'));
    var standard = saveStandardRecipe();

    function compareListener() {
        $("#set_comparison").click(function() {
            standard = saveStandardRecipe();
            compareRecipeTo(standard);
        });
    }

    setRecipeControls(rank, recipes);
    compareListener();

    $("#next").click(function() {
        rank = rank + 1;
        loadRecipe(user_directory, slug, rank, function() {
            compareRecipeTo(standard);
            setRecipeControls(rank, recipes);
            compareListener();
        });
    });

    $("#previous").click(function() {
        rank = rank - 1;
        loadRecipe(user_directory, slug, rank, function() {
            compareRecipeTo(standard);
            setRecipeControls(rank, recipes);
            compareListener();
        });
    });

    $(".recipe_button").click(function() {
        rank = parseInt((this).innerHTML);
        loadRecipe(user_directory, slug, rank, function() {
            compareRecipeTo(standard);
            setRecipeControls(rank, recipes);
            compareListener();
        });
    });

    $("#edit_recipe").click(function() {
        standard = saveStandardRecipe();
        loadRecipeForm(user_directory, slug, rank, function() {
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
        loadRecipeForm(user_directory, slug, rank, function() {
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
        loadRecipe(user_directory, slug, rank, function() {
            compareRecipeTo(standard);
            setRecipeControls(rank, recipes);
        });
    });

    $("#delete_recipe").click(function() {
        var agree = confirm("Are you sure you want to delete this recipe?")
        if (agree) {
            console.log('yes')
            deleteRecipe(user_directory, slug, rank)
        }
    })




});