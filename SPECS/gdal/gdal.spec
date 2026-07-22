# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gdal
Version:        3.13.1
Release:        %autorelease
Summary:        Geospatial data abstraction library
License:        MIT
URL:            https://github.com/OSGeo/gdal
#!RemoteAsset:  sha256:8023c9a6e08f151f4723f08982cc73d2bc95095df65e5c1ea563cafafb864ec6
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(proj)

%description
GDAL is a library and set of tools for raster and vector geospatial data.

%package        devel
Summary:        Development files for GDAL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, libraries, and CMake files for developing applications with GDAL.

%files
%doc NEWS.md
%doc README.md
%license LICENSE.TXT
%{_bindir}/gdal
%{_bindir}/gdal_contour
%{_bindir}/gdal_create
%{_bindir}/gdal_footprint
%{_bindir}/gdal_grid
%{_bindir}/gdal_rasterize
%{_bindir}/gdal_translate
%{_bindir}/gdal_viewshed
%{_bindir}/gdaladdo
%{_bindir}/gdalbuildvrt
%{_bindir}/gdaldem
%{_bindir}/gdalenhance
%{_bindir}/gdalinfo
%{_bindir}/gdallocationinfo
%{_bindir}/gdalmanage
%{_bindir}/gdalmdiminfo
%{_bindir}/gdalmdimtranslate
%{_bindir}/gdalsrsinfo
%{_bindir}/gdaltindex
%{_bindir}/gdaltransform
%{_bindir}/gdalwarp
%{_bindir}/gnmanalyse
%{_bindir}/gnmmanage
%{_bindir}/nearblack
%{_bindir}/ogr2ogr
%{_bindir}/ogrinfo
%{_bindir}/ogrlineref
%{_bindir}/ogrtindex
%{_bindir}/sozip
%{_datadir}/bash-completion/completions/gdal*
%{_datadir}/bash-completion/completions/ogr*
%{_datadir}/bash-completion/completions/sozip
%{_datadir}/gdal/
%{_libdir}/gdalplugins/
%{_libdir}/libgdal.so.*

%files devel
%{_bindir}/gdal-config
%{_includedir}/*
%{_libdir}/cmake/gdal/
%{_libdir}/libgdal.so
%{_libdir}/pkgconfig/gdal.pc

%changelog
%autochangelog
