#!/bin/sh -x
# 
cat /dev/null > ./results/missingtranslation.txt
cat /dev/null > ./results/missingcenter.txt
/usr/bin/grep -h -e '<'HAnimSite ~/www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/JinLOA4.x3d ./results/DonHumanoid.x3d ./standards/HAnimModelFootLeft.x3d ./standards/HAnimModelFootRight.x3d ./standards/HAnimModelHandLeft.x3d ./standards/HAnimModelHandRight.x3d | /usr/bin/grep -v USE|/usr/bin/grep -v translation| sort -u >> ./results/missingtranslation.txt
/usr/bin/grep -h -e '<'HAnimJoint ~/www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/JinLOA4.x3d ./results/DonHumanoid.x3d ./standards/HAnimModelFootLeft.x3d ./standards/HAnimModelFootRight.x3d ./standards/HAnimModelHandLeft.x3d ./standards/HAnimModelHandRight.x3d |/usr/bin/grep -v USE|/usr/bin/grep -v center | sort -u >> ./results/missingcenter.txt
sed "s/.*name='\([^']*\)'>/\1/" ./results/missingcenter.txt > ./results/findthesecenters.txt
sed "s/.*name='\([^']*\)'>/\1/" ./results/missingtranslation.txt > ./results/findthesetranslations.txt

sed -e 's/_tip$//' -e 's/_pt$//' ./results/findthesetranslations.txt > ./results/findthesetranslationsnotipnopt.txt
/usr/bin/fgrep -f ./results/findthesetranslationsnotipnopt.txt ~/www.web3d.org/specifications/X3dUnifiedObjectModel-4.0.xml|/usr/bin/grep value=|sort -u | sed 's/.*=//'| sed 's/"//g' > ./results/findthesetranslationsraw.txt

sort -u ./results/findthesecenters.txt > ./results/sortedcenters.txt
sort -u ./results/findthesetranslationsraw.txt > ./results/sortedtranslations.txt

echo "XML name attribute | name in file | default value (possibly none)" > ./results/FinalResult.txt
python ../hier2x3d/loa4.py  | sort -u >>./results/FinalResult.txt
/usr/bin/fgrep -f ./results/loa4defaulted.txt ./results/loa4nodefault.txt |sort -u > ./results/loa4both.txt

cat ./results/FinalResult.txt|/usr/bin/grep -v = |sed 's/ .*//'|sort -u|/usr/bin/grep -v XML > ./results/JointsSegments.txt
