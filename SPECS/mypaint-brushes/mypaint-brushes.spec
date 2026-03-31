# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mypaint-brushes
Version:        2.0.2
Release:        %autorelease
Summary:        Brushes to be used with the MyPaint library
License:        CC0-1.0
URL:            https://github.com/mypaint/mypaint-brushes
#!RemoteAsset:  sha256:01032550dd817bb0f8e85d83a632ed2e50bc16e0735630839e6c508f02f800ac
Source0:        https://github.com/mypaint/mypaint-brushes/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

%description
This package contains brush files for use with MyPaint and other programs.

%package        devel
Summary:        Files for developing with mypaint-brushes
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains a pkgconfig file which makes it easier to develop
programs using these brush files.

%conf -p
autoreconf -fiv

%files
%doc AUTHORS NEWS README
%license COPYING
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/2.0
%{_datadir}/mypaint-data/2.0/brushes/

%files devel
%license COPYING
%{_datadir}/pkgconfig/mypaint-brushes-2.0.pc

%changelog
%{?autochangelog}
