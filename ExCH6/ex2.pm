dtmc

module ex2

	// local state
	s : [0..4];
	a : bool;
	b : bool;
	
	[] s=0 -> (s'=1) & (a'=true);
	[] s=0 -> (s'=4) & (b'=true);
	[] s=1 -> (s'=2) & (a'=true);
	[] s=1 -> (s'=2) & (b'=true);
	[] s=2 -> (s'=3) & (b'=true) & (a'=false);
	[] s=3 -> (s'=3) & (b'=true);
	[] s=3 -> (s'=0) & (b'=false);
	[] s=4 -> (s'=4) & (b'=true);
	
endmodule

init
	(s=0 | s=3) & a=false & b=false
endinit