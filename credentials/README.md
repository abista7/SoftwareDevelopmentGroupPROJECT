# Credentials Folder

1. Server URL or IP: [`lingomingo.app`](https://lingomingo.app/) | `34.213.215.231`
2. SSH username: `ubuntu`
3. SSH password or key: `key.pem` & `key.pkk` included in the current directory
4. Database URL or IP and port: `localhost:5432`
5. Database username: `lingouser`
6. Database password: `HDo!n5!eW54z6*E#`
7. Database name: `lingo`
8. Django's admin panel: 
username:`admin `
password:`yVOiy6^lJj9vT$2Q`

## Connecting To Server Via SSH
1. Download the key files: `key.pem` for OpenSSH(macOS/Linux), or `key.pkk` for Putty(Windows)
1. On macOS/Linux terminal: 
```
ssh -i /path/to/key.pem ubuntu@34.213.215.231
```
#### OR
1. on Windows Computer, download software ["putty"](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
1. On the left side, click `Connection - Data`, enter `ubuntu` into `"Auto-login username"`
1. On the left side, click `Connection - SSH - Auth`, click on `Browse` button to locate key.pkk you downloaded.
1. Click `Session - Host Name`, enter `34.213.215.231` and type LingoAWS into `Saved Sessions` and click `Save`, then click `Open`.

## Acessing Django's Admin Panel
1. visit [https://lingomingo.app/admin/](https://lingomingo.app/admin/)
1. login with Username: `admin` and Password: `yVOiy6^lJj9vT$2Q`

## Acessing Our PostgreSQL Database
1. Database can be accessed on only on SSH with ubuntu with root priv
```bash
sudo -u postgres psql
```
1. To Exit
```PostgreSQL
\q
```

# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.
