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
		}
		if (currentSectionIndex === 1) {
			if (incomeTotal && !incomeTotal.value) {
				alert("Please tell us your income!");
				return false;
			} else if (debtTotal && !debtTotal.value) {
				alert("Please tell us your debt amount!");
				return false;
			}
		}
		currentSection.removeClass("is-active").next().addClass("is-active");
		headerSection.removeClass("is-active").next().addClass("is-active");

		if (currentSectionIndex === 9) {
			$(document).find(".form-wrapper .section").first().addClass("is-active");
			$(document).find(".steps li").first().addClass("is-active");
		}
	});
});
