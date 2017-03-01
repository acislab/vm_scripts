Connect-VIServer -Server vcenter.acis.ufl.edu -Protocol https

$servers = 1,2,3,4,5,6,7
$i = 0

Import-CSV machines.csv -Header fqdn,hostname,ip,mac | 
	ForEach-Object {
	    $server = "ece-acis-esx{0:D2}.acis.ufl.edu" -f $servers[($i % 7)]
		"making " + $_.fqdn + " on " + $server
		New-VM -VMHost $server -Name $_.fqdn -DiskGB 30 -MemoryGB 3 -NumCPU 2
		$nic = Get-NetworkAdapter -VM $_.fqdn
		Set-NetworkAdapter -NetworkAdapter $nic -MacAddress $_.mac -Confirm:$false
		$ctl = Get-ScsiController -VM $_.fqdn
		Set-ScsiController -ScsiController $ctl -Type VirtualLsiLogic

		$i += 1
	}

