<?php
// $command = escapeshellcmd('python3 arima.py');
$command = escapeshellcmd('python arima.py');
$output = shell_exec($command);

$forecast = explode(",", trim($output)); 
echo "Forecasted Tourists for Next 3 Months:\n"; 
foreach ($forecast as $month => $value) { 
    echo "Month " . ($month + 1) . ": $value\n"; 
} 
?>
