<template>
<div class="home">
<el-row display="margin-top:10px">
<el-input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
<el-input v-model="author" placeholder="请输入作者" style="display:inline-table; width: 30%; float:left"></el-input>
<el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
</el-row>
<el-row>
<el-table :data="booklist" style="width: 100%" border>
<el-table-column prop="id" label="编号" min-width="100">

<template slot-scope="scope"> {{ scope.row.pk }} </template>
</el-table-column>
<el-table-column prop="book_name" label="书名" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.name }} </template>
</el-table-column>
<el-table-column prop="book_author" label="作者" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.author }} </template>
</el-table-column>
<el-table-column prop="add_time" label="添加时间" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.add_date }} </template>
</el-table-column>
</el-table>
    </el-row>
  </div>
</template>

<script type="text/javascript">
export default{
  name: 'home',
  data () {
    return {
      input: '',
      author: '',
      booklist: []
    }
  },
  mounted: function () {
    this.showBooks()
  },
  methods: {
    addBook () {
      // console.log(this.input, this.author)
      // var req = 'http://localhost:8000/api/add_book?name=' + this.input + '&author=' + this.author
      // console.log(req)
      this.$http.get('http://localhost:8000/api/add_book?name=' + this.input + '&author=' + this.author).then((response) => {
        var res = JSON.parse(response.bodyText)
        if (res.error_num === 0) {
          this.showBooks()
          this.$message('增加图书成功！')
        } else {
          this.$message.error('新增图书失败，请重试吧')
          console.log(res['msg'])
        }
      })
    },

    showBooks () {
      this.$http.get('http://localhost:8000/api/show_book').then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.booklist = res['list']
        } else {
          this.$message.error('查询书籍失败，请重试')
          console.log(res['msg'])
        }
      })
    }
  }
}
</script>

<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
