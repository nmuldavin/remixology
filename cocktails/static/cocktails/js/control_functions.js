

// loadRecipe function makes a request to the GetRecipe view,
// passing the group slug and recipe rank through the url. It then loads
// the rendered response in to the recipe container div.
function loadRecipe(user_directory, slug, rank, callback) {
    $("#recipe_container").load(
    '/' + user_directory + '/cocktails/'+ slug + '/get_recipe/' + String(rank) + '/', function() {
        console.log("Loaded recipe " + rank);
        if(callback) {
            callback();
        }
    }).hide().fadeIn('fast');
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

function deleteRecipe(user_directory, slug, rank, callback) {
    $.get('/' + user_directory + '/cocktails/'+ slug + '/delete_recipe/' + String(rank) + '/', function(data) {
        if (data == 'success') {
            if (callback) {
                callback();
            }
        }
    })
}

function deleteCocktail(user_directory, slug, callback) {
    $.get('/' + user_directory + '/cocktails/'+ slug + '/delete_cocktail/', function(data) {
        if (data == 'success') {
            if (callback) {
                callback();
            }
        }
    })
}
// loadRecipe function makes a request to the GetRecipe view,
// passing the group slug and recipe rank through the url. It then loads
// the rendered response in to the recipe container div.
function loadRecipeForm(user_directory, slug, rank, callback) {
    $("#recipe_container").load(
    '/' + user_directory + '/cocktails/'+ slug + '/add_or_edit_recipe/' + String(rank) + '/', function() {
        console.log("Loaded recipe form " + rank);
        if(callback) {
            callback();
        }
    }).hide().fadeIn('slow');
}

// saveStandardRecipe reads the page HTML to build a table of recipe
// entry objects from the standard recipe (the default with rank=1) so
// that other recipes can be compared later.
function saveStandardRecipe() {
    var label = document.getElementById('recipe_label').innerHTML;
    var directions = document.getElementById('recipe_directions').innerHTML;
    var notes = document.getElementById('recipe_notes').innerHTML;
    var entries = [];
    var rows = document.getElementsByClassName('recipe-entry');
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        var entry = {
            present: true,
            index:i,
            amount: row.getElementsByClassName('entry-data amount')[0].innerHTML,
            ingredient: row.getElementsByClassName('entry-data ingredient')[0].innerHTML
        };
        entries.push(entry);
    }

    return {'label':label, 'directions':directions, 'notes':notes, 'entries':entries}
}

// Outline: for each ingredient, search standard for that ingredient.
// Note if an ingredient in the standard is present in the current.
// If not found: highlight entire intredient entry row
// If found: compare amount to the amount of the matching ingredient in the standard,
// highlight if different. Finally, list at the bottom any ingredients in the standard which did not have
// matches in the current
function compareRecipeTo(data) {

    var rows = document.getElementsByClassName('recipe-entry');
    var directions = document.getElementById('recipe_directions');

    var standard = data.entries;

    if(directions.innerHTML != data.directions) {
        directions.className += " diff";
    }
    else {
        directions.className = directions.className.replace(/\bdiff\b/,'');
    }

    for (var k = 0; k < standard.length; k++) {
            standard[k].present = false;
    }

    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        var ingredient = row.getElementsByClassName('entry-data ingredient')[0].innerHTML;
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
            row.className += " diff";
        }
        else {
            row.className = row.className.replace(/\bdiff\b/,'');
            var amount = row.getElementsByClassName('entry-data amount')[0]
            if(amount.innerHTML != standard[index].amount) {
                amount.className += " diff";
            }
            else {
                amount.className = amount.className.replace(/\bdiff\b/,'');
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


// populateForm uses the saved recipe data to pre-populate form fields.
function populateForm(data) {
    $("#id_recipe_form-label").val(data.label);

    var numEntries = data.entries.length;
    $(".recipe-entry:last").remove()
    changeManagementFormNumbers(-1);
    var newentry = $(".recipe-entry:last").clone();
    $(".recipe-entry:last").remove()
    for (var i = 0; i < numEntries; i++) {
        newentry.appendTo("#recipe-body");
        if (i != 0) {
            incrementIndices(1);
        }
        var amounts = document.querySelectorAll(".recipe-entry .amount .char_field");
        var amount = amounts[amounts.length-1];
        amount.value = data.entries[i].amount.trim();

        var ingredients = document.querySelectorAll(".recipe-entry .ingredient .char_field");
        var ingredient = ingredients[ingredients.length-1];
        ingredient.value = data.entries[i].ingredient.trim();
        newentry = $(".recipe-entry:last").clone();
    }

    $("#id_recipe_form-directions").val(data.directions);
    $("#id_recipe_form-notes").val(data.notes);

}

function changeManagementFormNumbers(n) {
    var totalforms = document.getElementById('id_entry_formset-TOTAL_FORMS');
    var minforms = document.getElementById('id_entry_formset-MIN_NUM_FORMS');
    var number = parseInt(totalforms.value);
    number = number + n;
    totalforms.value = String(number);
    minforms.value = String(number);
}

function incrementIndices(n) {

    var amounts = document.querySelectorAll(".recipe-entry .amount .char_field");
    var amount = amounts[amounts.length-1];

    var ingredients = document.querySelectorAll(".recipe-entry .ingredient .char_field");
    var ingredient = ingredients[ingredients.length-1];

    // Getting index from one of the strings, doesn't matter which one.

    var index = parseInt(amount.id.match(/(\d+)/g));
    index = index + n;

    // replacing index in ids:
    var str = amount.id;
    amount.id = str.replace(/(\d+)/g, index);

    str = ingredient.id;
    ingredient.id = str.replace(/(\d+)/g, index);

    // replacing index in names:
    str = amount.name;
    amount.name = str.replace(/(\d+)/g, index);

    str = ingredient.name;
    ingredient.name = str.replace(/(\d+)/g, index);

    changeManagementFormNumbers(n);
}

function formControlListeners() {
    $("#add_entry").click(function () {
        var newentry = $(".recipe-entry:last").clone();
        newentry.appendTo("#recipe-body");
        incrementIndices(1);
    });


    $("#remove_entry").click(function() {
        $(".recipe-entry:last").remove()
        changeManagementFormNumbers(-1);
    })
}


function formSubmitListener() {
$('#form_submit').click(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $('#add_recipe_form').serialize(), // get the form data
                type: $('#add_recipe_form').attr('method'), // GET or POST
                url: $('#add_recipe_form').attr('action'), // the file to call
                success: function(response) { // on success..
                    if (response =='saved') {
                        var url = window.location.reload()
                    }
                    else {
                        $('#recipe_container').html(response); // update the DIV
                        formControlListeners();
                        formSubmitListener();
                    }
                },
            });
            return false;
        });
}

function setRecipeControls(rank, recipes) {
    $("#add_recipe").show();
    $("#edit_recipe").show();
    $("#delete_recipe").show();
    $("#delete_cocktail").show();
    $("#form_submit").hide();
    $("#cancel_form").hide();

    $("#controls_container").css('visibility', 'visible');
    $('.recipe_button').css('visibility', 'visible');

    if (rank >= recipes) {
        $("#next").css('visibility','hidden');
    }
    else {
        $("#next").css('visibility','visible');
    }
    if (rank <= 1) {
        $("#previous").css('visibility','hidden');
    }
    else {
        $("#previous").css('visibility','visible');
    }
}

function setFormControls() {
    $("#controls_container").css('visibility', 'hidden');
    $("#add_recipe").hide();
    $("#edit_recipe").hide();
    $("#delete_recipe").hide();
    $("#delete_cocktail").hide();
    $("#form_submit").show();
    $("#cancel_form").show();
}

