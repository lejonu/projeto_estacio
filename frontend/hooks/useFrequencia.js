import React from "react";
import base64 from "react-native-base64";
import Axios from "axios";

export const useFrequencia = cpf => {
  async function insertFrequencia() {
    try {
      const response = await Axios.post(
        "registrarFrequencia",
        {
          cpf: base64.encode(cpf)
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        }
      );
    } catch (error) {
      console.log(error);
      return false;
    }
  }
  insertFrequencia();
  return true;
};
