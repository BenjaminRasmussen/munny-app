/**
 * jTinder initialization
 */

$("#tinderslide").jTinder({
    onDislike: function (item) {
    	// EVENT CALLS TO HERE
    },
    onLike: function (item) {
		//EVENT CALLS TO HERE
   },
	animationRevertSpeed: 150,
	animationSpeed: 350,
	threshold: 1.5,
	likeSelector: '.like',
	dislikeSelector: '.dislike'
});


/*
$("#tinderslide").jTinder({
    onDislike: function (item) {
        alert('Dislike image ' + (item.index()+1));
    },
    onLike: function (item) {
        alert('Like image ' + (item.index()+1));
    },
    animationRevertSpeed: 200,
    animationSpeed: 400,
    threshold: 1,
    likeSelector: '.like',
    dislikeSelector: '.dislike'
}); */