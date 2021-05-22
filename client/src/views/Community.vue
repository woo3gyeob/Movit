<template>
  <div>
    <ReviewList :reviews="reviews"/>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList'

export default {
  name: 'Community',
  components: {
    ReviewList
  },
  props: {
    reviews: {
      type: Array,
    }
  },
  created () {
  }
}
</script>

<style>

</style>