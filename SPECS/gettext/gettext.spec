# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond nls 1

Name:           gettext
Version:        0.26
Release:        %autorelease
Summary:        GNU Internationalization (i18n) and Localization (l10n) library and tools
License:        (GPL-3.0-or-later AND LGPL-2.1-or-later)
URL:            https://www.gnu.org/software/gettext/
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz

Patch0:         gettext-fix-nls-stub.patch

BuildSystem:    autotools

BuildOption(conf): --disable-csharp
BuildOption(conf): --with-xz
BuildOption(conf): --without-included-gettext
BuildOption(conf): --without-included-libunistring
BuildOption(conf): --enable-shared
BuildOption(conf): --disable-rpath
%if %{with nls}
BuildOption(conf): --enable-nls
%else
BuildOption(conf): --disable-nls
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  libunistring-devel
BuildRequires:  ncurses-devel
BuildRequires:  acl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libattr-devel
BuildRequires:  xz-devel
%if %{with nls}
BuildRequires:  gettext-tools
%endif

%description
Meta-package that installs the GNU gettext runtime and developer tools.

Provides:       bundled(gnulib)
Requires:       %{name}-tools = %{version}-%{release}
Requires:       libtextstyle%{?_isa} = %{version}-%{release}

%package devel
Summary:        Development files for the entire GNU gettext eco-system
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}
Requires:       libtextstyle%{?_isa} = %{version}-%{release}
%description devel
This is the one-stop package for developing internationalized applications.
It provides all headers, pkgconfig files, and development libraries for
gettext-runtime, gettext-tools, and libtextstyle.

%package runtime
Summary:        Runtime components for gettext
Requires:       envsubst = %{version}-%{release}
%description runtime
Contains runtime libraries (like libasprintf) and essential commands
(like gettext, ngettext) needed to run internationalized programs.

%package tools
Summary:        Tools for creating and managing message catalogs
Requires:       %{name}-runtime = %{version}-%{release}
%description tools
Contains tools for developers and translators to create and manage
translation files (.po, .mo), such as msgfmt and xgettext.

%package -n envsubst
Summary:        Substitutes the values of environment variables
%description -n envsubst
A standalone utility to substitute environment variables in shell scripts.

%package -n libtextstyle
Summary:        Library for styling text on terminal emulators
License:        LGPL-2.1-or-later
%description -n libtextstyle
Provides the libtextstyle library for styling console output.

%package -n libtextstyle-devel
Summary:        Development files for libtextstyle
Requires:       libtextstyle%{?_isa} = %{version}-%{release}
%description -n libtextstyle-devel
Contains development files for the libtextstyle library.

%package doc
Summary:        Documentation and examples for gettext
BuildArch:      noarch

%description doc
Contains detailed documentation (info, html) and extensive examples.

%if %{with nls}
%lang_package -n %{name}-runtime
%lang_package -n %{name}-tools
%endif

%conf -p
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

%if %{with nls}
%find_lang %{name}-runtime
%find_lang %{name}-tools
%endif

%files
%license COPYING
%doc AUTHORS NEWS README

%files runtime
%{_bindir}/gettext
%{_bindir}/ngettext
%{_bindir}/gettext.sh
%{_libdir}/libasprintf.so.*
%{_libdir}/libasprintf.so
%{_libdir}/preloadable_libintl.so
%{_mandir}/man1/gettext.1*
%{_mandir}/man1/ngettext.1*

%files tools
%{_bindir}/msg*
%{_bindir}/xgettext
%{_bindir}/autopoint
%{_bindir}/gettextize
%{_bindir}/printf_gettext
%{_bindir}/printf_ngettext
%{_bindir}/recode-sr-latin
%{_libdir}/libgettextlib-%{version}.so
%{_libdir}/libgettextsrc-%{version}.so
%{_libdir}/libgettextpo.so.*
%{_datadir}/aclocal/nls.m4
%{_datadir}/gettext/
%{_libexecdir}/gettext/
%{_mandir}/man1/msg*.1*
%{_mandir}/man1/xgettext.1*
%{_mandir}/man1/gettextize.1*
%{_mandir}/man1/autopoint.1*
%{_mandir}/man1/recode*.1*
%{_mandir}/man1/printf_gettext.1*
%{_mandir}/man1/printf_ngettext.1*

%files devel
# Development files for gettext-runtime
%{_includedir}/autosprintf.h
%{_libdir}/libasprintf.so
# Development files for gettext-tools
%{_includedir}/gettext-po.h
%{_libdir}/libgettextlib.so
%{_libdir}/libgettextsrc.so
%{_libdir}/libgettextpo.so
# Common development files
%{_datadir}/aclocal/nls.m4
%{_datadir}/%{name}-%{version}/
# API documentation
%{_mandir}/man3/*

%files -n libtextstyle
%license COPYING
%{_libdir}/libtextstyle.so.*

%files -n libtextstyle-devel
%{_includedir}/textstyle.h
%{_includedir}/textstyle/
%{_libdir}/libtextstyle.so

%files -n envsubst
%{_bindir}/envsubst
%{_mandir}/man1/envsubst.1*

%files doc
%doc AUTHORS NEWS README
%doc %{_docdir}/%{name}/
%{_infodir}/*.info*

%if %{with nls}
%files -n %{name}-runtime-lang -f %{name}-runtime.lang
%files -n %{name}-tools-lang -f %{name}-tools.lang
%endif

%changelog
%{?autochangelog}
