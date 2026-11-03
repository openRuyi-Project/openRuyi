# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aliftools

Name:           python-%{srcname}
Version:        0.1.10
Release:        %autorelease
Summary:        Helper tools for building Alif Type Foundry fonts
License:        Apache-2.0
URL:            https://github.com/aliftype/tools
#!RemoteAsset:  sha256:1790c786b097d6c07f13c99cd2d3d1e9845c43d7929c29d564b289aee0f5958b
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Downstream feature selection for the font build tools.
Patch2000:      2000-select-font-build-tools.patch

BuildOption(install):  -l alifTools
# Import only the top-level package because optional submodules require extras.
BuildOption(check):  -t

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Build filters and glyph-name tools for Alif Type Foundry fonts.

%pyproject_extras_subpkg -n python-%{srcname} filters

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/strip-glyph-names

%changelog
%autochangelog
