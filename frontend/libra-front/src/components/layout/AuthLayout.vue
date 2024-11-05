<template>
    <div id="authlayout">
        <!-- <h1>Libra</h1> -->
        <main id="main">
            <router-view /> 
        </main>
    </div>
</template>
<script>
export default {
    name: "AuthLayout",
};
</script>
<style>
/* Base Styling */
#authlayout {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-family: 'Roboto', sans-serif;
  background-color: #f4f6f8;
  margin: 0;
}

/* Form Container */
.form-container {
  width: 100%;
  max-width: 400px;
  background-color: #fff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.form-container h2 {
  margin-bottom: 20px;
  font-size: 1.8em;
  color: #333;
}

/* Form Fields */
.form-group {
  margin-bottom: 15px;
  text-align: left;
}

.form-group label {
  display: block;
  font-weight: bold;
  font-size: 0.9em;
  color: #666;
  margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
input[type="password"]{
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1em;
  transition: border-color 0.3s;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
  border-color: #4a90e2;
  outline: none;
}
.button-primary {
  width: 100%;
  padding: 12px;
  background-color: #4a90e2;
  border: none;
  border-radius: 5px;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.3s;
}

.button-primary:hover {
  background-color: #357ab9;
}

/* Secondary Button for Logout */
.button-secondary {
  background-color: #d9534f;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button-secondary:hover {
  background-color: #c9302c;
}

/* Link for Switching Between Forms */
.switch-link {
  display: block;
  margin-top: 15px;
  color: #4a90e2;
  text-decoration: none;
  font-size: 0.9em;
}

.switch-link:hover {
  text-decoration: underline;
}

/* Error Message */
.error-message {
  color: #d9534f;
  font-size: 0.9em;
  margin-top: 10px;
}

/* Success Message */
.success-message {
  color: #5cb85c;
  font-size: 0.9em;
  margin-top: 10px;
}

/* Responsive Adjustments */
@media (max-width: 480px) {
  .form-container {
    padding: 20px;
  }

  .button-primary,
  .button-secondary {
    font-size: 0.9em;
  }
}

</style>