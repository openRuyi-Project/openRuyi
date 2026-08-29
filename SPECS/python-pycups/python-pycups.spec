# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycups

Name:           python-%{srcname}
Version:        2.0.4
Release:        %autorelease
Summary:        Python bindings for CUPS
License:        GPL-2.0-or-later
URL:            https://github.com/OpenPrinting/pycups
#!RemoteAsset:  sha256:843e385c1dbf694996ca84ef02a7f30c28376035588f5fbeacd6bae005cf7c8d
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l cups

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(cups)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
These Python bindings are intended to wrap the CUPS API.

%generate_buildrequires
%pyproject_buildrequires

%install -p
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs
install -p -m 0644 psdriver.attr %{buildroot}%{_rpmconfigdir}/fileattrs/psdriver.attr
install -p -m 0755 postscriptdriver.prov %{buildroot}%{_rpmconfigdir}/postscriptdriver.prov

%files -f %{pyproject_files}
%doc README
%license COPYING
%{_rpmconfigdir}/fileattrs/psdriver.attr
%{_rpmconfigdir}/postscriptdriver.prov

%changelog
%autochangelog
