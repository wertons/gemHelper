<template>
  <li name="Gem row" class=" d-flex flex-row p-0 mb-2"
  v-if="matchesFilter()"
  >
    <div  class="col-5 border    p-2 text-left ">
      <img :src=gemIcon alt="Gem Icon" loading="lazy"/>
      <span name="Name">
        {{gemName}}
      </span>
    </div>
    <div name="Profit" class="col-7 p-2 text-left">
      {{gemProfit}} chaos for {{(gem.min.gemLevel + "|" + (gem.min.gemQuality != undefined ? gem.min.gemQuality : 0)) ?? "error"}} into {{(gem.max.gemLevel + "|" + (gem.max.gemQuality != undefined ? gem.max.gemQuality: 0)) ?? "error"}} | base cost {{gem.min.chaosValue}} chaos
    </div>
  </li>
</template>
<script lang="ts">
import Vue from 'vue';
import axios from 'axios';

export default Vue.extend({
  props:{
    gem: Object,
  },
  name: 'GemRow',
  data() {
    return {
      gemName: this.gem.name,
      gemProfit: this.gem.profit,
      gemIcon: this.gem.icon,
    };
  },
  mounted() {

  },
  methods: {
    matchesFilter(){

      let searchBar = document.querySelector("#searchBar");
      let searchParams = searchBar != null ? searchBar.value : "";

      return this.gemName.toLowerCase().includes(searchParams.toLowerCase());
    }
  },
});
</script>
