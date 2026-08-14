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
                    "Authorization":
                        `Bearer ${token}`
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
                        class="employee-action"
                        data-id="${employee.id}"
                    >
                        View
                    </button>
                </td>
            `;

            tableBody.appendChild(row);
        });

    } catch (error) {

        console.error(
            "Employee loading error:",
            error
        );

        message.textContent = error.message;
    }
}


document
    .getElementById("refreshEmployees")
    ?.addEventListener(
        "click",
        loadEmployees
    );