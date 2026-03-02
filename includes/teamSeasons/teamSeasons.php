<?php
include ("../createTeamID.php");
function printTeamInfo($data) {
  $teamInfo = $data[0];
  echo "<h1>" . removeSpclChars($teamInfo['City']) . " " . removeSpclChars($teamInfo['Name']) ."</h1>";
  echo "<p> Founded: " . removeSpclChars($teamInfo['Founding']) . "</p>";
}
function printTeamSeasonTable($colNames, $data) {
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
          if($colName == "Team"){
            $ID = createTeamID($row["Team"],explode("-",$row["Year"])[0]);
            $url = "../teamSeasonInfo/teamSeasonInfo.php?teamID=".urlencode($ID)."&seasonID=". urlencode($row["Year"]);
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
include ("../login.php");

$teamIdentifier = $_GET["teamID"];

$teamInfoStmt = $conn->prepare("
SELECT Name, City, Founding 
FROM team 
Where teamID = ?
");

$teamInfoStmt->bind_param("s", $teamIdentifier);

$teamInfoStmt->execute();

$teamInfoResult = $teamInfoStmt->get_result();

$teamInfo = array();
while($row = $teamInfoResult->fetch_assoc()){
   $teamInfo[] = $row;
}
printTeamInfo($teamInfo);

$teamSeasonStmt = $conn->prepare("
SELECT seasonID as Year,TeamName as Team, teamAbbr, LG, Coach, GM ,Seed, Record, expectedRecord, OffRtg, DefRtg, NetRtg, PostSeason
FROM teamseasoninfo
where teamID = ? ORDER BY seasonID DESC 
");

$teamSeasonStmt->bind_param("s", $teamIdentifier);

$teamSeasonStmt->execute();

$teamSeasonResult = $teamSeasonStmt->get_result();

$teamSeasonData = array();
while($row = $teamSeasonResult->fetch_assoc()){
   $teamSeasonData[] = $row;
}
$colNames = array_keys(reset($teamSeasonData));
printTeamSeasonTable($colNames,$teamSeasonData);


include ("../footer/footer.php");
?>
