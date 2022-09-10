<template>
  <div class="col-6 p-0 ">
    <slot></slot>
  </div>
</template>
<script lang="ts">
import Vue from 'vue';
import axios from 'axios';


export default Vue.extend({
  name: "FilterOptionContainer",
  data() {
    return {
    };
  },
  mounted() {
  },
  methods: {
  },
  components: {}
});
</script>
