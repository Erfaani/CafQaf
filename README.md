# CafQaf

CafQaf is a comprehensive cafe management automation system designed to streamline operations for cafe owners, managers, and developers. The name "CafQaf" is derived from the Persian term "کافه قهوه" (Cafe Qahveh), which translates to "coffee cafe."

## Features

### Key Functionalities
- **Order Management:** Efficiently manage and track customer orders.
- **Menu Management:** Customize and update the cafe's menu effortlessly.
- **Online Table Reservations:** Allow customers to book tables online.
- **Employee Management:** Keep track of staff schedules and roles.
- **Financial Reporting:** Generate detailed financial reports to analyze performance.
- **Online Ordering:** Enable customers to place orders online.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** Tailwind CSS
- **Database:** Default Django database (SQLite)

## Installation and Setup

To set up and run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Erfaani/cafqaf.git
   cd cafqaf
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser at [http://localhost:8000](http://localhost:8000).

## Usage

- **Admin Panel:** Accessible at `/admin`, where cafe managers can manage orders, employees, and menus.
- **Customer Portal:** Customers can place orders and reserve tables online.

## Target Audience

This project is tailored for:
- **Cafe Owners and Managers** looking to streamline operations and enhance customer experience.
- **Developers** who want to contribute to or customize a cafe management system.

## Contribution

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes and create a pull request.


## Contact

For any inquiries or support, feel free to reach out:
- **Email:** erfanjouybar@gmail.com
- **GitHub:** [yourusername](https://github.com/erfaani)

---

Thank you for using **CafQaf**! We hope it helps you manage your cafe operations effortlessly.

