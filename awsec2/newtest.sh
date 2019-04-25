read -p "Enter imgid : " imgid
read -p "Enter region : " region
echo "aws --profile agsafety ec2  describe-images --image-ids $imgid --region $region  | grep -w "DeviceName\|VolumeSize\|SnapshotId" "
aws --profile agsafety ec2  describe-images --image-ids $imgid --region $region  | grep "VolumeSize\|SnapshotId\|DeviceName" | grep snap | awk '{print $4}'
