#!/bin/perl
use strict;
use warnings;

# Genrerate HAnim humanoid from hierarchy
# $ARGV[0] -- hierarchy file
# $ARGV[1] -- python output

my %joints = ();
my $segments = "";

sub printPython {
	my($prev) = @_;  # $prev is $child
	$prev->{line} =~ /([ |]*)(.*) : (.*)/;
	my $parent_indent = length($1);
	my $parent_joint = $2;
	my $parent_segment = $3;
	if ($joints{$parent_joint}) {
		my $cenpj = $joints{$parent_joint};
		my @cenpj = split(/[ ,\t]+/, $cenpj);
		$cenpj = "$cenpj[0], $cenpj[2], $cenpj[1]";
		# print OUTPUT " " x $prev->{indent}. '("'.$parent_joint.'", ('.$cenpj.'), (0, 0, 0)),'."\n";
		foreach my $jnt (@{$prev->{children}}) {   # go through child joints
			&printPython($jnt);
			if ($jnt->{joint} =~ m/_tarsal_interphalangeal_1$/) { # we need to take this out
				# skip
			} else {
				$segments .= " " x $jnt->{indent}. '("'.$parent_joint.'", "'.$jnt->{joint}.'"),'."\n";
				my $cencj = $joints{$jnt->{joint}};
				my @cencj = split(/[ ,\t]+/, $cencj);
				$cencj = "$cencj[0], $cencj[2], $cencj[1]";
				print OUTPUT " " x $jnt->{indent}. '("'.$jnt->{joint}.'", ('.$cencj.'), ('.$cenpj.')),'."\n";
			}
		}
	}
}

sub readHierarchy {
	my $input = $ARGV[0];
	print "$input\n";
	open (HIER, "<$input");
	my $prev = {};
	$prev->{children} = ();
	$prev->{indent} = -1;
	foreach (<HIER>) {
		my $line = $_;
		chomp $line;
		$line =~ /([ |]*)(.*) : (.*)/;
		my $indent = length($1);
		my $joint = $2;
		my $segment = $3;
		my $obj = {};
		$obj->{line} = $line;
		$obj->{indent} = $indent;
		$obj->{joint} = $joint;
		$obj->{segment} = $segment;
		$obj->{children} = ();
		# print "$line\n";
		if ($obj->{indent} > $prev->{indent}) {
			$obj->{parent} = $prev;
			# print "$obj->{joint} parent 1 is $prev->{joint}\n";
		} elsif ($obj->{indent} == $prev->{indent}) {

			$obj->{parent} = $prev->{parent};
			# print "$obj->{joint} parent 2 is $prev->{parent}->{joint}\n";
		} else {
			while ($obj->{indent} < $prev->{indent}) {
				$prev = $prev->{parent};
			}
			$obj->{parent} = $prev->{parent};
			# print "$obj->{joint} parent 3 is $prev->{joint}\n";
		}
		push @{$obj->{parent}->{children}}, $obj;
		$prev = $obj;
	}
	while (0 < $prev->{indent}) {
		$prev = $prev->{parent};
	}
	close(HIER);
	return $prev;
}

open(TABLE, "sh sed.sh|");

while(<TABLE>) {
	chomp;
	my $joint = $_;
	my $center = <TABLE>;
	chomp $center;
	$joints{$joint} = $center;
}

close(TABLE);

my $results = $ARGV[1];
print "$results\n";
open(OUTPUT, ">$results");

print OUTPUT << "HUMANHEADER";
import bpy

skeleton = bpy.data.objects.new("Armature", bpy.data.armatures.new("Armature"))
bpy.context.collection.objects.link(skeleton)
bpy.context.view_layer.objects.active = skeleton
skeleton.select_set(True)
bpy.ops.object.mode_set(mode='EDIT')

# Create joints
joints = [
HUMANHEADER
my $prev = &readHierarchy();
$prev->{line} =~ /([ |]*)(.*) : (.*)/;
my $root_indent = length($1);
my $cenrj = $joints{$prev->{joint}};
if ($cenrj) {
	my @cenrj = split(/[ ,\t]+/, $cenrj);
	$cenrj = "$cenrj[0], $cenrj[2], $cenrj[1]";
	print OUTPUT " " x $root_indent. '("'.$prev->{joint}.'", ('.$cenrj.'), (0, 0, 0)),'."\n";
}
&printPython($prev);
print OUTPUT << "HUMANBODY";
]\n
for joint in joints:
    joint_name, joint_start, joint_end = joint
    bpy.ops.armature.bone_primitive_add(name=joint_name)
    new_segment = skeleton.data.edit_bones[joint_name]
    new_segment.head = joint_start
    new_segment.tail = joint_end

# Connect joints
segments = [
HUMANBODY
print OUTPUT $segments;
print OUTPUT << "HUMANFOOTER";
]

for segment in segments:
    parent_joint, child_joint = segment
    parent = skeleton.data.edit_bones[parent_joint]
    child = skeleton.data.edit_bones[child_joint]
    child.parent = parent

# Exit edit mode
bpy.ops.object.mode_set(mode='OBJECT')
HUMANFOOTER
close(OUTPUT);
