<?php
mysqli_report(MYSQLI_REPORT_OFF);
include ("../../includes/login.php");
$json = file_get_contents('PlayerInfo.json');
$json_data = json_decode($json, true);

$stmt = $conn->prepare("
    INSERT INTO player(PlayerID, Name, firstName, lastName, middleName, Position, College, Height, Weight, BirthDate, Draft) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?)
    ON DUPLICATE KEY UPDATE
        Name = VALUES(Name),
        firstName = VALUES(firstName),
        lastName = VALUES(lastName),
        middleName = VALUES(middleName),
        Position = VALUES(Position),
        College = VALUES(College),
        Height = VALUES(Height),
        Weight = VALUES(Weight),
        BirthDate = VALUES(BirthDate),
        Draft = VALUES(Draft)
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

    if(!$stmt->execute()) {
        echo "Error inserting player " . $PlayerID . ": " . $stmt->error . "\n";
    }
}
?>