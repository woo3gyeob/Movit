<template>
  <div>
    <h4>제목: {{ review.title }}</h4>
    <p>내용: {{ review.content }}</p>
    <ReviewListDetailComment 
      :commentCount="review.comment_count"
      :commentSet="review.comment_set"
      :reviewId ="review.id"
    />
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
      review:{},
    }
  },
  methods:{
    getReviewDetail () {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/community/${this.$route.params.reviewId}/`
      })
        .then(res =>{
          this.review = res.data

        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  mounted () {
    this.getReviewDetail()
  },

}
</script>

<style>

</style>