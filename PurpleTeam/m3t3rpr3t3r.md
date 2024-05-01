# m3t3rpr3t3r

Is a Linux terminal on the victim's computer. As such, many of our basic Linux commands can be used on the meterpreter even if it's on a Windows or other operating system. Here are some of the core commands we can use on the

#

#

#

# Core Commands

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for background
    bgkill                    Kills a background meterpreter script
    bglist                    Lists running background scripts
    bgrun                     Executes a meterpreter script as a background thread
    channel                   Displays information or control active channels
    close                     Closes a channel
    disable_unicode_encoding  Disables encoding of unicode strings
    enable_unicode_encoding   Enables encoding of unicode strings
    exit                      Terminate the meterpreter session
    get_timeouts              Get the current session timeout values
    guid                      Get the session GUID
    help                      Help menu
    info                      Displays information about a Post module
    irb                       Open an interactive Ruby shell on the current session
    load                      Load one or more meterpreter extensions
    machine_id                Get the MSF ID of the machine attached to the session
    pry                       Open the Pry debugger on the current session
    quit                      Terminate the meterpreter session
    read                      Reads data from a channel
    resource                  Run the commands stored in a file
    run                       Executes a meterpreter script or Post module
    sessions                  Quickly switch to another session
    set_timeouts              Set the current session timeout values
    use                       Deprecated alias for "load"
    uuid                      Get the UUID for the current session
    write                     Writes data to a channel

# File System Commands

    cat             read and output to stdout the contents of a file
    cd              change directory on the victim
    del             delete a file on the victim
    download        download a file from the victim system to the attacker system
    edit            edit a file with vim
    getlwd          print the local directory
    getwd           print working directory
    lcd             change local directory
    lpwd            print local directory
    ls              list files in current directory
    mkdir           make a directory on the victim system
    pwd             print working directory
    rm              delete (remove) a file
    rmdir           remove directory on the victim system
    upload          upload a file from the attacker system to the victim

# Networking Commands

    ipconfig        displays network interfaces with key information including IP address, etc.
    portfwd         forwards a port on the victim system to a remote service
    route           view or modify the victim routing table

# System Commands

    clearev         clears the event logs on the victim's computer
    drop_token      drops a stolen token
    execute         executes a command
    getpid          gets the current process ID (PID)
    getprivs        gets as many privileges as possible
    getuid          get the user that the server is running as
    kill            terminate the process designated by the PID
    ps              list running processes
    reboot          reboots the victim computer
    reg             interact with the victim's registry
    rev2self        calls RevertToSelf() on the victim machine
    shell           opens a command shell on the victim machine
    shutdown        shuts down the victim's computer
    steal_token     attempts to steal the token of a specified (PID) process
    sysinfo         gets the details about the victim computer such as OS and name

# User Interface Commands

    enumdesktops    lists all accessible desktops
    getdesktop      get the current meterpreter desktop
    idletime        checks to see how long since the victim system has been idle
    keyscan_dump    dumps the contents of the software keylogger
    keyscan_start   starts the software keylogger when associated with a process such as Word or browser
    keyscan_stop    stops the software keylogger
    screenshot      grabs a screenshot of the meterpreter desktop
    set_desktop     changes the meterpreter desktop
    uictl           enables control of some of the user interface components

# Privilege Escalation Commands

    getsystem       uses 15 built-in methods to gain sysadmin privileges

# Password Dump Commands

    hashdump        grabs the hashes in the password (SAM) file

Note that hashdump will often trip AV software, but there are now two scripts that are more stealthy, run hashdump and run smart_hashdump. Look for more in meterpreter script cheat sheet's.

# Timestamp Commands

    timestamp       manipulates the modify, access, and create attributes of a file

# Persistence

https://www.offensive-security.com/metasploit-unleashed/meterpreter-service/
