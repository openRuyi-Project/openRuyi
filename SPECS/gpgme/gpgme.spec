# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gpgme
Version:        2.0.0
Release:        %autorelease
Summary:        GnuPG Made Easy
License:        LGPL-2.1-or-later AND MIT
URL:            https://gnupg.org/related_software/gpgme/
#!RemoteAsset
Source:         https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --disable-silent-rules
BuildOption(conf): --disable-glib-binding
BuildOption(conf): --disable-python-binding
BuildOption(conf): --disable-qt-binding

BuildRequires:  make gcc
BuildRequires:  gnupg
BuildRequires:  libassuan-devel >= 2.4.2

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name} = %{version}

%description devel
This package contains the libraries, header files, documentation, and tools
needed for developing applications that use GPGME.

%install -a
find %{buildroot} -type f -name "*.la" -delete -print
rm -fv %{buildroot}%{_infodir}/dir

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README THANKS TODO VERSION
%{_bindir}/gpgme-json
%{_libdir}/libgpgme.so.45*

%files devel
%{_bindir}/gpgme-config
%{_bindir}/gpgme-tool
%{_includedir}/gpgme.h
%{_libdir}/libgpgme.so
%{_libdir}/pkgconfig/gpgme.pc
%{_libdir}/pkgconfig/gpgme-glib.pc
%{_datadir}/aclocal/gpgme.m4
%{_infodir}/gpgme.info*
%{_mandir}/man?/*
%dir %{_datadir}/common-lisp/
%dir %{_datadir}/common-lisp/source/
%{_datadir}/common-lisp/source/gpgme/

%changelog
%{?autochangelog}
