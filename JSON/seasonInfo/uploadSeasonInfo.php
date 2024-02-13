<?php
include ("../../includes/login.php");
$json = file_get_contents('seasonInfo.json');
$json_data = json_decode($json ,true);

$stmt = $conn->prepare("
 INSERT INTO season(seasonID , champion , MVP, ROY, pointsLeader, reboundLeader, assistsLeader) VALUES(?,?,?,?,?,?,?)
");

$stmt->bind_param("sssssss", $seasonID , $champion, $MVP, $ROY, $pointsLeader, $reboundLeader, $assistsLeader);

foreach ($json_data as $row) {
  $seasonID  = $row["seasonID"];
  $champion = $row["champion"];
  $MVP = $row["MVP"];
  $ROY = $row["ROY"];
  $pointsLeader = $row["pointsLeader"];
  $reboundLeader = $row["reboundLeader"];
  $assistsLeader = $row["assistsLeader"];


 $stmt->execute();
}
 ?>
