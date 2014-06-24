(window.getEnv = function(var_name, default_value) {
    if(typeof(globals[var_name]) != 'undefined') {
        return globals[var_name];
    }

    if(typeof(default_value) != 'undefined') {
        return default_value;
    }

    return;
});

(window.menu = function(){
	var $btn = $('.b-header__menu-btn'),
		$header = $('.b-header'),
		$menu = $('.b-header__menu'),
		$topLine = $('.b-header__content'),
		$content = $('.b-js-content');

	$btn.on('click', function(e){
		$header.toggleClass('active');
		return false;
	});

	$topLine.on('click',function(e){
		var time = setTimeout(function(){
			if($header.hasClass('active') && !$(e.target).hasClass('b-header__city') ){
				$header.removeClass('active');
			}
		},50)
	});
	
});

(window.topScrolling = function(){
	var $topLine = $('.b-header__content'),
	$header = $('.b-header'),
	$menu = $('.b-header__menu');

	$('.b-header__avatar').on('click',function(e){
		e.stopPropagation();
	})
	$topLine.on('click',function(e){
		if(!$header.hasClass('active') && !$(e.target).hasClass('b-header__city')){
			$('body').animate({scrollTop:0},300);
		}
	});
});

(window.grid = function(){
	$('.b-feed__list').imagesLoaded( function() {
		$('.b-feed__list').masonry({
			columnWidth: '.grid-sizer',
			itemSelector: '.b-feed-item',
			gutter : '.gutter-sizer',
			transitionDuration: 0
		});
	});
	$('.b-orgs__list').masonry({
		columnWidth: '.grid-sizer',
		itemSelector: '.b-orgs__item',
		gutter : '.gutter-sizer',
		transitionDuration: 0
	});
});

$(function(){
	
	
	window.grid();
	window.addPopup();
	window.menu();
	window.topScrolling();

});