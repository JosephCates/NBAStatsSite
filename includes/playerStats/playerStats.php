<?php
function printPlayerInfo($data) {
  $player = $data[0];
  echo "<h1>" . removeSpclChars($player['Name']) . "</h1>";
  echo "<h2>" . removeSpclChars($player['Position']) . "</h2>";
  echo "<p>"  . removeSpclChars($player['Height']) . " " . removeSpclChars($player['Weight']) . "</p>";
  echo "<p>"  . removeSpclChars($player['Birthdate']) . "</p>";
  echo "<p>"  . removeSpclChars($player['College']) . " " . removeSpclChars($player['Draft']) . "</p>";
}
function printPlayerStatsTable($colNames, $data) {
    echo "<table border='1'>";
    echo "<tr>";
    // Print the header
    foreach ($colNames as $colName) {
        echo "<th>" . removeSpclChars($colName) . "</th>";
    }
    echo "</tr>";

    // Print the rows
    foreach ($data as $row) {
        echo "<tr>";
        foreach ($colNames as $colName) {
          if($colName == "Team" && $row[$colName] != 'TOT'){
            $url = "../teamSeasonInfo/teamSeasonInfo.php?teamID=".urlencode($row["Team"])."&seasonID=". urlencode($row["Year"]);
            echo "<td><a href='".$url."'>" . removeSpclChars($row[$colName]) . "</a></td>";
          }else{
            echo "<td>".removeSpclChars($row[$colName])."</td>";
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

$playerInfoStmt = $conn->prepare("
    SELECT player.Name, player.Position, player.College, 
           player.Height, player.Weight, player.Birthdate, player.Draft
    FROM player 
    WHERE player.PlayerID = ? OR player.Name = ?
    LIMIT 1
");

$playerInfoStmt->bind_param("ss", $playerName, $playerName);

$playerInfoStmt->execute();

$playerInfoResult = $playerInfoStmt->get_result();

$playerInfo = array();
while($row = $playerInfoResult->fetch_assoc()){
   $playerInfo[] = $row;
}
printPlayerInfo($playerInfo);

$playerStatStmt = $conn->prepare("
    SELECT seasonID as Year, teamID as Team, Age, Pos, GP, GS, MP, 
           FG, FGA, `FG%`, `3P`, `3PA`, `3P%`, `2P`, `2PA`, `2P%`, 
           `eFG%`, FT, FTA, `FT%`, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS
    FROM playerseasonstats 
    INNER JOIN player ON player.PlayerID = playerseasonstats.PlayerID
    WHERE player.PlayerID = ? OR player.Name = ?
    ORDER BY seasonID ASC
");
$playerStatStmt->bind_param("ss", $playerName, $playerName);
$playerStatStmt->execute();
$playerStatResult = $playerStatStmt->get_result();
$playerStats = array();
while($row = $playerStatResult->fetch_assoc()){
   $playerStats[] = $row;
}
$colNames = array_keys(reset($playerStats));
printPlayerStatsTable($colNames,$playerStats);
include ("../footer/footer.php");
?>
