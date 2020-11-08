**Flask Chess website**

1) Create a .env file at the root of the project with these variables:

        APP_SECRET_KEY=<some string>
        
        DATABASE_URL=postgres://postgres:postgres@localhost:5432/dbname
        DATABASE_NAME=dbname
        DATABASE_HOST=localhost
        DATABASE_USER=postgres
        DATABASE_PASSWORD=postgres
        
        MAIL=<email address>
        MAIL_PASSWORD=<email password to send emails>
        
2) Install requirements