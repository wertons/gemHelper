<template>
  <li name="Gem row" class=" d-flex flex-row p-0 mb-2">
    <div  class="col-5 border border-primary p-2 text-left">
      <img :src=gemIcon alt="Gem Icon" />
      <span name="Name">
        {{gemName}}
      </span>
    </div>
    <div name="Profit" class="cold-7 p-2">
      {{gemProfit}} chaos for {{gem.max.variant}} -> {{gem.min.variant}}
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

  },
});
</script>
