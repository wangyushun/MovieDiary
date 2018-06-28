// 定义一个名为 button-counter 全局组件
Vue.component('button-counter', {
	template: '<button @click="on_click">You clicked me {{ count }} times.</button>',
  	data: function () {
	    return {
	       count: this.count_init,
	    }
  	},
  	props: ['count_init'],
  	methods: {
  		on_click: function () {
  			this.count++;
  			this.$emit('click_count', {count: this.count});
  		} 
  	},
});


var mycomp = {
	template: `
		<div>
			<input type="text" v-model="input_str" placeholder="请输入"/>
			<p>你输入的内容是：{{input_str}}</p>
			<input type="button" @click="on_click" value="click"/>
			<button-counter  v-show="isshow" count_init="6" @click_count="on_click_count"></button-counter>
		</div>
	`,
	data() {
		return {
			input_str: "",
			isshow: false,
		}
	},
	methods: {
		on_click() {
			if(this.isshow){
				this.isshow = false;
			}else{
				this.isshow = true;
			}
		},
		on_click_count(data) {
			console.log('count', data.count);
		}
	}
};

var app = new Vue({
	el:"#app",
	data: {
		msg: "666",
	},
	methods: {
		onClick: function(){
			alert('点到我了');
		},
	},
	components: {
		mycomp: mycomp,
	} 
});
