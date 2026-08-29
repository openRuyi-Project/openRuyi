# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-xdist
%global binary_name pytest_xdist

%bcond tests 1

Name:           python-%{srcname}
Version:        3.8.0
Release:        %autorelease
Summary:        pytest plugin for distributed testing and loop-on-failing modes
License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
#!RemoteAsset:  sha256:7e578125ec9bc6050861aa93f2d59f1d8d085595d6551c2c90b6f4fad8d3a9f1
Source0:        https://files.pythonhosted.org/packages/source/p/%{binary_name}/%{binary_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l xdist

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(execnet) >= 1.1
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(setproctitle)
BuildRequires:  python3dist(psutil) >= 3
BuildRequires:  python3dist(pytest) >= 6
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(execnet) >= 2.1
Requires:       python3dist(pytest) >= 7.0.0

Recommends:     python3dist(psutil) >= 3.0
Recommends:     python3dist(filelock)
Recommends:     python3dist(setproctitle)

# Update baipp to 2.14 #1266 https://github.com/pytest-dev/pytest-xdist/pull/1266/commits/46084729fd2785c626d8c4add0b5e695eb4fdde9
# Fix CI for pytest 9.0+ #1272 https://github.com/pytest-dev/pytest-xdist/pull/1272
%patchlist
0001-python-pytest-xdist-3.8.0-fix-for-pytest-9.0+.patch
0002-python-pytest-xdist-3.8.0-update-biapp.patch

%description
The pytest-xdist plugin extends pytest with new test execution
modes, the most used being distributing tests across multiple
CPUs to speed up test execution.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
sed -i 's/\r//' README.rst

%if %{with tests}
%check -a
export CI=true
# temp skip failed test cases due to internal API changes in pytest 9.0
%pytest -v \
  -k "not test_remote_usage_prog and not test_handlecrashitem_one"
%endif

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
