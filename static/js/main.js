document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });

    // Form validation
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

    const tables = document.querySelectorAll('table');
    tables.forEach(function(table) {
        const headerCells = table.querySelectorAll('th');
        const dataCells = table.querySelectorAll('td');

        dataCells.forEach(function(cell, index) {
            cell.setAttribute('data-label', headerCells[index % headerCells.length].textContent);
        });
    });

    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        function toggleMenu() {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        }

        hamburger.addEventListener('click', toggleMenu);

        const navLinksItems = navLinks.querySelectorAll('li a');
        navLinksItems.forEach(item => {
            item.addEventListener('click', (e) => {
                if (navLinks.classList.contains('active')) {
                    e.stopPropagation(); // Prevent the click from bubbling up
                    toggleMenu();
                }
            });
        });

        document.addEventListener('click', (e) => {
            if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
            }
        });
    }
});