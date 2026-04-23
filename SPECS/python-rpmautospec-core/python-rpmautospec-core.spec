# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rpmautospec_core

Name:           python-rpmautospec-core
Version:        0.1.5
Release:        %autorelease
Summary:        Minimum functionality for rpmautospec
License:        MIT
URL:            https://github.com/fedora-infra/rpmautospec-core
#!RemoteAsset:  sha256:c0acf19ed013355d02c1e28220ad9d6f9088f7f61b4a29d16d5364298bc6e6f3
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-rpmautospec-core = %{version}-%{release}
%python_provide python3-rpmautospec-core

%description
This package contains minimum functionality to determine if an RPM spec file
uses rpmautospec features.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
