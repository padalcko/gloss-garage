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
      message: formData.get("message"),
      source: "Gloss Garage Landing",
      page: window.location.href,
      createdAt: new Date().toISOString(),
    };

    formStatus.textContent = "Відправляємо заявку...";

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

      formStatus.textContent = "Дякуємо! Ми скоро звʼяжемось з вами.";
      leadForm.reset();
    } catch (error) {
      console.error(error);
      formStatus.textContent = "Помилка відправки. Напишіть нам у Telegram.";
    }
  });
}