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
        $sum{$t}{$p} += $val;
        $count{$t}{$p}++;
	if (!exists $min{$t}{$p} || $val < $min{$t}{$p}) {
		$min{$t}{$p} = $val;
	}
	if (!exists $max{$t}{$p} || $val > $max{$t}{$p}) {
		$max{$t}{$p} = $val;
	}
    }
}

# compute means of compiled summaries
foreach $t (keys %count) {
    #print "$t\n";
    foreach $p ( keys %{ $count{$t} }) {
	#print "$t $p\n";
        $mean{$t}{$p} = 
            $sum{$t}{$p} /
            $count{$t}{$p};
        $mean{$t}{$p} = int($mean{$t}{$p} + 0.5);
        print "$t $p $sum{$t}{$p} $count{$t}{$p} $mean{$t}{$p} $min{$t}{$p} $max{$t}{$p}\n";
    }
}

