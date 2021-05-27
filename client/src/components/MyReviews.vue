<template>
  <div class="background-img5">
    <div class="container padding5">
      <div class="container p-3" id="contain">
        <div class="box5" style="overflow:auto; display: inline-block;">
          <br>
          <h2 style="color:white;" class="mx-4 my-3">내가 작성한 리뷰</h2>
          <hr>
          <br>
          <b-list-group v-for="myReview in myReviews" :key="myReview.id">
            <b-list-group-item 
              button
              @click="goToMyReview(myReview.id)"
              style="width:1000px; background-color:rgb(31, 35, 39, 0.3); border-bottom-color:gray; color:white; text-align:left;" 
              variant="dark"
            >
              
              <h5>{{ myReview.title }}</h5>
              <p style="font-size:10px; opacity:0.5">{{myReview.created_at}}</p><br>
            
              <p>{{myReview.content.slice(0,100)}}...</p>

            </b-list-group-item>
          </b-list-group>
        </div>
        <div v-if="!myReviews.length">"작성한 리뷰가 없습니다."</div>
      </div>
    </div>
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
      /* color: rgb(23, 61, 61) */
  }
  .box5 {
    /* background-color: rgb(70, 70, 70); */
    /* border-style: solid; */
    /* border-color: rgb(54, 51, 51); */
    /* border-radius: 10px; */
    height: 850px;
    
  }
  .background-img5 { 
    background: linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.6)),url('../data/frozen3.jpg');
    background-color: black;
    height:100vh;
    background-repeat: no-repeat;
    /* object-fit: cover; */
    background-size: cover;
  }
</style>