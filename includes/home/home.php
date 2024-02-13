<?php
include ("../header/header.php");
?>
<!DOCTYPE html>
<html lang="en">
<link rel="stylesheet" href="home.css">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.13.2/themes/smoothness/jquery-ui.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.13.2/jquery-ui.min.js"></script>
    <script>
        $(function() {
            $("#txtpname").autocomplete({
                source: function(request, response) {
                    $.ajax({
                        url: "../autoComplete/autoComplete.php",
                        method: "GET",
                        dataType: "json",
                        data: { txtpname: request.term },
                        success: function(data) {
                            response(data);
                        },
                        error: function(jqXHR, textStatus, errorThrown) {
                            console.error("Autocomplete request failed: " + textStatus, errorThrown);
                        }
                    });
                },
                minLength: 1
            });
        });
    </script>
</head>
<body>
<div id="searchBar">
  <form action = "../playerStats/playerStats.php" method="GET" id="searchButton">
      <input type="text" name="txtpname" id="txtpname" size="30" class="form-control" placeholder="Search Player Name">
      <button type="submit">Enter</button>
  </form>
</div>


</body>
</html>

<?php
  include ("../footer/footer.php");
?>
