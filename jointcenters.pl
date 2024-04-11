#!/bin/perl
use strict;
use warnings;

open(TABLE, "sh sed.sh|");

while(<TABLE>) {
	chomp;
	my $joint = $_;
	my $center = <TABLE>;
	chomp $center;
	my @xyz = split(/[ \t\r]+/, $center);
	print "$joint\r\nX: ".$xyz[0]." m\r\nY: ".$xyz[1]." m\r\nZ: ".$xyz[2]." m\r\n________________________________________\r\n";
}

close(TABLE);
