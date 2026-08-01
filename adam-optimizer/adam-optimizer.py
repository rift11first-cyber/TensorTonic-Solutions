import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param = np.asarray(param, dtype=float)
    grad = np.asarray(grad, dtype=float)
    m = np.asarray(m, dtype=float)
    v = np.asarray(v, dtype=float)
    m1 = (beta1)*(m) + (1.0-beta1)*grad
    v1 = (beta2)*(v) + (1.0-beta2)*(grad**2)
    mm = m1/(1-beta1**t) 
    vv = v1/(1-beta2**t)
    p_n = param-lr*(mm/(np.sqrt(vv)+eps))
    return p_n , m1 , v1 
    
    