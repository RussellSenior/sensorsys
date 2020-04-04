#!/usr/bin/perl

@periods = (60,300,900,1800,3600,10800,21600,43200,86400);

if (exists $ENV{'K'}) {
	$k = $ENV{'K'};
}
else {
	$k = 1;
}

while (<>) {
    chomp;
    my ($caltime,$val) = split();
    $val = $val * $k;
    # print "$caltime $val\n";
    foreach my $p (@periods) {
        my $t = $caltime - ($caltime % $p);
        $sum{$p}{$t} += $val;
        $count{$p}{$t}++;
	if (!exists $min{$p}{$t} || $val < $min{$p}{$t}) {
		$min{$p}{$t} = $val;
	}
	if (!exists $max{$p}{$t} || $val > $max{$p}{$t}) {
		$max{$p}{$t} = $val;
	}
    }
}

# compute means of compiled summaries
print "{ \"summary\": [\n";
my $first_p = 1;
foreach $p (keys %count) {
    #print "$p\n";
    if (!$first_p) {
        print ",";
    } else { $first_p = 0; }
    print "{ \"period\": $p,\n \"t\": [";
    $first_t = 1;
    @times = sort { $a <=> $b} keys %{ $count{$p} };
    foreach $t (@times) {
	if (!$first_t) {
	    print ",";
        } else { $first_t = 0; }
	print "$t";
    }
    print "],\n \"sum\": [";
    $first_t = 1;
    foreach $t (@times) {
	if (!$first_t) {
	    print ",";
        } else { $first_t = 0; }
        print "$sum{$p}{$t}";
    }
    print "],\n \"count\": [";
    $first_t = 1;
    foreach $t (@times) {
	if (!$first_t) {
	    print ",";
        } else { $first_t = 0; }
        print "$count{$p}{$t}";
    }
    print "],\n \"mean\": [";
    $first_t = 1;
    foreach $t (@times) {
	if (!$first_t) {
	    print ",";
        } else { $first_t = 0; }
        $mean = 
            $sum{$p}{$t} /
            $count{$p}{$t};
        $mean = int($mean + 0.5);
        print "$mean";
    }
    print "],\n \"min\": [";
    $first_t = 1;
    foreach $t (@times) {
	if (!$first_t) {
	    print ",";
        } else { $first_t = 0; }
        print "$min{$p}{$t}";
    }
    print "],\n \"max\": [";
    $first_t = 1; 
    foreach $t (@times) {
	if (!$first_t) {
	    print ",";
        } else { $first_t = 0; }
        print "$max{$p}{$t}";
    }
    print "] }\n";
}
print "] }\n";

    
