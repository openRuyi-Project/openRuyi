# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0
# skip the tests, as some deps we don't have yet.
%bcond tests 0

Name:           libuser
Version:        0.64
Release:        %autorelease
Summary:        A user and group account administration library
License:        LGPL-2.0-or-later
URL:            https://pagure.io/libuser
VCS:            git:https://pagure.io/libuser
#!RemoteAsset:  sha256:17448006338dbf4fa19dd561335a75193b64ff58ac93cfb6ee7d8504f3f9bd64
Source:         https://pagure.io/libuser/archive/libuser-%{version}/libuser-libuser-%{version}.tar.gz
BuildSystem:    autotools

%if %{without doc}
# disable all the docs.
Patch:          0001-disable-docs.patch
%endif

BuildOption(conf):  --with-selinux
BuildOption(conf):  PYTHON=%{__python3}
BuildOption(conf):  --with-ldap
BuildOption(conf):  --with-audit
%if %{with doc}
BuildOption(conf):  --enable-gtk-doc
BuildOption(conf):  --with-html-dir=%{_datadir}/gtk-doc/html
%else
BuildOption(conf):  --disable-gtk-doc
%endif

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
%if %{with doc}
BuildRequires:  linuxdoc-tools
BuildRequires:  gtk-doc
%endif

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
Provides:       python3-%{name}
%python_provide python3-%{name}

%description -n python-libuser
Python 3 bindings for libuser.

%conf -p
./autogen.sh

%install -a
# todo: fix the name error.
# Avoid illegal package names
# TODO: Avoid illegal locale package name
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%if %{without tests}
%check
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README TODO docs/*.txt
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
%if %{with doc}
%{_datadir}/gtk-doc/html/*
%endif

%files -n python-libuser
%doc python/modules.txt
%{python3_sitearch}/*.so

%changelog
%autochangelog
