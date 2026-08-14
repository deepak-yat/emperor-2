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

const employeeForm =
    document.getElementById("employeeForm");

if (employeeForm) {
    employeeForm.addEventListener(
        "submit",
        createEmployee
    );
}


async function createEmployee(event) {

    event.preventDefault();

    const name =
        document.getElementById("employeeName").value.trim();

    const email =
        document.getElementById("employeeEmail").value.trim();

    const salary =
        Number(
            document.getElementById("employeeSalary").value
        );

    const departmentId =
        Number(
            document.getElementById("departmentId").value
        );

    const message =
        document.getElementById("employeeMessage");

    const button =
        document.getElementById("employeeSubmitButton");

    const buttonText =
        document.getElementById("employeeButtonText");

    const token =
        localStorage.getItem("access_token");

    if (!token) {
        window.location.href = "/login";
        return;
    }

    button.disabled = true;
    buttonText.textContent = "CREATING...";

    message.textContent = "";

    try {

        const response = await fetch(
            "/employees",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },

                body: JSON.stringify({
                    name: name,
                    email: email,
                    salary: salary,
                    department_id: departmentId
                })
            }
        );

        const data =
            await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Failed to create employee"
            );
        }

        message.textContent =
            "Employee created successfully.";

        message.style.color = "#aaa";

        buttonText.textContent =
            "CREATED";

        employeeForm.reset();

    } catch (error) {

        console.error(
            "Create employee error:",
            error
        );

        message.textContent =
            error.message;

        message.style.color = "#aaa";

        buttonText.textContent =
            "CREATE EMPLOYEE";

    } finally {

        button.disabled = false;
    }
}