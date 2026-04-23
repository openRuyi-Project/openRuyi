# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bitarray

Name:           python-%{srcname}
Version:        3.8.0
Release:        %autorelease
Summary:        Efficient arrays of booleans for Python
License:        PSF-2.0
URL:            https://github.com/ilanschnell/bitarray
#!RemoteAsset:  sha256:3eae38daffd77c9621ae80c16932eea3fb3a4af141fb7cc724d4ad93eff9210d
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(setuptools) >= 42

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
bitarray provides an object type which efficiently represents an array of booleans.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
