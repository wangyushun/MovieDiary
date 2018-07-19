// const api_base_url = "http://127.0.0.1:8000/api/";//测试定义
const api_base_url = 'http://wangyushun.pythonanywhere.com/api/';

const blogs_url = api_base_url + 'blogs/';
const blogtypes_url = api_base_url + 'blogtypes/';
const blogtags_url = api_base_url + 'blogtags/';

// 博客列表组件
const BlogList = {
    template: `
        <div>
            <back-top iClass="glyphicon glyphicon-arrow-up"></back-top>
            <p v-if="! isUpdateOk">{{errorMsg}}</p>
            <div v-else-if="blogList.results.length > 0">
                <p class="text-center">第{{blogList.page_number}}页/共{{blogList.num_pages}}页/共{{blogList.count}}篇</p>
                <div v-for="blog in blogList.results" class="blog-list-item">
                    <div>
                        <h3>
                            <router-link :to="{ name: 'blog', params: { id: blog.id }, query: { page: blogList.page_number }}">{{ blog.title }}</router-link>
                        </h3>
                        <p>发表于: {{ blog.create_time }} </p>
                        <p v-if="blog.blog_type">分类：{{ blog.blog_type.name }}</p>
                        <p v-if="blog.blog_tags.length > 0">
                            <span v-for="tag in blog.blog_tags" class="glyphicon glyphicon-tags">{{ tag.name }}</span>
                        </p>
                    </div>              
                    <!-- <div v-html="blog.text | truncatechars(30)"></div> -->
                </div>
                <div v-if="blogList.num_pages != 1">
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
            <p v-else>无相关记录</p>
        </div>
    `,
    data() {
        return {
            blogList: {},
            isUpdateOk: false,
            errorMsg: "",
        }
    },
    filters: {
        truncatechars: function(value, length=20) {
            return value.substr(0, length);
        }
    },
    methods: {
        get_blogs(url=blogs_url, params={}) {
            this.$http.get(url, {
                params: params,
            })
            .then(response => {
                this.blogList = response.data;
                this.isUpdateOk = true;
                // console.log(response.data);
            })
            .catch(error => {
                // console.log(error);
                this.isUpdateOk = false;
                this.errorMsg = error.response.status + ':' +error.response.statusText;
            });
        },
        //博客列表页码点击事件处理
        handle_page_click(event){
            let page_url = event.target.getAttribute("page_url");
            this.get_blogs(page_url);
        },
        get_data(){
            let blogtype_id = this.$route.query.blogtype_id;
            let blogtag_id = this.$route.query.blogtag_id;
            let page = this.$route.query.page;
            let params = {
                blogtype_id: blogtype_id,
                blogtag_id: blogtag_id,
            };

            if(page) {
                let page_url = blogs_url + '?page=' + page;
                this.get_blogs(page_url, params);
            }
            else{
                this.get_blogs(blogs_url, params);
            }
        }
    },
    created() {
        this.get_data();    
    },
    watch: {
        //监听路由参数改变
        '$route' (to, from) {
            this.get_data();
        }
    }
};

//博客详情组件
const BlogDetail = {
    template:`
        <div>
            <router-link class="btn float-button-back-list" 
                :to="{ name: 'bloglist', query: { page: fromPage }}">返<br>回</router-link>
            <template v-if="isUpdateOk">            
                <div>
                    <h3 class="blog-title" v-text="blog.title"></h3>
                    <div class="text_center">
                        <span v-if="blog.author">{{ blog.author }}</span>
                        <span class="unobtrusive-text" v-text="blog.create_time"></span>
                    </div>
                </div>
                <br>
                <div class="blog-text" v-html="blog.text"></div>
                <back-top iClass="glyphicon glyphicon-arrow-up" ></back-top>
            </template>
            <p v-else>{{errorMsg}}</p>
        </div>
    `,
    props: {
        id: Number,
    },
    data(){
        return {
            blog:"",
            isUpdateOk: false,
            errorMsg: "",
            fromPage: ""
        }
    },
    methods: {
        get_blog(){
            this.$http.get(blogs_url + this.id)
            .then(response => {
                this.blog = response.data;
                this.isUpdateOk = true;
                // console.log('blog', response.data)
            })
            .catch(error => {
                this.isUpdateOk = false;
                this.errorMsg = error.response.status + ':' +error.response.statusText;
            })
        }
    },
    created(){
        this.fromPage = this.$route.query.page;
        this.get_blog();
    }
};


//分类栏组件
const BlogTypes = {
    template: `
        <div class="blog-type-sidebar">
            <strong>分类</strong>
            <hr class="style-three" />
                <router-link class="btn blogtype-item" :to="{ name: 'bloglist'}">全部</router-link>
            <template v-for="type in blogtypes">
                <router-link class="btn blogtype-item" :to="{ name: 'bloglist', query: { blogtype_id: type.id }}">{{ type.name }}({{ type.blog_count }})</router-link>
            </template>
        </div>
    `,
    data(){
        return {
            blogtypes: {},
            errorMsg: ''
        };
    },
    methods:{
        get_blogtypes(url=blogtypes_url){
            this.$http.get(url)
            .then(response => {
                this.blogtypes = response.data.results;
                this.errorMsg = '';
            })
            .catch(error => {
                this.errorMsg = error.response.status + ':' +error.response.statusText;
            })
        }
    },
    created(){
        this.get_blogtypes();
    }
};


//标签栏组件
const BlogTags = {
    template: `
        <div class="blog-tag-sidebar">
            <strong>标签</strong>
            <hr class="style-three" />
                <router-link class="btn blogtag-item" :to="{ name: 'bloglist'}">全部</router-link>
            <template v-for="tag in blogtags">
                <router-link class="btn blogtag-item" :to="{ name: 'bloglist', query: { blogtag_id: tag.id }}">{{ tag.name }}({{ tag.blog_count }})</router-link>
            </template>
        </div>
    `,
    data(){
        return {
            blogtags: {},
            errorMsg: ''
        };
    },
    methods:{
        get_blogtags(url=blogtags_url){
            this.$http.get(url)
            .then(response => {
                this.blogtags = response.data.results;
                this.errorMsg = '';
            })
            .catch(error => {
                this.errorMsg = error.response.status + ':' +error.response.statusText;
            })
        }
    },
    created(){
        this.get_blogtags();
    }
};


//右侧边栏
const RightSideBar = {
    template: `
        <div class="right-sidebar">
            <blog-types></blog-types>
            <blog-tags></blog-tags>
        </div>
    `,
    components: {
        "blog-types": BlogTypes,
        "blog-tags": BlogTags,
    }
};



//回到顶部组件
const BackTop = {
    template: `
        <div class="back-to-top" @click="backToTop" v-show="showReturnToTop" @mouseenter="show" @mouseleave="hide">
        <i :class="[bttOption.iClass]" :style="{color:bttOption.iColor,'font-size':bttOption.iFontsize}"></i>
        <span class="tips" :class="[bttOption.iPos]" :style="{color:bttOption.textColor}" v-show="showTooltips">{{bttOption.text}}</span>
        </div>
    `,
    props: {
        text: { // 文本提示
            type: String,
            default: ''
        },
        textColor: { // 文本颜色
            type: String,
            default: '#71e2f1'
        },
        iPos: { // 文本位置
            type: String,
            default: 'bottom'
        },
        iClass: { // 图标形状
            type: String,
            default: 'fa fa-chevron-up'
        },
        iColor: { // 图标颜色
            type: String,
            default: '#71e2f1'
        },
        iFontsize: { // 图标大小
            type: String,
            default: '32px'
        },
        pageY: { // 页面滚动多少显示返回按钮
            type: Number,
            default: 300
        },
        transitionName: { // 过渡动画名称
            type: String,
            default: 'linear'
        }
    },
    data () {
        return {
            showTooltips: false,
            showReturnToTop: false
        }
    },
    computed: {
        bttOption () {
            return {
                text: this.text,
                textColor: this.textColor,
                iPos: this.iPos,
                iClass: this.iClass,
                iColor: this.iColor,
                iFontsize: this.iFontsize
            }
            }
    },
    methods: {
        show () { // 显示隐藏提示文字
            return this.showTooltips = true;
        },
        hide () {
            return this.showTooltips = false;
        },
        currentPageYOffset () {
            // 判断滚动区域大于多少的时候显示返回顶部的按钮
            window.pageYOffset > this.pageY ? this.showReturnToTop = true : this.showReturnToTop = false;
        },
        backToTop () {
            scrollIt(0, 500, this.transitionName, this.currentPageYOffset);
        }
    },
    created () {
        window.addEventListener('scroll', this.currentPageYOffset);
    },
    beforeDestroy () {
        window.removeEventListener('scroll', this.currentPageYOffset)
    }
};


function scrollIt(
    destination = 0,
    duration = 200,
    easing = "linear",
    callback
) {
    // define timing functions -- 过渡动效
    let easings = {
        // no easing, no acceleration
        linear(t) {
            return t;
        },
        // accelerating from zero velocity
        easeInQuad(t) {
            return t * t;
        },
        // decelerating to zero velocity
        easeOutQuad(t) {
            return t * (2 - t);
        },
        // acceleration until halfway, then deceleration
        easeInOutQuad(t) {
            return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
        },
        // accelerating from zero velocity
        easeInCubic(t) {
            return t * t * t;
        },
        // decelerating to zero velocity
        easeOutCubic(t) {
            return --t * t * t + 1;
        },
        // acceleration until halfway, then deceleration
        easeInOutCubic(t) {
            return t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1;
        },
        // accelerating from zero velocity
        easeInQuart(t) {
            return t * t * t * t;
        },
        // decelerating to zero velocity
        easeOutQuart(t) {
            return 1 - --t * t * t * t;
        },
        // acceleration until halfway, then deceleration
        easeInOutQuart(t) {
            return t < 0.5 ? 8 * t * t * t * t : 1 - 8 * --t * t * t * t;
        },
        // accelerating from zero velocity
        easeInQuint(t) {
            return t * t * t * t * t;
        },
        // decelerating to zero velocity
        easeOutQuint(t) {
            return 1 + --t * t * t * t * t;
        },
        // acceleration until halfway, then deceleration
        easeInOutQuint(t) {
            return t < 0.5 ? 16 * t * t * t * t * t : 1 + 16 * --t * t * t * t * t;
        }
    };

    // requestAnimationFrame()的兼容性封装：先判断是否原生支持各种带前缀的
    //不行的话就采用延时的方案
    (function() {
        var lastTime = 0;
        var vendors = ["ms", "moz", "webkit", "o"];
        for (var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
            window.requestAnimationFrame =
            window[vendors[x] + "RequestAnimationFrame"];
            window.cancelAnimationFrame =
            window[vendors[x] + "CancelAnimationFrame"] ||
            window[vendors[x] + "CancelRequestAnimationFrame"];
        }

        if (!window.requestAnimationFrame)
        window.requestAnimationFrame = function(callback, element) {
            var currTime = new Date().getTime();
            var timeToCall = Math.max(0, 16 - (currTime - lastTime));
            var id = window.setTimeout(
                function() {
                    callback(currTime + timeToCall);
                }, 
                timeToCall
            );
            lastTime = currTime + timeToCall;
            return id;
        };

        if (!window.cancelAnimationFrame)
            window.cancelAnimationFrame = function(id) {
                clearTimeout(id);
            };
    })();

    function checkElement() {
        // chrome,safari及一些浏览器对于documentElemnt的计算标准化,reset的作用
        document.documentElement.scrollTop += 1;
        let elm = document.documentElement.scrollTop !== 0 ? document.documentElement : document.body;
        document.documentElement.scrollTop -= 1;
        return elm;
    }

    let element = checkElement();
    let start = element.scrollTop; // 当前滚动距离
    let startTime = Date.now(); // 当前时间

    function scroll() { // 滚动的实现
        let now = Date.now();
        let time = Math.min(1, (now - startTime) / duration);
        let timeFunction = easings[easing](time);
        element.scrollTop = timeFunction * (destination - start) + start;

        if (element.scrollTop === destination) {
            callback; // 此次执行回调函数
            return;
        }
        window.requestAnimationFrame(scroll);
    }
    scroll();
}



// 全局组件注册
Vue.component('back-top', BackTop);




// 路由
const router = new VueRouter({
    routes: [
        { path: '/', redirect: '/bloglist/'},//根路由
        { path: '/bloglist/', component: BlogList, name: 'bloglist' },
        { path: '/blog/:id', component: BlogDetail, name: 'blog', props: true },
    ]
});


Vue.prototype.$http = axios;

const app = new Vue({
    router: router,
    data: {
    },
    methods: {
    },
    components: {
        'blog-list': BlogList,
        'blog-detail': BlogDetail,
        'rught-side-bar': RightSideBar,
    },

}).$mount('#app');






