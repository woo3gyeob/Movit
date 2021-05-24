<template>
  <div>
    <h2 class="mx-5 px-4">내가 작성한 리뷰들</h2>
      <ul v-for="myReview in myReviews" :key="myReview.id" class="shadow">
        <h4>{{ myReview.title }}</h4>
        <div>{{ myReview.content }}</div>
      </ul>
    <div v-if="!myReviews.length">"작성한 리뷰가 없습니다."</div>
  </div>
</template>

<script>
export default {
  name:'MyReviews',
  props :{
    myReviews:{
      type: Array
    }
  }
}
</script>

<style>
  h2 {
      text-align: left;
      color: black;
    }
</style>