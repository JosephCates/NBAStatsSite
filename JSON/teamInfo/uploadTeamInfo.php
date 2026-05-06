<?php
mysqli_report(MYSQLI_REPORT_OFF);
include ("../../includes/login.php");
$json = file_get_contents('teamInfo.json');
$json_data = json_decode($json, true);

$stmt = $conn->prepare("
    INSERT INTO team(teamID, Name, City, Founding)
    VALUES(?,?,?,?)
    ON DUPLICATE KEY UPDATE
        Name = VALUES(Name),
        City = VALUES(City),
        Founding = VALUES(Founding)
");

$stmt->bind_param("ssss", $teamID, $Name, $City, $Founding);

foreach ($json_data as $row) {
    $teamID   = $row["teamID"];
    $Name     = $row["Name"] ?? $row["name"] ?? "";
    $City     = $row["City"] ?? $row["city"] ?? "";
    $Founding = $row["Founding"] ?? $row["founding"] ?? "";

    if (!$stmt->execute()) {
        echo "Error inserting team " . $teamID . ": " . $stmt->error . "\n";
    }
}
?>