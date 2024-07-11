import React, { useState } from "react";
import { TextInput, Button } from "react-native-paper";
import { Text, View, StyleSheet } from "react-native";
import Axios, { formToJSON } from "axios";

const Frequencia = () => {
  const [cpf, setCpf] = useState("");

  async function sendFrequencia() {
    try {
      if (cpf !== "") {
        const response = await Axios.post(
          "registrarFrequencia",
          {
            cpf: cpf
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        );
      }

      setCpf("");
    } catch (error) {
      // console.log(error)
    }
  }

  return (
    <View style={styles.container}>
      <Text style={styles.text}>
        Insira o CPF para registrar a frequência
      </Text>
      <TextInput
        style={styles.inputText}
        label="CPF"
        value={cpf}
        onChangeText={cpf => setCpf(cpf)}
      />
      <Button
        style={styles.button}
        icon="account-clock"
        mode="contained"
        onPress={sendFrequencia}
      >
        Registrar Frequência
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 30
  },
  inputText: {
    marginBottom: 30
  },
  text: {
    fontSize: 18,
    marginBottom: 18,
    textAlign: "center"
  }
});
export default Frequencia;
