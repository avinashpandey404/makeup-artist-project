const bookingForm = document.getElementById("bookingForm");

bookingForm.addEventListener("submit", async function (e) {

    e.preventDefault();

    const responseMessage = document.getElementById("responseMessage");

    responseMessage.innerHTML = "Booking Processing...";

    const formData = {

        name: document.getElementById("name").value,

        email: document.getElementById("email").value,

        phone: document.getElementById("phone").value,

        service: document.getElementById("service").value,

        appointment_date: document.getElementById("appointment_date").value,

        message: document.getElementById("message").value
    };

    try {

        const response = await fetch(
            "http://YOUR-ALB-DNS/api/bookings",
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(formData)
            }
        );

        const result = await response.json();

        if (response.ok) {

            responseMessage.innerHTML =
                "✅ Booking Successful! We will contact you soon.";

            bookingForm.reset();

        } else {

            responseMessage.innerHTML =
                "❌ Booking Failed!";
        }

    } catch (error) {

        responseMessage.innerHTML =
            "❌ Server Error!";
    }
});
