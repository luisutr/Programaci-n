


def pi_leibniz_comp():
    n = 5000000
    return 4 * sum((-1.)**k / (2*k + 1) for k in xrange(n))


def pi_leibniz():
    num_pi=0
    for k in xrange(5000000):
        num_pi+=4 * ((-1.)**k / (2*k + 1))
    return  num_pi

print pi_leibniz()