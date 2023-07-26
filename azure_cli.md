# With this procedure U 'll install the azure cli in Parrot Security OS or same in Debian
#
#
#
#
Execute from your terminal
#
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ stretch main" | \
     sudo tee /etc/apt/sources.list.d/azure-cli.list
#
#
Install azure-cli
#
sudo apt-get update && sudo apt-get install azure-cli
#
Login in your azure account
#
az login
#
For understand what more U can do with azure cli
#
Execute this command
#
└──╼ #az
#
Welcome to the cool new Azure CLI!
#
Use `az --version` to display the current version.
Here are the base commands:
#
    account           : Manage Azure subscription information.
    acr               : Manage Azure Container Registries for private registries within Azure.
    acs               : Manage Azure Container Services.
    ad                : Manage Azure Active Directory Graph entities needed for Role Based Access
                       Control.
    advisor           : Manage Azure Advisor.
    aks               : Manage Azure Kubernetes Services.
    ams               : Manage Azure Media Services resources.
    appservice        : Manage App Service plans.
    backup            : Manage Azure Backups.
    batch             : Manage Azure Batch.
    batchai           : Manage Batch AI resources.
    billing           : Manage Azure Billing.
    cdn               : Manage Azure Content Delivery Networks (CDNs).
    cloud             : Manage registered Azure clouds.
    cognitiveservices : Manage Azure Cognitive Services accounts.
    configure         : Manage Azure CLI configuration. This command is interactive.
    consumption       : Manage consumption of Azure resources.
    container         : Manage Azure Container Instances.
    cosmosdb          : Manage Azure Cosmos DB database accounts.
    deployment        : Manage Azure Resource Manager deployments at subscription scope.
    disk              : Manage Azure Managed Disks.
    dla               : (PREVIEW) Manage Data Lake Analytics accounts, jobs, and catalogs.
    dls               : (PREVIEW) Manage Data Lake Store accounts and filesystems.
    dms               : Manage Azure Data Migration Service (DMS) instances.
    eventgrid         : Manage Azure Event Grid topics and subscriptions.
    eventhubs         : Manage Azure Event Hubs namespaces, eventhubs, consumergroups and geo
                       recovery configurations - Alias.
    extension         : Manage and update CLI extensions.
    feature           : Manage resource provider features.
    feedback          : Send feedback to the Azure CLI Team!
    find              : Find Azure CLI commands.
    functionapp       : Manage function apps.
    group             : Manage resource groups and template deployments.
    identity          : Managed Service Identities.
    image             : Manage custom virtual machine images.
    interactive       : Start interactive mode.
    iot               : Manage Internet of Things (IoT) assets.
    iotcentral        : Manage IoT Central assets.
    keyvault          : Manage KeyVault keys, secrets, and certificates.
    lab               : Manage Azure DevTest Labs.
    lock              : Manage Azure locks.
    login             : Log in to Azure.
    logout            : Log out to remove access to Azure subscriptions.
    managedapp        : Manage template solutions provided and maintained by Independent Software
                       Vendors (ISVs).
    maps              : Manage Azure Maps.
    monitor           : Manage the Azure Monitor Service.
    mysql             : Manage Azure Database for MySQL servers.
    network           : Manage Azure Network resources.
    policy            : Manage resource policies.
    postgres          : Manage Azure Database for PostgreSQL servers.
    provider          : Manage resource providers.
    redis             : Manage dedicated Redis caches for your Azure applications.
    relay             : Manage Azure Relay Service namespaces, WCF relays, hybrid connections, and
                       rules.
    reservations      : Manage Azure Reservations.
    resource          : Manage Azure resources.
    role              : Manage user roles for access control with Azure Active Directory and service
                       principals.
    search            : Manage Azure Search services, admin keys and query keys.
    servicebus        : Manage Azure Service Bus namespaces, queues, topics, subscriptions, rules
                       and geo-disaster recovery configuration alias.
    sf                : Manage and administer Azure Service Fabric clusters.
    snapshot          : Manage point-in-time copies of managed disks, native blobs, or other
                       snapshots.
    sql               : Manage Azure SQL Databases and Data Warehouses.
    storage           : Manage Azure Cloud Storage resources.
    tag               : Manage resource tags.
    vm                : Manage Linux or Windows virtual machines.
    vmss              : Manage groupings of virtual machines in an Azure Virtual Machine Scale Set
                       (VMSS).
    webapp            : Manage web apps.
#
#
#
#
#
# by C4N6
     
