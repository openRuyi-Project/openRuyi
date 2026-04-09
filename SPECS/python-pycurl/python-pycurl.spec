# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycurl

Name:           python-%{srcname}
Version:        7.45.7
Release:        %autorelease
Summary:        A Python interface to libcurl
License:        LGPL-2.1-only OR MIT
URL:            https://github.com/pycurl/pycurl
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} curl

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcurl)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%generate_buildrequires
%pyproject_buildrequires

%install -a
rm -rf %{buildroot}%{_datadir}/doc/pycurl

%files -f %{pyproject_files}
%doc ChangeLog README.rst examples doc

%changelog
%autochangelog
