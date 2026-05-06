<?php include ("../header/header.php"); ?>

<link rel="stylesheet" href="/NBAStats/includes/assets/css/home.css">

<!-- Basketball court SVG background -->
<div class="court-bg" aria-hidden="true">
    <svg viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice"
         fill="none" xmlns="http://www.w3.org/2000/svg"
         stroke="#ffffff" stroke-width="1.5">
        <!-- Perimeter -->
        <rect x="60" y="40" width="1080" height="620"/>
        <!-- Half-court line -->
        <line x1="600" y1="40" x2="600" y2="660"/>
        <!-- Centre circle -->
        <circle cx="600" cy="350" r="90"/>
        <circle cx="600" cy="350" r="18"/>
        <!-- Left key -->
        <rect x="60" y="220" width="190" height="260"/>
        <path d="M250,220 a130,130 0 0,1 0,260"/>
        <!-- Right key -->
        <rect x="950" y="220" width="190" height="260"/>
        <path d="M950,220 a130,130 0 0,0 0,260"/>
        <!-- Three-point lines -->
        <line x1="60"  y1="160" x2="175" y2="160"/>
        <line x1="60"  y1="540" x2="175" y2="540"/>
        <path d="M175,160 a370,370 0 0,1 0,380"/>
        <line x1="1140" y1="160" x2="1025" y2="160"/>
        <line x1="1140" y1="540" x2="1025" y2="540"/>
        <path d="M1025,160 a370,370 0 0,0 0,380"/>
    </svg>
</div>

<section class="home-hero">

    <!-- Heading -->
    <div class="home-logo fade-up">
        <p class="eyebrow">The Complete Reference</p>
        <h1>NBA<br>Stats</h1>
        <p class="sub">Every Season · Every Player · Every Team</p>
    </div>

    <!-- Search -->
    <div class="search-card fade-up-2">
        <span class="search-label">Search a player</span>
        <form action="../playerStats/playerStats.php" method="GET">
            <div class="search-row">
                <input
                    type="text"
                    name="txtpname"
                    id="txtpname"
                    class="search-input"
                    autocomplete="off"
                    placeholder="e.g. LeBron James, Kobe Bryant…"
                    aria-label="Player name">
                <button type="submit" class="search-btn">Find</button>
            </div>
        </form>

        <div class="quick-links">
            <a href="../playerIndex/playerIndex.php?letter=a" class="quick-link">Browse Players</a>
            <a href="../teamIndex/teamIndex.php"              class="quick-link">Teams</a>
            <a href="../seasons/seasons.php"                  class="quick-link">Seasons</a>
        </div>
    </div>

    <!-- Stat ticker -->
    <div class="ticker-wrap fade-up-3" aria-hidden="true">
        <div class="ticker-track">
            <?php
            $stats = [
                ["38,652", "All-Time Points Leader"],
                ["1,074",  "NBA Seasons Tracked"],
                ["30",     "Active Franchises"],
                ["4,500+", "Players Indexed"],
                ["1946",   "First Season"],
                ["50.4",   "Wilt's PPG Record"],
                ["100",    "Wilt's Single-Game High"],
            ];
            // Duplicate for seamless loop
            $stats = array_merge($stats, $stats);
            foreach ($stats as $s): ?>
            <div class="ticker-item">
                <span class="t-val"><?= htmlspecialchars($s[0]) ?></span>
                <span class="t-lbl"><?= htmlspecialchars($s[1]) ?></span>
            </div>
            <?php endforeach; ?>
        </div>
    </div>

</section>

<script>
$(function () {
    $("#txtpname").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "../autoComplete/autoComplete.php",
                method: "GET",
                dataType: "json",
                data: { txtpname: request.term },
                success: function (data) { response(data); },
                error: function (jqXHR, status, err) {
                    console.error("Autocomplete failed:", status, err);
                }
            });
        },
        minLength: 1
    });
});
</script>

<?php include ("../footer/footer.php"); ?>
