const toggleSidebar = () => {
    const sidebar = document.querySelector(".sidebar");
    sidebar.classList.toggle("sidebar-hidden");
    const shadow = document.querySelector(".fake-shadow");
    shadow.classList.toggle("shadow-show");
};

document.querySelector(".sidebar .close").addEventListener("click", toggleSidebar);
document.querySelector(".show-sidebar").addEventListener("click", toggleSidebar);
document.querySelector(".fake-shadow").addEventListener("click", toggleSidebar);
