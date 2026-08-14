// ========================================
// LOGIN
// ========================================

const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", handleLogin);
}


async function handleLogin(event) {

    event.preventDefault();

    console.log("LOGIN JS IS RUNNING");

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

        console.log(
            "LOGIN RESPONSE:",
            response.status,
            data
        );


        if (!response.ok) {

            throw new Error(
                data.detail || "Login failed"
            );
        }


        // Store JWT
        localStorage.setItem(
            "access_token",
            data.access_token
        );


        message.textContent =
            "Login successful.";

        buttonText.textContent =
            "SUCCESS";


        setTimeout(() => {

            window.location.href =
                "/dashboard";

        }, 500);


    } catch (error) {

        console.error(
            "LOGIN ERROR:",
            error
        );

        message.textContent =
            error.message;

        buttonText.textContent =
            "SIGN IN";

        button.disabled = false;
    }
}


// ========================================
// REGISTRATION
// ========================================

const registerForm =
    document.getElementById("registerForm");

if (registerForm) {

    registerForm.addEventListener(
        "submit",
        handleRegister
    );
}


async function handleRegister(event) {

    event.preventDefault();


    const username =
        document.getElementById("username").value.trim();

    const email =
        document.getElementById("email").value.trim();

    const password =
        document.getElementById("password").value;

    const confirmPassword =
        document.getElementById("confirmPassword").value;

    const message =
        document.getElementById("registerMessage");

    const button =
        document.getElementById("registerButton");

    const buttonText =
        document.getElementById(
            "registerButtonText"
        );


    message.textContent = "";


    if (password !== confirmPassword) {

        message.textContent =
            "Passwords do not match.";

        return;
    }


    button.disabled = true;

    buttonText.textContent =
        "CREATING ACCOUNT...";


    try {

        const response = await fetch(
            "/auth/register",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    user_name: username,
                    user_email: email,
                    user_password: password
                })
            }
        );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Registration failed"
            );
        }


        message.textContent =
            data.message ||
            "Registration successful. Waiting for admin approval.";


        buttonText.textContent =
            "ACCOUNT CREATED";


    } catch (error) {

        console.error(
            "REGISTRATION ERROR:",
            error
        );

        message.textContent =
            error.message;

        button.disabled = false;

        buttonText.textContent =
            "CREATE ACCOUNT";
    }
}


// ========================================
// LOGOUT
// ========================================

function logout() {

    localStorage.removeItem(
        "access_token"
    );

    window.location.href =
        "/login";
}


document
    .getElementById("logoutButton")
    ?.addEventListener(
        "click",
        logout
    );