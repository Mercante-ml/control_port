document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.querySelector('aside');
    const main = document.querySelector('main');

    if (menuToggle) {
        menuToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            sidebar.classList.toggle('active');
        });
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 768 && sidebar.classList.contains('active')) {
            if (!sidebar.contains(e.target) && e.target !== menuToggle) {
                sidebar.classList.remove('active');
            }
        }
    });

    // Filter Logic
    const searchInput = document.getElementById('searchInput');
    const filterChips = document.querySelectorAll('.filter-chip');
    const projectCards = document.querySelectorAll('.project-card');

    function filterContent() {
        const searchTerm = searchInput.value.toLowerCase();
        const activeFilter = document.querySelector('.filter-chip.active').dataset.filter;

        projectCards.forEach(card => {
            const projectName = card.dataset.name;
            const rows = card.querySelectorAll('.service-row');
            let hasVisibleService = false;

            rows.forEach(row => {
                const serviceType = row.dataset.type;
                const port = row.dataset.port;
                const matchesSearch = projectName.includes(searchTerm) || port.includes(searchTerm);
                const matchesFilter = activeFilter === 'all' || serviceType === activeFilter;

                if (matchesSearch && matchesFilter) {
                    row.style.display = '';
                    hasVisibleService = true;
                } else {
                    row.style.display = 'none';
                }
            });

            // Hide project card if no services match
            card.style.display = hasVisibleService ? '' : 'none';
        });
    }

    if (searchInput) {
        searchInput.addEventListener('input', filterContent);
    }

    filterChips.forEach(chip => {
        chip.addEventListener('click', () => {
            filterChips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            filterContent();
        });
    });

    console.log("Port Control Dashboard Loaded with Search and Filters");
});
