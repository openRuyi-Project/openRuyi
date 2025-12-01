# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           giflib
Version:        5.2.2
Release:        %autorelease
Summary:        A Library for Working with GIF Images
License:        MIT
URL:            https://giflib.sourceforge.net/
#!RemoteAsset
Source:         https://downloads.sf.net/giflib/giflib-%{version}.tar.gz
Patch:          0001-disable-doc.patch
BuildSystem:    autotools

BuildOption(install): PREFIX="%{_prefix}"
BuildOption(install): LIBDIR="%{_libdir}"
BuildOption(install): INCDIR="%{_includedir}"
BuildOption(install): BINDIR="%{_bindir}"

BuildRequires:  fdupes
BuildRequires:  libtool >= 2
BuildRequires:  gcc make

%description
A library for manipulating GIF image files. With the expiration of the LZW
patent, giflib can be used as a replacement for libungif.

%package        devel
Summary:        Development files for the giflib library
Requires:       %{name} = %{version}

%description    devel
This package contains the header files and symbolic links needed to develop
applications that use the giflib library.

# No configure
%conf

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

install -d -m 755 %{buildroot}%{_mandir}/man1
for i in doc/*.1; do
  install -pm 0644 ${i} %{buildroot}%{_mandir}/man1/
done

%fdupes -s doc

rm -f %{buildroot}%{_libdir}/libgif.a

%files
%license COPYING
%{_libdir}/lib*.so.*
%doc NEWS README doc
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/gif_lib.h
%{_libdir}/lib*.so

%changelog
%{?autochangelog}
