import numpy as np


def calc_sprime_c_td(Y_td, tau_td, i, pi):
    r'''
    Compute after-tax rate of return on savings invested in
    tax-deferred accounts.

    .. math::
        s^{'}_{c,td} = \frac{1}{Y_{td}}log((1-\tau_{td})*e^{i*Y_{td}}+
            \tau_{td}) - \pi

    Args:
        Y_td (scalar): number of years savings held in tax-deferred
            retirement account
        tau_td (scalar): effective marginal tax rate on investment
            income from tax-deferred accounts
        i (scalar): the nominal interest rate
        pi (scalar): the inflation rate

    Returns:
        sprime_c_td (scalar): the after-tax return on corporate
            investments made through tax-deferred accounts
    '''
    sprime_c_td = (
        (1 / Y_td) * np.log(((1 - tau_td) *
                             np.exp(i * Y_td)) + tau_td) - pi)

    return sprime_c_td


def calc_s_c_d_td(sprime_c_td, gamma, i, pi):
    r'''
    Compute the after-tax return on corprate debt investments made
    through tax-deferred accounts.

    ..math::
        s_{c,d,td} = \gamma(i-\pi) + (1-\gamma)s^{'}_{c,td}

    Args:
        sprime_c_td (scalar): the after-tax return on corporate
            investments made through tax-deferred accounts
        gamma (scalar): Fraction of debt owned through whole-life
            insurance policies
        i (scalar): the nominal interest rate
        pi (scalar): the inflation rate

    Returns:
        s_c_d_td (scalar): the after-tax return on corprate debt
            investments made through tax-deferred accounts

    '''
    s_c_d_td = gamma * (i - pi) + (1 - gamma) * sprime_c_td

    return s_c_d_td


def calc_s__d(s_d_td, alpha_d_ft, alpha_d_td, alpha_d_nt, tau_int,
              tau_w, i, pi):
    r'''
    Compute the after-tax return to debt investments.

    ..math::
        s_{j,d} = \alpha_{j,d,ft}((1-\tau_{int})i - \pi) +
            \alpha_{j,d,td}s_{j,d,td} + \alpha_{j,d,nt}(i-\pi) - \tau_{w}

    Args:
        s_d_td (scalar): after-tax return on debt investments made
            through tax-deferred acounts
        alpha_d_ft (scalar): fraction of debt investments held in
            full-tax accounts
        alpha_d_td (scalar): fraction of debt investments held in
            tax-deferred acounts
        alpha_d_nt (scalar): fraction of debt investments held in
            tax-free accounts
        tau_int (scalar): marginal tax rate on interest income
        tau_w (scalar): marginal tax rate on wealth
        i (scalar): nominal interest rate
        pi (scalar): inflation rate

    Returns:
        s__d (scalar): after-tax return on debt investments
    '''
    s__d = (alpha_d_ft * (((1 - tau_int) * i) - pi) + alpha_d_td *
            s_d_td + alpha_d_nt * (i - pi) - tau_w)

    return s__d


def calc_g__g(Y_g, tau_cg, m, E_c, pi):
    r'''
    Calculate the real, after-tax annualized return on short or long-
    term capital gains

    ..math::
        g_{icg} = \frac{1}{Y_{icg}}\ln\biggl[(1-\tau_{icg})e^{(\pi+mE)
            Y_{icg}}+\tau_{icg}\biggr] + \pi

    Args:
        Y_g (scalar): number of years asset held before gains realized
        tau_cg (scalar): tax rate on capital gains income
        m (scalar): share of equity return retained by the firm and reinvested
        E_c (scalar): expected, after-tax return on corporate equity
        pi (scalar): inflation rate

    Returns:
        g__g (scalar): real, after-tax annualized return on capital
            gains
    '''
    g__g = (
        (1 / Y_g) * np.log(((1 - tau_cg) * np.exp((pi + m * E_c) *
                                                  Y_g)) + tau_cg) - pi)

    return g__g


def calc_g(g_scg, g_lcg, omega_scg, omega_lcg, omega_xcg, m, E_c):
    r'''
    Calculate the after-tax, annualized, real rate of return on all
    capital gains

    ..math::
        g = \omega_{scg}\times g_{scg} + \omega_{lcg}\times g_{lcg} +
            \omega_{xcg}\times mE

    Args:
        g_scg (scalar): the real, after-tax annualized return on short-
            term capital gains
        g_lcg (scalar): the real, after-tax annualized return on long-
            term capital gains
        omega_scg (scalar): the fraction of capital gains that are
            short-term
        omega_lcg (scalar): the fraction of capital gains that are
            long-term
        m (scalar): share of equity return retained by the firm and reinvested
        E_c (scalar): expected, after-tax return on corporate equity

    Returns:
        g (scalar): the after-tax, annualized, real rate of return on
            all capital gains
    '''
    g = omega_scg * g_scg + omega_lcg * g_lcg + omega_xcg * m * E_c

    return g


def calc_s_c_e_td(Y_td, tau_td, i, pi, E_c):
    r'''
    Calculate the after-tax return on investmentes in corporate equity
    in tax-deferred accounts.

    ..math::
        s_{c,e,td} = \frac{1}{Y_{td}}\ln((1-\tau_{td})e^{(\pi+E)Y_{td}}
            +\tau_{td}) - \pi

    Args:
        Y_td (scalar): years investments are held in tax-deferred
            accounts
        tau_td (scalar): marginal tax rate on investments in
            tax-deferred accounts
        i (scalar): nominal interest rate
        pi (scalar): inflation rate
        E_c (scalar): expected, after-tax return on corporate equity

    Returns:
        s_c_e_td (scalar): the after-tax return on investmentes in
            corporate equity in tax-deferred accounts.
    '''
    s_c_e_td = (
        (1 / Y_td) * np.log(((1 - tau_td) *
                             np.exp((pi + E_c) * Y_td)) + tau_td) - pi)

    return s_c_e_td


def calc_s_c_e(s_c_e_ft, s_c_e_td, alpha_c_e_ft, alpha_c_e_td,
               alpha_c_e_nt, tau_w, E_c):
    r'''
    Calculate the after-tax return on investments in corporate equity

    ..math::
        s_{c,e} = \alpha_{c,e,ft}\times s_{c,e,ft} + \alpha_{c,e,td}
            \times s_{c,e,td} + \alpha_{c,e,nt}\times E - \tau_{w}

    Args:
        s_c_e_ft (scalar): after-tax return on investments in corporate
            equity in fully-taxable accounts
        s_c_e_td (scalar): after-tax return on investments in corporate
            equity in tax-deferred accounts
        alpha_c_e_ft (scalar): fraction of corporate equity investments
            made through full-taxable accounts
        alpha_c_e_td (scalar): fraction of corporate equity investments
            made through tax-deferred accounts
        alpha_c_e_nt (scalar): fraction of corporate equity investments
            made through tax-exempt accounts
        tau_w (scalar): marginal tax rate on wealth
        E_c (scalar): expected, after-tax return on corporate equity

    Returns:
        s_c_e (scalar): the after-tax return on investments in
            corporate equity
    '''
    s_c_e = (alpha_c_e_ft * s_c_e_ft + alpha_c_e_td * s_c_e_td +
             alpha_c_e_nt * E_c - tau_w)

    return s_c_e


def calc_s(p):
    '''
    Compute the after-tax rate of return to savers, s.

    .. math::
        s = ...

    Args:
        p (CCC Specification Object): model parameters

    Returns:
        (tuple): return to savers and required return to pass-through
            entities:

            * s_dict (dict): dictionary of s for investments in
                corporate and pass-through businesses and by type of
                financing
            * E_nc (scalar): required pre-tax return on pass-through
                investments

    '''
    # Compute after-tax rate of return on savings invested in
    # tax-deferred accounts
    sprime_c_td = calc_sprime_c_td(p.Y_td, p.tau_td,
                                   p.nominal_interest_rate,
                                   p.inflation_rate)
    # The after-tax return on corprate debt investments made through
    # tax-deferred accounts
    s_c_d_td = calc_s_c_d_td(sprime_c_td, p.gamma,
                             p.nominal_interest_rate, p.inflation_rate)
    # The after-tax return on corporate debt investments
    s_c_d = calc_s__d(s_c_d_td, p.alpha_c_d_ft, p.alpha_c_d_td,
                      p.alpha_c_d_nt, p.tau_int, p.tau_w,
                      p.nominal_interest_rate, p.inflation_rate)
    # The after-tax return on non-corporate debt investments made
    # through tax deferred accounts
    s_nc_d_td = s_c_d_td
    # The after-tax return on non-corporate debt investments
    s_nc_d = calc_s__d(s_nc_d_td, p.alpha_nc_d_ft, p.alpha_nc_d_td,
                       p.alpha_nc_d_nt, p.tau_int, p.tau_w,
                       p.nominal_interest_rate, p.inflation_rate)
    # The after-tax real, annualized return on short-term capital gains
    g_scg = calc_g__g(p.Y_scg, p.tau_scg, p.m, p.E_c, p.inflation_rate)
    # The after-tax real, annualized return on long-term capital gains
    g_lcg = calc_g__g(p.Y_lcg, p.tau_lcg, p.m, p.E_c, p.inflation_rate)
    # The after-tax real, annualized return on all capital gains
    g = calc_g(
        g_scg, g_lcg, p.omega_scg, p.omega_lcg, p.omega_xcg, p.m, p.E_c)
    # The after-tax return on corporate equity investments made in fully
    # taxable accounts
    s_c_e_ft = (1 - p.m) * p.E_c * (1 - p.tau_div) + g
    # The after-tax return on corporate equity investments made in
    # tax-deferred acounts
    s_c_e_td = calc_s_c_e_td(p.Y_td, p.tau_td, p.nominal_interest_rate,
                             p.inflation_rate, p.E_c)
    # The after-tax return on corporate equity investments
    s_c_e = calc_s_c_e(s_c_e_ft, s_c_e_td, p.alpha_c_e_ft,
                       p.alpha_c_e_td, p.alpha_c_e_nt, p.tau_w, p.E_c)
    # The after-tax return on corporate investments (all - debt and
    # equity combined)
    s_c = p.f_c * s_c_d + (1 - p.f_c) * s_c_e
    # The required rate of return on non-corporate investments
    E_nc = s_c_e
    # The after-tax rate of return on non-corporate equity investments
    s_nc_e = E_nc - p.tau_w
    # The after-tax return on non-corporate investments (all - debt and
    # equity combined)
    s_nc = p.f_nc * s_nc_d + (1 - p.f_nc) * s_nc_e
    # Return the after-tax rates of return on all types of investments
    s_dict = {'c': {'mix': s_c, 'd': s_c_d, 'e': s_c_e},
              'nc': {'mix': s_nc, 'd': s_nc_d, 'e': s_nc_e}}

    return s_dict, E_nc


def calc_r(p, f_dict, int_haircut_dict, E_dict, ace_dict):
    r'''
    Compute firm nominal discount rates

    ..math::
        r_{m,j} = f_{m,j}\[i(1-u_{j}) - \pi\] + (1-f_{m,j})E_{j} + \pi

    Args:
        p (CCC Specification Object): model parameters
        f_dict (dict): dictionary of fraction of investments financed
            with debt by entity type and financing method
        int_haircut_dict (dict): dictionary of haircut to interest paid
            deduction by entity type
        E_dict (dict): dictionary of pre-tax required rate of return by
            entity type
        ace_dict (dict): dictionary of allowance for corporate equity
            indicators by entity type

    Returns:
        r (dict): nominal, discount rate by entity type and financing
            method
    '''
    r = {}
    for t in p.entity_list:
        r[t] = {}
        for f in p.financing_list:
            r[t][f] = (
                f_dict[t][f] * (p.nominal_interest_rate *
                                (1 - (1 - int_haircut_dict[t]) *
                                 p.u[t])) + (1 - f_dict[t][f]) *
                (E_dict[t] + p.inflation_rate - E_dict[t] *
                 p.ace_int_rate * ace_dict[t])
            )

    return r


def calc_r_prime(p, f_dict, E_dict):
    r'''
    Compute firm nominal, after-tax rates of return

    ..math::
        r^{'}_{m,j} = f_{m,j}(i-\pi) + (1-f_{m,j})E_{j} + \pi

    Args:
        p (CCC Specification Object): model parameters
        f_dict (dict): dictionary of fraction of investments financed
            with debt by entity type and financing method
        E_dict (dict): dictionary of pre-tax required rate of return by
            entity type

    Returns:
        r_prime (dict): nominal, after-tax rate of return by entity type
            and financing method
    '''
    r_prime = {}
    for t in p.entity_list:
        r_prime[t] = {}
        for f in p.financing_list:
            r_prime[t][f] = (
                f_dict[t][f] * p.nominal_interest_rate +
                (1 - f_dict[t][f]) * (E_dict[t] + p.inflation_rate)
            )

    return r_prime
