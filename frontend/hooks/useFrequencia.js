import React from "react";
import base64 from "react-native-base64";
import Axios from "axios";
Axios.defaults.baseURL = "http://192.168.1.10:5000/";
//
//

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
      // return false;
    }
  }
  insertFrequencia();
  return true;
};
