# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_version %{version_no_tilde}

Name:           libpwquality
Version:        1.4.5
Release:        %autorelease
Summary:        A library for password generation and password quality checking
License:        BSD-3-Clause OR GPL-2.0-or-later
URL:            https://github.com/libpwquality/libpwquality/
#!RemoteAsset
Source0:        https://github.com/libpwquality/libpwquality/releases/download/libpwquality-%{version}/libpwquality-%{version}.tar.bz2
BuildSystem:    autotools

# https://github.com/libpwquality/libpwquality/pull/74
Patch0:         0001-setuptools.patch

BuildOption(conf):  --with-securedir=%{_pam_moduledir}
BuildOption(conf):  --with-pythonsitedir=%{python3_sitearch}
BuildOption(conf):  --with-python-binary=%{__python3}
BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  cracklib-devel
BuildRequires:  gettext
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-packaging

%description
This is a library for password quality checks and generation
of random passwords that pass the checks.
This library uses the cracklib and cracklib dictionaries
to perform some of the checks.

%package        devel
Summary:        Support for development of applications using the libpwquality library
Requires:       libpwquality = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Files needed for development of applications using the libpwquality
library.
See the pwquality.h header file for the API.

%package     -n python3-pwquality
Summary:        Python bindings for the libpwquality library
Requires:       libpwquality = %{version}-%{release}

%description -n python3-pwquality
This is pwquality Python module that provides Python bindings
for the libpwquality library. These bindings can be used
for easy password quality checking and generation of random
pronounceable passwords from Python applications.

%install -a
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_pam_moduledir}/*.la
mkdir %{buildroot}%{_pam_secconfdir}/pwquality.conf.d
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc README NEWS AUTHORS
%{_bindir}/pwmake
%{_bindir}/pwscore
%dir %{_pam_moduledir}
%{_pam_moduledir}/pam_pwquality.so
%{_libdir}/libpwquality.so.*
%dir %{_pam_secconfdir}
%config(noreplace) %{_pam_secconfdir}/pwquality.conf
%dir %{_pam_secconfdir}/pwquality.conf.d
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%{_includedir}/pwquality.h
%{_libdir}/libpwquality.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%files -n python3-pwquality
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info

%changelog
%{?autochangelog}
