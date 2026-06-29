// alerts.js
async function loadAlerts() {
  try {
    const response = await fetch('https://www.metservice.com/cap/severe-weather-warnings-rss.xml');
    // Parse XML and surface weather warnings relevant to active routes or regions
    // Link to full Civil Defence advice
  } catch(e) {
    // Fallback: "Check metservice.com for live warnings"
  }
}
