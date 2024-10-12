// Add event listeners when the document is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });

    // Add form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(function(field) {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });

            if (!isValid) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });

    // Add responsive table functionality
    const tables = document.querySelectorAll('table');
    tables.forEach(function(table) {
        const headerCells = table.querySelectorAll('th');
        const dataCells = table.querySelectorAll('td');

        // Add data-label attribute to cells for responsive display
        dataCells.forEach(function(cell, index) {
            cell.setAttribute('data-label', headerCells[index % headerCells.length].textContent);
        });
    });
});
