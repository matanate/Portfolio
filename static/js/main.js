document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector("header");
  const headerToggleBtn = document.getElementById("toggleHeaderBtn");
  const headerBtnIcon = headerToggleBtn.querySelector("i");

  function updateHeaderVisibility() {
    if (window.innerWidth < 1200) {
      header.classList.add("hidden");
    } else {
      header.classList.remove("hidden");
    }
  }
  updateHeaderVisibility();
  // Update visibility on window resize
  window.addEventListener("resize", updateHeaderVisibility);

  headerToggleBtn.addEventListener("click", function () {
    header.classList.toggle("hidden");
    if (headerBtnIcon.classList.contains("bi-list")) {
      headerBtnIcon.classList.remove("bi-list");
      headerBtnIcon.classList.add("bi-x");
    } else {
      headerBtnIcon.classList.remove("bi-x");
      headerBtnIcon.classList.add("bi-list");
    }
  });

  // set nav-item class to nav-item-active when the section top is above the center of the viewport and under the top of the viewport
  function scrollPosition() {
    const sections = document.querySelectorAll("section");
    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionBottom = sectionTop + section.clientHeight;
      const sectionCenter = sectionTop + section.clientHeight / 2;
      const viewportCenter = window.scrollY + window.innerHeight / 2;
      const navLink = document.querySelector(
        `.nav-link[href='#${section.id}']`
      );

      if (sectionTop < viewportCenter && sectionBottom >= viewportCenter) {
        navLink.classList.add("nav-item-active");
      } else {
        navLink.classList.remove("nav-item-active");
      }
    });
  }
  scrollPosition();
  window.addEventListener("scroll", scrollPosition);

  // Add click event listeners to filter options
  var filterOptions = document.querySelectorAll("#portfolio-filters li");
  filterOptions.forEach(function (option) {
    option.addEventListener("click", function () {
      var filterValue = this.getAttribute("data-filter");
      filterPortfolioItems(filterValue);
      // Remove 'filter-active' class from all options and add it to the clicked one
      filterOptions.forEach(function (el) {
        el.classList.remove("filter-active");
      });
      this.classList.add("filter-active");
    });
  });

  function filterPortfolioItems(filter) {
    var portfolioItems = document.querySelectorAll(".portfolio-item");
    portfolioItems.forEach(function (item) {
      var itemFilters = item.classList;
      if (filter === "*" || itemFilters.contains(filter)) {
        item.style.display = "block";
        item.classList.remove("fade-out");
        item.classList.add("fade-in");
      } else {
        item.classList.remove("fade-in");
        item.classList.add("fade-out");
        setTimeout(function () {
          item.style.display = "none";
        }, 500); // Adjust the duration of the fade-out transition
      }
    });
  }
});
