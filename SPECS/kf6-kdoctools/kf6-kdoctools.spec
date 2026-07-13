# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kdoctools
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kdoctools
Version:        6.27.0
Release:        %autorelease
Summary:        Tools to create documentation from DocBook
License:        LGPL-2.1-or-later AND MIT
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kdoctools
#!RemoteAsset:  sha256:69026ef8607cb6257e4d1f0e46e451130ef7ba67994a83e4f9a6c46eefd5a3f3
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  perl-URI
BuildRequires:  perl-Exporter
BuildRequires:  perl-MIME-Base64
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)

%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Build environment for kdoctools
Requires:       docbook-xsl
Requires:       kf6-extra-cmake-modules >= %{_kf6_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxslt-devel
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Provides tools to generate documentation in various format from DocBook files.
Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6DocTools.so.*
%{_kf6_bindir}/checkXML6
%{_kf6_bindir}/meinproc6
# The HTML files need to be in the main package or khelpcenter will have display issues
%{_kf6_htmldir}/*/
%{_kf6_datadir}/kdoctools/
%{_kf6_mandir}/man1/*.1*
%{_kf6_mandir}/man7/*.7*
%{_datadir}/man/*/man1/*.1*
%{_datadir}/man/*/man7/*.7*

%files devel
%{_kf6_cmakedir}/KF6DocTools/
%{_kf6_includedir}/KDocTools/
%{_libdir}/libKF6DocTools.so

%changelog
%autochangelog
