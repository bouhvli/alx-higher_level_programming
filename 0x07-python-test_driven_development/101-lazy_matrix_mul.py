import numpy
def lazy_matrix_mul(m_a, m_b):
    try:
        new_mat = numpy.dot(m_a, m_b)
        return new_mat
    except Exception as e:
        print("{}".format(e))
