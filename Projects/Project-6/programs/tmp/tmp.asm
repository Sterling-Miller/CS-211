# Lovingly crafted by the robots of CIS 211
# 2023-03-08 23:50:43.036347 from programs/mal/read_add_print.mal
#
    LOAD r14,const_15
   STORE  r14,var_x
    LOAD r14,const_20
   STORE  r14,var_y
    LOAD r14,var_x
    LOAD r13,var_y
   ADD  r14,r14,r13
   STORE  r14,r0,r0[511]
	HALT  r0,r0,r0
const_15:  DATA 15
const_20:  DATA 20
var_x: DATA 0
var_y: DATA 0
