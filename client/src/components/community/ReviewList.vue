<template>
  <div>
    <b-button @click="writeContent">글쓰기</b-button>
    <b-table 
      striped 
      hover
      :items="reviews"
      :fields="fields"
      :per-page="perPage"
      :current-page="currentPage"
      @row-clicked="rowClick"
    ></b-table>
    <!-- 아직 제대로 구현 안됨(페이지네이션) -->
    <!-- <b-pagination v-model="currentPage" :total-="rows" :per-page="perPage" align="center"></b-pagination> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name : "ReviewList",
  data() {
    return {
      reviews : [
        {
          id:343,
          username: '1',
          title:'하이',
          content: '이히',
          
        },
      ],
      currentPage: 1,
      perPage:10,
      fields: [
        {
          key: 'id',
          label:'번호'
        },
        {
          key: 'title',
          label:'제목'
        },
        {
          key: 'username',
          label: '글쓴이',
        },
        {
          key: 'created_at',
          label: '작성일',
        },
      ],
    }
  },
  methods:{
    getReviews () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/community/',
      })
        .then(res => {
          this.reviews = res.data
        })
        .catach(err => {
          console.log(err)
        })
    },
    rowClick (review){
      this.$router.push({
        path:`community/${review.id}`
      })
    },
    writeContent() {
      this.$router.push({
        path:`/community/create`,
      })
    },
  },
  created () {
    this.getReviews()
  }
}
</script>