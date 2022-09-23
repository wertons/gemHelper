<template>
  <div class="home ">
    <GemFilters @search="getGemList()"></GemFilters>
    <GemList :gems="gems"></GemList>
  </div>
</template>

<script>
import GemList from '../components/GemList.vue';
import GemFilters from '../components/GemFilters.vue';
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    GemList,
    GemFilters
  },
  data() {
    return {
      gems :null,
    };
  },
  methods: {
    /**
     * Get a list of gems applying current search options
    */
    getGemList() {
      const path = "http://127.0.0.1:5000/gemList";
      axios.post(path, {
        options: this.getGemFilters()
      })
        .then((res) => {
          this.gems = res.data;
        })
        .catch((err) => {
        });
    },
    /**
     * Get a list of currently selected  filters
    */
    getGemFilters(){
      let options = {};
      document.querySelectorAll("#gemFilters input").forEach(option => {
        //Do a special check for checkboxes as their default value is null
        if(option.classList.contains("form-check-input")){
          options[option.id] = option.checked ? true : false;
        } else{
          options[option.id] =  option.value;
        }
      })
      return options;

    }
  },
};
</script>
