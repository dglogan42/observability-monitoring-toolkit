app.post('/webhooks/sentry', (req, res) => {
  const payload = req.body;
  const issue = payload.data.issue;
  // Parse & log to DB
  console.log(`Sentry Alert: ${issue.title} - ${issue.tags.model}`);
  // Trigger UI notification
});
