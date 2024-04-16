#!/bin/bash
#perl hier2x3d.pl ./standards/Hierarchy.txt ./results/StandardHumanoid.x3d 4
#perl hier2x3d.pl /c/x3d-code/www.web3d.org/x3d/stylesheets/HAnimLOA4HierarchyTable.txt ./results/DonHumanoid.x3d 4
#perl hier2x3d.pl /c/x3d-code/www.web3d.org/x3d/stylesheets/HAnimLOA4HierarchyTable.txt ./results/DonHumanoid.x3d 4
perl centers.pl > ./WScenters.txt
perl hier2x3d.vrml.pl ./WScenters.txt < ./HierWS.txt | tee WSHumanoid.x3dv > ./results/WSTemplate.x3dv

# perl hier2x3d.barejoints.pl < HierWS.txt
# perl hier2x3d.barejoints.pl < HierWS.txt | tee WSHumanoid.x3d > ../../Lily/NewTemplate.x3d
#npx x3d-tidy -i C:/Users/john/Lily/NewTemplate.x3d -o C:/Users/john/Lily/NewTemplate.x3dv
