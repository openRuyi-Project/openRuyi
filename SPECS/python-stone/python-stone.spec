# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname stone

Name:           python-%{srcname}
Version:        3.5.3
Release:        %autorelease
Summary:        Interface description language for APIs
License:        MIT
URL:            https://github.com/dropbox/stone
#!RemoteAsset:  sha256:d0d99f14d154452e71b3e2752efdbbb1769e4fecbc1291b1dfd1a046f7b6a1cb
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch2000:      2000-allow-setuptools-scm-10.patch

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jinja2) >= 3.0.3
BuildRequires:  python3dist(packaging) >= 21
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Stone is an interface description language used to define APIs and generate
language bindings from those definitions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/stone

%changelog
%autochangelog
