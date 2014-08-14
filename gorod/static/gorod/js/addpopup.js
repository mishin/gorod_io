(window.addPopup = function(e){

	var $popup = $('.b-popup-add'),
	$window = $popup.find('.b-popup__window'),
	$addBtn = $('.b-header__add'),
	$overlay = $popup.find('.b-popup__overlay'),
    $addList = $('.b-header__add-list'),
    $wrapper = $window.find('#b-form__wrapper'),
	shownClass = 'b-popup_shown',
    formAjaxUrls = window.getEnv('formAjaxUrls'),
    name,
    $previewTools;

	$addBtn.on('click',function(e){
		$addList.addClass('active');
	});
    $(document).on('click',function(e){
        if( ! $(e.target).hasClass('b-header__add') ){
            $addList.removeClass('active');
        }
    });

    $addList.find('li').on('click',function(e){
        name  = $(this).attr('data-name'),
        title = $(this).attr('data-title');
        $wrapper.html(''); 
        $wrapper.attr('class','').addClass('b-form__wrapper_'+name);
        $.get(formAjaxUrls[name], function(html){
            $wrapper.html(html); 
            $wrapper.find('#id_title').attr('placeholder', 'Заголовок');
            $wrapper.find('.b-form__type span').text(title);
        });
        $popup.addClass(shownClass);
        $overlay.height($('body').outerHeight());
    });



    $window.on('submit', 'form', function(e){
        e.preventDefault();

        var data = new FormData($window.find('form')[0]),
        Deferred = $.ajax({
            url: formAjaxUrls[name],
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            type: 'POST'
        });

        $window.find('form>div').removeClass('error');
        $('.b-form__error').remove();

        Deferred.done(function(json){
            //$window.html(html);
            var $elem;
            if(!json.success){
            	$.each(json.errors,function(index, elem){
                    if(elem[0]=='picture'){
                        $elem = $window.find('.b-form__preview-wrapper');
                    }else{
                        $elem = $window.find('[name="'+elem[0]+'"]').closest('div');
                    }
                    $elem.addClass('error');
            		$.each(elem[1],function(index, errorText){
            			$('<span/>').addClass('b-form__error').text(errorText).appendTo($elem);
            		});
            	});
            }else{
                var okText = $('<div />').addClass('b-form__ok').text('Ваше сообщение будет добавлено после модерации');
            	$wrapper.html(okText).append('<i class="b-form__close"></i>');
            }
        });

    });

	$overlay.on('click',function(){
		$popup.removeClass(shownClass);
	});

	$(document).keydown(function(e) {
	    if( e.keyCode === 27 ) {
	        $popup.removeClass(shownClass);
	        return false;
	    }
	});
    $window.on('click', '.b-form__close', function(){
        $popup.removeClass(shownClass);
    });


	/*previw*/
	$window.on('click', '.b-form__preview, .b-form__change-preview', function(){
		$('.b-form__picture input').click();
	});
    $window.on('click', '.b-form__del-preview', function(){
        $('.b-form__preview').attr('style','');
        $('.b-form__picture input').val('');
    });
	$window.on('change', '.b-form__picture input', function(){
        var files = !!this.files ? this.files : [];
        if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support
 
        if (/^image/.test( files[0].type)){ // only image file
            var reader = new FileReader(); // instance of the FileReader
            reader.readAsDataURL(files[0]); // read the local file
 
            reader.onloadend = function(){ // set image data as background of div
                $('.b-form__preview').css("background-image", "url("+this.result+")");

                $previewTools = $popup.find('.b-form__preview-tools');
                $previewTools.addClass('b-form__preview-tools_active');
            }
        }
    });

});
