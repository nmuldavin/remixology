$(document).ready(function() {

    var slug = $("#recipe_container").attr("data-group");
    var rank = parseInt($("#recipe_container").attr("data-rank"));
    var current = [];
    var standard = [];

    function loadStandard() {
        var recipe = [];
        $('.recipe-entry').each(function() {
            var entry = []
            $(this).children('.entry-data').each(function(i, v) {
                entry.push($(this).html());
            });
            recipe.push(entry);
        });
        return recipe;
    };

    function compare() {
        var recipe = [];
        $('.recipe-entry').each(function() {
            var entry = [];
            var ingredient = $(this).children('.ingredient').html();
            if(!searchColumn(standard, 1, ingredient)) {
                $(this).addClass('diff');
                $(this).children('.entry-data').each(function(i, v) {
                    var value = $(this).html();
                    entry.push(value);
                });
            recipe.push(entry);
            };

        });
        return recipe;
    };

    function loadrecipe(groupslug, reciperank, init) {
        $("#recipe_container").html('').load(
            "/cocktails/"+ groupslug + "/" + String(reciperank), function() {
                if(init) {
                    standard = loadStandard();
                }
                else {
                    compare();
                }
            });
    };


    function searchColumn(table, index, value) {
        var found = false;
        //console.log("Looking for" + value)
        $.each(table, function(i, v) {
            //console.log(v[index]);
            if (v[index] == value) {
                // console.log("Got it");
                found = true;

            };
        });
        return found;
    };

    function searchList(list, value) {
        var found = false;
        list.children().each(function() {
            if ($(this).html() == value) {
                console.log($(this).html() + "does not match origininal:" + value)
                found = true;
            };
        });
        return found;
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


