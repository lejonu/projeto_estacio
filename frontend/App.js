import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import BottomNavigator from "./components/BottomNavigator";
import { SafeAreaProvider } from "react-native-safe-area-context";
import Axios from "axios";
// Axios.defaults.baseURL = "http://127.0.0.1:5000/";
// Axios.defaults.baseURL = "http://localhost:5000/";
Axios.defaults.baseURL = "http://192.168.1.10:5000/";

export default function App() {
  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <BottomNavigator />
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
