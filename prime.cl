__kernel void prime(__global int* result, int n)
{
    unsigned int gid = get_global_id(0);
    unsigned int L= get_local_size(0);
	unsigned int i;
	unsigned int j;
	unsigned int ok=1;

    for(i=gid; i<n; i=i+L){
    ok=1;
        if(i==0|| i==1){
            ok=0;
        }
        for(j=2; j<=i/2; j++) {
            if( (i%j)==0 ) {
                ok=0;
            }
        }
        if(ok) {
            result[i]=1;
        } else {
            result[i]=0;
        }
    }

}