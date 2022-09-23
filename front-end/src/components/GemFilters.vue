<template>
  <div class=" container border border-primary rounded-bottom rounded-5 border-2 mb-3 p-0" id="gemFilters">
    <section name="filterOptions" class="d-flex  m-4">
      <div class="col-6 p-0">

        <FilterOptionContainer>
          <div class="form-check text-left ">
            <input class="form-check-input" type="checkbox" value="" id="corruptedCheck">
            <label class="form-check-label" for="corruptedCheck">
              Show Corrupted Gems
            </label>
          </div>
        </FilterOptionContainer>
        <FilterOptionContainer>
          <div class="form-check text-left ">
            <input class="form-check-input" type="checkbox" value="" id="doubleCorruptedCheck">
            <label class="form-check-label" for="doubleCorruptedCheck">
              Show Double Corrupted Gems
            </label>
          </div>
        </FilterOptionContainer>
        <FilterOptionContainer>
          <div class="form-check text-left ">
            <input class="form-check-input" type="checkbox" value="" id="awakenedCheck" checked>
            <label class="form-check-label" for="awakenedCheck">
              Show Awakened Gems
            </label>
          </div>
        </FilterOptionContainer>
      </div>
      <div class="col-6 p-0">
        <FilterOptionContainer>
          <div class="form-check text-left ">
            <input class="form-check-input" type="checkbox" value="" id="qualityCheck" checked>
            <label class="form-check-label" for="qualityCheck">
              Show Gems with Quality
            </label>
          </div>
        </FilterOptionContainer>
        <FilterOptionContainer>
          <div class="form-check text-left ">
            <input class="form-check-input" type="checkbox" value="" id="altQualCheck">
            <label class="form-check-label" for="altQualCheck">
              Show Alternate Quality Gems
            </label>
          </div>
        </FilterOptionContainer>
        <FilterOptionContainer>
          <div class="form-check text-left ">
            <input class="form-check-input" type="checkbox" value="" id="lowConfidenceCheck">
            <label class="form-check-label" for="lowConfidenceCheck">
              Show Low Confidence Prices
            </label>
          </div>
        </FilterOptionContainer>
      </div>

    </section>

    <div class="col-12 border border-top">
      <div class="container d-flex p-2">
        <div class=" col-10">
          <input type="search" id="searchBar" class="form-control" placeholder="Search ..." aria-label="Searchbar" />

        </div>
        <div class="col-2">
          <button type="button" class="btn btn-primary  " @click="$emit('search')">Apply filters</button>

        </div>

      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import FilterOptionContainer from './FilterOptionContainer.vue';

export default Vue.extend({
  name: "GemFilters",
  data() {
    return {
    };
  },
  mounted() {
  },
  methods: {
  },
  components: {
    FilterOptionContainer,
  }
});
</script>
