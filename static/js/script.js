document.addEventListener('DOMContentLoaded', () => {
    // Handle candidate form submission
    const candidateForm = document.getElementById('candidateForm');
    if (candidateForm) {
        candidateForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(candidateForm);
            const response = await fetch('/candidates', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            alert(result.message);
            location.reload();
        });
    }

    // Handle query form submission
    const queryForm = document.getElementById('queryForm');
    if (queryForm) {
        queryForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(queryForm);
            const response = await fetch('/employee_support', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            alert(result.response);
            location.reload();
        });
    }
});