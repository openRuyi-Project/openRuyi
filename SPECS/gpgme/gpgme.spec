# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gpgme
Version:        2.0.1
Release:        %autorelease
Summary:        GnuPG Made Easy
License:        LGPL-2.1-or-later AND MIT
URL:            https://gnupg.org/related_software/gpgme/
VCS:            git:https://git.gnupg.org/gpgme.git
#!RemoteAsset:  sha256:821ab0695c842eab51752a81980c92b0410c7eadd04103f791d5d2a526784966
Source:         https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-glib-binding
BuildOption(conf):  --disable-python-binding
BuildOption(conf):  --disable-qt-binding

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gnupg
BuildRequires:  pkgconfig(libassuan)

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries, header files, documentation, and tools
needed for developing applications that use GPGME.

%install -a
rm -fv %{buildroot}%{_infodir}/dir

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README THANKS TODO VERSION
%{_bindir}/gnupg-key-manage
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
%autochangelog
