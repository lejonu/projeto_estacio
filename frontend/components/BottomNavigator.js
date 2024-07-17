import * as React from "react";
import { BottomNavigation } from "react-native-paper";

import Alunos from "./Alunos";
import Graph from "./Graph";
import Lgpd from "./Lgpd";
import Frequencia from "./Frequencia";

const AlunosRoute = () => <Alunos />;
const GraphRoute = () => <Graph />;
const Frequency = () => <Frequencia />;
const RecentsRoute = () => <Lgpd />;

const BottomNavigator = () => {
  const [index, setIndex] = React.useState(0);

  const [routes] = React.useState([
    {
      key: "frequencia",
      title: "Frequência",
      focusedIcon: "account-clock",
      unfocusedIcon: "account-clock-outline"
    },
    {
      key: "alunos",
      title: "Alunos",
      focusedIcon: "account-circle",
      unfocusedIcon: "account-circle-outline"
    },
    {
      key: "graph",
      title: "Graph",
      focusedIcon: "finance"
    },
    {
      key: "recents",
      title: "Termos de Uso",
      focusedIcon: "book-open",
      unfocusedIcon: "book-open-outline"
    }
  ]);

  const renderScene = BottomNavigation.SceneMap({
    alunos: AlunosRoute,
    graph: GraphRoute,
    recents: RecentsRoute,
    frequencia: Frequency
  });

  return (
    <BottomNavigation
      navigationState={{ index, routes }}
      onIndexChange={setIndex}
      renderScene={renderScene}
      shifting={true}
    />
  );
};

export default BottomNavigator;
