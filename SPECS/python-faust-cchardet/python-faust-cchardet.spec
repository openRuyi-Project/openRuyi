# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname faust-cchardet
%global pypi_name faust_cchardet

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        High speed universal character encoding detector
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://github.com/faust-streaming/cchardet
#!RemoteAsset:  sha256:ffae2d6fccd414adf542931602b7b28239d6d85a22f493e54df02d6bbc7d3dcd
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(generate_buildrequires):  -p
BuildOption(install):  cchardet

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cChardet is high speed universal character encoding detector.

%files -f %{pyproject_files}
%doc README.md
%license COPYING
%{_bindir}/cchardetect

%changelog
%autochangelog
