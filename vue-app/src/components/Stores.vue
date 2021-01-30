<template>

  <div class="container">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th style="width: 320px">Name</th>
          <th>Postcode</th>
        </tr>
      </thead>
    </table>
    <div class="container scroll">
      <table class="table table-bordered">
        <tbody>
          <tr v-for="item in stores" :key="item.name">
            <td>{{ item.name }}</td>
            <td>{{ item.postcode }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Stores",
  props: ["stores"],
};
</script>