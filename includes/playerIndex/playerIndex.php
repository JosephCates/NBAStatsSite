<?php
include ("../header/header.php");
function printPlayerLink($list){
  $suffixArray = array("II", "III", "IV", "Jr.", "Sr.");
  foreach ($list as $name){
    if($name['middleName'] == ""){
      $url = "../playerStats/playerStats.php?txtpname=" . urlencode($name['firstName'] . ' ' . $name['lastName']);
      echo "<p><a href='" . $url . "'>" . h($name['Name']) . "</a></p>";
    } else if(in_array($name['middleName'], $suffixArray) && $name['middleName'] !== ""){
      $url = "../playerStats/playerStats.php?txtpname=" . urlencode($name['firstName'] . ' ' . $name['lastName'] . ' ' . $name['middleName']);
      echo "<p><a href='" . $url . "'>" . h($name['Name']) . "</a></p>";
    } else {
      $url = "../playerStats/playerStats.php?txtpname=" . urlencode($name['firstName'] . ' ' . $name['middleName'] . ' ' . $name['lastName']);
      echo "<p><a href='" . $url . "'>" . h($name['Name']) . "</a></p>";
    }
  }
}
function createPlayerLinkHeader(){
  $alphabet = range('A', 'Z');
  foreach($alphabet as $letter){
    $url = "playerIndex.php?letter=" . urlencode($letter);
    echo "<a href='" . $url . "'>" . h($letter) . "</a>";
    if($letter !== "Z"){
      echo "/";
    }
  }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <?php createPlayerLinkHeader(); ?>
</head>
<body>
  <div id="index">
    <?php
    require "../login.php";
    $letter = $_GET["letter"];
    $letterWithWildcard = $letter . "%";

    $playerListStmt = $conn->prepare("
        SELECT PlayerID, Name, firstName, lastName, middleName 
        FROM player 
        WHERE lastName LIKE ? 
        ORDER BY Name ASC
    ");
    $playerListStmt->bind_param("s", $letterWithWildcard);
    $playerListStmt->execute();
    $playerListResult = $playerListStmt->get_result();

    $list = array();
    while($row = $playerListResult->fetch_assoc()){
        $list[] = $row;
    }
    printPlayerLink($list);
    ?>
  </div>
</body>
<?php include ("../footer/footer.php"); ?>
</html>