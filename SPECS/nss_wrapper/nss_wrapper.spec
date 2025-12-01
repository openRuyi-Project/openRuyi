# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nss_wrapper
Version:        1.1.16
Release:        %autorelease
Summary:        A wrapper for the user, group and hosts NSS API
License:        BSD-3-Clause
URL:            http://cwrap.org/
#!RemoteAsset
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
BuildSystem:    cmake

# Fix tests
Patch0:         0001-nwrap-fix-tests.patch

BuildOption(conf):  -DUNIT_TESTING=ON

BuildRequires:  cmake
BuildRequires:  cmocka-cmake
BuildRequires:  perl

Recommends:     cmake
Recommends:     pkgconfig

%description
There are projects which provide daemons needing to be able to create, modify
and delete Unix users. Or just switch user ids to interact with the system e.g.
a user space file server. To be able to test that you need the privilege to
modify the passwd and groups file. With nss_wrapper it is possible to define
your own passwd and groups file which will be used by software to act correctly
while under test.

If you have a client and server under test they normally use functions to
resolve network names to addresses (dns) or vice versa. The nss_wrappers allow
you to create a hosts file to setup name resolution for the addresses you use
with socket_wrapper.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
NSS_WRAPPER_PASSWD=/path/to/passwd
NSS_WRAPPER_GROUP=/path/to/group
NSS_WRAPPER_HOSTS=/path/to/host

This package doesn't have a devel package cause this project is for
development/testing.

%install -a
sed -i '1 s|/usr/bin/env\ perl|/usr/bin/perl|' %{buildroot}%{_bindir}/nss_wrapper.pl

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_bindir}/nss_wrapper.pl
%dir %{_libdir}/cmake/nss_wrapper
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config-version.cmake
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config.cmake
%{_libdir}/pkgconfig/nss_wrapper.pc
%{_mandir}/man1/nss_wrapper.1*
%{_libdir}/libnss_wrapper.so*

%changelog
%{?autochangelog}
