	$(document).ready(function() {

		$("div.prettyRadiobuttons").addClass("radiolist");
		$("div.radiolist p").append('<a class="radio-select" href="#">Select</a> <a class="radio-deselect" href="#">Cancel</a>');
		$(".radiolist .radio-select").click(
			function(event) {
				event.preventDefault();
				var $boxes = $(this).parent().parent().children();
				$boxes.removeClass("selected");
				$(this).parent().addClass("selected");
				$(this).parent().find(":radio").attr("checked","checked");
			}
		);

		$(".radiolist .radio-deselect").click(
			function(event) {
				event.preventDefault();
				$(this).parent().removeClass("selected");
				$(this).parent().find(":radio").removeAttr("checked");
			}
		);
	});

	var Paginator = {
		jumpToPage: function(pages) {
			var page = prompt("Enter a number between 1 and " + pages + " to jump to that page", "");
			if (page != undefined){
            page = parseInt(page, 10)
            if (!isNaN(page) && page > 0 && page <= pages){
					window.location.href = "?page=" + page;
				}
			}
		}
	};

	var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
	document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
	try {
		var pageTracker = _gat._getTracker("UA-406217-10");
		pageTracker._trackPageview();
	} catch(err) {}
                  
