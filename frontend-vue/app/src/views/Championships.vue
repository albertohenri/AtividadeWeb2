<template>
<div>
<h1>TABELA DE TÍTULOS</h1>
  <table class="table table-striped table-dark table-hover">
    <caption>Lista de títulos</caption>
    <thead class="thead-dark">
      <tr>
        <th class="campeonato" scope="col">Campeonato</th>
        <th scope="col">Títulos</th>
        <th class="ano" scope="col">Ano</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Mundial</td>
        <td>1</td>
        <td>1983</td>
      </tr>
      <tr>
        <td>Libertadores</td>
        <td>3</td>
        <td>1983, 1995, 2017</td>
      </tr>
      <tr>
        <td>Recopa Sul-Americana</td>
        <td>2</td>
        <td>1996, 2018</td>
      </tr>
      <tr>
        <td>Série A</td>
        <td>2</td>
        <td>1981, 1996</td>
      </tr>
      <tr>
        <td>Copa do Brasil</td>
        <td>5</td>
        <td>1989, 1994, 1997, 2001, 2016</td>
      </tr>
    </tbody>
  </table>
</div>
</template>

<script>
export default {
    name: 'Championships',
};
</script>