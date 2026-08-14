document.addEventListener("DOMContentLoaded", () => {
    loadEmployees();
});


async function loadEmployees() {

    const token = localStorage.getItem("access_token");

    if (!token) {
        window.location.href = "/login";
        return;
    }

    const tableBody =
        document.getElementById("employeeTableBody");

    const employeeCount =
        document.getElementById("employeeCount");

    const message =
        document.getElementById("employeeMessage");

    try {

        const response = await fetch(
            "/employees",
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
                data.detail ||
                "Unable to load employees"
            );
        }

        tableBody.innerHTML = "";

        employeeCount.textContent = data.length;

        if (data.length === 0) {

            tableBody.innerHTML = `
                <tr>
                    <td colspan="6" class="table-loading">
                        No employees found.
                    </td>
                </tr>
            `;

            return;
        }

        data.forEach(employee => {

            const row =
                document.createElement("tr");

            row.innerHTML = `
                <td>${employee.id}</td>
                <td>${employee.name}</td>
                <td>${employee.email}</td>
                <td>${employee.salary}</td>
                <td>${employee.department_id}</td>

                <td>
                    <button
                        class="employee-action view-button"
                        data-id="${employee.id}"
                    >
                        View
                    </button>

                    <button
                        class="employee-action delete-button"
                        data-id="${employee.id}"
                    >
                        Delete
                    </button>
                </td>
            `;

            tableBody.appendChild(row);
        });


        // Attach delete events AFTER all rows exist
        document
            .querySelectorAll(".delete-button")
            .forEach(button => {

                button.addEventListener(
                    "click",
                    () => {
                        deleteEmployee(
                            button.dataset.id
                        );
                    }
                );

            });


    } catch (error) {

        console.error(
            "Employee loading error:",
            error
        );

        message.textContent =
            error.message;
    }
}


async function deleteEmployee(employeeId) {

    const confirmed = confirm(
        "Are you sure you want to delete this employee?"
    );

    if (!confirmed) {
        return;
    }

    const token =
        localStorage.getItem("access_token");

    if (!token) {
        window.location.href = "/login";
        return;
    }

    try {

        const response = await fetch(
            `/employees/${employeeId}`,
            {
                method: "DELETE",

                headers: {
                    "Authorization":
                        `Bearer ${token}`
                }
            }
        );

        const data =
            await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail ||
                "Unable to delete employee"
            );
        }

        alert(
            "Employee deleted successfully."
        );

        await loadEmployees();

    } catch (error) {

        console.error(
            "Delete employee error:",
            error
        );

        alert(error.message);
    }
}


document
    .getElementById("refreshEmployees")
    ?.addEventListener(
        "click",
        loadEmployees
    );