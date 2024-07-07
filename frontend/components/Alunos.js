import React, { useState, useEffect } from "react";
import {
  Text,
  View,
  StyleSheet,
  ScrollView
} from "react-native";
import { TextInput, Button } from "react-native-paper";
import {
  ActivityIndicator,
  MD2Colors
} from "react-native-paper";
import Axios, { formToJSON } from "axios";
import {
  DataTable,
  PaperProvider
} from "react-native-paper";

import { useCpf } from "../hooks/useCpf";

const Alunos = () => {
  const [cpf, setCpf] = React.useState("");
  const [nome, setNome] = React.useState("");
  const [idade, setIdade] = React.useState("");
  const [sexo, setSexo] = React.useState("");
  const [celular, setCelular] = React.useState("");
  const [curso, setCurso] = React.useState("");
  const [turno, setTurno] = React.useState("");
  const [reloadAlunos, setReloadAlunos] = React.useState(0);

  const [items, setItems] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  const [page, setPage] = React.useState(0);
  const [numberOfItemsPerPageList] = React.useState([
    2, 3, 4, 5
  ]);
  const [itemsPerPage, onItemsPerPageChange] =
    React.useState(numberOfItemsPerPageList[3]);

  useEffect(() => {
    const ourRequest = Axios.CancelToken.source();

    async function fetchData() {
      try {
        const response = await Axios.get("alunos", {
          cancelToken: ourRequest.token
        });

        setItems(await response.data);
        setIsLoading(false);
      } catch (error) {
        // console.log(error)
      }
    }

    fetchData();
  }, [reloadAlunos]);

  const from = page * itemsPerPage;
  const to = Math.min(
    (page + 1) * itemsPerPage,
    items.length
  );

  React.useEffect(() => {
    setPage(0);
  }, [itemsPerPage]);

  async function insertAluno() {
    try {
      if (useCpf(cpf)) {
        const response = await Axios.post(
          "novoAluno",
          {
            cpf,
            nome,
            idade,
            sexo,
            celular,
            curso,
            turno
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        );
      } else {
        console.log("CPF inválido");
      }

      setCpf("");
      setNome("");
      setIdade("");
      setSexo("");
      setCelular("");
      setCurso("");
      setTurno("");
      setReloadAlunos(reloadAlunos => reloadAlunos + 1);
    } catch (error) {
      // console.log(error)
    }
  }

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
    <PaperProvider>
      <ScrollView>
        <View style={styles.container}>
          <View>
            <Text style={styles.text}>
              Alunos Cadastrados
            </Text>
            <DataTable>
              <DataTable.Header>
                <DataTable.Title
                  textStyle={{ color: "#808080" }}
                >
                  Nome
                </DataTable.Title>
                <DataTable.Title
                  textStyle={{ color: "#808080" }}
                >
                  CPF
                </DataTable.Title>
              </DataTable.Header>

              {items.slice(from, to).map(item => (
                <DataTable.Row key={item.cpf}>
                  <DataTable.Cell
                    textStyle={{ color: "#484d50" }}
                  >
                    {item.nome}
                  </DataTable.Cell>
                  <DataTable.Cell
                    textStyle={{ color: "#484d50" }}
                  >
                    {item.cpf}
                  </DataTable.Cell>
                </DataTable.Row>
              ))}

              <DataTable.Pagination
                page={page}
                numberOfPages={Math.ceil(
                  items.length / itemsPerPage
                )}
                onPageChange={page => setPage(page)}
                label={`${from + 1}-${to} of ${
                  items.length
                }`}
                numberOfItemsPerPageList={
                  numberOfItemsPerPageList
                }
                numberOfItemsPerPage={itemsPerPage}
                onItemsPerPageChange={onItemsPerPageChange}
                showFastPaginationControls
                selectPageDropdownLabel={
                  "Registros por página"
                }
              />
            </DataTable>
          </View>
          <View style={styles.container}>
            <Text style={styles.text}>
              Inserir novo aluno
            </Text>
            <TextInput
              style={styles.inputText}
              label="CPF"
              value={cpf}
              onChangeText={cpf => setCpf(cpf)}
            />
            <TextInput
              style={styles.inputText}
              label="Nome"
              value={nome}
              onChangeText={nome => setNome(nome)}
            />

            <TextInput
              style={styles.inputText}
              label="Idade"
              value={idade}
              onChangeText={idade => setIdade(idade)}
            />
            <TextInput
              style={styles.inputText}
              label="Sexo"
              value={sexo}
              onChangeText={sexo => setSexo(sexo)}
            />

            <TextInput
              style={styles.inputText}
              label="Celular"
              value={celular}
              onChangeText={celular => setCelular(celular)}
            />
            <TextInput
              style={styles.inputText}
              label="Curso"
              value={curso}
              onChangeText={curso => setCurso(curso)}
            />
            <TextInput
              style={styles.inputText}
              label="Turno"
              value={turno}
              onChangeText={turno => setTurno(turno)}
            />
            <Button
              style={styles.button}
              icon="account-clock"
              mode="contained"
              onPress={insertAluno}
            >
              Inserir Aluno
            </Button>
          </View>
        </View>
      </ScrollView>
    </PaperProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 5
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

export default Alunos;