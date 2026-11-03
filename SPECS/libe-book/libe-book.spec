# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libe-book
Version:        0.1.4
Release:        %autorelease
Summary:        Import library for legacy e-book formats
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libe-book
VCS:            git:https://git.code.sf.net/p/libebook/code
#!RemoteAsset:  sha256:104b7e791b6632745898e9b6a0037b7540235771a4d8c3bde2c764466ad912f1
Source0:        https://downloads.sourceforge.net/libebook/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  CXXFLAGS="%{optflags} -std=gnu++17"
BuildOption(conf):  --with-liblangtag
BuildOption(conf):  --with-tools
BuildOption(conf):  --enable-tests
BuildOption(conf):  --without-docs

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)

%description
libe-book reads legacy e-book formats and produces librevenge document
events. Its tools extract text and convert e-books to HTML.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc README
%license COPYING
%{_bindir}/ebook2html
%{_bindir}/ebook2raw
%{_bindir}/ebook2text
%{_libdir}/libe-book-0.1.so.*

%files devel
%{_includedir}/libe-book-0.1/
%{_libdir}/libe-book-0.1.so
%{_libdir}/pkgconfig/libe-book-0.1.pc

%changelog
%autochangelog
