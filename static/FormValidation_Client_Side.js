
function username_validation(){

        const username_regex = /.{2,30}[\S]/i;
        const username_input = document.getElementById('username');
        username_input.value = username_input.value.trim();

        if(username_regex.test(username_input.value)){

            username_input.className = "form-control";
        }
        else{
            username_input.className = "form-control is-invalid";
        }
}

function password_validation(){

        const password_regex = /.{2,30}[\S]/i;
        const password_input = document.getElementById('password');
        password_input.value = password_input.value.trim();

        if(password_regex.test(password_input.value)){

            password_input.className = "form-control";
        }
        else{
            password_input.className = "form-control is-invalid";
        }
}

function email_registration(){

     const email_regex = /.{2,30}[\S]@[a-z]+\./i;
        const email_input = document.getElementById('email');
        email_input.value = email_input.value.trim();

        if(email_regex.test(email_input.value)){
            email_input.className = "form-control";
        }
        else{
            email_input.className = "form-control is-invalid";
        }
}

