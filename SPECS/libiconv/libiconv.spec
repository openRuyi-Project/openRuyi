# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libiconv
Version:        1.19
Release:        %autorelease
Summary:        GNU charset conversion library
License:        LGPL-2.1-only AND GPL-3.0-only
URL:            https://www.gnu.org/software/libiconv/
VCS:            git:https://git.savannah.gnu.org/cgit/libiconv.git
#!RemoteAsset:  sha256:88dd96a8c0464eca144fc791ae60cd31cd8ee78321e67397e25fc095c4a19aa6
Source0:        https://ftpmirror.gnu.org/gnu/libiconv/libiconv-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-extra-encodings

%description
GNU libiconv provides an implementation of the iconv() function and
the iconv program for converting between character encodings. It is
useful on systems which do not have such a function or where the
existing implementation cannot convert from/to Unicode.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and development libraries
needed for building applications that use libiconv.

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS NOTES README
%license COPYING COPYING.LIB
%{_libdir}/libcharset.so.*
%{_libdir}/libiconv.so.*
%{_bindir}/iconv
%{_mandir}/man1/*
%{_docdir}/libiconv/*.*

%files devel
%{_includedir}/iconv.h
%{_includedir}/libcharset.h
%{_includedir}/localcharset.h
%{_libdir}/libcharset.so
%{_libdir}/libiconv.so
%{_mandir}/man3/*

%changelog
%autochangelog
