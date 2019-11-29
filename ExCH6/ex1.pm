dtmc

module ex1

	// local state
	s : [1..4];
	r : bool;
	y : bool;
	g : bool;
	b : bool;
	
	[] s=1 -> (s'=3) & (g'=true);
	[] s=3 -> (s'=2) & (y'=true);
	[] s=2 -> (s'=4) & (b'=true);
	[] s=4 -> (s'=2) & (y'=true);
	[] s=2 -> (s'=1) & (r'=true);
	
endmodule

init
	s=4 & r=false & b=false & y=false & g=false
endinit