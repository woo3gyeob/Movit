<template>
  <div>
    <MyMovieList/>
    <MyReviews/>
  </div>
</template>

<script>
import MyMovieList from '@/components/MyMovieList'
import MyReviews from '@/components/MyReviews'

export default {
  name: 'Mypage',
  components: {
    MyMovieList,
    MyReviews,
  }
}
</script>

<style>

</style>