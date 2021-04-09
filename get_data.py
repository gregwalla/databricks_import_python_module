import os

class Blobconnector: 
  "Helps to work with data from an azure blob container "
  def __init__(self, container_name):
    self.container_name = container_name
    self.pth = f"/dbfs/mnt/{container_name}"  
    self.mount_point = f"/mnt/{container_name}" #DBFS path, set here to the same name as the container
    self.blob_name = 'azstogwmb' # Azure Blob storage account name
    self.scope = "azkey" #Azure Key Vault-backed secret scope with Azure Key Vault DNS name and Resource ID
    self.key = "azstogwmbaccesskey" #secret in ms-gw-keyvault to store key1 from Blob storage account.
    
  @property
  def introduce_self(self):
    print(f"Container name is :  {self.container_name}" )
    
  @property
  def listfiles(self):
    for file in os.listdir(self.pth):
      print(file)
      
  @property
  def unmount(self):
    dbutils.fs.unmount(self.mount_point)
      
  @property
  def mount(self):
    dbutils.fs.mount(
      source = f"wasbs://{self.container_name}@{self.blob_name}.blob.core.windows.net",
      mount_point = self.mount_point ,
      extra_configs = {f"fs.azure.account.key.{self.blob_name}.blob.core.windows.net":dbutils.secrets.get(scope = self.scope, key =  self.key)} )