import React from "react";
import { Text, View, StyleSheet } from "react-native";
import { ScrollView } from "react-native";

const Lgpd = () => {
  return (
    <View style={styles.container}>
      <ScrollView>
        <Text style={styles.title}>
          Termos de Uso e Política de Privacidade
        </Text>
        <Text style={styles.title}>
          Termos e Condições de Uso
        </Text>
        <Text style={styles.text}>
          Os presentes termos e condições de uso visam
          regular a utilização por você, usuário, de nossos
          serviços pelo aplicativo ‘Registro de Frequência’
          da auto escola ‘Passagem Obrigatória’. Para a
          utilização de alguns serviços e canais de
          atendimento poderá ser feita mediante o registro
          do usuário; Não nos responsabilizamos por danos a
          terceiros que decorram de falhas de acesso,
          transmissão, difusão ou disponibilização de
          conteúdo e de serviços do aplicativo; A oferta de
          serviços e/ou conteúdo desse aplicativo obedecem a
          critérios de acessibilidade;
        </Text>
        <Text style={styles.title}>Termo de Aceitação</Text>
        <Text style={styles.text}>
          Ao utilizar os nossos Serviços, o usuário aceita e
          concorda com todos os termos e condições expostas
          que se encontram vigentes na data. Alertamos que
          estes Termos e Condições de Uso poderão ser
          modificados a qualquer momento, em virtude de
          alterações na legislação ou nos Serviços, em
          decorrência da utilização de novas ferramentas
          tecnológicas ou, ainda, sempre que, a exclusivo
          critério da autoescola, caso tais alterações se
          façam necessárias. A utilização dos serviços
          online disponibilizados pelo aplicativo por
          qualquer usuário implicará em expressa aceitação
          destes Termos e Condições de Uso.
        </Text>
        <Text style={styles.title}>
          Tratamento de Informações
        </Text>
        <Text style={styles.text}>
          A sua privacidade e o sigilo de suas informações
          são muito importantes. Tomamos os cuidados
          necessários para garantir a proteção, o sigilo e o
          uso adequado dos seus dados pessoais. A autoescola
          se compromete a cumprir as normas previstas na
          LGPD (Lei Geral de Proteção de Dadas Pessoais) e a
          realizar o tratamento de dados pessoais em
          conformidade com os seguintes princípios: a)
          apenas para as finalidades determinadas nessa
          política, valendo-se da quantidade adequada de
          dados, pertinentes e limitados à necessidade e
          objetivo do tratamento; b) de forma transparente,
          sendo garantido ao titular dos dados o livre
          acesso, a exatidão dos dados e a sua consulta
          facilitada; c) de forma segura, por meio da adoção
          de medidas técnicas aptas a proteger os dados
          pessoais, prevenir e mitigar danos decorrentes de
          eventual acesso não autorizado, ou de situação
          acidental ou ilícita de violação de dados. A
          autoescola realizará a gestão de dados pessoais
          durante o ciclo de vida destas informações; e em
          hipótese alguma haverá tratamento de dados para
          fins discriminatórios ilícitos ou abusivos.
        </Text>
        <Text style={styles.title}>
          Os dados cadastrados neste aplicativo são
          criptografados.
        </Text>
        <Text style={styles.text}>
          O envio de informações ao banco de dados só será
          feito mediante aceitação do usuário ao
          disponibilizar seu CPF, que poderá, a qualquer
          momento, requerer o cancelamento do envio de
          informações; O CPF, o nome e número do celular do
          usuário serão criptografados antes de serem
          armazenados na base de dados. O aplicativo faz uso
          de cookies para processar consultas em
          determinadas bases de dados e realizar operações;
          Podemos, a qualquer momento e sem aviso prévio aos
          usuários, alterar ou extinguir qualquer conteúdo
          desse aplicativo, bem como mudar sua concepção
          visual e estrutura de conteúdo.
        </Text>

        <Text style={styles.title}>
          Acesso a Conteúdo Restrito e Suspensão de Acesso
        </Text>
        <Text style={styles.text}>
          Os Serviços estão disponíveis em conteúdo fechado.
          Considerando que você é responsável pela
          veracidade das informações cadastradas, informamos
          que o cadastro de informações falsas pode gerar
          inconsistência na prestação dos serviços, bem como
          impactar ou interromper o seu acesso. A qualquer
          tempo, sem aviso prévio, A autoescola poderá
          suspender, cancelar ou interromper o acesso aos
          Serviços, respeitadas as condições da legislação
          aplicável.
        </Text>
        <Text style={styles.title}>
          Relacionamento com Terceiros
        </Text>
        <Text style={styles.text}>
          Este aplicativo contém links que levam a sites de
          terceiros, cujos conteúdos não são de nossa
          responsabilidade e sobre os quais não incide essa
          política de privacidade.
        </Text>
        <Text style={styles.title}>
          Conteúdos publicados na forma de notícia
        </Text>
        <Text style={styles.text}>
          Os conteúdos publicados na área de notícias do
          aplicativo, nos formatos de textos, fotos, vídeos
          ou áudios, têm caráter institucional ou avisos aos
          usuários; A autoescola disponibiliza esses
          conteúdos como de uso público, permitindo sua
          reprodução em parte ou na íntegra, porém é vedada
          a reprodução dos mesmos de forma alterada, que
          prejudiquem ou mudem a sua interpretação com
          objetivos inversos à informação original. Fica
          vedada, também, a reprodução dos mesmos para fins
          comerciais.
        </Text>
        <Text style={styles.title}>
          O que é a Lei Geral de Proteção de Dados Pessoais?
        </Text>
        <Text style={styles.text}>
          É uma lei que estabelece regras ao uso de dados
          pessoais de pessoas físicas por entidades públicas
          e privadas. A LGPD é uma norma que garante
          direitos aos titulares dos dados e estabelece uma
          regra mínima para coleta, armazenamento,
          tratamento e compartilhamento de dados pessoais de
          pessoas físicas. As regras estabelecidas pela LGPD
          devem ser observadas por todos os setores do
          mercado: bancos, hospitais, comércios, empresas de
          e-commerce e também o setor público.
        </Text>
        <Text style={styles.text}>
          A LGPD pode ser acessada no link:
          http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm
        </Text>
        <Text style={styles.title}>
          Data de publicação deste documento: 14/07/2024
          12:12
        </Text>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    marginBottom: "5%",
    padding: 20
  },
  title: {
    marginBottom: "5%",
    marginTop: "5%",
    fontSize: 16,
    alignSelf: "center"
  },
  text: {
    marginBottom: "5%",
    fontSize: 12
  }
});

export default Lgpd;
