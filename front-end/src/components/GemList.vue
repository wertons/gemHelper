<template>
  <ul class="list-group d-inline-flex container p-0 overflow-auto" style="height:80vh">

    <GemRow v-for="gem in gems" :key="gem" class="list-group-item gem-row "
    :gem="gem"
    >
    </GemRow>
  </ul>
</template>
<script lang="ts">
import Vue from 'vue';
import GemRow from './GemRow.vue';

export default Vue.extend({
  name: "GemList",
  data() {
    return {
    };
  },
  props:{
    gems: Object,
  },
  mounted() {
  },
  methods: {
  },
  components: { GemRow }
});
</script>
