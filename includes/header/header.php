<!DOCTYPE html>
<html lang="en">
  <style>
  .navBar{
    height:50px;
    border: 1px solid gray;
    padding: 15px;
    /*background-color: blue;*/
  }
  .navBar a{
    text-size: 16px;
    text-align: center;
    display: inline-block;
    width:21%;
    color: black;
    text-decoration: none;
    padding: 16px 25px;
    border: 1px solid gray;
    /*background-color: blue;*/
  }
  </style>
  <body>
    <header>
      <div class="navBar">
        <?php if(htmlspecialchars($_SERVER["PHP_SELF"]) == "/NBAStats/includes/home/home.php") : ?>
            <a id = "button" href="home.php">Search</a>
        <?php else : ?>
            <a id = "button" href="../home/home.php">Search</a>
        <?php endif; ?>
        <?php if(htmlspecialchars($_SERVER["PHP_SELF"]) == "/NBAStats/includes/players/playerIndex.php") : ?>
            <a id = "button" href="playerIndex.php?letter=a">Players</a>
        <?php else : ?>
            <a id = "button" href="../playerIndex/playerIndex.php?letter=a">Players</a>
        <?php endif; ?>
        <?php if(htmlspecialchars($_SERVER["PHP_SELF"]) == "/NBAStats/teamIndex/teamIndex.php") : ?>
            <a id = "button" href="teamIndex.php">Teams</a>
        <?php else : ?>
            <a id = "button" href="../teamIndex/teamIndex.php">Teams</a>
        <?php endif; ?>
        <?php if(htmlspecialchars($_SERVER["PHP_SELF"]) == "/NBAStats/includes/seasons/seasons.php") : ?>
            <a id = "button" href="seasons.php">Seasons</a>
        <?php else : ?>
            <a id = "button" href="../seasons/seasons.php">Seasons</a>
        <?php endif; ?>
      </div>
    </header>
  </body>
</html>
