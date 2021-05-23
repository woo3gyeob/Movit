<template>
  <div>
    리뷰들
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

</style>