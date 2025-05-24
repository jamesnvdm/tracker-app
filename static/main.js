document.getElementById('meal-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const meal = document.getElementById('meal').value;

    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ meal: meal })
    });

    const data = await response.json();
    document.getElementById('response').textContent = JSON.stringify(data, null, 2);
});
