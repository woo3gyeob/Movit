<template>
  <div>
    MyPage 안에서 라우터 설정 하기
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