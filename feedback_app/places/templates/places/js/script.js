document.addEventListener("DOMContentLoaded", function () {
  // Handle dynamic form updates
  const stateSelect = document.querySelector('select[name="state"]');
  const citySelect = document.querySelector('select[name="city"]');

  if (stateSelect && citySelect) {
    stateSelect.addEventListener("change", function () {
      const selectedState = this.value;

      // Clear current city options
      citySelect.innerHTML = '<option value="">Select City</option>';

      if (selectedState) {
        // Fetch cities for selected state
        fetch(`/api/cities/?state=${selectedState}`)
          .then((response) => response.json())
          .then((cities) => {
            cities.forEach((city) => {
              const option = document.createElement("option");
              option.value = city;
              option.textContent = city;
              citySelect.appendChild(option);
            });
          });
      }
    });
  }

  // Handle star rating
  const ratingInputs = document.querySelectorAll(".star-rating input");
  const ratingValue = document.querySelector("#rating-value");

  if (ratingInputs.length && ratingValue) {
    ratingInputs.forEach((input) => {
      input.addEventListener("change", function () {
        ratingValue.textContent = this.value;
      });
    });
  }

  // Image preview for place images
  const imageInput = document.querySelector('input[type="file"]');
  const imagePreview = document.querySelector("#image-preview");

  if (imageInput && imagePreview) {
    imageInput.addEventListener("change", function () {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          imagePreview.src = e.target.result;
          imagePreview.style.display = "block";
        };
        reader.readAsDataURL(file);
      }
    });
  }

  // Form validation
  const reviewForm = document.querySelector("#review-form");
  if (reviewForm) {
    reviewForm.addEventListener("submit", function (e) {
      const rating = document.querySelector('input[name="rating"]:checked');
      const text = document.querySelector('textarea[name="text"]');

      if (!rating) {
        e.preventDefault();
        alert("Please select a rating");
        return;
      }

      if (!text.value.trim()) {
        e.preventDefault();
        alert("Please write a review");
        return;
      }
    });
  }

  // Lazy loading for images
  const images = document.querySelectorAll("img[data-src]");
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute("data-src");
        observer.unobserve(img);
      }
    });
  });

  images.forEach((img) => imageObserver.observe(img));

  // Filter form reset
  const resetButton = document.querySelector("#reset-filters");
  if (resetButton) {
    resetButton.addEventListener("click", function (e) {
      e.preventDefault();
      document
        .querySelectorAll(".filter-form select, .filter-form input")
        .forEach((input) => {
          input.value = "";
        });
      document.querySelector(".filter-form").submit();
    });
  }

  // Smooth scroll to reviews
  const reviewLinks = document.querySelectorAll('a[href="#reviews"]');
  reviewLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      document.querySelector("#reviews").scrollIntoView({
        behavior: "smooth",
      });
    });
  });
});
