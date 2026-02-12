# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kdoctools
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kdoctools
Version:        6.22.0
Release:        %autorelease
Summary:        Tools to create documentation from DocBook
License:        LGPL-2.1-or-later AND MIT
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kdoctools
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  perl-URI
BuildRequires:  perl-Exporter
BuildRequires:  perl-MIME-Base64
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-tools
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

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/en_GB/
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files
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
%{?autochangelog}
