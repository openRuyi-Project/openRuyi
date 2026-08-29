# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}
# When bootstrapping new Python we need to build flit in bootstrap mode.
# The Python RPM dependency generators and pip are not yet available.
# Change to 1 for bootstrap
%if "%{flavor}" == "bootstrap"
%bcond bootstrap 1
%else
%bcond bootstrap 0
%endif

%global srcname flit_core

%if "%{flavor}" == "bootstrap"
Name:           python-flit-core-bootstrap
%else
Name:           python-flit-core
%endif
Version:        3.12.0
Release:        %autorelease
Summary:        PEP 517 build backend for packages using Flit
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://flit.pypa.io/
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:18f63100d6f94385c6ed57a72073443e1a71a4acb4339491615d0f16d6ff01b2
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
%if %{without bootstrap}
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
%endif

# RPM generators are not yet available when we bootstrap
%if %{with bootstrap}
Provides:       python3dist(flit-core) = %{version}-%{release}

Requires:       python(abi) = %{python3_version}
%else
Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}
%endif

%description
This provides a PEP 517 build backend for packages using Flit.
The only public interface is the API specified by PEP 517,
at flit_core.buildapi.

%prep
%autosetup -p1 -n flit_core-%{version}
# Remove vendored tomli that flit_core includes to solve the circular dependency on older Pythons
# (flit_core requires tomli, but flit_core is needed to build tomli).
# We don't use this, as tomllib is a part of standard library since Python 3.11.
# Remove the bits looking for the license files of the vendored tomli.
rm -rf flit_core/vendor
sed -iE 's/, *"flit_core\/vendor\/\*\*\/LICENSE\*"//' pyproject.toml

%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if %{with bootstrap}
%{python3} -m flit_core.wheel
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
%{python3} bootstrap_install.py --install-root %{buildroot} --installdir %{python3_sitelib} dist/flit_core-%{version}-py3-none-any.whl
# for consistency with %%pyproject_install/brp-python-rpm-in-distinfo:
echo rpm > %{buildroot}%{python3_sitelib}/flit_core-%{version}.dist-info/INSTALLER
rm %{buildroot}%{python3_sitelib}/flit_core-%{version}.dist-info/RECORD
%else
%pyproject_install
%endif

%files
%doc README.rst
%license %{python3_sitelib}/flit_core-*.dist-info/licenses/LICENSE
%{python3_sitelib}/flit_core-*.dist-info/
%{python3_sitelib}/flit_core/

%changelog
%autochangelog
