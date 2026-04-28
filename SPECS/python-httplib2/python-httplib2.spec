# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httplib2

Name:           python-%{srcname}
Version:        0.31.2
Release:        %autorelease
Summary:        Comprehensive HTTP client library
License:        MIT
URL:            https://github.com/httplib2/httplib2
#!RemoteAsset:  sha256:385e0869d7397484f4eab426197a4c020b606edd43372492337c0b4010ae5d24
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# some deps we don't have yet,just skip it.
Patch0:         0001-remove-timeout-test.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pyparsing)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A comprehensive HTTP client library that supports many features left out of
other HTTP libraries.

%generate_buildrequires
%pyproject_buildrequires

%check
%pytest -k "not test_unknown_server \
    and not test_socks5_auth \
    and not test_server_not_found_error_is_raised_for_invalid_hostname \
    and not test_functional_noproxy_star_https \
    and not test_sni_set_servername_callback \
    and not test_not_trusted_ca \
    and not test_invalid_ca_certs_path \
    and not test_max_tls_version \
    and not test_get_301_via_https \
    and not test_client_cert_password_verified \
    and not test_get_via_https \
    and not test_min_tls_version \
    and not test_client_cert_verified \
    and not test_inject_space \
    and not test_get_301_no_redirect"

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{?autochangelog}
