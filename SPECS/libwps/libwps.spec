# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libwps
Version:        0.4.14
Release:        %autorelease
Summary:        Microsoft Works document import library
License:        MPL-2.0 AND LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://libwps.sourceforge.net/
VCS:            git:https://git.code.sf.net/p/libwps/code
#!RemoteAsset:  sha256:365b968e270e85a8469c6b160aa6af5619a4e6c995dbb04c1ecc1b4dd13e80de
Source0:        https://downloads.sourceforge.net/libwps/%{name}-%{version}.tar.xz
BuildSystem:    autotools

# Upstream backport. Decode escaped control characters in Lotus 1-2-3 cell text.
# https://sourceforge.net/p/libwps/code/ci/2e1d8e8b8ee0ff54d5c8448b6ead95aaf12f1e52/
Patch1000:      1000-decode-lotus-control-characters.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-tools
BuildOption(conf):  --without-docs

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)

%description
libwps parses legacy Microsoft Works word-processing and spreadsheet
files. Its tools export text, HTML and comma-separated values.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
sed -n '/^\/\* librevenge$/,/\*\//p' src/lib/WPSOLEStream.cpp > POLE-LICENSE.txt
grep -Fq "Redistributions in binary form" POLE-LICENSE.txt

%files
%doc README
%license COPYING.MPL COPYING.LGPL POLE-LICENSE.txt
%{_bindir}/wks2csv
%{_bindir}/wks2raw
%{_bindir}/wks2text
%{_bindir}/wps2html
%{_bindir}/wps2raw
%{_bindir}/wps2text
%{_libdir}/libwps-0.4.so.*

%files devel
%{_includedir}/libwps-0.4/
%{_libdir}/libwps-0.4.so
%{_libdir}/pkgconfig/libwps-0.4.pc

%changelog
%autochangelog
