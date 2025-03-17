document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('packing-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            const inputs = form.querySelectorAll('input');
            let valid = true;
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    valid = false;
                    input.style.borderColor = '#e74c3c';
                } else {
                    input.style.borderColor = '#ddd';
                }
            });
            if (!valid) {
                e.preventDefault();
                alert('Please fill in all fields!');
            }
        });
    }
});