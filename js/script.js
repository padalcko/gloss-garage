const WEBHOOK_URL = "https://padalko.app.n8n.cloud/webhook/gloss-garage";

const leadForm = document.getElementById("leadForm");
const formStatus = document.getElementById("formStatus");

if (leadForm) {
  leadForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(leadForm);

    const leadData = {
      name: formData.get("name"),
      phone: formData.get("phone"),
      email: formData.get("email"),
      message: formData.get("message"),
      source: "Gloss Garage Landing",
      page: window.location.href,
      createdAt: new Date().toISOString(),
    };

    formStatus.textContent = "Wysyłamy zgłoszenie...";

    try {
      const response = await fetch(WEBHOOK_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(leadData),
      });

      if (!response.ok) {
        throw new Error("Webhook error");
      }

      formStatus.textContent = "Dziękujemy! Wkrótce się z Tobą skontaktujemy.";
      leadForm.reset();
    } catch (error) {
      console.error(error);
      formStatus.textContent = "Błąd wysyłki. Napisz do nas na WhatsApp.";
    }
  });
}