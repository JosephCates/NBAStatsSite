<?php
function printTeamLink($list){
  foreach ($list as $team){
    $url = "../teamSeasons/teamSeasons.php?teamID=" . urlencode($team['teamID']);
    echo "<p><a href='$url'>" . $team['City'] .' ' .$team['Name'] . "</a></p>";
  }
}
include ("../header/header.php");
require "../login.php";
$teamListResult = $conn->query("SELECT teamID, Name, City FROM team;");
$teamList = array();
while($row = $teamListResult->fetch_assoc()){
   $teamList[] = $row;
}
printTeamLink($teamList);
include ("../footer/footer.php");
?>
