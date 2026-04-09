# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           djvulibre
Version:        3.5.29
Release:        %autorelease
Summary:        DjVu viewers, encoders, and utilities
License:        GPL-2.0-or-later
URL:            http://djvu.sourceforge.net/
VCS:            git:https://git.code.sf.net/p/djvu/djvulibre-git
#!RemoteAsset
Source0:        http://downloads.sourceforge.net/djvu/djvulibre-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-threads

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  hicolor-icon-theme

%description
DjVuLibre is a free implementation of DjVu, including viewers, decoders,
simple encoders, and utilities.

%package        devel
Summary:        Development files for DjVuLibre
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for DjVuLibre.

%install -a
cd desktopfiles
for i in 22 32 48 64 ; do
    install -d %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/
    if [ -f ./prebuilt-hi${i}-djvu.png ]; then
        cp -a ./prebuilt-hi${i}-djvu.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/image-vnd.djvu.mime.png
    fi
done

%files
%doc README COPYRIGHT NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/djvu/
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_libdir}/libdjvulibre.so.*

%files devel
%doc doc/
%{_includedir}/libdjvu/
%{_libdir}/pkgconfig/ddjvuapi.pc
%{_libdir}/libdjvulibre.so

%changelog
%autochangelog
