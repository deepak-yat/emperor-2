async function protectPage() {

    const token = localStorage.getItem("access_token");

    // No token → login
    if (!token) {
        window.location.replace("/login");
        return;
    }

    try {

        const response = await fetch("/auth/me", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        // Invalid or expired token
        if (!response.ok) {
            localStorage.removeItem("access_token");
            window.location.replace("/login");
            return;
        }

        const user = await response.json();

        console.log("Authenticated user:", user);

        window.currentUser = user;

        // Get role from backend
        const role = (
            user.role_name ||
            user.role ||
            ""
        ).toLowerCase();

        const path = window.location.pathname;

        console.log("Role:", role);
        console.log("Path:", path);

        // Add Employee page
        if (
            path === "/employees/create-page" &&
            role !== "admin" &&
            role !== "hr"
        ) {
            window.location.replace("/dashboard");
            return;
        }

        // Admin dashboard
        if (
            path === "/dashboard/admin" &&
            role !== "admin"
        ) {
            window.location.replace("/dashboard");
            return;
        }

        // HR dashboard
        if (
            path === "/dashboard/hr" &&
            role !== "hr"
        ) {
            window.location.replace("/dashboard");
            return;
        }

        // Manager dashboard
        if (
            path === "/dashboard/manager" &&
            role !== "manager"
        ) {
            window.location.replace("/dashboard");
            return;
        }

        // Employee dashboard
        if (
            path === "/dashboard/employee" &&
            role !== "employee"
        ) {
            window.location.replace("/dashboard");
            return;
        }

    } catch (error) {

        console.error(
            "Authentication error:",
            error
        );

        localStorage.removeItem("access_token");
        window.location.replace("/login");
    }
}

protectPage();