Connect-VIServer -Server vcenter.acis.ufl.edu -Protocol https

$nodes = 1,2,3,4,5,6,7
$hosts = @(47, 39, 11, 42, 44, 5, 28, 30, 20, 9, 8, 43, 52, 50)
#$hosts = @(44)
foreach($i in $hosts){
	$name = "ece-acis-dc{0:D2}5.acis.ufl.edu" -f $i
	$mac = "00:50:56:00:23:{0:X2}" -f ($i + 170)
	$node = "ece-acis-esx{0:D2}.acis.ufl.edu" -f $nodes[($i % 7)]
	"$name $mac $node"
# Commented out because I just wnated a list of hosts and MACs
	New-VM -VMHost $node -Name $name -DiskGB 20 -MemoryGB 1
	$nic = Get-NetworkAdapter -VM $name
	Set-NetworkAdapter -NetworkAdapter $nic -MacAddress $mac -Confirm:$false
	$ctl = Get-ScsiController -VM $name
	Set-ScsiController -ScsiController $ctl -Type VirtualLsiLogic
	
}


