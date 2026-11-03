# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libepubgen
Version:        0.1.1
Release:        %autorelease
Summary:        EPUB generator for document converters
License:        MPL-2.0
URL:            https://sourceforge.net/p/libepubgen/
VCS:            git:https://git.code.sf.net/p/libepubgen/code
#!RemoteAsset:  sha256:03e084b994cbeffc8c3dd13303b2cb805f44d8f2c3b79f7690d7e3fc7f6215ad
Source0:        https://downloads.sourceforge.net/libepubgen/%{name}-%{version}.tar.xz
BuildSystem:    autotools

# Upstream backport. Remove the redundant Content-Type element from generated XHTML.
# https://sourceforge.net/p/libepubgen/code/ci/92760e4b0b8da126029c5ff858ebec27df4acfa8/
Patch1000:      1000-omit-obsolete-epub-content-type-meta.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tests

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(libxml-2.0)

%description
libepubgen writes EPUB publications from librevenge document events.
It is used by the EPUB export filter in LibreOffice Writer.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/libepubgen-0.1.so.*

%files devel
%{_includedir}/libepubgen-0.1/
%{_libdir}/libepubgen-0.1.so
%{_libdir}/pkgconfig/libepubgen-0.1.pc

%changelog
%autochangelog
