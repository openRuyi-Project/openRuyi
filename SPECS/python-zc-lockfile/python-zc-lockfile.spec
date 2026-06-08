# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zc-lockfile
%global pypi_name zc_lockfile

Name:           python-%{srcname}
Version:        4.0
Release:        %autorelease
Summary:        Basic inter-process locks
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zc.lockfile
VCS:            git:https://github.com/zopefoundation/zc.lockfile.git
#!RemoteAsset:  sha256:d3ab0f53974296a806db3219b9191ba0e6d5cbbd1daa2e0d17208cb9b29d2102
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l zc +auto
# zc.lockfile.tests imports zope.testing, which is not packaged
BuildOption(check):  -e 'zc.lockfile.tests'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
zc.lockfile provides a basic, cross-platform, inter-process lock implemented
with a lock file.

%prep -a
# Upstream pins an exact setuptools build version; relax it to build against
# the setuptools shipped by openRuyi.
sed -i -E 's/setuptools *== *[0-9.]+/setuptools/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
