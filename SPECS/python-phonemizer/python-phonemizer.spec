# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname phonemizer

Name:           python-%{srcname}
Version:        3.3.0
Release:        %autorelease
Summary:        Simple text to phones converter for multiple languages
License:        GPL-3.0-or-later
URL:            https://github.com/bootphon/phonemizer
#!RemoteAsset:  sha256:5e0c38122effe0b331a24e674aff256874ece169d70a9cf1120337b56f8e3d0c
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%install -a
rm -rf %{buildroot}%{python3_sitelib}/test
rm -rf %{buildroot}%{python3_sitelib}/docs

%description
The phonemizer allows simple phonemization of words and texts in many languages.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/phonemize

%changelog
%autochangelog
