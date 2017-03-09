<html>
<body>
<?php
$cmd = "/opt/harvest/bin/hchu -b cscr501 -npw $_POST["h_password"] -ousr $_POST["h_usrname"] -eh /opt/harvest/bin/harvest.eh"
exec($cmd,$ret);
if ($ret){
    echo "failed to change password, ret=$ret ";
}
?>
</body>
</html>