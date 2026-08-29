# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hiredis

Name:           python-%{srcname}
Version:        3.3.1
Release:        %autorelease
Summary:        Python wrapper for hiredis
License:        MIT
URL:            https://github.com/redis/hiredis-py
#!RemoteAsset:  sha256:da6f0302360e99d32bc2869772692797ebadd536e1b826d0103c72ba49d38698
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

# TODO: We need some kind of CI to detect this - 251
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python extension that wraps protocol parsing code in hiredis.
It primarily speeds up parsing of multi bulk replies.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
