#!/usr/bin/perl

@periods = (60,300,900,1800,3600,10800,21600,43200,86400);

if (exists $ENV{'START'}) {
	$start = $ENV{'START'};
}
$end = time();

$f = $start - ($start % 86400);
$g = $end - ($end % 86400);

# print "@ARGV $ARGV\n";

# load table
foreach $sensor (@ARGV) {
    # print "sensor = $sensor\n";

    for ($day = $f ; $day <= $g ; $day += 86400) {
	print "$sensor $day.sum\n";
        open(FH,"$sensor/$day.sum");
        while (<FH>) {
	    chomp;
	    my ($caltime,$d,$sum,$n,$mean,$min,$max) = split();
	    $table{$caltime}{$d}{$sensor} = $mean;
        }
        close(FH);
    }
}

# dump table
foreach $t (keys %table) {
    foreach $d ( keys %{ $table{$t} }) {
	
	printf("%s %d",$t,$d);
	for ($c=0 ; $c<=$#ARGV ; $c++) {
	    $sensor = $ARGV[$c];
	    # foreach $sensor ( keys %{ $table{$t}{$d} }) {
	    if (exists $table{$t}{$d}{$sensor}) {
		printf("\t%7.2f",(1/1000.0)*$table{$t}{$d}{$sensor});
	    }
	    else {
		printf("\t     --");
	    }
	}
	printf("\n");
    }
}

printf("SENSORS:");
for ($c = 0 ; $c<=$#ARGV ; $c++) {
    printf(" %s",$ARGV[$c]);
}
printf("\n");
