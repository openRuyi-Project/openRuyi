# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libgpg-error
Version:        1.55
Release:        %autorelease
Summary:        Library That Defines Common Error Values for All GnuPG Components
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnupg.org/software/libgpg-error/
#!RemoteAsset
Source0:        https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2
#!RemoteAsset
Source1:        https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2.sig
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildSystem:    autotools
BuildOption(conf): --enable-install-gpg-error-config

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon, and possibly more in the future.

%package devel
Summary:        Development package for libgpg-error
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Requires:       glibc-devel
Requires:       libgpg-error = %{version}

%description devel
Files needed for software development using libgpg-error.

%conf -p
autoreconf -fiv

%install -a
rm -r %{buildroot}%{_datadir}/common-lisp
%find_lang %{name} --generate-subpackages

%files -n libgpg-error
%license COPYING.LIB COPYING
%doc README NEWS ChangeLog AUTHORS ABOUT-NLS
%{_libdir}/libgpg-error*.so.*

%files devel
%{_bindir}/*
%{_libdir}/libgpg-error*.so
%{_libdir}/pkgconfig/gpg-error.pc
%{_includedir}/*
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gpg-error.m4
%{_datadir}/aclocal/gpgrt.m4
%dir %{_datadir}/libgpg-error
%{_datadir}/libgpg-error/errorref.txt
%{_infodir}/gpgrt.info*
%{_mandir}/man1/gpg-error-config.*
%{_mandir}/man1/gpgrt-config.*

%changelog
%{?autochangelog}
