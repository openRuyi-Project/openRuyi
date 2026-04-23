# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cycler

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        Cycle through lists in various ways (used by matplotlib)
License:        BSD-3-Clause
URL:            https://github.com/matplotlib/cycler
#!RemoteAsset:  sha256:9c87405839a19696e837b3b818fed3f5f69f16f1eec1a1ad77e043dcea9c772f
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
General purpose library used by matplotlib to cycle through lists for
colors, marker styles, etc.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
