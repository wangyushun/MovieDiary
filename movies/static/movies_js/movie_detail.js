$comment_form = $('#comment_form')
$comment_form.on('submit', function(event){
	event.preventDefault();
	for (instance in CKEDITOR.instances) {
		CKEDITOR.instances[instance].updateElement();
	}
	let text = CKEDITOR.instances['id_comment'].document.getBody().getText().trim(); //取得纯文本 ;
	if (text == '') {
		$('#comment-error').text("评论内容不能为空");
		CKEDITOR.instances['id_comment'].setData('');
		return;
	}
	else{
		$('#comment-error').text("");
	}

	$.ajax({
		url: $comment_form.attr('action'),
		type: "POST",//$comment_form.attr('method'),
		cache: false,
		data: $comment_form.serialize(),
		success: function(data){
			//评论内容插入到评论区
			let comment_html = 
				`<div class="comment-item">
					<span>
						<span class="comment-user">${data.username} </span>
						<span>${data.time}</span>
					</span>                     
					<p>${data.context}</p>
				</div>`;
			$('#comment-section').prepend(comment_html);
			for (instance in CKEDITOR.instances) {
				CKEDITOR.instances[instance].setData('');
			}
		},
		error: function(err){
			$('#comment-error').text(err.error_text);
		}
	})
});






