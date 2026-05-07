# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jansson
Version:        2.15.0
Release:        %autorelease
Summary:        A C library for encoding, decoding and manipulating JSON data
License:        MIT
URL:            https://www.digip.org/jansson/
VCS:            git:https://github.com/akheron/jansson
#!RemoteAsset:  sha256:a7eac7765000373165f9373eb748be039c10b2efc00be9af3467ec92357d8954
Source0:        https://github.com/akheron/jansson/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  bzip2

%description
Jansson is a C library for encoding, decoding and manipulating JSON data.

%package        devel
Summary:        files for jansson development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
files for jansson development

%files
%license LICENSE
%{_libdir}/libjansson.so.*

%files devel
%license LICENSE
%doc CHANGES
%{_libdir}/libjansson.so
%{_libdir}/pkgconfig/jansson.pc
%{_includedir}/jansson*.h

%changelog
%autochangelog
