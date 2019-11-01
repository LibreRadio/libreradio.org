<?php
	exec("cd /var/www/libreradio.org");
	exec("git checkout master");
	shell_exec("git pull");
	die("done");
?>
