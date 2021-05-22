<template>
  <div>
    디테일
    {{ review.title }}
    {{ review.content}}
    <ReviewListDetailComment/>
  </div>
</template>

<script>
import ReviewListDetailComment from '@/components/community/ReviewListDetailComment'
import axios from 'axios'

export default {
  name:'ReviewListDetail',
  components:{
    ReviewListDetailComment
  },
  data () {
    return {
      review:null,
    }
  },
  methods:{
    getReviewDetail () {
      axios({
        method:'get',
        url: `community/${this.$route.params.reviewId}/`
      })
        .then(res =>{
          console.log(res)
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created () {
    this.getReviewDetail()
  }

}
</script>

<style>

</style>