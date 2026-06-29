const timeline = new Animation(
  new KeyframeEffect(coolantPath, [
    { strokeDashoffset: 0 },
    { strokeDashoffset: -120 }
  ], { duration: 2000 }),
  document.timeline
);

// Chain sequences
async function runThermalSequence() {
  await batteryPulse.play(); 
  coolantFlow.play();
  // ... heat exchanger etc.
}
