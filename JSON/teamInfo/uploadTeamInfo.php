<?php
include ("../../includes/login.php");
$json = file_get_contents('teamInfo.json');
$json_data = json_decode($json ,true);

$stmt = $conn->prepare("
 INSERT INTO team(teamID, Name , City, Founding) VALUES(?,?,?,?)
");

$stmt->bind_param("ssss", $teamID, $Name $City, $Founding)

foreach ($json_data as $row) {
  $teamID = $row["teamID"];
  $Name = $row["Name"];
  $City, = $row["City"];
  $Founding = $row["Founding"]


 $stmt->execute();
}
?>
