# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpsl
Version:        0.21.5
Release:        %autorelease
Summary:        C library for the Public Suffix List
License:        MIT
URL:            https://rockdaboot.github.io/libpsl
VCS:            git:https://github.com/rockdaboot/libpsl
#!RemoteAsset
Source:         https://github.com/rockdaboot/libpsl/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=false
BuildOption(conf):  -Druntime=libidn2
BuildOption(conf):  -Dbuiltin=true
BuildOption(conf):  -Dpsl_distfile=%{_datadir}/publicsuffix/public_suffix_list.dafsa
BuildOption(conf):  -Dpsl_file=%{_datadir}/publicsuffix/effective_tld_names.dat
BuildOption(conf):  -Dpsl_testfile=%{_datadir}/publicsuffix/test_psl.txt

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  icu4c-devel
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  publicsuffix-list
BuildRequires:  pkgconfig(python3)

Requires:       publicsuffix-list

%description
libpsl is a C library to handle the Public Suffix List, used by web clients to
manage cookies, certificates, and domain highlighting.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       publicsuffix-list

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package     -n psl
Summary:        Command-line utility to explore the Public Suffix List

%description -n psl
This package contains a command-line utility to explore the Public Suffix List.

%package     -n psl-make-dafsa
Summary:        Compiles the Public Suffix List into DAFSA form
BuildArch:      noarch

%description -n psl-make-dafsa
This script compiles a plain text Public Suffix List into a
Deterministic Acyclic Finite State Automaton (DAFSA).

%prep -a
rm -frv list
ln -sv %{_datadir}/publicsuffix list
%py3_shebang_fix src/psl-make-dafsa

%files
%license COPYING
%{_libdir}/libpsl.so.5
%{_libdir}/libpsl.so.5.*
%{_mandir}/man1/psl-make-dafsa.1.gz
%{_mandir}/man1/psl.1.gz

%files devel
%doc AUTHORS NEWS
%{_includedir}/libpsl.h
%{_libdir}/libpsl.so
%{_libdir}/pkgconfig/libpsl.pc

%files -n psl
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/psl

%files -n psl-make-dafsa
%license COPYING
%{_bindir}/psl-make-dafsa

%changelog
%{?autochangelog}
