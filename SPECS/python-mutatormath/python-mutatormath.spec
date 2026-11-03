# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mutatormath

Name:           python-%{srcname}
Version:        3.0.1
Release:        %autorelease
Summary:        Python library for multidimensional interpolation
License:        BSD-3-Clause
URL:            https://github.com/LettError/MutatorMath
#!RemoteAsset:  sha256:8127c1ffad1646f11a953752296c43f5d88cbd5293fff03f093d916b0bc13864
Source0:        https://files.pythonhosted.org/packages/source/M/MutatorMath/MutatorMath-%{version}.zip
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(prep):  -n MutatorMath-%{version}
BuildOption(install):  -l mutatorMath

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
MutatorMath interpolates glyph outlines and font metrics in a
multidimensional design space.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
