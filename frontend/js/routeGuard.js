async function protectPage() {

    const token = localStorage.getItem("access_token");

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

        if (!response.ok) {
            localStorage.removeItem("access_token");
            window.location.replace("/login");
            return;
        }

        const user = await response.json();

        console.log("Authenticated user:", user);

        window.currentUser = user;

    } catch (error) {
        console.error("Authentication error:", error);
        localStorage.removeItem("access_token");
        window.location.replace("/login");
    }
}

protectPage();