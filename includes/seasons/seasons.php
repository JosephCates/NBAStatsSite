<?php
include ("../printTable.php");
include ("../header/header.php");
require "../login.php";

$seasonIndex = $conn->query("SELECT seasonID, Champion, MVP, ROY, pointsLeader, reboundLeader, assistsLeader
  FROM season ORDER BY seasonID DESC;");
$seasonIndexStore = array();
while($row = $seasonIndex->fetch_assoc()){
   $seasonIndexStore[] = $row;
}
$colNames = array_keys(reset($seasonIndexStore));
$caller = "seasons";
printTable($colNames,$seasonIndexStore,$caller);
include ("../footer/footer.php");
?>
