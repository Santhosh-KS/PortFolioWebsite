let translations = {}; // Object to hold loaded translations
let currentLanguage = "en"; // Default language

async function loadTranslations() {
  try {
    const [enResponse, deResponse] = await Promise.all([
      fetch("en.json"),
      fetch("de.json"),
    ]);

    const enData = await enResponse.json();
    const deData = await deResponse.json();

    translations = {
      en: enData,
      de: deData,
    };
    console.log("Translations loaded:", translations);
    updateContent(); // Update content after translations are loaded
  } catch (error) {
    console.error("Failed to load translations:", error);
  }
}

function updateContent() {
  document.querySelectorAll("[data-key]").forEach((element) => {
    const key = element.getAttribute("data-key");
    if (translations[currentLanguage] && translations[currentLanguage][key]) {
      element.innerHTML = translations[currentLanguage][key];
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  loadTranslations(); // Start loading translations when the DOM is ready

  // Language selector logic
  const languageSelector = document.getElementById("language-selector");
  if (languageSelector) {
    languageSelector.addEventListener("change", (event) => {
      currentLanguage = event.target.value;
      updateContent();
    });
  }

  // Tab functionality for Tools section
  window.openTab = function (evt, tabName) {
    let i, tabcontent, tabbuttons;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tabbuttons = document.getElementsByClassName("tab-button");
    for (i = 0; i < tabbuttons.length; i++) {
      tabbuttons[i].className = tabbuttons[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  };

  // Make the first tab active by default, but only after translations are loaded
  // This will be handled by the updateContent() call within loadTranslations()
  // For initial display, you might want to call openTab with a default value here
  // after `loadTranslations()` finishes. Or, ensure your initial `style.css`
  // hides all but the default tab.
  document.querySelector(".tab-button").click();

  // Smooth scrolling for navigation links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();

      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth",
      });
    });
  });

  // Contact Form Submission
  const contactForm = document.getElementById("contact-form");
  const formMessage = document.getElementById("form-message");

  if (contactForm) {
    contactForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      // Simulate form submission
      formMessage.classList.remove("success", "error");
      formMessage.style.display = "block";
      formMessage.textContent = "Sending message...";

      // In a real application, you would send this data to a server
      // For example:
      // const formData = new FormData(contactForm);
      // const response = await fetch('/api/contact', {
      //     method: 'POST',
      //     body: formData
      // });
      // const result = await response.json();

      setTimeout(() => {
        const success = Math.random() > 0.5; // Simulate success or failure

        if (success) {
          formMessage.textContent = "Message sent successfully!";
          formMessage.classList.add("success");
          contactForm.reset();
        } else {
          formMessage.textContent = "Failed to send message. Please try again.";
          formMessage.classList.add("error");
        }
      }, 2000); // Simulate network delay
    });
  }
});
