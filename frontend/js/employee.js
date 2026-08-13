document.addEventListener("DOMContentLoaded", () => {
    loadEmployees();
});


async function loadEmployees() {

    const token =
        localStorage.getItem("access_token");

    if (!token) {
        return;
    }

    const tableBody =
        document.getElementById("employeeTableBody");

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
                data.detail || "Failed to load employees"
            );
        }

        tableBody.innerHTML = "";

        if (data.length === 0) {

            tableBody.innerHTML = `
                <tr>
                    <td colspan="5">
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
            `;

            tableBody.appendChild(row);

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