document.addEventListener("DOMContentLoaded", () => {

    loadDashboard();

});


async function loadDashboard() {

    const token =
        localStorage.getItem("access_token");

    if (!token) {
        return;
    }


    try {

        const response = await fetch(
            "/auth/me",
            {
                method: "GET",

                headers: {
                    "Authorization":
                        `Bearer ${token}`
                }
            }
        );


        if (!response.ok) {

            localStorage.removeItem(
                "access_token"
            );

            window.location.href = "/login";

            return;
        }


        const user = await response.json();


        console.log(
            "Current user:",
            user
        );


        displayUser(user);

        buildNavigation(user);


    } catch (error) {

        console.error(
            "Failed to load user:",
            error
        );

    }

}


function displayUser(user) {

    document.getElementById(
        "userName"
    ).textContent =
        user.user_name;


    document.getElementById(
        "welcomeMessage"
    ).textContent =
        `Welcome, ${user.user_name}`;


    document.getElementById(
        "profileUsername"
    ).textContent =
        user.user_name;


    document.getElementById(
        "profileEmail"
    ).textContent =
        user.user_email;


    document.getElementById(
        "profileRole"
    ).textContent =
        user.role_name || "No role";


    document.getElementById(
        "profileApproved"
    ).textContent =
        user.is_approved ? "YES" : "NO";


    document.getElementById(
        "profileActive"
    ).textContent =
        user.is_active ? "YES" : "NO";

}


function buildNavigation(user) {

    const nav =
        document.getElementById(
            "sidebarNav"
        );


    nav.innerHTML = "";


    addNavigationLink(
        nav,
        "Dashboard",
        "/dashboard"
    );


    addNavigationLink(
        nav,
        "My Profile",
        "/employees/me"
    );


    if (
        user.role_name === "Admin" ||
        user.role_name === "HR" ||
        user.role_name === "Manager"
    ) {

        addNavigationLink(
            nav,
            "Employees",
            "/employees"
        );

    }


    if (
        user.role_name === "Admin" ||
        user.role_name === "HR"
    ) {

        addNavigationLink(
            nav,
            "Add Employee",
            "/employees/create"
        );

    }


    if (user.role_name === "Admin") {

        addNavigationLink(
            nav,
            "Pending Users",
            "/admin/pending-users"
        );

    }

}


function addNavigationLink(
    nav,
    text,
    url
) {

    const link =
        document.createElement("a");

    link.textContent = text;

    link.href = url;

    nav.appendChild(link);

}


document
    .getElementById("logoutButton")
    ?.addEventListener(
        "click",
        () => {

            localStorage.removeItem(
                "access_token"
            );

            window.location.href =
                "/login";

        }
    );