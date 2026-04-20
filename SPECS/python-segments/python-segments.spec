# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname segments

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Unicode Standard tokenization routines and orthography profile segmentation
License:        Apache-2.0
URL:            https://github.com/cldf/segments
#!RemoteAsset:  sha256:bba71f5520ddd54c8aa2f4d765a60618c6862162d6e7356a4a097f2223166f5b
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The segments package provides Unicode Standard
tokenization routines and orthography segmentation,
implementing the linear algorithm described in the orthography
profile specification from The Unicode Cookbook (Moran and Cysouw 2018 DOI).

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/segments

%changelog
%autochangelog
