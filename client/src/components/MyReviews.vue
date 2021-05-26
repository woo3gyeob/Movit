<template>
  <div>
    <b-list-group v-for="myReview in myReviews" :key="myReview.id">
      <b-list-group-item 
        button
        @click="goToMyReview(myReview.id)"
        style="background-color:rgb(29, 56, 66); border-bottom-color:gray; color:white; text-align:left" 
        variant="dark"
      >
        <h5>{{ myReview.title }}</h5>

      </b-list-group-item>
    </b-list-group>
    
    <!-- <ul v-for="myReview in myReviews" :key="myReview.id" class="shadow">
      <a href="#"><h4>{{ myReview.title }}</h4></a>
    </ul> -->
    <div v-if="!myReviews.length">"작성한 리뷰가 없습니다."</div>
  </div>
</template>

<script>
import Vue from 'vue'
import { BListGroup, BListGroupItem } from 'bootstrap-vue'
Vue.component('b-list-group', BListGroup)
Vue.component('b-list-group-item', BListGroupItem)

export default {
  name:'MyReviews',
  props :{
    myReviews:{
      type: Array
    }
  },
  methods: {
    goToMyReview(review) {
      this.$router.push({
        name: 'ReviewListDetail',
        params: {
          reviewId: review
        }
      })
    }
  },
}
</script>

<style>
  h2 {
      text-align: left;
      color: black;
  }

</style>