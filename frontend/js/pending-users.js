document.addEventListener("DOMContentLoaded", () => {
    loadPendingUsers();
});


async function loadPendingUsers() {

    const token = localStorage.getItem("access_token");

    if (!token) {
        window.location.href = "/login";
        return;
    }

    const tableBody =
        document.getElementById("pendingUsersBody");

    const message =
        document.getElementById("pendingMessage");

    try {

        const response = await fetch(
            "/admin/pending-users",
            {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Unable to load pending users"
            );
        }

        tableBody.innerHTML = "";

        if (data.length === 0) {

            tableBody.innerHTML = `
                <tr>
                    <td colspan="7" class="table-loading">
                        No pending registrations.
                    </td>
                </tr>
            `;

            return;
        }

        data.forEach(user => {

            const row =
                document.createElement("tr");

            row.innerHTML = `
                <td>${user.user_id}</td>
                <td>${user.user_name}</td>
                <td>${user.user_email}</td>
                <td>${user.employee_id}</td>

                <td>
                    <select
                        class="role-select"
                        id="role-${user.user_id}"
                    >
                        <option value="">Select role</option>
                        <option value="2">Manager</option>
                        <option value="3">HR</option>
                        <option value="4">Employee</option>
                    </select>
                </td>

                <td>
                    <span class="pending-status">
                        PENDING
                    </span>
                </td>

                <td>
                    <button
                        class="approve-button"
                        data-user-id="${user.user_id}"
                    >
                        Approve
                    </button>
                </td>
            `;

            tableBody.appendChild(row);
        });

        attachApprovalHandlers();

    } catch (error) {

        console.error(
            "Pending users error:",
            error
        );

        message.textContent =
            error.message;
    }
}


function attachApprovalHandlers() {

    const buttons =
        document.querySelectorAll(
            ".approve-button"
        );

    buttons.forEach(button => {

        button.addEventListener(
            "click",
            () => {

                const userId =
                    button.dataset.userId;

                approveUser(userId);
            }
        );

    });
}


async function approveUser(userId) {

    const roleSelect =
        document.getElementById(
            `role-${userId}`
        );

    const roleId =
        Number(roleSelect.value);

    if (!roleId) {

        alert("Please select a role.");

        return;
    }

    const token =
        localStorage.getItem("access_token");

    try {

        const response = await fetch(
            `/admin/users/${userId}/approve`,
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },

                body: JSON.stringify({
                    role_id: roleId
                })
            }
        );

        const data =
            await response.json();

        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Unable to approve user"
            );
        }

        alert(
            "User approved successfully."
        );

        loadPendingUsers();

    } catch (error) {

        console.error(
            "Approval error:",
            error
        );

        alert(error.message);
    }
}


document
    .getElementById("refreshPendingUsers")
    ?.addEventListener(
        "click",
        loadPendingUsers
    );