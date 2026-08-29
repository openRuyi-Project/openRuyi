# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kimageformats

%bcond avif 0
%bcond heif 0
%bcond exr 1
%bcond jxl 1
%bcond jp2 1

# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kimageformats
Version:        6.28.0
Release:        %autorelease
Summary:        Image format plugins for Qt
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kimageformats.git
#!RemoteAsset:  sha256:91808c6de080ab5b506721c1f78ad5772bcb1f70bba7262c275ccd98de8b6b38
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
%if %{with avif}
BuildOption(conf):  -DKIMAGEFORMATS_AVIF:BOOL=TRUE
%else
BuildOption(conf):  -DKIMAGEFORMATS_AVIF:BOOL=FALSE
%endif
%if %{with heif}
BuildOption(conf):  -DKIMAGEFORMATS_HEIF:BOOL=TRUE
%else
BuildOption(conf):  -DKIMAGEFORMATS_HEIF:BOOL=FALSE
%endif

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
%if %{with exr}
BuildRequires:  openexr-devel
%endif
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
%if %{with avif}
BuildRequires:  cmake(libavif) >= 0.8.2
%endif
%if %{with heif}
BuildRequires:  cmake(libheif) >= 1.10.0
%endif
%if %{with jp2}
BuildRequires:  cmake(OpenJPEG)
%endif
%if %{with jxl}
BuildRequires:  pkgconfig(libjxl) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_cms) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_threads) >= 0.9.4
%endif
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libraw_r)

Requires:       qt6-qtimageformats >= %{qt6_version}

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package        eps
Summary:        EPS image format plugin for Qt
Recommends:     ghostscript

%description    eps
This plugin provides support for the EPS document format for QtGui. As
it invokes ghostscript for conversion, it should only be used in trusted
environments.

%package        devel
Summary:        Development files for kimageformats
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for kimageformats, a framework
to provide additional image format plugins for QtGui.

%files
%license LICENSES/*
%dir %{_kf6_plugindir}/imageformats
%{_kf6_plugindir}/imageformats/kimg_ani.so
%if %{with avif}
%{_kf6_plugindir}/imageformats/kimg_avif.so
%endif
%{_kf6_plugindir}/imageformats/kimg_dds.so
%if %{with exr}
%{_kf6_plugindir}/imageformats/kimg_exr.so
%endif
%{_kf6_plugindir}/imageformats/kimg_ff.so
%{_kf6_plugindir}/imageformats/kimg_hdr.so
%if %{with heif}
%{_kf6_plugindir}/imageformats/kimg_heif.so
%endif
%if %{with jxl}
%{_kf6_plugindir}/imageformats/kimg_jxl.so
%endif
%if %{with jp2}
%{_kf6_plugindir}/imageformats/kimg_jp2.so
%endif
%{_kf6_plugindir}/imageformats/kimg_kra.so
%{_kf6_plugindir}/imageformats/kimg_iff.so
%{_kf6_plugindir}/imageformats/kimg_ora.so
%{_kf6_plugindir}/imageformats/kimg_pcx.so
%{_kf6_plugindir}/imageformats/kimg_pfm.so
%{_kf6_plugindir}/imageformats/kimg_pic.so
%{_kf6_plugindir}/imageformats/kimg_psd.so
%{_kf6_plugindir}/imageformats/kimg_pxr.so
%{_kf6_plugindir}/imageformats/kimg_qoi.so
%{_kf6_plugindir}/imageformats/kimg_ras.so
%{_kf6_plugindir}/imageformats/kimg_raw.so
%{_kf6_plugindir}/imageformats/kimg_rgb.so
%{_kf6_plugindir}/imageformats/kimg_sct.so
%{_kf6_plugindir}/imageformats/kimg_tim.so
%{_kf6_plugindir}/imageformats/kimg_tga.so
%{_kf6_plugindir}/imageformats/kimg_xcf.so

%files eps
%license LICENSES/*
%dir %{_kf6_plugindir}/imageformats
%{_kf6_plugindir}/imageformats/kimg_eps.so

%files devel
%{_kf6_cmakedir}/KF6ImageFormats/

%changelog
%autochangelog
