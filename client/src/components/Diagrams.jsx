<svg width="600" height="400" viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Battery Pack -->
  <rect x="50" y="100" width="150" height="200" rx="10" fill="#4ade80" stroke="#166534" stroke-width="8"/>
  <text x="125" y="210" text-anchor="middle" fill="black" font-size="16" font-weight="bold">Battery Pack</text>
  
  <!-- Animated Coolant Flow -->
  <path id="coolant" d="M200 150 Q300 100 400 150" fill="none" stroke="#3b82f6" stroke-width="20" stroke-dasharray="20,10">
    <animate attributeName="stroke-dashoffset" values="0; -60" dur="2s" repeatCount="indefinite"/>
  </path>
  <text x="300" y="130" text-anchor="middle" fill="#1e40af" font-size="14">Coolant Flow</text>
  
  <!-- Heat Exchanger with pulse -->
  <rect x="420" y="120" width="80" height="160" rx="10" fill="#eab308" stroke="#854d0e">
    <animate attributeName="opacity" values="0.7;1;0.7" dur="3s" repeatCount="indefinite"/>
  </rect>
  
  <!-- Heat Pump -->
  <circle cx="520" cy="200" r="60" fill="#ef4444" stroke="#991b1b"/>
  <text x="520" y="205" text-anchor="middle" fill="white" font-size="13">Heat Pump</text>
</svg>
