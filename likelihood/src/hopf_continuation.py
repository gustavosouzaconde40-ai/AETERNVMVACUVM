# AETERNVM VACUVM - Matrix-Free Hopf Continuation & Shift-Invert Solver
import numpy as np
from numpy.fft import fftn, ifftn
from scipy.sparse.linalg import LinearOperator, eigs, gmres
from .aeternvm_model import solve_Psi0_from_I, mu_eff_of_I

def make_A_operator(N, L, Khat, ksq, adv_mult, Sprime, mu_eff_scalar, D=0.05, adv_coeff=0.6):
    shape = (N, N, N, N)
        total_size = N**4
            ksq_local = ksq
                Khat_local = Khat
                    adv_local = adv_mult

                        def matvec(v):
                                v4 = v.reshape(shape)
                                        Vf = fftn(v4)
                                                lap = np.real(ifftn(-ksq_local * Vf)) * D
                                                        conv = np.real(ifftn(Khat_local * Vf)) * Sprime
                                                                adv = np.real(ifftn(1j * adv_local * Vf)) * adv_coeff
                                                                        out = - (mu_eff_scalar * v4) + lap + conv + adv
                                                                                return out.ravel().astype(np.complex128)

                                                                                    return LinearOperator((total_size, total_size), matvec=matvec, dtype=np.complex128)

                                                                                    def make_shift_invert_operator_from_A(Aop, sigma, gmres_tol=1e-6, gmres_maxiter=400):
                                                                                        size = Aop.shape[0]
                                                                                            def binv_matvec(v):
                                                                                                    def matvec_Ashift(x):
                                                                                                                return Aop.matvec(x) - sigma * x
                                                                                                                        Ashift_op = LinearOperator((size, size), matvec=matvec_Ashift, dtype=np.complex128)
                                                                                                                                x, info = gmres(Ashift_op, v, tol=gmres_tol, maxiter=gmres_maxiter)
                                                                                                                                        if info != 0:
                                                                                                                                                    x, info2 = gmres(Ashift_op, v, tol=gmres_tol*10, maxiter=gmres_maxiter*2)
                                                                                                                                                                if info2 != 0:
                                                                                                                                                                                raise RuntimeError(f"GMRES failed for sigma={sigma}")
                                                                                                                                                                                        return x
                                                                                                                                                                                            return LinearOperator((size, size), matvec=binv_matvec, dtype=np.complex128)