<?php
include ("../../includes/login.php");
mysqli_report(MYSQLI_REPORT_OFF);
$json = file_get_contents('playerSeasonStats.json');
$json_data = json_decode($json, true);

$stmt = $conn->prepare("
    INSERT INTO playerseasonstats(playerID, seasonID, teamID, Age, Pos, GP, GS, MP, FG, FGA, `FG%`, `3P`, `3PA`, `3P%`, `2P`, `2PA`, `2P%`, `eFG%`, FT, FTA, `FT%`, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ON DUPLICATE KEY UPDATE
        Age = VALUES(Age),
        Pos = VALUES(Pos),
        GP = VALUES(GP),
        GS = VALUES(GS),
        MP = VALUES(MP),
        FG = VALUES(FG),
        FGA = VALUES(FGA),
        `FG%` = VALUES(`FG%`),
        `3P` = VALUES(`3P`),
        `3PA` = VALUES(`3PA`),
        `3P%` = VALUES(`3P%`),
        `2P` = VALUES(`2P`),
        `2PA` = VALUES(`2PA`),
        `2P%` = VALUES(`2P%`),
        `eFG%` = VALUES(`eFG%`),
        FT = VALUES(FT),
        FTA = VALUES(FTA),
        `FT%` = VALUES(`FT%`),
        ORB = VALUES(ORB),
        DRB = VALUES(DRB),
        TRB = VALUES(TRB),
        AST = VALUES(AST),
        STL = VALUES(STL),
        BLK = VALUES(BLK),
        TOV = VALUES(TOV),
        PF = VALUES(PF),
        PTS = VALUES(PTS)
");

$stmt->bind_param("sssisiiddddddddddddddddddddddd", $playerID, $seasonID, $teamID, $Age, $Pos, $GP, $GS, $MP, $FG, $FGA, $FGpct, $threeP, $threePA, $threePpct, $twoP, $twoPA, $twoPpct, $eFGpct, $FT, $FTA, $FTpct, $ORB, $DRB, $TRB, $AST, $STL, $BLK, $TOV, $PF, $PTS);

foreach ($json_data as $row) {
    $playerID = $row["playerID"];
    $seasonID = $row["seasonID"];
    $teamID = $row["teamID"];
    $Age = $row["Age"];
    $Pos = $row["Pos"];
    $GP = $row["GP"];
    $GS = $row["GS"];
    $MP = $row["MP"];
    $FG = $row["FG"];
    $FGA = $row["FGA"];
    $FGpct = $row["FG%"];
    $threeP = $row["3P"];
    $threePA = $row["3PA"];
    $threePpct = $row["3P%"];
    $twoP = $row["2P"];
    $twoPA = $row["2PA"];
    $twoPpct = $row["2P%"];
    $eFGpct = $row["eFG%"];
    $FT = $row["FT"];
    $FTA = $row["FTA"];
    $FTpct = $row["FT%"];
    $ORB = $row["ORB"];
    $DRB = $row["DRB"];
    $TRB = $row["TRB"];
    $AST = $row["AST"];
    $STL = $row["STL"];
    $BLK = $row["BLK"];
    $TOV = $row["TOV"];
    $PF = $row["PF"];
    $PTS = $row["PTS"];

    if(!$stmt->execute()) {
        echo "Error inserting stats for player " . $playerID . " season " . $seasonID . ": " . $stmt->error . "\n";
    }
}
?>