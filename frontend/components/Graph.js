import React, { useState, useEffect } from "react";
import Plot from "react-native-plotly";
import { View, StyleSheet } from "react-native";
import Axios from "axios";
import {
  ActivityIndicator,
  MD2Colors
} from "react-native-paper";

const Graph = () => {
  const [plot, setPlot] = useState(0);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const ourRequest = Axios.CancelToken.source();

    async function fetchGraph() {
      try {
        const response = await Axios.get("graph01App", {
          cancelToken: ourRequest.token
        });

        setPlot(await response.data);
        setIsLoading(false);
      } catch (error) {
        console.log(error);
      }
    }

    fetchGraph();
  }, []);

  if (isLoading)
    return (
      <View style={styles.container}>
        <ActivityIndicator
          animating={true}
          color={MD2Colors.red800}
        />
      </View>
    );

  return (
    !isLoading && (
      <Plot data={plot.data} layout={plot.layout} />
    )
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 30
  }
});

export default Graph;
