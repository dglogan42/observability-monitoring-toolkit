import Plot from 'react-plotly.js';

function SHAPPlot({ shapData }) {
  return <Plot 
    data={shapData.data} 
    layout={shapData.layout} 
    style={{width: "100%", height: "500px"}}
  />;
}
