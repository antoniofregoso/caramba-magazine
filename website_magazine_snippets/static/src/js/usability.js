
//filter functions

// bind filter button click
var $grid = $('.grid')
$('.filters-button-group').on( 'click', 'button', function() {
  var filterValue = $( this ).attr('data-filter');
  // use filterFn if matches value
  $grid.isotope({ filter: filterValue });
});

//bind sort button click
$('.sort-by-button-group').on( 'click', 'button', function() {
  var sortValue = $(this).attr('data-sort-value');
  $grid.isotope({ sortBy: sortValue });
});

//change is-checked class on buttons
$('.btn-group').each( function( i, btnGroup ) {
  var $btnGroup = $( btnGroup );
  $btnGroup.on( 'click', 'button', function() {
    $btnGroup.find('.active').removeClass('active');
    $( this ).addClass('.active');
  });
});