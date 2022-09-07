<template>
  <ul class="list-group d-inline-flex container">

    <GemRow v-for="gem in gems" :key="gem" class="list-group-item gem-row "
    :gem="gem"
    >
    </GemRow>
  </ul>
</template>
<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import GemRow from '../components/GemRow.vue';

export default Vue.extend({
  name: "GemList",
  data() {
    return {
      gems: null,
    };
  },
  mounted() {
    this.getGemList();
  },
  methods: {
    getGemList() {
      const path = "http://localhost:5000/gemList";
      axios.get(path)
        .then((res) => {
          this.gems = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  components: { GemRow }
});
</script>
