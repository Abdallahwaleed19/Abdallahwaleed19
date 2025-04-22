// Scroll animations with Intersection Observer
document.addEventListener('DOMContentLoaded', function () {
    // Animate elements when they come into view using Intersection Observer
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate__animated', 'animate__fadeInUp');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });

    // Book checkout animation
    const checkoutButtons = document.querySelectorAll('.checkout-btn');
    checkoutButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();

            const bookCard = this.closest('.book-card');

            // Optional ripple animation
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            ripple.style.left = `${e.offsetX}px`;
            ripple.style.top = `${e.offsetY}px`;
            this.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);

            // Card fade out and status update
            bookCard.classList.add('animate__animated', 'animate__fadeOut');

            setTimeout(() => {
                const availability = bookCard.querySelector('.availability');
                availability.textContent = 'Checked Out';
                availability.classList.remove('bg-success');
                availability.classList.add('bg-danger');

                bookCard.classList.remove('animate__fadeOut');
                bookCard.classList.add('animate__fadeIn');

                showNotification('Book checked out successfully!', 'success');
            }, 500);
        });
    });

    // Show notification
    function showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `notification alert alert-${type} animate__animated animate__fadeInRight`;
        notification.textContent = message;

        const notificationContainer = document.getElementById('notification-container') ||
            (() => {
                const container = document.createElement('div');
                container.id = 'notification-container';
                container.style.position = 'fixed';
                container.style.top = '20px';
                container.style.right = '20px';
                container.style.zIndex = '9999';
                document.body.appendChild(container);
                return container;
            })();

        notificationContainer.appendChild(notification);

        setTimeout(() => {
            notification.classList.remove('animate__fadeInRight');
            notification.classList.add('animate__fadeOutRight');

            setTimeout(() => {
                notification.remove();
            }, 600);
        }, 3000);
    }
});
