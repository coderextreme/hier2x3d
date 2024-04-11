#!/bin/perl
use strict;
# use warnings;

# Genrerate HAnim humanoid from hierarchy
#
# STDIN is a joint:segment hierarchy like ones that appear in the standard.  This is a requirement.
# The centers are pulled from sed.sh
# STDOUT is XML Skeleton

my %centerOf = ();

my $trailing_joints = "";
my $trailing_sites = "";
my $trailing_segments = "";


sub printXML {
	my($prev) = shift @_;  # $prev is parent
	$prev->{line} =~ /^([ |]*)(.*) : (.*)\r*$/;
	my $parent_indent = length($1);
	my $parent_joint = $2;
	my $parent_segment = $3;
	# print STDERR "$1$2 : $3\r\n";

	if ($centerOf{$parent_joint}) {
		if ($parent_joint =~ /_end$/) {
			print " " x $parent_indent.'<HAnimSegment DEF="Toddler_'.$parent_segment.'" name="'.$parent_segment.'">'."\n";
			print " " x ($parent_indent+2).'<HAnimSite DEF="Toddler_'.$parent_joint.'" name="'.$parent_joint.'" translation="'.$centerOf{$parent_joint}.'"/>';
			print " " x $parent_indent.'</HAnimSegment>'."\n";
			$trailing_segments .= " " x $parent_indent.'<HAnimSegment USE="Toddler_'.$parent_segment.'" name="'.$parent_segment.'" containerField="segments"/>'."\n";
			$trailing_sites .= " " x $parent_indent.'<HAnimSite USE="Toddler_'.$parent_joint.'" name="'.$parent_joint.'" containerField="sites"/>'."\n";
		} else {
			$trailing_joints .= " " x $parent_indent.'<HAnimJoint USE="Toddler_'.$parent_joint.'" name="'.$parent_joint.'" containerField="joints"/>'."\n";
			print " " x $parent_indent.'<HAnimJoint DEF="Toddler_'.$parent_joint.'" name="'.$parent_joint.'"';
			if ($parent_indent == 0) {
				print " " x $parent_indent." containerField='skeleton'";
			}
			print ' center="'.$centerOf{$parent_joint}.'" skinCoordIndex=" 0 " skinCoordWeight=" 0 "';
			print ">\n";
		}
	}
	foreach my $child (@{$prev->{children}}) {   # go through child joints
		&printXML($child);
	}
	if ($centerOf{$parent_joint}) {
		# print STDERR "$parent_joint center = $centerOf{$parent_joint}\n";
		if ($parent_joint =~ /_end$/) {
		} else {
			print " " x $parent_indent."</HAnimJoint>\n";
		}
	}
}

open(TABLE, "sh sed.sh|");

while(<TABLE>) {
	chomp;
	my $joint = $_;
	$joint =~ s/\r*$//;
	my $center = <TABLE>;
	$center =~ s/\r*$//;
	chomp $center;
	# print STDERR "$joint center = $center\r\n";
	$centerOf{$joint} = $center;
}

close(TABLE);


sub nodeConstructor {
	my $parent = shift @_;
	my $line = <STDIN>;
	if (!defined ($line)) {
		# print STDERR "Bailing!\n";
		return 0;
	} else {
		# print $line;
	}
	$line =~ s/\r*$//;
	$line =~ m/^([ |]*)(.*) : (.*)$/;
	# print STDERR "OUCH $1$2\r\n";
	my $indent = length($1);
	my $joint = $2;
	my $segment = $3;
	my $obj = {};
	$obj->{line} = $line;
	$obj->{indent} = $indent;
	$obj->{joint} = $joint;
	$obj->{parent} = $parent;
	$obj->{children} = ();  # initialize with no childred
	if ($parent) {
		push @{$parent->{children}}, $obj;
	}
	return $obj;
}

sub readHierarchy {
	my $parent = shift @_;
	my $child = {};
	while ($child = &nodeConstructor($parent)) {
		&readHierarchy($child);
	}
	return $parent;
}

print << "HUMANHEADER";
<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 4.0//EN" "https://www.web3d.org/specifications/x3d-4.0.dtd">
<X3D profile="Immersive" version="4.0" xmlns:xsd="http://www.w3.org/2001/XMLSchema-instance" xsd:noNamespaceSchemaLocation="https://www.web3d.org/specifications/x3d-4.0.xsd">
<head>
  <component level='1' name='HAnim'/>
  <meta content='JohnBoy.x3d' name='title'/>
  <meta name='identifier' content='http://www.web3d.org/x3d/content/examples/HumanoidAnimation/JohnBoy.x3d'/>
  <meta name='description' content='An attempt at a standard LOA-4 skeleton'/>
  <meta name='generator' content='h2.pl'/>
  <meta name='modified' content="14 Jan 2023"/>
  <meta content='John Carlson' name='creator'/>
  <meta content='9 November 2020' name='created'/>
  <meta content='../license.html' name='license'/>
</head>
<Scene>
    <NavigationInfo speed='1.5' type='"EXAMINE" "ANY"'/>
    <Viewpoint centerOfRotation='0 0 0' description='default'/> 
    <HAnimHumanoid DEF='Toddler_HAnim'  info='"humanoidVersion=2.0"' name='HAnim' scale='1 1 1' translation='0 0 0' version='2.0'>
HUMANHEADER
my $parent = &nodeConstructor(0);
&readHierarchy($parent);
&printXML($parent);
print $trailing_joints;
print $trailing_segments;
print $trailing_sites;
print << "HUMANFOOTER";
    </HAnimHumanoid>
</Scene>
</X3D>
HUMANFOOTER
