document.getElementById('dataForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const value1 = document.getElementById('value1').value;
    const value2 = document.getElementById('value2').value;
    const resultMessage = document.getElementById('resultMessage');

    if (value1 && value2) {
        console.log('Values:', value1, value2);
        try {
            const response = await fetch('http://34.122.90.96:5000/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ value1, value2 })
            });
            const result = await response.json();
            console.log('Response from backend:', result);

            // Display the result message
            resultMessage.textContent = result.message || 'Unexpected response';
            resultMessage.style.color = 'green';
        } catch (error) {
            console.error('Error:', error);

            // Display error message
            resultMessage.textContent = 'Error submitting data';
            resultMessage.style.color = 'red';
        }
    } else {
        alert('Please fill in both values');
    }
});
