# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mailutils
Version:        3.21
Release:        %autorelease
Summary:        GNU Mailutils - a suite of utilities for electronic mail
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.gnu.org/software/mailutils/
VCS:            git:https://git.savannah.gnu.org/git/mailutils.git
#!RemoteAsset:  sha256:e47c1edc699b8d6675fdbc77db3a84ae837f18e1f2094fe29d48bb58a97ef5e9
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

# https://git.savannah.gnu.org/cgit/mailutils.git/commit/?id=a7da7302f84638568639b41abe71b0ad1ce90fd0
Patch0001:      0001-Minor-fix.patch

BuildOption(conf):  --sbindir=%{_bindir}
BuildOption(conf):  --libexecdir=%{_libdir}/mailutils
BuildOption(conf):  --with-gdbm
BuildOption(conf):  --with-gnutls
BuildOption(conf):  --disable-python
BuildOption(conf):  --without-guile
BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  emacs
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libgsasl)
BuildRequires:  gdbm-devel

%description
GNU Mailutils is a rich and powerful protocol-independent mail framework
that contains a series of useful mail libraries, clients, and servers.
It provides utilities such as mail, frm, messages, readmsg, and sieve.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%install -a
# Rename mail to gnu-mail to avoid conflict with other mail implementations
mv %{buildroot}%{_bindir}/mail %{buildroot}%{_bindir}/gnu-mail
mv %{buildroot}%{_mandir}/man1/mail.1 %{buildroot}%{_mandir}/man1/gnu-mail.1
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc ChangeLog NEWS README THANKS TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
%{_libdir}/libmailutils.so.*
%{_libdir}/libmu*.so.*
%{_libdir}/mailutils
%{_datadir}/emacs/site-lisp/mailutils-mh*
%{_datadir}/mailutils/mh/

%files devel
%{_includedir}/mailutils
%{_libdir}/libmailutils.so
%{_libdir}/libmu*.so
%{_datadir}/aclocal/mailutils.m4

%changelog
%autochangelog
