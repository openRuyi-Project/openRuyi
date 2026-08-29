# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-ulid
%global pypi_name python_ulid

Name:           python-%{srcname}
Version:        3.1.0
Release:        %autorelease
Summary:        Universally unique lexicographically sortable identifier
License:        MIT
URL:            https://github.com/mdomke/python-ulid
#!RemoteAsset:  sha256:ff0410a598bc5f6b01b602851a3296ede6f91389f913a5d5f8c496003836f636
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ulid

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(typing-extensions)

Requires:       python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A ULID is a universally unique lexicographically sortable identifier.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/ulid

%changelog
%autochangelog
