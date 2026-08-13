const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", handleLogin);
}


async function handleLogin(event) {

    event.preventDefault();

    const username =
        document.getElementById("username").value.trim();

    const password =
        document.getElementById("password").value;

    const message =
        document.getElementById("loginMessage");

    const button =
        document.getElementById("loginButton");

    const buttonText =
        document.getElementById("buttonText");


    message.textContent = "";

    button.disabled = true;

    buttonText.textContent = "AUTHENTICATING...";


    try {

        const response = await fetch(
            "/auth/login",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    user_name: username,
                    user_password: password
                })
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail || "Login failed"
            );

        }


        /*
         * The backend returned our JWT.
         */

        localStorage.setItem(
            "access_token",
            data.access_token
        );


        message.textContent =
            "Login successful.";


        /*
         * Give the user a short visual
         * confirmation before redirecting.
         */

        buttonText.textContent = "SUCCESS";


        setTimeout(() => {

            window.location.href =
                "/dashboard";

        }, 500);


    } catch (error) {

        message.textContent =
            error.message;

        buttonText.textContent =
            "SIGN IN";

        button.disabled = false;

    }

}

function logout() {

    localStorage.removeItem("access_token");

    window.location.href = "/login";
}


document
    .getElementById("logoutButton")
    ?.addEventListener("click", logout);