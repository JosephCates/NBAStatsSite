<?php
include ("../../includes/login.php");
$json = file_get_contents('PlayerInfo.json');
$json_data = json_decode($json ,true);

$stmt = $conn->prepare("
 INSERT INTO player(PlayerID , Name, firstName, lastName, middleName, Position, College, Height, Weight, BirthDate, Draft) VALUES(?,?,?,?,?,?,?,?,?,?,?)
");

$stmt->bind_param("sssssssssss", $PlayerID, $Name, $firstName, $lastName, $middleName, $Position, $College, $Height, $Weight, $BirthDate, $Draft);

foreach ($json_data as $row) {
  $PlayerID = $row["PlayerID"];
  $Name = $row["Name"];
  $firstName = $row["firstName"];
  $lastName = $row["lastName"];
  $middleName = $row["middleName"];
  $Position = $row["Position"];
  $College = $row["College"];
  $Height = $row["Height"];
  $Weight = $row["Weight"];
  $BirthDate = $row["BirthDate"];
  $Draft = $row["Draft"];


 $stmt->execute();
}
 ?>
