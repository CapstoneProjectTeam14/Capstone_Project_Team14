// ReactApp.js

import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import * as d3 from "d3";

const ONOSVisualizer = () => {
  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    // Fetch ONOS node data from the specified URL
    axios
      .get("http://localhost:3002/onos-data") // Update the URL if needed
      .then((response) => setNodes(response.data.nodes))
      .catch((error) => console.error("Error fetching ONOS node data:", error));
  }, []);

  const svgRef = useRef();

  useEffect(() => {
    // Initialize D3.js
    const svg = d3.select(svgRef.current);

    // Render the D3.js graph when nodes change
    const updateGraph = () => {
      const nodesGroup = svg.selectAll(".node").data(nodes);

      // Enter
      const enterNodes = nodesGroup.enter().append("g").attr("class", "node");

      enterNodes
        .append("circle")
        .attr("r", 50) // Increase the circle radius to 30
        .attr("cx", (d, i) => i * 80 + 40) // Adjust spacing between circles
        .attr("cy", 50)
        .style("fill", (d) =>
          d.status === "ACTIVE" || d.status === "READY" ? "green" : "red"
        )
        .append("title")
        .text((d) => `${d.id}: ${d.status}`);

      // Add text element for each circle
      enterNodes
        .append("text")
        .attr("x", (d, i) => i * 80 + 40)
        .attr("y", 50)
        .attr("dy", "0.3em") // Adjust vertical alignment of text
        .style("text-anchor", "middle") // Center text in circle
        .style("fill", "white") // Set text color to white
        .text((d) => d.id);

      // Update
      nodesGroup
        .attr("transform", (d, i) => `translate(${i * 60 + 30}, 50)`)
        .select("circle")
        .style("fill", (d) =>
          d.status === "ACTIVE" || d.status === "READY" ? "green" : "red"
        );

      // Exit
      nodesGroup.exit().remove();
    };

    updateGraph();
  }, [nodes]);

  return (
    <div id="onos">
      <h1>ONOS Cluster Visualizer</h1>
      <svg ref={svgRef} width="75vw"></svg>
    </div>
  );
};

export default ONOSVisualizer;