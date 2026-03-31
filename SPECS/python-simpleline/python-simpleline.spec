# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname simpleline

Name:           python-%{srcname}
Version:        1.9.0
Release:        %autorelease
Summary:        Python text UI framework
License:        MIT
URL:            https://github.com/janpipek/iso639-python
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  pyproject-rpm-macros
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  intltool
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pygobject)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

Requires:       python3dist(rpm)

%description
Simpleline is a Python library for creating text UI.
It is designed to be used with line-based machines
and tools (e.g. serial console) so that every new line
is appended to the bottom of the screen.
Printed lines are never rewritten!

%generate_buildrequires
%pyproject_buildrequires

# No configure
%conf

%install -a
# TODO: Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
rm -rf %{buildroot}%{_datadir}/locale/en_GB/
%find_lang %{name} --generate-subpackages

%check
make test

%files
%doc ChangeLog README.md
%license LICENSE.md
%{python3_sitelib}/*

%changelog
%{?autochangelog}
