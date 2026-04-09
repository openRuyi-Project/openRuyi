# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxslt
Version:        1.1.43
Release:        %autorelease
Summary:        XSL Transformation Library
License:        GPL-2.0-or-later AND MIT
URL:            https://gitlab.gnome.org/GNOME/libxslt
#!RemoteAsset
Source0:        https://download.gnome.org/sources/libxslt/1.1/libxslt-%{version}.tar.xz
Source1:        xslt-config.1
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-python
BuildOption(conf):  --disable-silent-rules

BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)

%description
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism. This package contains the runtime libraries and
command-line tools.

%package        devel
Summary:        Development files for libxslt
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel
Requires:       pkgconfig(libgcrypt)

%description    devel
This package contains the header files, pkg-config files, and documentation
needed to develop applications that use the libxslt libraries.

%install -a
rm -fr %{buildroot}%{_datadir}/doc
install -D -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/xslt-config.1
%fdupes %{buildroot}%{_datadir}

%files
%license Copyright
%doc AUTHORS NEWS TODO FEATURES
# Files from original 'tools' package
%{_bindir}/xsltproc
%{_mandir}/man1/xsltproc.1%{?ext_man}
# Files from original 'libxslt1' package
%{_libdir}/libxslt.so.1*
# Files from original 'libexslt0' package
%{_libdir}/libexslt.so.0*

%files devel
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/*.sh
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%dir %{_libdir}/cmake/libxslt/
%{_libdir}/cmake/libxslt/FindGcrypt.cmake
%{_libdir}/cmake/libxslt/libxslt-config.cmake
%{_includedir}/*
%{_bindir}/xslt-config
%{_mandir}/man1/xslt-config.1%{?ext_man}
%{_mandir}/man3/*
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/libexslt/
%{_datadir}/gtk-doc/html/libxslt/
%doc doc/*.html doc/tutorial doc/tutorial2

%changelog
%autochangelog
