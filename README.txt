The development is under this folder x3d-code/www.web3d.org/x3d/tools/HAnim:


HAnim/hier2x3d/build.xml -- ant script for building LOA1 - LOA4, Don's Humanoid (from X3DUOM?), and corrected standard (spaces, etc.).  Create X3D HAnim models/scenes from standard hierarchies, LOA1 - LOA4, result scenes found in results. Note that LOA0 is missing.
HAnim/hier2x3d/hier2x3d.pl -- perl script to build each humanoid x3d file
HAnim/hier2x3d/hier2x3d.sh -- sample script to build a couple of humanoids, see build.xml
HAnim/hier2x3d/sed.sh -- script to scrape even A annexes
HAnim/hier2x3d/sitesed.sh -- script to scrap odd A annexes
HAnim/hier2x3d/loa4.py -- Produce final result, parse X3DUOM, create loa4 result of X3DUOM of default and no default centers and translations.
HAnim/hier2x3d/README.txt -- this file
HAnim/hier2x3d/work.sh -- create missing/duplicate LOA4 centers  and translations report, results/FinalResult.txt, edit to replace .x3d files with your own (for now).


HAnim/results/DonHumanoid.x3d -- result from /c/x3d-code/www.web3d.org/x3d/stylesheets/HAnimLOA4HierarchyTable.txt
HAnim/results/Humanoid1.x3d -- result from LOA1
HAnim/results/Humanoid2.x3d -- result from LOA2
HAnim/results/Humanoid3.x3d -- result from LOA3
HAnim/results/Humanoid4.x3d -- result from LOA4
HAnim/results/StandardHumanoid.x3d -- result from cleaned up LOA4

Input standards

HAnim/standards/4.7.txt
HAnim/standards/A.10.txt
HAnim/standards/A.11.txt
HAnim/standards/A.2.txt
HAnim/standards/A.3.txt
HAnim/standards/A.4.txt
HAnim/standards/A.5.txt
HAnim/standards/A.6.txt
HAnim/standards/A.7.txt
HAnim/standards/A.8.txt
HAnim/standards/A.9.txt
HAnim/standards/B.2.txt
HAnim/standards/Hier1.txt
HAnim/standards/Hier2.txt
HAnim/standards/Hier3.txt
HAnim/standards/Hier4.txt
HAnim/standards/Hierarchy.txt (modified cleaned up Hier4.txt)
