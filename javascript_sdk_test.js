const SmsGatewayApi = require('sms_gateway_api');

function randomString(length = 10) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    let result = '';
    for (let i = 0; i < length; i++) {
        result += letters.charAt(Math.floor(Math.random() * letters.length));
    }
    return result;
}

function main() {
    const defaultClient = SmsGatewayApi.ApiClient.instance;
    defaultClient.basePath = 'http://localhost:8000';

    const authApi = new SmsGatewayApi.AuthenticationApi();
    const smsApi = new SmsGatewayApi.SMSApi();

    // 1. Register a new user
    const username = randomString();
    const password = 'testpassword';
    const email = `${username}@example.com`;
    const userCreate = new SmsGatewayApi.UserCreate(username, email, password);
    userCreate.full_name = "Test User JS";

    console.log('1. Registering a new user...');
    authApi.registerAuthRegisterPost(userCreate, (error, data, response) => {
        if (error) {
            console.error('Exception when calling AuthenticationApi.registerAuthRegisterPost:', error.response ? error.response.text : error.message);
            return;
        }
        
        console.log('User registered successfully:');
        console.log(data);

        // 2. Login with the new user
        console.log('\n2. Logging in...');
        const opts = {}; // grant_type is handled by the client
        authApi.loginAuthLoginPost(username, password, opts, (loginError, loginData, loginResponse) => {
            if (loginError) {
                console.error('Exception when calling AuthenticationApi.loginAuthLoginPost:', loginError.response ? loginError.response.text : loginError.message);
                return;
            }

            console.log('Login successful:');
            console.log(loginData);
            const accessToken = loginData.access_token;

            // 3. Configure API client with the access token
            if (accessToken) {
                const oauth = defaultClient.authentications['OAuth2PasswordBearer'];
                oauth.accessToken = accessToken;
            }

            // 4. Send an SMS
            const smsCreate = new SmsGatewayApi.SmsCreate('+0987654321', 'Hello from the JavaScript SDK!');

            console.log('\n3. Sending an SMS...');
            smsApi.sendSmsSmsPost(smsCreate, (smsError, smsData, smsResponse) => {
                if (smsError) {
                    console.error('Exception when calling SMSApi.sendSmsSmsPost:', smsError.response ? smsError.response.text : smsError.message);
                } else {
                    console.log('SMS sent successfully:');
                    console.log(smsData);
                }

                
            });
        });
    });
}

if (require.main === module) {
    main();
} 