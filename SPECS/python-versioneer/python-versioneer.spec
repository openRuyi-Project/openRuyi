# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname versioneer

Name:           python-%{srcname}
Version:        0.29
Release:        %autorelease
Summary:        VCS-based management of project version strings
License:        Unlicense
URL:            https://github.com/python-versioneer/python-versioneer
#!RemoteAsset:  sha256:5ab283b9857211d61b53318b7c792cf68e798e765ee17c27ade9f6c924235731
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Versioneer is a tool to automatically update version strings (in
setup.py and the conventional ‘from PROJECT import _version’ pattern)
by asking the version control system about the current tree.

%pyproject_extras_subpkg -n python-versioneer toml

%generate_buildrequires
%pyproject_buildrequires -x toml

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/versioneer

%changelog
%autochangelog
