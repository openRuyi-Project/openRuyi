# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-runner

Name:           python-%{srcname}
Version:        6.0.1
Release:        %autorelease
Summary:        Invoke pytest as a distutils command
License:        MIT
URL:            https://github.com/pytest-dev/pytest-runner
#!RemoteAsset:  sha256:70d4739585a7008f37bf4933c013fdb327b8878a5a69fcbb3316c88882f0f49b
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Dead upstream, remove pkg_resources
# https://salsa.debian.org/python-team/packages/pytest-runner/-/blob/debian/6.0.1-1/debian/patches/stop-using-pkg_resources.patch
Patch2000:      2000-stop-using-pkg_resources.patch

BuildOption(install):  -l ptr

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pytest-runner provides setuptools commands for invoking pytest with dependency
resolution.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
