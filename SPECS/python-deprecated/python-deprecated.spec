# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname deprecated

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        Python @deprecated decorator to deprecate old classes, functions or methods
License:        MIT
URL:            https://github.com/laurent-laporte-pro/deprecated
VCS:            git:https://github.com/laurent-laporte-pro/deprecated.git
#!RemoteAsset:  sha256:b1b50e0ff0c1fddaa5708a2c6b0a6588bb09b892825ab2b214ac9ea9d92a5223
Source:         https://files.pythonhosted.org/packages/source/D/Deprecated/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(wrapt)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Deprecated provides a @deprecated decorator for Python to mark old classes,
functions, or methods as deprecated. It emits warnings when deprecated code
is called.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.rst
%doc README.md

%changelog
%autochangelog
