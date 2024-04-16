The development was under this folder x3d-code/www.web3d.org/x3d/tools/HAnim:


./build.xml -- ant script for building LOA1 - LOA4, Don's Humanoid (from X3DUOM?), and corrected standard (spaces, etc.).  Create X3D HAnim models/scenes from standard hierarchies, LOA1 - LOA4, result scenes found in results. Note that LOA0 is missing.
./hier2x3d.pl -- perl script to build each humanoid x3d file
./hier2x3d.sh -- sample script to build a couple of humanoids, see build.xml
./sed.sh -- script to scrape even A annexes
./sitesed.sh -- script to scrap odd A annexes
./loa4.py -- Produce final result, parse X3DUOM, create loa4 result of X3DUOM of default and no default centers and translations.
./README.txt -- this file
./work.sh -- create missing/duplicate LOA4 centers  and translations report, results/FinalResult.txt, edit to replace .x3d files with your own (for now).


./results/DonHumanoid.x3d -- result from /c/x3d-code/www.web3d.org/x3d/stylesheets/HAnimLOA4HierarchyTable.txt
./results/Humanoid1.x3d -- result from LOA1
./results/Humanoid2.x3d -- result from LOA2
./results/Humanoid3.x3d -- result from LOA3
./results/Humanoid4.x3d -- result from LOA4
./results/StandardHumanoid.x3d -- result from cleaned up LOA4

Input standards

./standards/4.7.txt
./standards/A.10.txt
./standards/A.11.txt
./standards/A.2.txt
./standards/A.3.txt
./standards/A.4.txt
./standards/A.5.txt
./standards/A.6.txt
./standards/A.7.txt
./standards/A.8.txt
./standards/A.9.txt
./standards/B.2.txt
./standards/Hier1.txt
./standards/Hier2.txt
./standards/Hier3.txt
./standards/Hier4.txt
./standards/Hierarchy.txt (modified cleaned up Hier4.txt)
