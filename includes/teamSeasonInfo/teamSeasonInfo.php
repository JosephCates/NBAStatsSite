<?php
function printTeamRosterTable($colNames, $data) {
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
          if($colName == "Name"){
            $nameLi = explode(" ",$row["Name"]);
            if(count($nameLi) == 2){
              $url = "../playerStats/playerStats.php?txtpname=" . urlencode($nameLi[0] . ' ' . $nameLi[1]);
              echo "<td><a href='$url'>" . $row[$colName] . "</a></td>";
            }else{
                $url = "../playerStats/playerStats.php?txtpname=" . urlencode($nameLi[0] . ' ' . $nameLi[1] .' ' . $nameLi[2]);
                echo "<td><a href='$url'>" . $row[$colName] . "</a></td>";
              }
          }else{
            echo "<td>".$row[$colName]."</td>";
          }
        }
        echo "</tr>";
      }
    echo "</table>";
}
?>
s
<?php
include ("../header/header.php");
include ("../printTable.php");
include ("../login.php");
$teamIdentifier = $_GET["teamID"];
$seasonIdentifier = $_GET["seasonID"];

$teamRosterResult = $conn->query("SELECT player.Name as Name,PS.Age, PS.Pos, PS.GP, PS.GS, PS.MP, PS.FG, PS.FGA, PS.`FG%`, PS.`3P`, PS.`3PA`, PS.`3P%`, PS.`2P`, PS.`2PA`, PS.`2P%`, PS.`eFG%`,PS.FT, PS.FTA, PS.`FT%`,PS.ORB, PS.DRB, PS.TRB, PS.AST, PS.STL,PS.BLK,PS.TOV,PS.PF,PS.PTS
FROM teamseasoninfo
INNER JOIN playerseasonstats PS ON (PS.teamID=teamseasoninfo.TeamAbbr and PS.seasonID=teamseasoninfo.seasonID)
INNER JOIN player ON PS.playerID=player.playerID
WHERE teamseasoninfo.TeamAbbr='$teamIdentifier' and teamseasoninfo.seasonID='$seasonIdentifier'
 ;");


$teamRoster = array();
while($row = $teamRosterResult->fetch_assoc()){
   $teamRoster[] = $row;
}
$colNames = array_keys(reset($teamRoster));
printTeamRosterTable($colNames,$teamRosterResult);
include ("../footer/footer.php");
?>
