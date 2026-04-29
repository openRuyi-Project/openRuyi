# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tox-current-env
%global pypi_name tox_current_env

Name:           python-%{srcname}
Version:        0.0.16
Release:        %autorelease
Summary:        Tox plugin to run tests in current Python environment
License:        MIT
URL:            https://github.com/fedora-python/tox-current-env
VCS:            git:https://github.com/fedora-python/tox-current-env.git
#!RemoteAsset:  sha256:2e453c3e82e837d35846004a678db4504e24e5c0419d6e42aa07ca8294fad1bd
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# The default pyproject check in openRuyi is an import smoke test. Exclude
# hooks3 because it implements the legacy tox 3 hook path and fails with tox 4.
BuildOption(check):  -e tox_current_env.hooks3 tox_current_env
BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tox) >= 4.0.0
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The tox-current-env plugin for tox allows running tests in the current Python
environment rather than creating a new virtual environment. This is especially
useful in RPM packaging environments where dependencies are already installed
globally and we simply want tox to execute the test suite against the installed
system packages.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
