# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dropboxdrivefs

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        Dropbox filesystem implementation for fsspec
License:        BSD-3-Clause
URL:            https://github.com/richardkiss/dropboxdrivefs
#!RemoteAsset:  sha256:6f3c6061d045813553ce91ed0e2b682f1d70bec74011943c92b3181faacefd34
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(dropbox)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Dropboxdrivefs provides an fsspec-compatible filesystem backed by Dropbox.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# The upstream wheel metadata accidentally discovers the top-level test package.
rm -rf %{buildroot}%{python3_sitelib}/test

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
