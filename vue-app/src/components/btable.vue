<template>
  <div class="container">
      <h2> with Vue bootstap Btable</h2>
    <b-table sticky-header :items="items" head-variant="light"></b-table>
  </div>
</template>

<script>
  export default {
  name: "Items",
  props: ["items"],
};
</script>