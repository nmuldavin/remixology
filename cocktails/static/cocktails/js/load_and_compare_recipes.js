

// loadRecipe function makes an ajax request to the GetRecipe view,
// passing the group slug and recipe rank through the url. It then loads
// the recipe data in to the recipe.html template and reloads.
function loadRecipe(slug, rank, callback) {
    $("#recipe_container").html('').load(
    '/cocktails/'+ slug + '/get_recipe/' + String(rank), function() {
        console.log("Loaded recipe " + rank);
        if(callback) {
            callback();
        }
    });
}

function loadRecipeForm(slug, rank, callback) {
    $("#recipe_container").html('').load(
    '/cocktails/'+ slug + '/add_or_edit_recipe/' + String(rank), function() {
        console.log("Loaded recipe form " + rank);
        if(callback) {
            callback();
        }
    });
}

// saveStandardRecipe reads the page HTML to build a table of recipe
// entry objects from the standard recipe (the default with rank=1) so
// that other recipes can be compared later.
function saveStandardRecipe() {
    var standard = [];
    var rows = document.getElementsByClassName('recipe-entry')
        for (var i = 0; i < rows.length; i++) {
            var row = rows[i];
            var entry = {
                present: true,
                index:i,
                amount: row.getElementsByClassName('entry-data amount')[0].innerHTML,
                ingredient: row.getElementsByClassName('entry-data ingredient')[0].innerHTML
            };
            standard.push(entry);
        };
    return standard;
};

// Outline: for each ingredient, search standard for that ingredient.
// Note if an ingredient in the standard is present in the current.
// If not found: highlight entire intredient entry row
// If found: compare amount to the amount of the matching ingredient in the standard,
// highlight if different. Finally, list at the bottom any ingredients in the standard which did not have
// matches in the current
function compareRecipeTo(standard) {
    var rows = document.getElementsByClassName('recipe-entry');

    for (var k = 0; k < standard.length; k++) {
            standard[k].present = false;
    }

    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        var ingredient = row.getElementsByClassName('entry-data ingredient')[0].innerHTML
        var index;
        var found = false;
        for (var j = 0; j < standard.length; j++) {
            var standrow = standard[j];
            if(ingredient == standrow.ingredient) {
                standrow.present = true;
                found = true;
                index = standrow.index;
                break;
            }
        }

        if(!found) {
            row.className += " diff"
        }

        else {
            var amount = row.getElementsByClassName('entry-data amount')[0]
            if(amount.innerHTML != standard[index].amount) {
                amount.className += " diff"
            }
        }
        var anymissing = false;
        var missingstring = '';
        for (var l = 0; l < standard.length; l++) {
            if(standard[l].present == false) {
                missingstring += standard[l].amount + '' + standard[l].ingredient + ', '
                anymissing = true;
            }
        }

    }

    if(anymissing) {
            missingstring = 'Not Included: ' + missingstring;
            var tablecont = document.getElementById('recipe-table-container');
            var missingnote = document.createElement('p');
            missingnote.className = 'tiny';
            missingnote.innerHTML = missingstring;
            tablecont.appendChild(missingnote);

        }
}


$(document).ready(function() {
    var slug = document.getElementById('recipe_container').getAttribute('data-group');
    var recipes = parseInt(document.getElementById('recipe_container').getAttribute('data-recipes'));
    var rank = parseInt(document.getElementById('recipe_container').getAttribute('data-reciperank'));
    var standard = saveStandardRecipe();

    if(rank >= recipes) {
        $("#next").css('visibility','hidden');
    }
    if(rank <= 1) {
        $("#previous").css('visibility','hidden');
    }


    $("#next").click(function() {
        rank = rank + 1;
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            $("#previous").css('visibility','visible');
            if(rank >= recipes) {
                $("#next").css('visibility','hidden');
            }
        });
    });

    $("#previous").click(function() {
        rank = rank - 1;
        loadRecipe(slug, rank, function() {
            compareRecipeTo(standard);
            $("#next").css('visibility','visible');
            if(rank <= 1) {
                $("#previous").css('visibility','hidden');
            }
        });
    });

    $("#add_recipe").click(function() {
        rank = recipes + 1;
        loadRecipeForm(slug, rank, function() {
            $("#add_recipe").css('visibility', 'hidden');
            $("#previous").css('visibility','hidden');
            $("#next").css('visibility','hidden');
        })
    })

});