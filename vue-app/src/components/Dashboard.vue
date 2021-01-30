<template>
  <div class="container">
    <Header />
    <div class="row">
      <div class="col-md-7 mrgnbtm">
        <div class="row">
          <div class="form-group col-md-6">
            <label htmlFor="exampleInputEmail1">Find stores</label>
            <input
              type="text"
              @input="queryForKeywords()"
              class="form-control"
              v-model="storename"
              name="storename"
              id="storename"
              aria-describedby="emailHelp"
              placeholder="ex: IG1 4RS or Stratford"
            />
          </div>
        </div>

        <div class="hello" v-if="!this.errorMessage">
          <h2> Stores</h2>
          <div class="row mrgnbtm">
            <Stores v-if="stores.length > 0" :stores="stores" :errorMessage="errorMessage" :offset="offset"/>
          </div>
          <!-- <div class="row ">
            <Btable v-if="items.length > 0" :items="items" :errorMessage="errorMessage" :offset="offset"/>
          </div> -->
        </div>
         <div class="hello" v-else>
           <h2> {{ this.errorMessage}}</h2>
         </div>
      </div>
    </div>
  </div>
</template>


<script>
import Header from "./Header.vue";
// import Btable from "./btable.vue"
import { findStore } from "../services/UserService";
import Stores from "./Stores";

export default {
  name: "Dashboard",
  components: {
    Header,
    // Btable,
    Stores,
  },
  data() {
    return {
      stores: [],
      storename: "",
      items: [],
      errorMessage: '',
      offset: 3
    };
  },
  methods: {
    queryForKeywords() {
        if (document.getElementById('storename').value.length >= 2) {
          // Added pause
          setTimeout(() => this.getAllStores(), 1000);
        } else {
            this.stores = []
        }
    },
    getAllStores() {
      findStore(this.storename, this.offset).then((response) => {
        if(response){
            this.stores = response.stores;
            // this.items = response.stores;
            this.offset= this.response.p;
        } else {
          this.errorMessage = "Failed to feth the data";
        }
      });
    },
  },
  mounted () {
    this.getAllStores();
  }
};
</script>