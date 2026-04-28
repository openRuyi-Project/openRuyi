# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change to 1 to enable
%bcond aspell 0
%bcond nuspell 0

Name:           enchant
Version:        2.8.12
Release:        %autorelease
Summary:        Generic Spell Checking Library
License:        LGPL-2.1-or-later
URL:            https://rrthomas.github.io/enchant/
VCS:            git:https://github.com/rrthomas/enchant
#!RemoteAsset
Source0:        https://github.com/rrthomas/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

%if %{with aspell}
BuildOption(conf):  --with-aspell
%endif
BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  vala
BuildRequires:  groff
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libvoikko)
BuildRequires:  pkgconfig(hunspell)
%if %{with aspell}
BuildRequires:  pkgconfig(aspell)
%endif
%if %{with nuspell}
BuildRequires:  pkgconfig(nuspell)
%endif

%description
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

%package        devel
Summary:        Development files for the Enchant spell checking library
Requires:       pkgconfig(glib-2.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel

%description    devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%conf -p
autoreconf -fiv

# TODO: test require unittest-cpp.
%check

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING.LIB
%{_bindir}/enchant-2
%{_bindir}/enchant-lsmod-2
# enchant libs
%{_libdir}/libenchant-2.so.*
%dir %{_libdir}/enchant-2
# backend libs
%if %{with aspell}
%{_libdir}/enchant-2/enchant_aspell.so
%endif
%{_libdir}/enchant-2/enchant_hunspell.so
%if %{with nuspell}
%{_libdir}/enchant-2/enchant_nuspell.so
%endif
%{_libdir}/enchant-2/enchant_voikko.so
# data
%{_datadir}/enchant-2/enchant.ordering
# docs
%{_docdir}/%{name}/enchant.html
%{_docdir}/%{name}/enchant-2.html
%{_docdir}/%{name}/enchant-lsmod-2.html
%{_mandir}/man1/enchant-2.1*
%{_mandir}/man1/enchant-lsmod-2.1*
%{_mandir}/man5/enchant.5*

%files devel
%{_includedir}/enchant-2
%{_libdir}/*.so
%{_libdir}/pkgconfig/enchant-2.pc

%changelog
%{?autochangelog}
