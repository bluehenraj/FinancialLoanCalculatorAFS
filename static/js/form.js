$(document).ready(function () {

	$(".form-wrapper div.button").click(function () {
		var button = $(this);
		var currentSection = button.parents(".section");
		var currentSectionIndex = currentSection.index();
		var headerSection = $('.steps li').eq(currentSectionIndex);
		var firstName = document.getElementById("firstname");
		var lastName = document.getElementById("lastname");
		var incomeTotal = document.getElementById("incomeTotal");
		var debtTotal = document.getElementById("debtTotal");
		if (currentSectionIndex === 0) {
			if (firstName && !firstName.value) {
				alert("Please tell us your first name!");
				return false;
			} else if (lastName && !lastName.value) {
				alert("Please tell us your last name!");
				return false;
			}
			document.getElementById("tips").innerHTML = "Filling out the information as accurately as possible can give you the best quote!";
		}
		else if (currentSectionIndex === 1) {
			if (incomeTotal && !incomeTotal.value) {
				alert("Please tell us your income!");
				return false;
			} else if (debtTotal && !debtTotal.value) {
				alert("Please tell us your debt amount!");
				return false;
			}
			document.getElementById("tips").innerHTML = "2 in 10 Americans spend at least 50% of their monthly income on debt repayment.";
		}
		else if (currentSectionIndex === 2) {
			document.getElementById("tips").innerHTML = "21% of households do not read their bills carefully.";
		}
		else if (currentSectionIndex === 3) {
			document.getElementById("tips").innerHTML = "United States citizens spent a total of 3.6 trillion in 2019 on their healthcare.";
		}
		else if (currentSectionIndex === 4) {
			document.getElementById("tips").innerHTML = "The rise in food prices has pushed 44 million people into poverty since 2010.";
		}
		else if (currentSectionIndex === 5) {
			document.getElementById("tips").innerHTML = "The average American's car payment is a whopping $545 per month.";
		}
		else if (currentSectionIndex === 6) {
			document.getElementById("tips").innerHTML = "You're almost done!";
		}
		else if (currentSectionIndex === 7) {
			document.getElementById("tips").innerHTML = "American Financial Solutions has plenty of programs to help!";
		}
		currentSection.removeClass("is-active").next().addClass("is-active");
		headerSection.removeClass("is-active").next().addClass("is-active");

		if (currentSectionIndex === 8) {
			$(document).find(".form-wrapper .section").first().addClass("is-active");
			$(document).find(".steps li").first().addClass("is-active");
		}
		bounce($('.tipman'));
	});
	$('.one form .btn').on('click', function () {
		$(this).parents('.one').animate({
			top: '-500px'
		}, 500);

		$(this).parents('.one').siblings('.two').
			animate({
				top: '0px'
			}, 500);
		return false;
	});

	$('.two .close').on('click', function () {
		$(this).parent().animate({
			top: '-500px'
		}, 500);

		$(this).parent().siblings('.one').animate({
			top: '0px'
		}, 500);
		return false;
	});
});

function bounce(thing) {
	var interval = 100;
	var distance = 20;
	var times = 6;
	var damping = 0.8;

	for (var i = 0; i < (times + 1); i++) {
		var amt = Math.pow(-1, i) * distance / (i * damping);
		$(thing).animate({
			top: amt
		}, 100);
	}
	$(thing).animate({
		top: 0
	}, interval);
}