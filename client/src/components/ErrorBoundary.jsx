class ErrorBoundary extends React.Component {
  state = { hasError: false, retryCount: 0 };
  retry = () => {
    this.setState({ hasError: false, retryCount: this.state.retryCount + 1 });
  };
  componentDidCatch(error, info) {
    // Log to Sentry
    console.error('SHAP Error:', error);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <p>Failed to render SHAP visualization. (Attempt {this.state.retryCount})</p>
          <button onClick={this.retry}>Retry Plot</button>
          <button onClick={() => window.location.reload()}>Full Refresh</button>
        </div>
      );
    }
    return this.props.children;
  }
}
