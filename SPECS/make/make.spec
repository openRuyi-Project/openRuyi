# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond_with guile

Name:           make
Version:        4.4.1
Release:        %autorelease
Summary:        A tool which controls the generation of executables and non-source files of a program
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/make/
VCS:            git:https://https.git.savannah.gnu.org/git/make.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

%if %{with guile}
BuildOption(conf):  --with-guile
%else
BuildOption(conf):  --without-guile
%endif

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
%if %{with guile}
BuildRequires:  pkgconfig(guile-2.0)
%endif

Provides:       %{name}-devel%{?_isa} = %{version}-%{release}

%description
GNU Make is a tool which controls the generation of executables and other
non-source files of a program from the program's source files.

Make gets its knowledge of how to build your program from a file called
the makefile, which lists each of the non-source files and how to compute
it from other files. When you write a program, you should write a makefile
for it, so that it is possible to use Make to build and install the program.

%build -p
touch configure aclocal.m4 Makefile.in

%install -a
ln -sf make %{buildroot}/%{_bindir}/gmake
ln -sf make.1 %{buildroot}/%{_mandir}/man1/gmake.1
rm -f %{buildroot}/%{_infodir}/dir
%find_lang %{name} --generate-subpackages

%check
# check will fail if running the test with -j2
# http://savannah.gnu.org/bugs/?func=detailitem&item_id=53152
if [ "%{_smp_mflags}" = "-j2" ]; then
    echo "test will fail with make -j2 check"
else
/usr/bin/env LANG=C make check || {
    for f in tests/work/*/*.diff; do
        test -f "$f" || continue
        printf "++++++++++++++ %s ++++++++++++++\n" "${f##*/}"
        cat "$f"
    done
}
fi

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/*
%{_includedir}/*
%doc NEWS
%{_mandir}/*/*
%{_infodir}/*

%changelog
%autochangelog
