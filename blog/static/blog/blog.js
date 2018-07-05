// const blog_path = "http://127.0.0.1:8000/api/blogs/";//测试定义
const blog_path = 'http://wangyushun.pythonanywhere.com/api/blogs/';

// 博客列表组件
const BlogList = {
	template: `
		<div>
			<p v-if="blogList.length == 0">暂未发表博客!</p>
			<div v-else>				
				<p class="text-center">第{{blogList.page_number}}页/共{{blogList.num_pages}}页/共{{blogList.count}}篇</p>
				<div v-for="blog in blogList.results" class="blog-list-item">
					<div>
						<h3 :blog_url="blog.url" :blog_id="blog.id" @click="handle_blog_click($event)">
							<router-link :to="/blog/ + blog.id">{{ blog.title }}</router-link>
						</h3>
						<p>发表于: {{ blog.create_time }} </p>	
					</div>				
					<!-- <div v-html="blog.text | truncatechars(30)"></div> -->
				</div>
				<div>
					<nav aria-label="Page navigation">
                		<ul class="pagination">
                			<li v-if="blogList.page_links.previous_url">
                				<span class="btn" :page_url="blogList.page_links.previous_url" @click="handle_page_click($event)">&laquo;</span>
                			</li>
                	 		<li v-else>
                	 			<span>&laquo;</span>
                	 		</li>
                	 		<template v-for="link in blogList.page_links.page_links">
								<li v-if="(link[0] && link[1]) == null"><span>...</span></li>
								<li v-else :class="{active: link[2]}">
									<span class="btn" :page_url="link[0]" @click="handle_page_click($event)">{{link[1]}}</span>
								</li>
							</template>
                	 		<li v-if="blogList.page_links.next_url">
                	 			<span class="btn" :page_url="blogList.page_links.next_url" @click="handle_page_click($event)" aria-label="Next" aria-hidden="true">&raquo;</span>
                	 		</li>
                            <li v-else class="disable">
                            	<span>&raquo;</span>
                            </li>
                	 	</ul>
            		</nav>
				</div>
			</div>
		</div>
	`,
	data() {
		return {
			blogList: '',
		}
	},
	filters: {
		truncatechars: function(value, length=20) {
			return value.substr(0, length);
		}
	},
	methods: {
		get_blogs(url=blog_path) {
			this.$http.get(url)
			.then(response => {
				this.blogList = response.data;
				console.log(response.data);
			})
			.catch(function(error){
				console.log('error', error);
			});
		},
		//博客列表页码点击事件处理
		handle_page_click(event){
			let page_url = event.target.getAttribute("page_url");
			this.get_blogs(page_url);
		},
		//博客文章点击事件处理
		handle_blog_click($event){

		}
	},
	// mounted() {
	created() {
		this.get_blogs();
	}
};

//博客详情组件
const BlogDetail = {
	template:`
		<div>
			<template v-if="blog">
				<div>
					<h3 class="blog-title" v-text="blog.title"></h3>
					<p class="text_center">
						<span v-if="blog.author">{{ blog.author }}</span>
						<span class="unobtrusive-text" v-text="blog.create_time"></span>
					</p>
				</div>
				<br>
				<div class="blog-text" v-html="blog.text">
				</div>
			</template>
		</div>
	`,
	data(){
		return {
			blog:""
		}
	},
	methods: {
		get_blog(){
			this.$http.get(blog_path + this.$route.params.id)
			.then(response => {
				this.blog = response.data;
				console.log('blog', response.data)
			})
			.catch(error => {
				console.log('error:', error);
			})
		}
	},
	created(){
		console.log(this.$route.params.id);
		this.get_blog();
	}
};



const router = new VueRouter({
	routes: [
		{ path: '/', redirect: '/bloglist'},//根路由
		{ path: '/bloglist', component: BlogList, name: 'bloglist' },
		{ path: '/blog/:id', component: BlogDetail, name: 'blog' },
	]
});


Vue.prototype.$http = axios;

const app = new Vue({
	router: router,// (缩写) 相当于 router: router
	data: {
	},
	methods: {
	},
	components: {
		'blog-list': BlogList,
		'blog-detail': BlogDetail,
	},

}).$mount('#app');






