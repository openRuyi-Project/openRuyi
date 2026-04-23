# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname coverage

Name:           python-%{srcname}
Version:        7.13.4
Release:        %autorelease
Summary:        Code coverage measurement for Python
License:        Apache-2.0
URL:            https://github.com/coveragepy/coveragepy
#!RemoteAsset:  sha256:e5c8f6ed1e61a8b2dcdf31eb0b9bbf0130750ca79c1c49eb898e2ad86f5ccc91
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(setuptools)

%description
Coverage.py is a Python module that measures code coverage during Python
execution. It uses the code analysis tools and tracing hooks provided in the
Python standard library to determine which lines are executable, and which
have been executed.

%pyproject_extras_subpkg -n python-coverage toml

%generate_buildrequires
%pyproject_buildrequires -x toml

%install -a
rm %{buildroot}/%{_bindir}/coverage
# make compat symlinks
pushd %{buildroot}%{_bindir}
ln -s coverage-%{python3_version} coverage-3
ln -s coverage-%{python3_version} coverage
popd

%files -f %{pyproject_files}
%doc README.rst
%license NOTICE.txt
%{python3_sitearch}/a1_coverage.pth
%{_bindir}/coverage
%{_bindir}/coverage3
%{_bindir}/coverage-3*

%changelog
%autochangelog
