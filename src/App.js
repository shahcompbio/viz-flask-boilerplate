import React, { useState, useEffect } from "react";
import "./App.css";

const App = () => {
  // Initial data fetch

  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/name")
      .then((res) => res.json())
      .then((result) => {
        setData(result);
      });
  }, []);

  return data ? data : null;
};

export default App;
