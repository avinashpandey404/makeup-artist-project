const bookingForm = document.getElementById('bookingForm');

bookingForm.addEventListener('submit', async (e) => {

    e.preventDefault();

    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        date: document.getElementById('date').value,
        service: document.getElementById('service').value
    };

    console.log(data);

    alert('Booking Submitted Successfully');

    // Replace later with backend API

    // fetch('YOUR_BACKEND_API', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(data)
    // })

});
