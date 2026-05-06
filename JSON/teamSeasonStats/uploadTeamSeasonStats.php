<?php
mysqli_report(MYSQLI_REPORT_OFF);
include ("../../includes/login.php");

$json = file_get_contents('teamSeasonInfo.json');
$json_data = json_decode($json, true);

$stmt = $conn->prepare("
    INSERT INTO teamseasoninfo(teamID, seasonID, TeamAbbr, TeamName, LG, Record, Seed, PostSeason, OffRtg, DefRtg, NetRtg, expectedRecord, Coach, GM)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ON DUPLICATE KEY UPDATE
        TeamAbbr = VALUES(TeamAbbr),
        TeamName = VALUES(TeamName),
        LG = VALUES(LG),
        Record = VALUES(Record),
        Seed = VALUES(Seed),
        PostSeason = VALUES(PostSeason),
        OffRtg = VALUES(OffRtg),
        DefRtg = VALUES(DefRtg),
        NetRtg = VALUES(NetRtg),
        expectedRecord = VALUES(expectedRecord),
        Coach = VALUES(Coach),
        GM = VALUES(GM)
");

$stmt->bind_param("ssssssssssssss", $teamID, $seasonID, $TeamAbbr, $TeamName, $LG, $Record, $Seed, $PostSeason, $OffRtg, $DefRtg, $NetRtg, $expectedRecord, $Coach, $GM);

foreach ($json_data as $row) {
    $teamID         = $row["teamID"];
    $seasonID       = $row["seasonID"];
    $TeamAbbr       = $row["TeamAbbr"];
    $TeamName       = $row["TeamName"];
    $LG             = $row["LG"];
    $Record         = $row["Record"];
    $Seed           = $row["Seed"];
    $PostSeason     = $row["PostSeason"];
    $OffRtg         = $row["OffRtg"];
    $DefRtg         = $row["DefRtg"];
    $NetRtg         = $row["NetRtg"];
    $expectedRecord = $row["expectedRecord"];
    $Coach          = $row["Coach"];
    $GM             = $row["GM"];

    if (!$stmt->execute()) {
        echo "Error inserting team season " . $teamID . " " . $seasonID . ": " . $stmt->error . "\n";
    }
}
?>