<?php
function printPlayerInfo($data) {
  $player = $data[0];
  echo "<h1>" . $player['Name'] . "</h1>";
  echo "<h2>" . $player['Position'] . "</h2>";
  echo "<p>" . $player['Height'] . " " . $player['Weight'] . "</p>";
  echo "<p>" . $player['Birthdate'] . "</p>";
  echo "<p>" . $player['College'] . " " . $player['Draft'] . "</p>";
}
function printPlayerStatsTable($colNames, $data) {
    echo "<table border='1'>";
    echo "<tr>";
    // Print the header
    foreach ($colNames as $colName) {
        echo "<th>$colName</th>";
    }
    echo "</tr>";

    // Print the rows
    foreach ($data as $row) {
        echo "<tr>";
        foreach ($colNames as $colName) {
          if($colName == "Team" and $row[$colName] != 'TOT'){
            $url = "../teamSeasonInfo/teamSeasonInfo.php?teamID=".urlencode($row["Team"])."&seasonID=". urlencode($row["Year"]);
            echo "<td><a href='$url'>" . $row[$colName] . "</a></td>";
          }else{
            echo "<td>".$row[$colName]."</td>";
          }
        }
        echo "</tr>";
      }
    echo "</table>";
}
?>

<?php
include ("../header/header.php");
require "../login.php";
$playerName = $_GET["txtpname"];
$playerInfoResult = $conn->query("SELECT player.Name,player.Position,player.College, player.Height, player.Weight, player.Birthdate, player.Draft
FROM playerseasonstats INNER JOIN player ON player.PlayerID=playerseasonstats.PlayerID
where player.PlayerID=\"$playerName\" or player.Name=\"$playerName\";");
$playerInfo = array();
while($row = $playerInfoResult->fetch_assoc()){
   $playerInfo[] = $row;
}
printPlayerInfo($playerInfo);

$playerStatsResult = $conn->query("SELECT seasonID as Year, teamID as Team, Age, Pos, GP, GS, MP, FG, FGA, `FG%`, `3P`, `3PA`, `3P%`, `2P`, `2PA`, `2P%`, `eFG%`, FT, FTA, `FT%`, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS
  FROM playerseasonstats INNER JOIN player ON player.PlayerID=playerseasonstats.PlayerID
  where player.PlayerID=\"$playerName\" or player.Name=\"$playerName\"
  ORDER by seasonID ASC;");
$playerStats = array();
while($row = $playerStatsResult->fetch_assoc()){
   $playerStats[] = $row;
}
$colNames = array_keys(reset($playerStats));
printPlayerStatsTable($colNames,$playerStats);
include ("../footer/footer.php");
?>
