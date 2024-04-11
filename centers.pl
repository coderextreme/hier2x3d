#!/usr/bin/perl
use strict;
use warnings;

use Math::Trig;

#my $centerFile = "../../Lily/InputDir.old2/7_1 joint location.txt";
# my $centerFile = "../../Lily/InputDir/lilly_7_2 joint location.txt";
my $centerFile = "../../Lily/InputDir.old2/lily_6_1_joint_rotate.txt";



my $joint = "WRONG JOINT";
open (CENTERS, "<$centerFile") or die "Could not open center locations and translations file, $centerFile";

my $firstLine = <CENTERS>; # Joint location
my $secondLine = <CENTERS>; # First line of underscores
while (<CENTERS>) {
	chomp;
	$joint = $_;
	if (/^S/) {
		$joint = lc($joint);
	}
	if (/^([ \t]*)\r$/) {
		$joint = $1;
		next;
	}
	# 
	if (/^([ \r\t]*)$/) {
		# skip blank lines
		next;
	}
	while ($joint =~ /(.*)\r$/) {
		# spin until no new carriage returns
		$joint = $1;
	}
	if ($joint =~ /^[XYZxyz]/) {  # centers and rotations
		$joint = uc($joint);
	}
	$joint =~ s/skullbase end/skullbase_end/g;
	if ($joint =~ /^([^ ]*) .*$/) {  # centers and rotations
		$joint = $1;
	}
	my %jointobj = ();
	#print STDERR "Joint found in centers, $joint\n";
	#print STDERR "Entering $joint \r\n";
	while(<CENTERS>) {
		chomp;
		my $line = $_;
		while ($line =~ /(.*)\r$/) {  # strip off carriage returns
			$line = $1;
		}
		if ($line =~ /___/) {
			# print STDERR "Exiting $joint \r\n";
			last;
		} elsif ($line =~ /^([XYZxyz]):  *([-0-9.e][-0-9.e]*) m ?\r*$/) { # centers and translations
			my $axis = uc($1);
			#print STDERR "$axis: ";
			my $number = $2;
			#print STDERR "$number\n";
			$jointobj{$axis} = $number;
		} elsif ($line =~ /^([XYZxyz]):  *([-0-9.e][-0-9.e]*) ° *\r*$/) {   # rotations
			my $axis = lc($1);
			#print STDERR "$axis: ";
			my $number = $2;
			# print STDERR "$number\n";
			#$jointobj{$axis} = $number;
		} else {
			# print STDERR "Bogus $line\n";
		}
	}
	print "$joint\r\n";
	print $jointobj{X}." ".$jointobj{Y}." ".$jointobj{Z}."\r\n";
}

close(CENTERS);
