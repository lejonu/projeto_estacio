import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";
import {
  ActivityIndicator,
  MD2Colors
} from "react-native-paper";
import Axios, { formToJSON } from "axios";
import {
  DataTable,
  PaperProvider
} from "react-native-paper";

const Alunos = () => {
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
  }, []);

  const from = page * itemsPerPage;
  const to = Math.min(
    (page + 1) * itemsPerPage,
    items.length
  );

  React.useEffect(() => {
    setPage(0);
  }, [itemsPerPage]);

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
      <View style={styles.container}>
        <Text style={styles.text}>Alunos Cadastrados</Text>
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
            label={`${from + 1}-${to} of ${items.length}`}
            numberOfItemsPerPageList={
              numberOfItemsPerPageList
            }
            numberOfItemsPerPage={itemsPerPage}
            onItemsPerPageChange={onItemsPerPageChange}
            showFastPaginationControls
            selectPageDropdownLabel={"Registros por página"}
          />
        </DataTable>
      </View>
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
