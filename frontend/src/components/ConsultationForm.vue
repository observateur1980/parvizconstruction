<template>
  <form @submit.prevent="handleSubmit" novalidate>
    <div class="form-group">
      <label for="full_name">Full Name *</label>
      <input
        id="full_name"
        v-model.trim="form.full_name"
        type="text"
        required
        :class="{'input-error': errors.full_name}"
        autocomplete="name"
      />
      <div v-if="errors.full_name" class="error-msg">{{ errors.full_name }}</div>
    </div>

    <div class="form-group">
      <label for="email">Email *</label>
      <input
        id="email"
        v-model.trim="form.email"
        type="email"
        required
        :class="{'input-error': errors.email}"
        autocomplete="email"
      />
      <div v-if="errors.email" class="error-msg">{{ errors.email }}</div>
    </div>

    <div class="form-group">
      <label for="phone">Phone *</label>
      <input
        id="phone"
        v-model.trim="form.phone"
        type="tel"
        required
        :class="{'input-error': errors.phone}"
        autocomplete="tel"
        pattern="^[+0-9 ()-]{7,20}$"
      />
      <div v-if="errors.phone" class="error-msg">{{ errors.phone }}</div>
    </div>

    <div class="form-group">
      <label for="postal_code">Postal Code *</label>
      <input
        id="postal_code"
        v-model.trim="form.postal_code"
        type="text"
        required
        :class="{'input-error': errors.postal_code}"
        autocomplete="postal-code"
      />
      <div v-if="errors.postal_code" class="error-msg">{{ errors.postal_code }}</div>
    </div>

    <fieldset class="form-group">
      <legend>Project Types *</legend>
      <div v-for="type in projectTypeOptions" :key="type" class="checkbox-group">
        <input
          type="checkbox"
          :id="type"
          :value="type"
          v-model="form.project_types"
        />
        <label :for="type">{{ type }}</label>
      </div>
      <div v-if="errors.project_types" class="error-msg">{{ errors.project_types }}</div>
    </fieldset>

    <div class="form-group">
      <label for="project_description">Project Description (Optional)</label>
      <textarea
        id="project_description"
        v-model.trim="form.project_description"
        rows="5"
      ></textarea>
    </div>

    <div v-if="errors.recaptcha" class="error-msg">{{ errors.recaptcha }}</div>

    <button type="submit" :disabled="submitting">
      {{ submitting ? 'Submitting...' : 'Submit Request' }}
    </button>

    <div v-if="successMessage" class="success-msg">{{ successMessage }}</div>
    <div v-if="serverErrorMessage" class="error-msg">{{ serverErrorMessage }}</div>
  </form>
</template>

<script>
export default {
  name: 'ConsultationForm',
  data() {
    return {
      form: {
        full_name: '',
        email: '',
        phone: '',
        postal_code: '',
        project_types: [],
        project_description: '',
        recaptcha_token: '',
      },
      projectTypeOptions: [
        'Residential',
        'Commercial',
        'Industrial',
        'Renovation',
        'Other'
      ],
      errors: {},
      successMessage: '',
      serverErrorMessage: '',
      submitting: false,
    };
  },
  methods: {
    validateForm() {
      this.errors = {};
      let valid = true;

      if (!this.form.full_name) {
        this.errors.full_name = 'Full name is required.';
        valid = false;
      }

      if (!this.form.email) {
        this.errors.email = 'Email is required.';
        valid = false;
      } else if (!this.validEmail(this.form.email)) {
        this.errors.email = 'Email is invalid.';
        valid = false;
      }

      if (!this.form.phone) {
        this.errors.phone = 'Phone is required.';
        valid = false;
      } else if (!this.validPhone(this.form.phone)) {
        this.errors.phone = 'Phone number is invalid.';
        valid = false;
      }

      if (!this.form.postal_code) {
        this.errors.postal_code = 'Postal code is required.';
        valid = false;
      }

      if (!this.form.project_types.length) {
        this.errors.project_types = 'At least one project type must be selected.';
        valid = false;
      }

      return valid;
    },
    validEmail(email) {
      // Simple email regex
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    },
    validPhone(phone) {
      // Allow digits, spaces, parentheses, + and -
      const re = /^[+0-9 ()-]{7,20}$/;
      return re.test(phone);
    },
    async handleSubmit() {
      this.successMessage = '';
      this.serverErrorMessage = '';
      if (!this.validateForm()) {
        return;
      }

      this.submitting = true;
      try {
        // Obtain reCAPTCHA token
        const token = await this.$recaptcha('consultation_form_submit');
        this.form.recaptcha_token = token;

        // Prepare payload without recaptcha_token in serializer fields but included in POST
        const payload = {
          full_name: this.form.full_name,
          email: this.form.email,
          phone: this.form.phone,
          postal_code: this.form.postal_code,
          project_types: this.form.project_types,
          project_description: this.form.project_description,
          recaptcha_token: this.form.recaptcha_token,
        };

        const response = await this.$http.post('/api/consultation/', payload);

        if (response.status === 201) {
          this.successMessage = response.data.message || 'Request submitted successfully.';
          this.resetForm();
        } else {
          this.serverErrorMessage = 'Unexpected server response.';
        }
      } catch (error) {
        if (error.response && error.response.data) {
          if (typeof error.response.data === 'object') {
            this.errors = { ...this.errors, ...error.response.data };
          } else {
            this.serverErrorMessage = error.response.data;
          }
        } else {
          this.serverErrorMessage = 'Failed to submit request. Please try again later.';
        }
      } finally {
        this.submitting = false;
      }
    },
    resetForm() {
      this.form.full_name = '';
      this.form.email = '';
      this.form.phone = '';
      this.form.postal_code = '';
      this.form.project_types = [];
      this.form.project_description = '';
      this.form.recaptcha_token = '';
      this.errors = {};
    }
  }
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
.form-group,
fieldset {
  margin-bottom: 1rem;
}
input[type="text"],
input[type="email"],
input[type="tel"],
textarea {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}
input[type="checkbox"] {
  margin-right: 0.5rem;
}
.checkbox-group {
  display: flex;
  align-items: center;
  margin-bottom: 0.25rem;
}
button {
  padding: 0.75rem;
  font-size: 1.1rem;
  border: none;
  background-color: #0069d9;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}
button[disabled] {
  background-color: #a0a0a0;
  cursor: not-allowed;
}
.error-msg {
  color: #d93025;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}
.success-msg {
  color: #188038;
  font-size: 1rem;
  margin-top: 1rem;
}
.input-error {
  border-color: #d93025;
}
</style>
