frappe.ui.pages['help'].on_page_load = function(wrapper) {
    // Hide the Help menu
    frappe.provide('frappe.help');
    frappe.help.set_help_menu = () => {};
}
