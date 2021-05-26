<template>
  <div class="background-img padding">
    <div class="overflow-auto">
      <h1>Movit Community</h1>
      <br><br>
      <b-table 
        striped 
        hover
        :items="reviews"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        @row-clicked="rowClick"
        dark
        responsive
      ></b-table>
      <!-- 아직 제대로 구현 안됨(페이지네이션) -->
      <!-- <b-pagination v-model="currentPage" :total-="rows" :per-page="perPage" align="center"></b-pagination> -->
      <button @click="writeContent" class="btn btn-dark">글쓰기</button>
      <br><br>
      <b-pagination
        v-model="currentPage"
        pills :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
        align="center"
        class="customPagination"
      ></b-pagination>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import { BPagination, BTable } from 'bootstrap-vue'
Vue.component('b-pagination', BPagination)
Vue.component('b-table', BTable)
import axios from 'axios'

export default {
  name : "ReviewList",
  data() {
    return {
      perPage: 10,
      currentPage: 1,
      reviews : [
      ],
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
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },
    getReviews: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.setToken(),
      })
        .then(res => {
          this.reviews = res.data
        })
        .catch(err => {
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
  },
  computed: {
    rows() {
      return this.reviews.length
    }
  }
}
</script>

<style>
  .background-img { 
    background: linear-gradient(rgba(0,0,0,0.3),rgba(0,0,0,0.5)),url('data/lalaland.jpg');
    background-color: black;
    height:100vh;
    background-repeat: no-repeat;
  }
  .padding {
    padding: 5% 15% ;
  } 

</style>