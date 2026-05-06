<?php
// Determine active page for nav highlighting
$currentPage = htmlspecialchars($_SERVER["PHP_SELF"]);

function isActive($paths) {
    global $currentPage;
    foreach ((array)$paths as $path) {
        if (strpos($currentPage, $path) !== false) return true;
    }
    return false;
}

// Resolve path prefix so CSS links work from any subdirectory
// All pages live one level deep under /NBAStats/includes/
$cssBase = "/NBAStats/includes/assets/css/";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="<?= $cssBase ?>global.css">
    <!-- jQuery UI (autocomplete pages only — harmless to load everywhere) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js" defer></script>
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.13.2/themes/smoothness/jquery-ui.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.13.2/jquery-ui.min.js" defer></script>
</head>
<body>

<nav class="site-nav" role="navigation" aria-label="Main navigation">
    <div class="container">
        <a class="nav-logo" href="/NBAStats/includes/home/home.php">
            NBA<span>.</span>Stats
        </a>

        <button class="nav-toggle" aria-label="Toggle menu" onclick="this.closest('nav').querySelector('.nav-links').classList.toggle('open')">
            <span></span><span></span><span></span>
        </button>

        <ul class="nav-links" role="list">
            <li>
                <a href="/NBAStats/includes/home/home.php"
                   <?= isActive('home/home') ? 'class="active"' : '' ?>>
                    Search
                </a>
            </li>
            <li>
                <a href="/NBAStats/includes/playerIndex/playerIndex.php?letter=a"
                   <?= isActive('playerIndex') ? 'class="active"' : '' ?>>
                    Players
                </a>
            </li>
            <li>
                <a href="/NBAStats/includes/teamIndex/teamIndex.php"
                   <?= isActive('teamIndex') ? 'class="active"' : '' ?>>
                    Teams
                </a>
            </li>
            <li>
                <a href="/NBAStats/includes/seasons/seasons.php"
                   <?= isActive('seasons') ? 'class="active"' : '' ?>>
                    Seasons
                </a>
            </li>
        </ul>
    </div>
</nav>

<main class="site-main">
