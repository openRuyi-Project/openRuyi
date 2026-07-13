# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           osinfo-db-tools
Version:        1.12.0
Release:        %autorelease
Summary:        Tools for managing the osinfo database
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Url:            https://releases.pagure.org/libosinfo/
VCS:            git:https://gitlab.com/libosinfo/osinfo-db-tools
#!RemoteAsset:  sha256:f3315f675d18770f25dea8ed04b20b8fc80efb00f60c37ee5e815f9c3776e7f3
Source:         https://releases.pagure.org/libosinfo/osinfo-db-tools-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libsoup-3.0)
# fo tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization.

%install -a
%find_lang %{name} --generate-subpackages

%files
%doc NEWS README
%license COPYING
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%changelog
%autochangelog
