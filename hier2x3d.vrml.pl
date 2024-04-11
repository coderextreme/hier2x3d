#!/bin/perl
use strict;
# use warnings;

# Genrerate HAnim humanoid from hierarchy
#
# STDIN is a joint:segment hierarchy like ones that appear in the standard.  This is a requirement.
# The centers are pulled from sed.sh
# STDOUT is XML Skeleton

my %centerOf = ();

my $trailing_joints = "]\njoints [\n";
my $trailing_sites = "]\nsites [\n";
my $trailing_segments = "]\nsegments [\n";


sub printXML {
	my($prev) = shift @_;  # $prev is parent
	$prev->{line} =~ /^([ |]*)(.*) : (.*)\r*$/;
	my $parent_indent = length($1);
	my $parent_joint = $2;
	my $parent_segment = $3;
	# print STDERR "$1$2 : $3\r\n";

	if ($centerOf{$parent_joint}) {
		if ($parent_joint =~ /_end$/) {
			print " " x $parent_indent.'DEF Toddler_'.$parent_segment.' HAnimSegment { name "'.$parent_segment.'" children ['."\n";
                	print " " x ($parent_indent+2).'DEF Toddler_'.$parent_joint.' HAnimSite { name "'.$parent_joint.'" translation '.$centerOf{$parent_joint}.' }';
			$trailing_segments .= " " x $parent_indent.'USE Toddler_'.$parent_segment."\n";
			$trailing_sites    .= " " x $parent_indent.'USE Toddler_'.$parent_joint."\n";
			#print STDERR "Uncomment for purposes of matching " x $parent_indent."]}\n";
		} else {
			$trailing_joints .= " " x $parent_indent.'USE Toddler_'.$parent_joint.''."\n";
			print               " " x $parent_indent.'DEF Toddler_'.$parent_joint.' HAnimJoint { name "'.$parent_joint.'"';;
			print ' center '.$centerOf{$parent_joint}.' skinCoordIndex [ ] skinCoordWeight [ ] children ['."\n";
			#print STDERR "Uncomment for purposes of matching " x $parent_indent."]}\n";
		}
	}
	foreach my $child (@{$prev->{children}}) {   # go through child joints
		&printXML($child);
	}
	if ($centerOf{$parent_joint}) {
		print " " x $parent_indent."]}\n";
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
#X3D V4.0 utf8

PROFILE Immersive

COMPONENT HAnim:2
COMPONENT Texturing:3

NavigationInfo { type [ "EXAMINE" "ANY"] headlight FALSE }

PointLight { location 0 10 0 }
DirectionalLight { }
DirectionalLight { direction 0 0 1 }

DEF ToddlerView Transform { children [
 Transform { translation 0 0.924 0 children [ ]}
  DEF ViewToddler Viewpoint { description "Toddler Front View"
   position 0 1.5 2 orientation 0.5 0 0 -0.5 centerOfRotation 0 0.5 0 }
  DEF SceneCoordSystem Transform { scale 0.175 0.175 0.175 children [
   Inline { url ["JointCoordinateAxes.x3dv"] } ]}

DEF ToddlerHumanoid Group { children [

DEF Toddler HAnimHumanoid {
  skeleton [
HUMANHEADER
my $parent = &nodeConstructor(0);
&readHierarchy($parent);
&printXML($parent);
print "\n".$trailing_joints;
print "\n".$trailing_segments;
print "\n".$trailing_sites;
print << "HUMANFOOTER";
]
  skin [ 
DEF babyskin Shape { # 
 appearance Appearance {
   texture ImageTexture { url [ "IMAGE.png" ] }

   material Material {
emissiveColor 0 0 0 
specularColor 0 0 0
shininess 0.5
transparency 0 
		}
	} # appearance
	geometry DEF ToddlerSkin IndexedFaceSet { # triangle mesh
                creaseAngle 0 
		ccw    TRUE
		convex TRUE
		solid  TRUE
		coord DEF ToddlerSkinCoord Coordinate {
		    point [ ]
		}
		coordIndex [
		]
		texCoordIndex [
		]
                texCoord TextureCoordinate {
                    point [ ]
                }
	} # geometry
   } # Shape 
 ]  # skin 
 skinCoord USE ToddlerSkinCoord
}
]}   # Added by John
]}   # ToddlerView
HUMANFOOTER
