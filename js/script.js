const WEBHOOK_URL = "https://padalko.app.n8n.cloud/webhook/gloss-garage";

const leadForm = document.getElementById("leadForm");
const formStatus = document.getElementById("formStatus");

const pageLanguage = document.documentElement.lang || "pl";

const formMessages = {
  pl: {
    sending: "Wysyłamy zgłoszenie...",
    success: "Dziękujemy! Wkrótce się z Tobą skontaktujemy.",
    error: "Błąd wysyłki. Napisz do nas na WhatsApp."
  },

  ru: {
    sending: "Отправляем заявку...",
    success: "Спасибо! В ближайшее время мы с вами свяжемся.",
    error: "Ошибка отправки. Напишите нам в WhatsApp."
  }
};

const messages = formMessages[pageLanguage] || formMessages.pl;


if (leadForm && formStatus) {

  leadForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const formData = new FormData(leadForm);

    const leadData = {
      name: formData.get("name"),
      phone: formData.get("phone"),
      email: formData.get("email"),
      message: formData.get("message"),

      language: pageLanguage,

      source: "Gloss Garage Landing",
      page: window.location.href,
      createdAt: new Date().toISOString()
    };


    formStatus.textContent = messages.sending;


    try {

      const response = await fetch(WEBHOOK_URL, {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify(leadData)
      });


      if (!response.ok) {
        throw new Error("Webhook error");
      }


      formStatus.textContent = messages.success;

      leadForm.reset();


    } catch (error) {

      console.error(error);

      formStatus.textContent = messages.error;

    }

  });

}