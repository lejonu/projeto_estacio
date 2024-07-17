import React, { useState } from "react";
import { TextInput, Button } from "react-native-paper";
import { Text, View, StyleSheet } from "react-native";
import { useFrequencia } from "../hooks/useFrequencia";
import { useCpf } from "../hooks/useCpf";
import { Banner } from "react-native-paper";

const Frequencia = () => {
  const [cpf, setCpf] = useState("");
  const [visible, setVisible] = React.useState(false);
  const [bannerMessage, setBannerMessage] = useState("");
  const [bannerIcon, setBannerIcon] = useState("");
  const insertFrequencia = () => {
    if (useCpf(cpf)) {
      if (useFrequencia(cpf)) {
        setCpf("");
        setBannerIcon("playlist-check");
        setBannerMessage(
          "Frequência inserida com sucesso!"
        );
        setVisible(true);
        setInterval(() => {
          setVisible(false);
        }, 3000);
      }
    } else {
      setBannerIcon("playlist-remove");
      setBannerMessage(
        "Houve um problema na inserção. Tente novamente"
      );
      setVisible(true);
      console.log("Error");
    }
  };

  return (
    <View style={styles.container}>
      <Banner
        visible={visible}
        icon={bannerIcon}
        style={styles.banner}
      >
        {bannerMessage}
      </Banner>
      <Text style={styles.text}>
        Insira o CPF para registrar a frequência
      </Text>
      <TextInput
        style={styles.inputText}
        label="CPF"
        value={cpf}
        onChangeText={cpf => setCpf(cpf)}
        keyboardType="numeric"
      />
      <Button
        style={styles.button}
        icon="account-clock"
        mode="contained"
        onPress={insertFrequencia}
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
  },
  banner: {
    marginBottom: 30
  }
});
export default Frequencia;
