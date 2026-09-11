# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname virtualenv

Name:           python-%{srcname}
Version:        21.7.4
Release:        %autorelease
Summary:        Tool to create isolated Python environments
License:        MIT
URL:            https://github.com/pypa/virtualenv
#!RemoteAsset:  sha256:c9d960c95fa458171e58222a5ccab7465298e4b6559977865e627c4719f1e825
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Use system wheels instead of bundled ones
Patch2000:      2000-use-system-wheels.patch

BuildOption(install):  -l %{srcname}
# Exclude broken modules from import tests
BuildOption(check):  -e '*activate_this' -e '*windows*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools-wheel
BuildRequires:  python-pip-wheel
# Tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(pytest-mock)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}
# For convenience
Provides:       virtualenv = %{version}-%{release}

Requires:       python-setuptools-wheel
Requires:       python-pip-wheel

%description
virtualenv is a tool to create isolated Python environments.
A subset of it has been integrated into the Python standard library under
the venv module. The venv module does not offer all features of this library,
to name just a few more prominent:

- is slower (by not having the app-data seed method),
- is not as extendable,
- cannot create virtual environments for arbitrarily installed Python versions
  (and automatically discover these),
- does not have as rich programmatic API (describe virtual environments
  without creating them).

%prep -a
# Remove the wheels provided by RPM packages
rm -f src/virtualenv/seed/wheels/embed/pip-*
rm -f src/virtualenv/seed/wheels/embed/setuptools-*
rm -f src/virtualenv/seed/wheels/embed/wheel-*

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Skip tests that require internet access & bundled wheels & automatic updates
%pytest -W ignore::DeprecationWarning \
    -vv -k "not test_download_ and \
            not test_can_build_c_extensions and \
            not test_create_distutils_cfg and \
            not test_seed_link_via_app_data and \
            not test_embed_wheel_versions and \
            not test_embed_wheel_oldest_supported_is_present and \
            not test_embed_wheel_future_version_reuses_newest and \
            not test_wheel_ and \
            not test_base_bootstrap_via_pip_invoke and \
            not test_acquire and \
            not test_bundle and \
            not test_periodic_update and \
            not test_py_info_cache_clear and \
            not test_app_data_parallel_ok and \
            not test_base_bootstrap_link_via_app_data_not_writable"

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/virtualenv

%changelog
%autochangelog
