<template>
  <li name="Gem row" class=" d-flex flex-row p-0 mb-2"
  v-if="matchesFilter()"
  >
    <div  class="col-5 border border-primary p-2 text-left">
      <img :src=gemIcon alt="Gem Icon" loading="lazy"/>
      <span name="Name">
        {{gemName}}
      </span>
    </div>
    <div name="Profit" class="cold-7 p-2">
      {{gemProfit}} chaos for {{gem.min.variant ?? "error"}} into {{gem.max.variant ?? "error"}} | base cost {{gem.min.chaosValue}} chaos
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

      let searchParams = document.querySelector("#searchBar").value;

      return this.gemName.toLowerCase().includes(searchParams.toLowerCase());
    }
  },
});
</script>
