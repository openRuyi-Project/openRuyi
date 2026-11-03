# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libuser
Version:        0.64
Release:        %autorelease
Summary:        A user and group account administration library
License:        LGPL-2.0-or-later
URL:            https://codeberg.org/libuser/libuser
VCS:            git:https://codeberg.org/libuser/libuser
#!RemoteAsset:  sha256:34abb60ac0ee336adcbff5f99008a5d9396fd4d0a5c31612e9c26c679eb9e596
Source:         https://codeberg.org/libuser/libuser/archive/libuser-%{version}.tar.gz
BuildSystem:    autotools

# Create edit files beside symlink targets; https://codeberg.org/libuser/libuser/commit/93134cfbc7c80dff0fe5b4b6b2352d44419dfadd
Patch1000:      1000-edit-at-symlink-target.patch
# Restore Python password tests; https://codeberg.org/libuser/libuser/commit/3341a12021e5dbfd198cdb13ea8c4e1509ba2d42
Patch1001:      1001-python-crypt-r.patch

BuildOption(prep):  -n %{name}
BuildOption(conf):  --with-selinux
BuildOption(conf):  PYTHON=%{__python3}
BuildOption(conf):  --with-ldap
BuildOption(conf):  --with-audit
BuildOption(conf):  --enable-gtk-doc
BuildOption(conf):  --with-html-dir=%{_datadir}/gtk-doc/html

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  gettext-devel
BuildRequires:  bison
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(audit)
BuildRequires:  gtk-doc
BuildRequires:  diffutils
BuildRequires:  python3dist(crypt-r)
BuildRequires:  openldap
BuildRequires:  openldap-client
BuildRequires:  openssl

%description
The libuser library implements a standardized interface for manipulating
and administering user and group accounts.

%package        devel
Summary:        Files needed for developing applications which use libuser
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(glib-2.0)

%description    devel
The libuser-devel package contains header files and libraries for
developing applications with libuser.

%package     -n python-libuser
Summary:        Python 3 bindings for the libuser library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}

%description -n python-libuser
Python 3 bindings for libuser.

%conf -p
# Skip SGML output until linuxdoc-tools is available.
sed -i '/^all: sgml\/libuser.txt sgml\/libuser.html$/d' docs/Makefile.am
./autogen.sh
# Load the MDB module provided by openRuyi for the LDAP tests.
sed -i '/^database mdb/i moduleload %{_libexecdir}/openldap/back_mdb.so' tests/slapd.conf.in

%install -a
%find_lang %{name} --generate-subpackages

%check -p
export LC_ALL=C.UTF-8

%files -f %{name}.lang
%doc AUTHORS NEWS README TODO docs/*.txt
%license COPYING
%config(noreplace) %{_sysconfdir}/libuser.conf
%attr(0755,root,root) %{_bindir}/*
%{_libdir}/*.so.*
%dir %{_libdir}/libuser
%{_libdir}/libuser/*.so
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%{_includedir}/libuser/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libuser.pc
%{_datadir}/gtk-doc/html/libuser/

%files -n python-libuser
%doc python/modules.txt
%{python3_sitearch}/libuser*.so

%changelog
%autochangelog
