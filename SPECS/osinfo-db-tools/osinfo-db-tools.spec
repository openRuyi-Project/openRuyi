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
#!RemoteAsset
Source:         https://releases.pagure.org/libosinfo/osinfo-db-tools-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  libarchive-devel
BuildRequires:  libxml2-devel >= 2.6.0
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libsoup-3.0)
# fo tests
BuildRequires:  pytest
BuildRequires:  python3dist(requests)

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization.

%install -a
# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*

%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc NEWS README
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
